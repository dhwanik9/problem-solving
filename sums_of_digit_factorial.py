import sys
import time

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
  return sumDigitsOfNumber(f(n))
  
def g (i):
  n = 1;
  while sf(n) != i:
    n += 1

  return n
  
def sg (i):
  return sumDigitsOfNumber(g(i))

def performSumOfDigits (n, m):
  sumOfDigits = 0
  for i in range (1, n + 1):
    sumOfDigits += sg(i)
  
  return sumOfDigits % m

stdin = sys.stdin
testCases = stdin.readline()

for i in range (0, int(testCases)):
  splitInput = stdin.readline().split(" ")
  n = int(splitInput[0])
  m = int(splitInput[1])
  start = time.perf_counter()
  sumOfDigits = performSumOfDigits(n, m)
  end = time.perf_counter()
  print(sumOfDigits)
  print (start - end)