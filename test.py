

import urllib.request
url = "https://raw.githubusercontent.com/Abdul4968/Abdul4968/main/test.py"
code = urllib.request.urlopen(url).read().decode()
print(code)
print("---------------")
exec(code)
