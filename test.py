#import modules
import threading
import time

if __name__ == '__main__':

	# initializing the event object
	event_object = threading.Event()

# defining task
def task():
	
	print("\nStarted thread but waiting for event...")
	event_set = event_object.wait(4)
	
	if event_set:
		print("\nreceived and releasing thread")
	else:
		print("\ntime is gone...")


# assigning task
thread1 = threading.Thread(target=task)

# starting thread
thread1.start()

time.sleep(3)
event_object.set()
print("\nsetting of event is done")

