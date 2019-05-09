import gevent

def sleep(seconds=0, ref=True):
     hub = get_hub()
     loop = hub.loop
     if seconds <= 0:
         waiter = Waiter()
         loop.run_callback(waiter.switch)
         waiter.get()
     else:
         hub.wait(loop.timer(seconds, ref=ref))

gevent.sleep(1)



def beep(interval):
    while True:
        print("Beep %s" % interval)
        gevent.sleep(interval)

for i in range(10):
    gevent.spawn(beep, i)

# beep(20)

beep(1)