from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import io

class AudioRecognizer:

    def __init__(self):
        self.client = speech.SpeechClient()

    def audio_recognize(self, srcPath, encoding, sampleRate):
        with io.open(path, 'rb') as audio_file:
            content = audio_file.read()

        audio = types.RecognitionAudio(content=content)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
            sample_rate_hertz=sampleRate,
            enable_word_time_offsets = True,
            language_code='ko-KR')

        response = self.client.recognize(config, audio)

        for result in response.results:
            return (u'{}'.format(result.alternatives[0].transcript))
