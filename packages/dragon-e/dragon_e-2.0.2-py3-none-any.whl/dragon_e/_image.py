from PIL import Image
from . import _dragon_e
import math
colors = {
        0: "000000",
        1: "ff0000",
        2: "00ff00",
        3: "0000ff",
        4: "ffff00",
        5: "ff00ff",
        6: "00ffff",
        7: "abcdef",
        8: "555555",
        9: "aaaaaa",
}
reversed_colors = {v: k for k, v in colors.items()}

def imageencrypt(msg, key):
    encrypted_message = _dragon_e.stealthencrypt(msg, key)
    im = Image.new("RGB", (math.ceil(math.sqrt(len(encrypted_message))), math.ceil(math.sqrt(len(encrypted_message)))), "white")
    pixels = im.load()
    for i in range(len(encrypted_message)):
        pixels[i%im.size[0], i//im.size[0]] = tuple(int(colors[int(encrypted_message[i])][j:j+2], 16) for j in range(0, 6, 2))
    return im

def rgb2hex(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(r, g, b)

def imagedecrypt(path: str, key):
    im = Image.open(path)
    pixels = im.load()
    encrypted_message = ""
    for j in range(im.size[0]):
        for i in range(im.size[1]):
            encrypted_message += str(reversed_colors[rgb2hex(*pixels[i, j])] if pixels[i, j] != (255, 255, 255) else '')
    return _dragon_e.decrypt(encrypted_message, key)