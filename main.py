word=input('Enter a string ')

upper=word.upper()
lower=word.lower()

def format_Aa(a):
  upper_lower=''
  type=0
  for x in a:
    if type == 0:
      upper_lower=upper_lower + x.upper()
      type=1
    elif type == 1:
      upper_lower=upper_lower + x.lower()
      type=0
  print(upper_lower)
  return('')

def line(a):
  for x in a:
    print(x)
  return('')

print(word[::-1])  
print(upper)
print(lower)
print(format_Aa(word))
print(line(word))
