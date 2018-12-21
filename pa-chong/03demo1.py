import re


match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print(match.group(0))

match1 = re.match(r'[1-9]\d{5}', '100081 BIT ')
if match1: # 它可能是空的
    print(match1.group(0))

match2 = re.split(r'[1-9]\d{5}', 'BIT 100081 TSU 100084   ')
if match2: # 它可能是空的
    print(match2)

match3 = re.search(r'PY.*?N', 'PYABNCDNEFN')
if match3: # 它可能是空的
    print(match3.group(0))