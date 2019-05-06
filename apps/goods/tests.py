from django.test import TestCase

# Create your tests here.
import requests
url='http://127.0.0.1/goods/'
p=requests.get(url).content.decode('utf-8')
print(p)