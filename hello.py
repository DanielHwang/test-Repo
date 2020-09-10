# import os
# import sys

import requests

# print(sys.version)
# print(sys.executable)


# def greet(who_to_greet):
#     greeting = "hello, {}".format(who_to_greet)
#     return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)
# print(greet("Daniel"))


# name = input("Your name? ")
# print("hello, ", name)
