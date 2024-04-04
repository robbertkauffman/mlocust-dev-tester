# Shim for Locust: User, events, constant, between, tag & task

class User():
  host: str = ""
  
  def __init__(self, host):
    self.host = host

class EventHook:
  def fire(self, **kwargs):
    print("New request came in:")
    for key, value in kwargs.items():
      print(f"- {key}: {value}")

class events:
  request = EventHook()
  request_failure = EventHook()
  request_success = EventHook()

def constant(_):
  pass

def between(_min, _max):
  pass

def tag(_):
  def decorator(func):
    def wrapper(_):
      return func(_)
    return wrapper
  return decorator

def task(_):
  def decorator(func):
    def wrapper(_):
      return func(_)
    return wrapper
  return decorator