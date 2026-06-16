import edge_tts


class TTSService:

    def __init__(self):

        self.voice = "en-US-AriaNeural"

    async def initialize(self):

        pass

    async def synthesize(self, text):

        communicate = edge_tts.Communicate(
            text,
            self.voice
        )

        audio_data = b""

        async for chunk in communicate.stream():

            if chunk["type"] == "audio":

                audio_data += chunk["data"]

        return audio_data