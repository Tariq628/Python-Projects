from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_time(msg):
    with open("water.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")
w_time = time()
e_time = time()
p_time = time()
watersecs = 5
eyessecs = 10
physecs = 15
while True:
    if time() - w_time > watersecs:
        musiconloop("water.mp3", "drank")
        w_time = time()
        log_time("water drinking at ")

    if time() - e_time > eyessecs:
        musiconloop("eyes.mp3", "exdone")
        log_time("Eyes Exercise Done at ")
        e_time = time()

    if time() - p_time > physecs:
        musiconloop("eyes.mp3", "yxdone")
        log_time("Physical Exercise Done at ")
        p_time = time()