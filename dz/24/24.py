
# Задание 1

import re

s = '1X, Text ABC 123 A1B2C3'
reg = r'(\d)[A-z]'
print(re.findall(reg, s+'A'))




# Задание 2

import re

s = 'text from #START# till #END#'
reg = r'#START#(.*)#END#'
print(re.findall(reg, s))




# Задание 3

s = '12_24__56'
s1 = re.sub(r'(_+)', r'\1A', s)
reg = r'(\d+)_A'
print(re.findall(reg, s1))