
import asrt_sdk


def func(text):
    print('[result]', text)


sr = asrt_sdk.SpeechRecognizer()
sr.SetCallbackFunction(func)
#sr.RecogniteFromFile('D:\\语音数据集\\ST-CMDS-20170001_1-OS\\20170001P00241I0052.wav')

import time

sr.Start()

time.sleep(20)

sr.Stop()

