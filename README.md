# YouTube Automation

This is an experimental but serious automation project for generating YouTube Shorts end-to-end using a fully self-hosted stack.

The goal is simple: once triggered, the system should run without manual intervention and output a finished short-form video.

This repository represents an evolving system, not a polished product.

---

## What This Project Does

The pipeline automates the full lifecycle of a short-form video:

1. **Script, description, and image prompt generation**  
   Uses a self-hosted LLM to generate:
   - video script
   - video description
   - SDXL-style prompts for image generation

2. **Image generation**  
   Images are generated locally using ComfyUI.

3. **Voiceover generation**  
   Voiceover audio is generated using Kokoro TTS.

4. **Subtitle generation**  
   Subtitles are generated from the voiceover using faster-whisper, with support for different subtitle styles.

5. **Video assembly**  
   Images, voiceover, and subtitles are merged into a single vertical video using FFmpeg, including basic cinematic effects.

The final output is a ready-to-publish YouTube Short.

---

## Current Scope

- Target platform: **YouTube Shorts**
- Video format: **vertical (9:16)**
- Fully self-hosted
- Designed to run end-to-end once triggered

Support for other short-form platforms (Instagram Reels, TikTok) is intentionally left open but is **not a current priority**.

---

## Design Philosophy

- **Automation-first**  
  The system is designed to run without manual steps once execution begins.

- **Self-hosted by default**  
  All major components (LLMs, image generation, TTS, transcription) run locally.

- **Modular services**  
  Each major responsibility is isolated into its own service (LLM, ComfyUI, TTS, Whisper, orchestration).

- **Practical over perfect**  
  This project favors working systems and iteration over premature abstraction.

---

## What This Is Not

- A SaaS product
- A beginner-friendly tutorial
- A one-click setup
- A finalized or stable architecture

Breaking changes are expected as the system evolves.

---

## Future Direction (High-Level)

This section intentionally avoids timelines or implementation details.

Planned areas of improvement include:
- Performance and stability improvements
- Smarter orchestration and failure handling
- Modular / plugin-style workflows
- Strategy and decisioning layers to control:
  - content generation
  - prompt selection
  - visual pacing
  - subtitle behavior
- Improved extensibility for additional platforms

Details will emerge as the system matures.

---

## Project Status

Active development.  
Architecture and workflows are expected to change.

This README reflects the current intent, not a final state.
