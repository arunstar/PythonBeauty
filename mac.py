#%%

print("Hello Mac")

import re

text = "I want ($500)"

pattern = re.compile(r'\(([^)]+)\)')
matches = pattern.finditer(text)

for match in matches:
    print(match)