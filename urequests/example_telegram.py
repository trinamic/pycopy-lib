try:
    import urequests as requests
except ImportError:
    import requests

r = requests.get("https://api.telegram.org/bot")
print(r)
print(r.content)
print(r.text)
# You can access .content multiple times of course
print(r.content)
print(r.json())

# It's mandatory to close response objects as soon as you finished
# working with them. On Pycopy platforms without full-fledged
# OS, not doing so may lead to resource leaks and malfunction.
r.close()
