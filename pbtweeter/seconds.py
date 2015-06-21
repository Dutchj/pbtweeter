def time_to_seconds(time):
    h = int(time[:2])*3600
    m = int(time[3:5])*60
    s = int(time[6:8])
    return h+m+s

def seconds_to_time(sec):
    h = divmod(sec,3600)
    m = divmod(h[1],60)
    s = m[1]
    return "{H}:{M}:{S}".format(H=str(h[0]),M=str(m[0]).zfill(2),S=str(s).zfill(2))