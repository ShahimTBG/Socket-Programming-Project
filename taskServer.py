import os
import time
import argparse
import socket
import threading
from concurrent.futures import ThreadPoolExecutor


def blocksProcessed(sleepVal):
    
    app.update(sleepVal)
    #process being launched   
    app.process(app.blocksProcessed)
    app.blocksProcessed += app.blocksProcessed

def readStart(clientsocket: socket):
        startBytes = clientsocket.recv(1024)
        start = startBytes.decode('utf-8')
        return start  

class TaskServer():
    """
    Processes a task
    """
    
    def read_from_file():
        global data_into_list
        file = open("textNumbers.txt", "r")
        data = file.read()
        
        data_into_list = data.split("\n")
        data_into_list.remove('')
        data_into_list = [int(i) for i in data_into_list]
        print("\n", data_into_list, "\n")
        
            
    def get_next_number():
        pass
    
    
    
    def __init__(self, name=__name__, sleep=1):
        self.name = name
        self.sleepTime = sleep
        self.blocksProcessed = 0
        print("The task %s is starting in process %s" % (name, os.getpid()))
        self.init()

    def init(self):
        pass

    def update(self, sleep):
        self.sleepTime = sleep
        print(f'sleep time has been updated to {sleep} seconds')

    def process(self, blocksProcessed):
        self.blocksProcessed = blocksProcessed
        print('process is being ran')
        

    def destroy(self):
        print('Process is being destroyed')
   
    def read_from_client(clientsocket: socket):

            if(readStart(clientsocket) == "start"):
                TaskServer.read_from_file()
            else:
                pass
           
        
        
    #while clientsocket is connected
    
if __name__ == "__main__":
    # do arg parsing here
    #arg parsing
    parser = argparse.ArgumentParser(description = 'sleep time')

    parser.add_argument('-s', type = int, help = 'Enter sleep time')
    #Creating the arguments

    
    args = parser.parse_args() #passing in arguments 
    sleep = args.s

    print(sleep)
    app = TaskServer()
    print(f"blocks processed: {app.blocksProcessed}")
    #process being launched
    app.process(app.blocksProcessed)
    app.blocksProcessed = 1
    print(f"blocks processed: {app.blocksProcessed}")
    app.init()

    #Create socket
    socketOne = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketOne.bind((socket.gethostname(), 60603))
    address = socket.gethostname()
    
    #Starting the pool thread
    pool = ThreadPoolExecutor(2)
    while True:
        socketOne.listen(5)
        (clientsocket, address) = socketOne.accept()
        print(f"Connection from {address} has been established!")
        app.blocksProcessed += 1
        print(f"blocks processed: {app.blocksProcessed}")
        a = pool.submit(TaskServer.read_from_client(clientsocket))
        print('client is now disconnected')
        b = pool.submit(TaskServer.read_from_client(clientsocket))       
        
    app.destroy()

    
                        
    
    
    
