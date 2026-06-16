from src.stt.base_stt import STTService
from src.tts.base_tts import TTSService
from src.llm.agent import CustomerSupportAgent


class AudioPipeline:

    def __init__(self):

        self.stt = STTService()

        self.tts = TTSService()

        self.agent = CustomerSupportAgent()

    async def initialize(self):

        await self.stt.initialize()

        await self.tts.initialize()

        await self.agent.initialize()

    async def process_audio(self, audio_bytes):

        text = await self.stt.transcribe(audio_bytes)

        print("\nUser Said:\n")
        print(text)

        response_text = await self.agent.process_query(text)

        print("\nAI Response:\n")
        print(response_text)

        response_audio = await self.tts.synthesize(
            response_text
        )

        return response_audio