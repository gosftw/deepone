import math
import os
import sys

import requests

r = requests.get('https://google.com')
name = input('Your Name? ')
print(f'hello {name}')
print(r.ok)
