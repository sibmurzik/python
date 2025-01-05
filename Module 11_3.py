#"Интроспекция"

import requests
import sys
import inspect
from pprint import pprint

print(callable(requests))
pprint(dir(requests))
help(requests)
help(requests.get)
print(type(requests))
print(type(requests.get))


response= requests.get('https://urban-university.pro/api/v1/courses/lesson/1079Request Method:GET')
print(inspect.getmodule(response))
#newResponce = requests.models
print(response)
print(type(response))
print(sys.getsizeof(response))
print(inspect.getmembers(response))
print(response.status_code, 'type', type(response.status_code))
if response.status_code == 401:
    print( response.reason)
pprint(response.headers)
pprint(response.content)
