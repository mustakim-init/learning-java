# Gemini CLI / Agent Instructions

This repository is an AI-guided, beginner-friendly Java learning system aligned with **CSE110: Programming Language I** at BRAC University.

## Operating Instructions:
1. **Always read `progress.json` and `AGENTS.md` before taking any action.**
2. The student is a **complete beginner**. Explain everything with real-world analogies, step-by-step.
3. **Generate REAL visual diagrams** (HTML/JS files or Python scripts) instead of ASCII art. See `AGENTS.md` Rule 3 for details.
4. Check the student's current position (`progress.current_position`) and never repeat completed lessons.
5. When a lesson or exercise is finished:
   - Update `progress.json` with the new completed lesson and advance `current_position`.
   - Run `node tutor.js sync` to update `PROGRESS.md`.

See `AGENTS.md` for full detailed protocols.
