import sys
from PyQt5 import QtWidgets, uic

class Calculator (QtWidgets.QMainWindow):

    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = uic.loadUi('design.ui', self)  #can also use generated code, I prefer ui file
        self.show()

        self.ui.reset.clicked.connect(self.button_clicked)
        self.ui.sign.clicked.connect(self.button_clicked)
        self.ui.percent.clicked.connect(self.button_clicked)
        self.ui.divide.clicked.connect(self.button_clicked)
        self.ui.multiply.clicked.connect(self.button_clicked)
        self.ui.subtract.clicked.connect(self.button_clicked)
        self.ui.add.clicked.connect(self.button_clicked)
        self.ui.equal.clicked.connect(self.button_clicked)
        self.ui.nine.clicked.connect(self.button_clicked)
        self.ui.eight.clicked.connect(self.button_clicked)
        self.ui.seven.clicked.connect(self.button_clicked)
        self.ui.six.clicked.connect(self.button_clicked)
        self.ui.five.clicked.connect(self.button_clicked)
        self.ui.four.clicked.connect(self.button_clicked)
        self.ui.three.clicked.connect(self.button_clicked)
        self.ui.two.clicked.connect(self.button_clicked)
        self.ui.one.clicked.connect(self.button_clicked)
        self.ui.zero.clicked.connect(self.button_clicked)
        self.ui.dot.clicked.connect(self.button_clicked)


        self.left = 0
        self.right = 0
        self.action = None
        self.result = 0
        self.last_action = None
        self.memory = 0

        self.action_map = {
        "÷": self.divide_function, 
        "x": self.multiply_function, 
        "+": self.add_function,
        "-": self.subtract_function      
        }


    def button_clicked(self):
        print(f"{self.sender().text()} clicked")
        clicked_button  = self.sender().text().lower()

        if clicked_button == "ac":
            self.ui.display.setText("0 ")
            self.memory = 0
            
        elif clicked_button == "c":
            self.ui.display.setText("0 ")
            self.ui.reset.setText("AC")
            self.memory = 0

        elif clicked_button  in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.ui.reset.setText("C")
            self.ui.display.setText(f"{self.ui.display.text().lstrip('0')}{clicked_button}")

        elif clicked_button == ".":
            self.ui.reset.setText("C")
            if "."  not in self.ui.display.text(): self.ui.display.setText(f"{self.ui.display.text().lstrip('0')}{clicked_button}")

        elif clicked_button == "%":
            self.left = float(self.ui.display.text())
            self.right = 100
            self.result = self.divide_function(self.left, self.right)
            self.ui.display.setText(f"{self.result}")
            self.memory  = self.result

        elif clicked_button == "+/-":
            self.left = float(self.ui.display.text())
            self.right = -1
            self.result = self.multiply_function(self.left, self.right)
            self.ui.display.setText(f"{self.result}")
            self.memory  = self.result
    
        elif clicked_button in ["÷", "x", "+", "-"]:
            self.left = float(self.ui.display.text())
            self.ui.display.setText("0 ") #clears the input screen
            self.action = clicked_button  # store the operation somewhere

        elif clicked_button == "=":

            if clicked_button != self.last_action: self.right = float(self.ui.display.text())  #only updates if  new operation and not just double equals
            else: self.left = self.result #results from last operation

            self.result = self.action_map.get(self.action)(self.left, self.right)
            self.ui.display.setText(f"{self.result}")
            self.memory = self.result
        
        self.last_action = clicked_button

    def add_function(self, left, right):
        return left + right
    
    def subtract_function(self, left, right):
        return  left - right

    def multiply_function(self, left, right):
        return left * right

    def divide_function(self, left, right):
        return  left / right


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window =  Calculator()
    sys.exit(app.exec_())