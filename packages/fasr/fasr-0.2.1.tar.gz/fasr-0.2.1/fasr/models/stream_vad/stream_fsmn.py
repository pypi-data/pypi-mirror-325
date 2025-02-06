from .base import StreamVADModel
from funasr import AutoModel
from fasr.config import registry
from fasr.data import Waveform, AudioSpanList, AudioSpan
from typing_extensions import Self
from typing import Dict
from pathlib import Path


DEFAULT_CHECKPOINT_DIR = Path(__file__).parent.parent.parent / "asset" / "fsmn-vad"


@registry.stream_vad_models.register("stream_fsmn")
class FSMNForStreamVAD(StreamVADModel):
    fsmn: AutoModel | None = None
    is_detected: bool = False
    offset: int = 0
    state: Dict = {}

    def detect_chunk(
        self, waveform: Waveform, is_last: bool, **kwargs
    ) -> AudioSpanList[AudioSpan]:
        chunk_size = len(waveform.data) // (waveform.sample_rate / 1000)
        sample_rate = waveform.sample_rate
        data = waveform.data
        state = kwargs.get("state", self.state)

        segments = self.fsmn.generate(
            input=data,
            fs=sample_rate,
            chunk_size=chunk_size,
            is_final=is_last,
            cache=state,
        )[0]["value"]

        channel_segments = AudioSpanList[AudioSpan]()
        if len(segments) > 0:
            for segment in segments:
                start, end = segment
                if start != -1 and end == -1:
                    self.is_detected = True
                    start_idx = start * sample_rate // 1000 - self.offset
                    end_idx = len(data)
                    segment_waveform = waveform[start_idx:end_idx]
                    channel_segments.append(
                        AudioSpan(
                            start_ms=start,
                            end_ms=end,
                            waveform=segment_waveform,
                            sample_rate=sample_rate,
                            is_last=False,
                        )
                    )

                if start == -1 and end != -1:
                    self.is_detected = False
                    start_idx = 0
                    end_idx = end * sample_rate // 1000 - self.offset
                    segment_waveform = waveform[start_idx:end_idx]
                    channel_segments.append(
                        AudioSpan(
                            start_ms=start,
                            end_ms=end,
                            waveform=segment_waveform,
                            sample_rate=sample_rate,
                            is_last=True,
                        )
                    )

                if start != -1 and end != -1:
                    self.is_detected = False
                    start_idx = start * sample_rate // 1000 - self.offset
                    end_idx = end * sample_rate // 1000 - self.offset
                    segment_waveform = waveform[start_idx:end_idx]
                    channel_segments.append(
                        AudioSpan(
                            start_ms=start,
                            end_ms=end,
                            waveform=segment_waveform,
                            sample_rate=sample_rate,
                            is_last=True,
                        )
                    )
        else:
            if self.is_detected:
                channel_segments.append(
                    AudioSpan(
                        start_ms=-1,
                        end_ms=-1,
                        waveform=waveform,
                        sample_rate=sample_rate,
                        is_last=False,
                    )
                )

        self.offset += len(data)
        segments = channel_segments
        if is_last:
            self.reset()
        return segments

    def reset(self):
        self.state = {}
        self.is_detected = False
        self.offset = 0

    def from_checkpoint(
        self, disable_update: bool = True, disable_pbar: bool = True, *args, **kwargs
    ) -> Self:
        checkpoint_dir = DEFAULT_CHECKPOINT_DIR
        self.fsmn = AutoModel(
            model=str(checkpoint_dir),
            disable_update=disable_update,
            disable_pbar=disable_pbar,
        )
        return self
