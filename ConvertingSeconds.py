def convert_seconds(input):
    hour = int(input/3600)
    rest = input - hour*3600
    if hour > 1 or hour == 0:
        htext = " hours"
    else:
        htext = " hour"
    string_h = str(hour) + htext
    minute = int(rest/60)
    rest2 = rest - minute*60
    if minute > 1 or minute == 0:
        mtext = " minutes"
    else:
        mtext = " minute"
    string_m = str(minute) + mtext
    second = rest2
    if second > 1 or second == 0:
        stext = " seconds"
    else:
        stext = " second"
    string_s = str(second) + stext
    return string_h + ', ' + string_m + ', ' + string_s
           
print convert_seconds(3600)

# converting seconds into hours, minutes, and seconds