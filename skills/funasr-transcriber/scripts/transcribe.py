#!/usr/bin/env python3
"""FunASR audio transcription with auto-detect single/multi-speaker formatting."""
import sys
import time

import torch
from funasr import AutoModel

# Patch distribute_spk to handle None timestamps from cam++ speaker model
import funasr.models.campplus.utils as _campplus_utils
_original_distribute_spk = _campplus_utils.distribute_spk


def _safe_distribute_spk(sentence_list, sd_time_list):
    sd_time_list = [
        (st, ed, spk) for st, ed, spk in sd_time_list
        if st is not None and ed is not None
    ]
    return _original_distribute_spk(sentence_list, sd_time_list)


_campplus_utils.distribute_spk = _safe_distribute_spk


def detect_device():
    if torch.cuda.is_available():
        return "cuda:0"
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return "mps"
    return "cpu"


DEVICE = detect_device()


# ---------------------------------------------------------------------------
# Model functions
# ---------------------------------------------------------------------------

def transcribe_sensevoice(audio_path):
    """SenseVoiceSmall — 234M, zh/yue/en/ja/ko + emotion/event detection."""
    from funasr.utils.postprocess_utils import rich_transcription_postprocess

    model = AutoModel(
        model="iic/SenseVoiceSmall",
        vad_model="fsmn-vad",
        vad_kwargs={"max_single_segment_time": 30000},
        # punc_model="ct-punc",
        spk_model="cam++",
        device=DEVICE,
        disable_update=True,
        disable_pbar=True,
    )
    res = model.generate(
        input=[audio_path],
        cache={},
        batch_size_s=0,
        language="auto",
        use_itn=True,
        merge_vad=True,
        merge_length_s=15,
    )
    segments = []
    for sent in res[0]["sentence_info"]:
        segments.append({
            "spk": sent["spk"],
            "start": sent["start"],
            "end": sent["end"],
            "text": rich_transcription_postprocess(sent["sentence"]),
        })
    full_text = rich_transcription_postprocess(res[0]["text"])
    return segments, full_text


def transcribe_nano(audio_path):
    """Fun-ASR-Nano-2512 — 800M, 31 languages."""
    model = AutoModel(
        model="FunAudioLLM/Fun-ASR-Nano-2512",
        vad_model="fsmn-vad",
        vad_kwargs={"max_single_segment_time": 30000},
        punc_model="ct-punc",
        spk_model="cam++",
        device=DEVICE,
        disable_update=True,
        disable_pbar=True,
    )
    res = model.generate(input=[audio_path], cache={}, batch_size_s=0)
    segments = []
    for sent in res[0]["sentence_info"]:
        segments.append({
            "spk": sent["spk"],
            "start": sent["start"],
            "end": sent["end"],
            "text": sent["sentence"],
        })
    return segments, res[0]["text"]


MODELS = {
    "sensevoice": transcribe_sensevoice,
    "nano": transcribe_nano,
}


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def format_time(ms):
    s, ms = divmod(ms, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}" if h else f"{m:02d}:{s:02d}.{ms:03d}"


def merge_consecutive(segments, gap_threshold_ms=1500):
    """Merge consecutive same-speaker segments into paragraph-level turns."""
    if not segments:
        return []
    merged = [segments[0].copy()]
    for seg in segments[1:]:
        prev = merged[-1]
        same_speaker = seg["spk"] == prev["spk"]
        short_gap = (seg["start"] - prev["end"]) < gap_threshold_ms
        if same_speaker and short_gap:
            prev["text"] += seg["text"]
            prev["end"] = seg["end"]
        else:
            merged.append(seg.copy())
    return merged


def format_single_speaker(segments, verbose=False):
    """Clean paragraph output — no speaker labels, grouped by pause gaps."""
    turns = merge_consecutive(segments, gap_threshold_ms=3000)
    lines = []
    for turn in turns:
        if verbose:
            lines.append(f"[{format_time(turn['start'])} -> {format_time(turn['end'])}]")
        lines.append(turn["text"])
    return "\n\n".join(lines)


def format_multi_speaker(segments, verbose=False):
    """Dialogue output — speaker label on turn change, grouped turns."""
    turns = merge_consecutive(segments, gap_threshold_ms=1500)
    lines = []
    for turn in turns:
        parts = [f"[Speaker {turn['spk']}]"]
        if verbose:
            parts.insert(0, f"[{format_time(turn['start'])} -> {format_time(turn['end'])}]")
        parts.append(turn["text"])
        lines.append(" ".join(parts))
    return "\n\n".join(lines)


def format_output(segments, verbose=False):
    """Auto-detect single vs multi-speaker and format accordingly."""
    if not segments:
        return ""
    num_speakers = len({s["spk"] for s in segments})
    if num_speakers <= 1:
        return format_single_speaker(segments, verbose)
    return format_multi_speaker(segments, verbose)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv):
    audio_path = None
    output_path = None
    model_name = "sensevoice"
    verbose = False

    i = 1
    while i < len(argv):
        arg = argv[i]
        if arg.startswith("--model="):
            model_name = arg.split("=", 1)[1]
        elif arg == "--model":
            i += 1
            model_name = argv[i]
        elif arg == "--verbose":
            verbose = True
        elif audio_path is None:
            audio_path = arg
        elif output_path is None:
            output_path = arg
        i += 1
    return audio_path, output_path, model_name, verbose


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <audio_path> [output_txt] [--model sensevoice|nano] [--verbose]", file=sys.stderr)
        sys.exit(1)

    audio_path, output_path, model_name, verbose = parse_args(sys.argv)

    if model_name not in MODELS:
        print(f"Unknown model: {model_name}. Available: {', '.join(MODELS)}", file=sys.stderr)
        sys.exit(1)

    t0 = time.monotonic()
    segments, full_text = MODELS[model_name](audio_path)
    elapsed = time.monotonic() - t0
    print(f"[Transcription completed: {elapsed:.1f}s, model={model_name}]", file=sys.stderr)
    text = format_output(segments, verbose) if segments else full_text

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        print(text)
