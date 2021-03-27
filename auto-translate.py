from pynput.keyboard import Key, Listener
import pyperclip
from googletrans import Translator


def on_press(key):
    if key == Key.num_lock:
        text = pyperclip.paste()
        p = Translator()
        text2 = p.translate(text,dest='tr')
        ttext = text2.text 
        pyperclip.copy(ttext)
def on_release(key):
    if key == Key.esc:
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()