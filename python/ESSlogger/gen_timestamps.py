import datetime

dt = datetime.datetime(2010, 12, 1, 11, 47, 14)
end = datetime.datetime(2010, 12, 1, 12, 1, 8)
step = datetime.timedelta(seconds=20)

while dt < end:
    print(dt.strftime('%H:%M:%S'))
    dt += step
