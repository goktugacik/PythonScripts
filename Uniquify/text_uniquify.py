import os
from googletrans import Translator

translator = Translator()

lines = [line.rstrip('\n') for line in open('turkce.txt')]
f = open("demofile.txt", "w")
for line in lines:
    text = translator.translate(line, src='tr', dest='en')
    text = translator.translate(text.text, src='en', dest='de')
    text = translator.translate(text.text, src='de', dest='fr')
    text = translator.translate(text.text, src='fr', dest='it')
    text = translator.translate(text.text, src='it', dest='es')
    text = translator.translate(text.text, src='es', dest='en')
    print(text.text)
    f.write(text.text + "\n" )
