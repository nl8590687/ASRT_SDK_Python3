
from .Recorder import AudioRecorder
import threading
import time
import wave
import requests
import numpy as np


class SpeechRecognizer():
    def __init__(self, url_server = 'http://127.0.0.1:20000/', token_client = 'qwertasd'):
        self.url_server = url_server
        self.token_client = token_client

        self.IsRecognizing = False
        self.__func_callback__ = None
        self.__recorder__ = AudioRecorder()
        pass

    def SetCallbackFunction(self, func_callback):
        if(str(type(func_callback)) != "<class 'function'>"):
            raise TypeError('Parameter "func_callback" need the type of "function", but yours is "' + str(type(func_callback)) + '". ')
        self.__func_callback__ = func_callback

    def Start(self, interval = 6):
        if(self.__func_callback__ == None):
            raise ValueError('[ASRT SDK] You have not set callback function here. Please call function "SetCallbackFunction" to do this. ')
        t1 = threading.Thread(target=self.__thread_recognize__, args = (interval,))
        self.IsRecognizing = True
        t1.start()
        pass
    
    def __thread_recognize__(self, interval):
        self.__recorder__.Initialize()
        self.__recorder__.RecordAsync()
        while(True):
            time.sleep(interval)
            if(self.IsRecognizing == False):
                break
            wavs = self.__recorder__.GetAudioSamples()
            self.__recorder__.__clear_audio_buffer__()
            # test function
            #wavs = self.__test_function__()
            # test function
            t2 = threading.Thread(target = self.__post_to_server__, args=(wavs,))
            t2.start()
            

        pass

    def __post_to_server__(self, wavs, fs = 16000):

        datas={'token':self.token_client, 'fs':fs, 'wavs':wavs}
        r = requests.post(self.url_server, datas)
        r.encoding='utf-8'
        self.__func_callback__(text = r.text)
        pass

    def StopAsync(self):
        wavs = self.__recorder__.GetAudioSamples()
        self.__recorder__.StopRecording()
        self.IsRecognizing = False
        self.__recorder__.__clear_audio_buffer__()
        t2 = threading.Thread(target = self.__post_to_server__, args=(wavs,))
        t2.start()
        self.__recorder__.Close()
        pass

    def Stop(self):
        wavs = self.__recorder__.GetAudioSamples()
        self.__recorder__.StopRecording()
        self.IsRecognizing = False
        self.__recorder__.__clear_audio_buffer__()
        self.__post_to_server__(wavs)
        self.__recorder__.Close()
        pass

    def RecogniteFromFile(self, filename):
        wf = wave.open(filename, 'rb')
        num_frame = wf.getnframes()
        str_data=wf.readframes(num_frame)
        wave_data = np.fromstring(str_data, dtype = np.short) # 将声音文件数据转换为数组矩阵形式
        wave_data.shape = -1, wf.getnchannels() # 按照声道数将数组整形，单声道时候是一列数组，双声道时候是两列的矩阵
        wave_data = wave_data.T # 将矩阵转置
        self.__post_to_server__(wave_data[0], wf.getframerate())
        pass

    def __test_function__(self, filename = 'D:\\语音数据集\\ST-CMDS-20170001_1-OS\\20170001P00241I0052.wav'):
        '''
        测试用函数
        '''
        wf = wave.open(filename, 'rb')
        num_frame = wf.getnframes()
        str_data=wf.readframes(num_frame)
        wave_data = np.fromstring(str_data, dtype = np.short) # 将声音文件数据转换为数组矩阵形式
        wave_data.shape = -1, wf.getnchannels() # 按照声道数将数组整形，单声道时候是一列数组，双声道时候是两列的矩阵
        wave_data = wave_data.T # 将矩阵转置
        return wave_data[0]

