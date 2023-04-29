import time
sec = input("enter the time in seconds")

def countdown(sec):
    while sec>0:
        mins = int(sec/60)
        secs = int(sec%60)
 
        timer = f'{mins}:{secs}'
        print(timer)
        sec=sec-1

countdown( int(sec))