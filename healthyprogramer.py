
from pygame import mixer
import time
from datetime import datetime

def playSong(event,msg):
    print (msg)
    song_file=event+'.mp3'
    mixer.init()
    mixer.music.load(song_file)
    mixer.music.play()

def Done(event):
    act_dict={'water':'drank','eye':'idone','exercise':'xdone'}
    print (f"Type '{act_dict[event]}' when you are Done:")
    res = input("Enter:-")
    if act_dict[event]==res.lower():
        print ("Thanks for doing the activity")
        writeLog(event)
        mixer.music.stop()
    else:
        print ("Check the Input Again.")
        print ("make sure you type the correct input after doing the activity")
        Done(event)

def writeLog(event):
    log_file=event+'.txt'
    f=open(log_file,'a+')
    msg="You did the "+event+" activity"
    done_time=str(time.asctime(time.localtime(time.time())))
    f.write(done_time+' : '+msg+"\n")
    f.close()

def doActivity(event,msg):
        playSong(event,msg)
        Done(event)
        return int(time.time())

if __name__=='__main__':
    print ("\n****************Welcome to Helthy Programmer******************\n")
    off_flag=False
    cur_hour=datetime.now().hour
    cur_day=datetime.now().strftime("%A")
    off_start=9
    off_close=17
    if cur_hour>off_start and cur_hour<off_close and cur_day not in ['Sunday','Saturday']:
        print(f"Today is{cur_day} at {cur_hour} hours")
        off_flag=True
    else:
        print(f"Today is {cur_day} at {cur_hour}:{datetime.now().minute} hour")
        print ("This is not office time... Thank You :-)")
    

    water_start=eye_start=exe_start=int(time.time())
    while (off_flag):
        water_time = 30*60
        eye_time = 40*60
        exe_time = 45*60
        time.sleep(300)
        if int(time.time())-water_start>=water_time:
            msg="It's time to Drink the water"
            event="water"
            water_start=doActivity(event,msg)
        elif int(time.time()) - eye_start >= eye_time:
            msg = "It's time to Do some exercise"
            event="eye"
            eye_start=doActivity(event,msg)
        elif int(time.time()) - exe_start >= exe_time:
            msg = "It's time to Do some physical activity"
            event = "exercise"
            exe_start = doActivity(event, msg)
