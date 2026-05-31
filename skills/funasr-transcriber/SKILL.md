---
name: funasr-transcriber
description: 基于 FunASR 的音视频转录工具。当用户需要将音频或视频文件转为文字时触发。触发短语包括"识别这个音频"、"转录录音文件"、"识别音频"、"音频转文字"、"转录视频"。支持会议、访谈、录音、语音备忘、播客、讲座、通话、视频等场景。特性包括 FFmpeg 格式转换、自动区分单/多人讲话、说话人分段、时间戳输出、中英文转录。
---

# FunASR Audio Transcription

Transcribe audio/video files using FunASR.

## Quick Start

```bash
# Transcribe with default model (SenseVoice, 234M)
python scripts/transcribe.py audio.mp3

# Save to file
python scripts/transcribe.py audio.mp3 transcript.txt

# Switch to Nano model (800M, 31 languages)
python scripts/transcribe.py audio.mp3 transcript.txt --model=nano

# With timestamps for long audio (meetings, lectures)
python scripts/transcribe.py meeting.wav --verbose
```


## Video Files

```bash
# Extract audio then transcribe
ffmpeg -i video.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 -y audio.wav
python scripts/transcribe.py audio.wav output.txt
```

## Models

Switch via `--model=sensevoice` or `--model=nano`. Default is **sensevoice**.

| Flag | Model | Params | Best For |
|------|-------|--------|----------|
| `--model=sensevoice` | SenseVoiceSmall | 234M | Default — lightweight, zh/yue/en/ja/ko + emotion/event detection |
| `--model=nano` | Fun-ASR-Nano-2512 | 800M | 31 languages, highest accuracy, dialect support |

Sub-models (auto-loaded):
- VAD: `fsmn-vad` (voice activity detection)
- Punctuation: `ct-punc` (Chinese + English punctuation restoration)

## Audio Formats

Supports WAV, MP3, M4A, FLAC. Videos require audio extraction with FFmpeg.

## Install
```bash
pip install funasr
brew install ffmpeg  # macOS
```

Full install guide: [references/installation.md](references/installation.md)
