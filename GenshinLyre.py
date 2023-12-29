import keyboard
import time

class Intervalo:
    def __init__(self,tempo,letras):
        self.tempo = tempo
        self.letras = letras

nota1 = Intervalo(1,["a","b"])
nota2 = Intervalo(2,["c","d"])

listanotas = [nota1,nota2]

for i in range(10):
    for element in listanotas:
        if element.tempo == i:
            for elemento in element.letras:
                keyboard.press_and_release(elemento)
    time.sleep(1)