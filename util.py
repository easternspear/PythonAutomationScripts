from PySide2.QtWidgets import *
import pyautogui
import time
import datetime

# File
def ChooseFile(f):
  return QFileDialog.getOpenFileName(None,"Choose File",dir="./",filter=f)

def ChoosePyFile():
  return ChooseFile("Python File(*.py)")

def ReadFile(file):
  try:
    f = open(file,"r")
    result = f.read()
    f.close()
    return result
  except:
    print("Cannot read file: " + file)

def WriteFile(file,m,content):
  try:
    f = open(file,mode=m)
    f.write(content)
    f.close()
  except:
    print("Cannot write to file: " + file)
    
def SaveFile(f):
  return QFileDialog.getSaveFileName(None,"Save",dir="./",filter=f)

def SavePyFile():
  return SaveFile("Python File(*.py)")

# pyautogui
def GetMousePosition():
  return pyautogui.position()

def switchapp():
  pyautogui.hotkey('alt', 'tab')

def waitImage(img):
  log('Searching image: '+ img)
  x = None
  while x == None:
    try:
      x,y = pyautogui.locateCenterOnScreen(img,grayscale=True)
      log('Result: '+ str(x)+','+str(y))
    except:
      log('Result: Not found')
  log('Found image: '+ img + " at coordinate: " + str(x)+','+str(y))    
  return x,y

def waitClickImage(img):
  result = waitImage(img)
  log('Attempt to click on image: '+img+" at coordinate: "+str(result[0])+","+ str(result[1]))    
  pyautogui.click(result[0], result[1])
  log('Click done')

def waitClickAllImage(img):
  execute = True
  log('Searching image: ' + img)
  while execute:
    try:
      x,y = pyautogui.locateCenterOnScreen(img,grayscale=True)
      log('Result: ' + str(x)+","+str(y))
      log('Attempt to click on image: '+img+" at coordinate: "+str(x)+","+ str(y))   
      pyautogui.click(x,y)
      log('Click done')
    except:
      execute = False
      log('Done')

# log      
def log(msg):
  print(datetime.datetime.now(), msg)