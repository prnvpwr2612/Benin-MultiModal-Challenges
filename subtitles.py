import assemblyai as aai

aai.settings.api_key = "5fc8ffde21da4c28a6be841a3dbd7491"

transcript = aai.Transcriber().transcribe("test.mp4")

subtitles = transcript.export_subtitles_srt()

f = open("subtitles3.srt", "a")
f.write(subtitles)
f.close()