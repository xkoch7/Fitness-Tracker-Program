import tkinter as tk
from frontend import BMICalculator
from unittest.mock import MagicMock
def testBMICalculatorFail():
    #this will fail not correct bmi correst bmi that will pass is 25.82 while 100.0 will fail

    result = BMICalculator.calculateBMI(70, 180, MagicMock())
    assert result != 100.0

def testBMICalculatorPass():
    tk.Tk = MagicMock()
    result = BMICalculator.calculateBMI(70, 180, MagicMock())
    assert result == 25.82