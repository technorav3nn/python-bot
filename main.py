import sys
import os
import json
import time
import math

from functools import reduce

def clearFn():
  os.system('clear')

def mathIterable(method : str, iter : list):
  if(method == 'divide'):
    return reduce((lambda x, y: x / y), iter)
  if(method == "subtract"):
    return reduce((lambda x, y : x - y), iter)

def resetFn():
  input('Enter anything to continue...\n')
  main(False)


def main(reset : bool):
  if(reset):
    clearFn()
  clearFn()

  print('Welcome to test thingy. Commands here:')

  commandsList = [
    "Math",
    "Repeat",
    "More coming soon"
  ]

  joinedCommandArr = ', \n'.join(commandsList)

  isReset = ('\nIt seems you got an invalid command before... Make sure to type the commands only inside this list!\n' if(reset) else '\u200b')

  print(joinedCommandArr)
  print(isReset)
  print(f"\nCurrently {len(commandsList)} commands.")
  command = input("Enter your command...\n")

  isCommand = None

  loweredCommandList = map(lambda item : item.lower(), commandsList)

  if(command.lower() in list(loweredCommandList)):
    isCommand = True
  else:
    isCommand = False
  if (isCommand):
    print('is a command!')
    if(command.lower() == "math"):
      validOper = ['+', '-', '*', '/']
      oper = input('Enter operation (+, -, /, *).\n')

      if(oper in validOper):
        print('Enter math, enter numbers like: \"11 11\" (will return 22)')
        maths = input().split()

        for i in range(len(maths)):  
          maths[i] = int(maths[i]) 

        print(f"Sum = {sum(maths)}") if(oper == str("+")) else print(f"Answer of multiplication: {math.prod(maths)}") if(oper == str("*")) else print(f"Divided answer: {mathIterable('divide', maths)}") if(oper == str("/")) else print(f"Subtraction answer: {mathIterable('subtract', maths)}") if(oper == str("-")) else print("That is not an operator") and main(True)

        time.sleep(3)
        print('returning...')
        time.sleep(1)
        main(False)

      else:
        input('Invalid operator! Enter anything to continue...')
        time.sleep(0.3)
        main(True)

    elif(command.lower() == "repeat"):
      repeatText = input('Enter text to repeat\n')
      print('Reading your text...')
      time.sleep(0.2)
      print(f"Repeated text: \n{str(repeatText)}")
      resetFn()

  elif(not isCommand):
    print('Not a command! Resetting...')
    time.sleep(3)
    main(True)
    
main(False)