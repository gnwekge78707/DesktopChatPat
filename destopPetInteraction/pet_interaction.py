import os
import wave
import pyaudio
import argparse

from destopPetInteraction.chater import Chater
from destopPetInteraction.predictor import Predictor


class PetInteraction():
    def __init__(self):
        self.predictor = Predictor()
        self.chatter = Chater()

    """
    record stop with keyboard interrupt
    """
    def record_wave(self,
                    wavfile,
                    duration=10,
                    channels=1,
                    sampling_rate=16000,
                    sampling_bits=16,
                    chunk_size=1024,
                    keyboard_interrupt='keep_audio'):
        format_ = None
        if sampling_bits == 8:
            format_ = pyaudio.paInt8
        if sampling_bits == 16:
            format_ = pyaudio.paInt16
        elif sampling_bits == 24:
            format_ = pyaudio.paInt24
        elif sampling_bits == 32:
            format_ = pyaudio.paFloat32
        else:
            raise ValueError('Unsupported sampling bits')

        audio = pyaudio.PyAudio()
        stream = audio.open(format=format_,
                            channels=channels,
                            rate=sampling_rate,
                            input=True,
                            frames_per_buffer=chunk_size)

        frames = []

        print('Start to record with {}-seconds audio\n'
              'Type Ctrl-C to get an early stop (a shorter audio)'
              .format(duration))

        try:
            for _ in range(0, int(sampling_rate / chunk_size * duration)):
                data = stream.read(chunk_size)
                frames.append(data)
                print('.', end='', flush=True)
        except KeyboardInterrupt:
            used_seconds = int(len(frames) * chunk_size / sampling_rate)
            print('\n-*- Early stop with {} seconds'.format(used_seconds))
            pass


        print('\nRecording finished')

        stream.stop_stream()
        stream.close()
        audio.terminate()

        print('Convert PCM frames to WAV... ', end='')
        wavfp = wave.open(wavfile, 'wb')
        wavfp.setnchannels(channels)
        wavfp.setsampwidth(audio.get_sample_size(format_))
        wavfp.setframerate(sampling_rate)
        wavfp.writeframes(b''.join(frames))
        wavfp.close()
        print('OK')

    def audio2text(self) -> str:
        #self.record_wave('output.wav')
        res, res1 = self.predictor.predictSingleStep()
        print("audio recog res :: \n", res)
        return res

    def query_bot(self, query : str) -> str:
        res = self.chatter.interact(query)
        if res == 'answer not found':
            words = self.chatter.get_words(query)
            if ('截图' in res) or ('截屏' in res):
                """todo"""
            """
            handle self defined command
            """
            return 'answer not found'
        else:
            print("chatter bot output :: \n", res)
            return res

    def is_sublist(self, list1, list2):
        for i in range(len(list2) - len(list1) + 1):
            if list2[i: i+len(list1)] == list1:
                return True
        return False

    def step(self):
        text, pinyin = self.predictor.predictSingleStep()
        print("audio recog res :: \n", text)
        if self.is_sublist(['jie2', 'tu2'], pinyin) or self.is_sublist(['jie2', 'pin2'], pinyin) or self.is_sublist(['jie2', 'ping2'], pinyin):
            """
            snapshot
            """
        elif self.is_sublist(['bo1', 'fang4'], pinyin) or self.is_sublist(['ge1', 'qu3'], pinyin) or self.is_sublist(['zan4', 'ting1'], pinyin):
            """
            music player
            """
        else:
            res = self.chatter.interact(text)
            if res == 'answer not found':
                res = '猫猫也不知道捏'
            print("chatter bot output :: \n", res)
            return res
        return '好哒~'


if __name__ == '__main__':
    pet = PetInteraction()
    print("******************output of pet******************\n", pet.step())   #识别 处理 预测 回答
    print("******************output of pet******************")
    final_output = pet.query_bot(pet.audio2text()) #识别 预测
