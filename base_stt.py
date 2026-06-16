import whisper
import tempfile


class STTService:

    def __init__(self):

        self.model = None

    async def initialize(self):

        self.model = whisper.load_model(
            "base"
        )

    async def transcribe(self, audio_bytes):

        with tempfile.NamedTemporaryFile(
            suffix=".wav"
        ) as temp_audio:

            temp_audio.write(audio_bytes)

            temp_audio.flush()

            result = self.model.transcribe(
                temp_audio.name
            )

        return result["text"]