def fact (n):
  factValue = n
  if n > 1:
    factValue = factValue * fact(n - 1)
  
  return factValue

def sumDigitsOfNumber (n):
  if n == 0:
    return 0
  
  return int(n % 10) + sumDigitsOfNumber(int(n / 10))
  
def f (n):
  if n == 0:
    return 0
    
  return fact(int(n % 10)) + f(int(n / 10))
  
def sf (n):
  factSum = f(n)
  sumOfFactSum = sumDigitsOfNumber(factSum)
    
  print(sumOfFactSum)
  
def g (i):
  pass
  
sf(342)