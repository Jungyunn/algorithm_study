hour, minutes = map(int, input().split())

if (hour !=0):
    if (minutes >= 45):
        print(hour, minutes-45)
    else:
        print(hour-1, minutes+60-45)

if (hour ==0):
    if (minutes >= 45):
        print(hour, minutes-45)
    else:
        print(23, minutes+60-45)