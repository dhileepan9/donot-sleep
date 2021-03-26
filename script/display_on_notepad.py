import os
import time

def notepad_runner(filename):
    os.system("start notepad.exe " + filename)
    time.sleep(10)
    os.system("taskkill /im notepad.exe /f")