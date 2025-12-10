from pathlib import Path
from gtts import gTTS

class GTtsEngine:

    def __init__(self, lang="en"):
        self.lang = lang

    def text_to_speech(self, text: str, out_path: Path):
        out_path.parent.mkdir(parents=True, exist_ok=True)
        tts = gTTS(text=text, lang=self.lang)
        tts.save(str(out_path))
        return out_path
