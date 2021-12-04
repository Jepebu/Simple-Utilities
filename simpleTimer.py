
def start():
    import time
    startTime = time.time()
    return startTime

def stop(startTime):
    import time
    stopTime = time.time()
    totalTime = stopTime - startTime
    return totalTime
