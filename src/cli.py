import argparse
from pathlib import Path
from tts_engine import GTtsEngine

def parse_args():
    parser = argparse.ArgumentParser(description="Simple TTS Tool using gTTS")
    parser.add_argument("--text", help="Text to convert to speech")
    parser.add_argument("--infile", help="Text file for batch conversion")
    parser.add_argument("--outdir", default="output", help="Folder to save audio files")
    parser.add_argument("--lang", default="en", help="Language code (default: en)")
    return parser.parse_args()

def main():
    args = parse_args()
    engine = GTtsEngine(lang=args.lang)
    outdir = Path(args.outdir)

    # Single text mode
    if args.text:
        out_path = outdir / "tts_output.mp3"
        engine.text_to_speech(args.text, out_path)
        print(f"Audio saved at {out_path}")

    # Batch mode
    elif args.infile:
        infile = Path(args.infile)
        lines = infile.read_text(encoding="utf-8").splitlines()

        for i, line in enumerate(lines, start=1):
            if not line.strip():
                continue
            out_path = outdir / f"line_{i}.mp3"
            engine.text_to_speech(line, out_path)
            print(f"Saved: {out_path}")

    else:
        print("Please use --text or --infile")

if __name__ == "__main__":
    main()
