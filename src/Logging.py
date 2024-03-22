from datetime import datetime

def writeLog(username, action):    
    currentTime = datetime.now()
    formattedTime = currentTime.strftime("%d/%m/%Y %H:%M:%S")

    f = open("logs.txt", "a")
    f.write(f"{username}: {action} at {formattedTime}.\n")
    f.close()