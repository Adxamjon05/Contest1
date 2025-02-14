import time
def decorator_1(func):
  def wrapper(*args, **kwargs):
    start_time=time.time()
    func(*args, **kwargs)
    end_time=time.time()
    time_spent=end_time-start_time
    print(time_spent, "seconds")
  return wrapper
