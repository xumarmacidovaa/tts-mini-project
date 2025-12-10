\# TTS Mini Project -- gTTS Version Super simple Text-to-Speech tool
(perfect for beginners & quick demos)

One-click ready: just download, install two packages, and start turning
text into MP3 files.

\## Features - Convert a single sentence → one MP3  - Convert a .txt
file (one line = one MP3) → batch mode  - Choose language (\--lang fr,
\--lang es, etc.)  - 100% offline install after the first run (gTTS
caches voices)

\## Quick Start (3 commands)

\`\`\`bash \# 1. Clone or download this repo git clone
https://github.com/your-username/tts-mini-project.git cd
tts-mini-project

\# 2. (Recommended) Create a virtual environment python -m venv venv \#
Windows: venv\\Scripts\\activate \# Mac/Linux: source venv/bin/activate

\# 3. Install dependencies and run! pip install -r requirements.txt

\# Try it instantly python src/cli.py \--text \"Hello world, this is
gTTS speaking\"

\# Batch example python src/cli.py \--infile samples/batch_input.txt
\--lang en
