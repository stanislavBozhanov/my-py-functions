""" distance takes kilometers """
def avg_speed_secs(distance, seconds):
    return distance / (seconds / 3600)


""" distane takes kilometers, time_format takes strings H:M:S format"""
def avg_speed_time(distance, time_format):
    parts = time_format.split(":")
    seconds = int(parts[0])*(60*60) + int(parts[1])*60 + int(parts[2])
    return avg_speed_secs(distance, seconds)


#print(avg_speed_secs(1, 85))
#print(avg_speed_time(91, '04:31:40'))