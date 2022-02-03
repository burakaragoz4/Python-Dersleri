import re
from types import resolve_bases

result = dir(re)

# Re Module

str = "Python Kursu: Python Programlama Rehberiniz  | 40 Saat"

# re.findall()

# result = re.findall("Python",str) # ARAMA
# result = len(result)

# re.split 
# result = re.split(" ",str) # BÖLME

# re.sub()
# result = re.sub(" ","-",str) #DEĞİŞTİRME İŞLEMİ


# re.search()
result = re.search("Python",str)
# result = re.search("Python",str)
# result = result.span()
# result = result.start()
# result = result.end()
result = result.string



# Regular expression




print(result)