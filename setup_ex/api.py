import requests

class CustomApi(object):
    def __init__(self, *args, **kwargs):
        print("This is a custom api")

    def func(self, x, y):
        return x * y

