import random as rm
import csv
import re

# Первая задача - сохранение списка случайных чисел в файл
def FirstTask():
  minBorder = 1
  maxBorder = 100
  numCnt = 100
  step = 1
  numList = []
  while (len(numList) != numCnt):
    numList.append(str(rm.randrange(minBorder, maxBorder, step)))
  resultFile = open('numbers.csv', 'w+')
  with resultFile:
      wr = csv.writer(resultFile)
      wr.writerow(numList)
  return "\nData successfully saved to file."

# Вторая задача - сортировка чисел из задачи 1
def SecondTask():
  errMsg = ""
  try:
    successMsg = "\nOriginal list of numbers: \n"
    with open('numbers.csv') as File:  
      reader = csv.reader(File)
      for numbers in reader:
        successMsg += ", ".join(numbers) + "\n\nSorted list of numbers from lowest to highest: \n" + ", ".join(map(str, sorted(map(int, numbers))))
  except IOError:
      errMsg = "\nERROR! File not available. Try task '1', then do this."
  return successMsg if errMsg == "" else errMsg

# Возведение в степень
def Exponentiation(num, degree):
  inDegree = degree
  inNum = num
  resultNum = 1
  if inDegree in (0,1):
    resultNum = 1 if inDegree == 0 else inNum
  else:
    while (inDegree > 0):
      if inDegree % 2 != 0:
        resultNum *= inNum
      inNum *= inNum
      inDegree //= 2
  return resultNum

# Третья задача - возведение числа в степень
def ThirdTask():
  successMsg = ""
  errMsg = ""
  try:
    inNum = int(input("\nPlease enter an integer number raised to a degree from 1 to 10:\n"))
    inDegree = int(input("Please enter an integer degree of number from 0 to 9:\n"))
    if (inNum >= 1 and inNum <=10) and (inDegree >= 0 and inDegree <= 9):
      resultNum = Exponentiation(num = inNum, degree = inDegree)
      successMsg = "\nSUCCESS! The number {num} to the {degree} power has a meaning: {result}".format(num = inNum, degree = inDegree, result = resultNum)
    else:
      errMsg = "\nERROR! The tasks you entered do not meet the requirements. Restart the script and try again."  
  except TypeError:
    errMsg = "\nERROR! The tasks you entered do not meet the requirements. Restart the script and try again."
  return successMsg if errMsg == "" else errMsg

# Четвертая задача - палиндром ли введенная строка?
def FourthTask():
  msg = ""
  inStr = input("\nPlease enter the phrase without line break:\n")
  try:
    if isinstance(int(inStr),int) == True:
      msg = "The entered data is not a phrase."
  except Exception as E:
    inStr = (re.sub(r'[^A-Za-zА-Яа-я0-9]', '', inStr)).lower()

    if len(inStr) <= 500:
      leftBorder = 0
      rightBorder = len(inStr) -1
      while (leftBorder < rightBorder):
          if (inStr[leftBorder] != inStr[rightBorder]):
            msg = "\nThe data you specified is not a palindrome."
            break           
          leftBorder+=1
          rightBorder-=1
      msg = "\nSUCCESS! The phrase you entered is a palindrome." if msg == "" else msg
    else:
      msg = "\nThe maximum string length of 500 characters has been exceeded."
  return msg
    
  

  