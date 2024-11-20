import pyautogui as pg
import random
import time

msg = ["Bombarda", "Avada Kedavra", "Priori Incantatem", "Expecto Patronum"]

# Tempo de espera para o disparo
time.sleep(5)

for i in range(10):
    a = random.choice(msg)
    pg.write(a)
    pg.press("enter")
    time.sleep(1.3)
