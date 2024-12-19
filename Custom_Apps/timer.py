import time


def timer(mins=2):
    minutes = mins
    seconds = 0
    while minutes >= 0:
        print(f"{minutes:02}:{seconds:02}")
        time.sleep(0.3)
        if seconds == 0:
            if minutes == 0:
                return True
            minutes -= 1
            seconds = 59
        else:
            seconds -= 1
