range(start=0, stop=5, step=1)

start = 0
stop = 5
step = 1
def range_(start, stop, step):
    if stop > start and step > 0:
        while start <= stop: 
            start += step
            yield start
    if stop > start and step < 0:
        while start <= stop: 
            stop -= step
            yield stop
