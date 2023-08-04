import os
import time
from subprocess import Popen, STDOUT, PIPE



if __name__ == "__main__":
    print("main starting")
    Popen(["python", "./taskProcessor.py", "-s2"])
    Popen(["python", "./taskServer.py", "-s5"])
    print("main done")


    