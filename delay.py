import re
import math

HOUR = 60*60*1000
MIN = 60*1000
SEC = 1000

##1_1
#START = "00:26:44,500"
#END = "00:37:55,300"

##1_2
#START = "00:37:59,200"
#END = "00:51:05,300"

##1_3
#START = "00:51:11,200"

##1_4
START = "01:39:58,300"
END = "03:00:00,000"

INPUT = "1_3.srt"
OUTPUT = "1_4.srt"
DELAY = 2.5


def delay(t, d_s, start, end):
    t1 = ts2int(t)
    s_ts = ts2int(start)
    e_ts = ts2int(end)
    if t1 >= s_ts and t1 <= e_ts:
        print "t1" + str(t1)
        return int2ts(t1 + int(d_s * SEC))
    else :
        return t

def ts2int(ts):
    m = re.search("([0-9]{2}):([0-9]{2}):([0-9]{2}),([0-9]{3})", ts)
    h = int(m.group(1))
    mi = int(m.group(2))
    se = int(m.group(3))
    ms = int(m.group(4))
    tsint = h*HOUR + mi*MIN + se*SEC + ms
    return tsint

def int2ts(i):
    h, mod = divmod( i, HOUR )
    m, mod = divmod( mod,  MIN )
    s, ms  = divmod( mod, SEC)
    ts = '{0:02d}:{1:02d}:{2:02d},{3:03d}'.format( h, m, s, ms)
    print ts
    return ts

def process(l):
    m = re.search("^([0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}) --> ([0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3})", l)
    if m:
        t1 = delay(m.group(1), DELAY, START, END)
        t2 = delay(m.group(2), DELAY, START, END)
        return t1 + " --> " + t2
    else:
        return l


with open(OUTPUT, 'w') as output:
    with open(INPUT) as f:
        for line in f:
            pl = process(line.strip())
            output.write(pl)
            output.write('\n')
