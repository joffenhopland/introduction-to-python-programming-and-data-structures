def main():
    totalSeconds = int(input("Enter total seconds: "))
    print("The hours, minutes, and seconds for total seconds", 
        totalSeconds, "is", format(totalSeconds))

def format(seconds):
    hour = seconds // 3600 % 24
    minute = seconds // 60 % 60
    second = seconds % 60
    
    return ("0" + str(hour) if hour < 10 else str(hour)) + ":" \
        + ("0" + str(minute) if minute < 10 else str(minute)) + ":" \
        + ("0" + str(second) if second < 10 else str(second))

main()