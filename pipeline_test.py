import asyncio

from src.pipeline import AudioPipeline


async def main():

    pipeline = AudioPipeline()

    await pipeline.initialize()

    with open("test.wav", "rb") as file:

        audio_bytes = file.read()

    response_audio = await pipeline.process_audio(
        audio_bytes
    )

    with open("response.mp3", "wb") as output:

        output.write(response_audio)

    print("\nPipeline completed successfully")


asyncio.run(main())