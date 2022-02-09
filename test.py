from time import sleep
import subprocess
from subprocess import Popen, check_call
import psutil
import ctypes
import pandas as pd

# to create lists to use it in DataFrame as columns
cpu, ws, pb, handles = [], [], [], []


# The function is for getting data
def for_search_hwnd():
    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int),
                                         ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible
    titles = []
    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True
    EnumWindows(EnumWindowsProc(foreach_window), 0)
    return len(titles)


# collects necessary information
def main_process(dream):
    while code.poll() is None:
        cpu.append(psutil.cpu_percent())
        p = psutil.Process()
        ws.append(p.memory_info().rss)
        pb.append(p.memory_info().private)
        hwnd_l = for_search_hwnd()
        handles.append(hwnd_l)
        sleep(float(dream))
        

command = input('Input the process one has to start: ')
dreamtime = input('Input the time of waiting: ')
code = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
try:
    main_process(dreamtime)
except TypeError:
    print('Check your types of objects in func.')
else:
    data = pd.DataFrame({'CPU': cpu, 'WorkingSet': ws,
                     'PrivateBytes': pb, 'Handles': handles})

