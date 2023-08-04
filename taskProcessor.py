import os
import time
import argparse
import socket
import sys
class TaskProcessor():
    """
    Processes a task
    """
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
             

def main():
    # do arg parsing here
    #arg parsing
    parser = argparse.ArgumentParser(description = 'sleep time')

    parser.add_argument('-s', type = int, help = 'Enter sleep time')
    #Creating the arguments

    args = parser.parse_args() #passing in arguments 
    sleep = args.s

    print(sleep)
    app = TaskProcessor()
    print(f"blocks processed: {app.blocksProcessed}")
    #process being launched
    app.process(app.blocksProcessed)
    app.blocksProcessed = 1


    print(f"blocks processed: {app.blocksProcessed}")
    app.init()

    #Socket Creation Client
    socketOne = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketOne.connect((socket.gethostname(), 60603))
    
    '''
    Need to convert the sleep number from int to bytes so that I
    can send it to the server 
    '''
    
    #Sending the word "start" to the server
    socketOne.send('start'.encode())
    print('Connection established with server!')
    

    print(f"blocks processed: {app.blocksProcessed}")
    app.update(args.s)

    #process being launched
    app.process(app.blocksProcessed)
    app.blocksProcessed += app.blocksProcessed


    print(f"blocks processed: {app.blocksProcessed}")
    time.sleep(5)
    app.destroy()
    
    

if __name__ == "__main__":
    main()
    