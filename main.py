import threading
import multiprocessing
import time

try:
    while(True):
        time.sleep(0.5)
except KeyboardInterrupt:
    time.sleep(0.2)