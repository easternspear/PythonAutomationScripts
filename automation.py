import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QShortcut
from PySide2.QtCore import QFile, Qt, QEvent
from PySide2.QtGui import QKeySequence
from ui_automation import Ui_MainWindow
from util import *

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.connectButtonEvents()
    self.shortcutBinding()
    self.importUtil()

  def shortcutBinding(self):
    addClick = QShortcut(QKeySequence("Alt+q"),self)
    addClick.activated.connect(self.instructionAddClick)
    addSleep = QShortcut(QKeySequence("Alt+w"),self)
    addSleep.activated.connect(self.instructionAddSleep)
    addPress = QShortcut(QKeySequence("Alt+e"),self)
    addPress.activated.connect(self.instructionAddPress)
    addHotkey = QShortcut(QKeySequence("Alt+r"),self)
    addHotkey.activated.connect(self.instructionAddHotkey)
    addWrite = QShortcut(QKeySequence("Alt+a"),self)
    addWrite.activated.connect(self.instructionAddWrite)
    addWaitImage = QShortcut(QKeySequence("Alt+s"),self)
    addWaitImage.activated.connect(self.instructionAddWaitImage)
    addClickImage = QShortcut(QKeySequence("Alt+d"),self)
    addClickImage.activated.connect(self.instructionAddClickImage)
    addClickAllImage = QShortcut(QKeySequence("Alt+f"),self)
    addClickAllImage.activated.connect(self.instructionAddClickAllImage)
    clearInstruction = QShortcut(QKeySequence("Alt+x"),self)
    clearInstruction.activated.connect(self.instructionClear)
    openTxtFile = QShortcut(QKeySequence("Ctrl+o"),self)
    openTxtFile.activated.connect(self.readPyFile)
    saveTxtFile = QShortcut(QKeySequence("Ctrl+s"),self)
    saveTxtFile.activated.connect(self.savePyFile)

  def connectButtonEvents(self):
    self.ui.btn_file.clicked.connect(self.readPyFile)
    self.ui.btn_add_click.clicked.connect(self.instructionAddClick)
    self.ui.btn_add_sleep.clicked.connect(self.instructionAddSleep)
    self.ui.btn_add_press.clicked.connect(self.instructionAddPress)
    self.ui.btn_add_hotkey.clicked.connect(self.instructionAddHotkey)
    self.ui.btn_add_write.clicked.connect(self.instructionAddWrite)
    self.ui.btn_add_wait_image.clicked.connect(self.instructionAddWaitImage)
    self.ui.btn_add_click_image.clicked.connect(self.instructionAddClickImage)
    self.ui.btn_add_click_all_image.clicked.connect(self.instructionAddClickAllImage)
    self.ui.btn_clear_instruction.clicked.connect(self.instructionClear)
    self.ui.btn_save.clicked.connect(self.savePyFile)

  def readPyFile(self):
    file = ChoosePyFile()
    if file[0] is not "":
      self.ui.txt_file.setText(file[0])
      self.instructionSetTxt(ReadFile(file[0]))

  def savePyFile(self):
    filename = self.ui.txt_file.text()

    if filename is "":
      file = SavePyFile()
      if file[0] is not "":
        WriteFile(file[0],"w",self.instructionGetTxt())  
        self.ui.txt_file.setText(file[0])
    else:
      WriteFile(filename,"w",self.instructionGetTxt())   
      self.ui.txt_file.setText(filename)

  def importUtil(self):
    self.ui.txt_instructions.setPlainText("from util import *\n\npyautogui.PAUSE = 0.5\n\nswitchapp()\n")

  def instructionAddClick(self):
    x,y = GetMousePosition()
    self.instructionAddTxt("pyautogui.click("+str(x)+","+str(y)+")")

  def instructionAddSleep(self):
    self.instructionAddTxt("time.sleep(1)")

  def instructionAddPress(self):
    self.instructionAddTxt("pyautogui.press('enter')")

  def instructionAddHotkey(self):
    self.instructionAddTxt("pyautogui.hotkey('ctrl', 'c')")

  def instructionAddWrite(self):                
    self.instructionAddTxt("pyautogui.write('message')")                

  def instructionAddWaitImage(self):
    self.instructionAddTxt("waitImage('imagepath')")

  def instructionAddClickImage(self):
    self.instructionAddTxt("waitClickImage('imagepath')")

  def instructionAddClickAllImage(self):    
    self.instructionAddTxt("waitClickAllImage('imagepath')")

  def instructionGetTxt(self):
    return self.ui.txt_instructions.toPlainText()

  def instructionSetTxt(self,instruction):
    self.ui.txt_instructions.setPlainText(instruction)

  def instructionAddTxt(self,instruction):
    txt = self.instructionGetTxt()
    txt += instruction + "\n"
    self.instructionSetTxt(txt)

  def instructionClear(self):
    self.instructionSetTxt("")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())