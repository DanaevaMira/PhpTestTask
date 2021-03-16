import function as f

def main():
  taskNum = 0
  result = ""
  exitFlag = ""
  commonErrMsg = "\nAn error has occurred. You may have entered incorrect data. Try again."
  while (taskNum != 5 or (taskNum == 5 and exitFlag == "0")):
    try:
      taskNum = int(input("\n\nReference:\nTask 1. Write a set of random numbers to a file;\nTask 2. Sort numbers from task 1;\nTask 3. Raise a given number to a given power;\nTask 4. Determine if a phrase is a palindrome.\n\nTo exit the program, press '5'. \n\nEnter the task number from '1', '2', '3', '4' or press '5' if you want to quit the program: \n"))      
      if taskNum == 1:
        result = f.FirstTask()
      elif taskNum == 2:
        result = f.SecondTask()
      elif taskNum == 3:
        result = f.ThirdTask()
      elif taskNum == 4:
        result = f.FourthTask()	
      elif taskNum == 5:
        exitFlag = input("\nAre you sure you want to exit?\nEnter '1'-- if you want to exit and '0'-- if not.\n")
        if exitFlag not in ("0", "1"):
          print("\nAn error has occurred. The program has been completed ahead of schedule.")
        elif exitFlag == "1":
          print("\nThe program has been successfully completed.")
      else:
        print(commonErrMsg)
        break
      if taskNum in (1,2,3,4):
        print(result)
    except Exception as E:
      print(commonErrMsg)
      break

if __name__ == "__main__":
    main()
    




    







