# FunASR Installation Guide

## Prerequisites

### 1. Python 3.8+

```bash
python --version
```

### 2. FFmpeg (required for video/audio conversion)

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install ffmpeg
```

**Windows:**
```bash
winget install ffmpeg
```

Verify: `ffmpeg -version`

## Install FunASR

```bash
pip install funasr
```

Optional (ModelScope or HuggingFace model download):
```bash
pip install modelscope huggingface_hub
```

## Model Auto-Download

Models are downloaded automatically on first use from ModelScope (default) or HuggingFace.

### ASR Models

| Model | ID | Params | Languages | Notes |
|-------|----|--------|-----------|-------|
| **SenseVoiceSmall** | `iic/SenseVoiceSmall` | 234M | zh, yue, en, ja, ko | Default. Lightweight, + emotion/event detection |
| **Fun-ASR-Nano-2512** | `FunAudioLLM/Fun-ASR-Nano-2512` | 800M | 31 languages | Best accuracy, supports dialects |
| **Paraformer-zh** | `paraformer-zh` | 220M | Mandarin | With timestamps, hotword support |
| **Whisper-large-v3-turbo** | `iic/Whisper-large-v3-turbo` | 809M | Multilingual | OpenAI Whisper variant |

### Sub-models (used by default)

| Model | ID | Params | Purpose |
|-------|----|--------|---------|
| **FSMN-VAD** | `fsmn-vad` | 0.4M | Voice activity detection — segments long audio |
| **CT-Punc** | `ct-punc` | 290M | Punctuation restoration — zh + en |
| **CAM++** | `cam++` | 7.2M | Speaker diarization — per-segment speaker labels |

Model cache: `~/.cache/modelscope/hub/`

## Verify Installation

```bash
python scripts/transcribe.py test.wav
```
