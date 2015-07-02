def time_to_seconds(time):
    times = time.split(':')
    h = 0
    m = 0
    s = int(times.pop(-1))
    if times:
        m = int(times.pop(-1))*60
    if times:
        h = int(times.pop(-1))*3600
    return h+m+s

def seconds_to_time(sec):
    h = divmod(sec,3600)
    m = divmod(h[1],60)
    s = m[1]

    if sec < 60:
        return str(sec)+' seconds'
    elif h[0] == 0:
        return '{M}:{S}'.format(M=str(m[0]), S=str(s).zfill(2))
    else:
        return '{H}:{M}:{S}'.format(H=str(h[0]), M=str(m[0]).zfill(2), S=str(s).zfill(2))
