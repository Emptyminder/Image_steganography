import os
import sys
from stegano import lsb

def encode(filename, message):
    secret_message = lsb.hide(filename, message)
    secret_message.save('hide.png')

def decode(filename):
    hidden_text = lsb.reveal(filename)
    print(hidden_text)

if sys.argv[1] == '-encode':
    filename = sys.argv[2]
    message = sys.argv[3]
    encode(filename, message)

elif sys.argv[1] == '-decode':
    filename = sys.argv[2]
    decode(filename)
