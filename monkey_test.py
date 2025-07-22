import time


def modifier_sleep(s):
    print(f'Te quedan {s} segundos para dormir')
    
time.sleep = modifier_sleep


time.sleep(10)

