import tkinter as tk
from frontend import BMICalculator
def testBMICalculatorFail():
    #this will fail not correct bmi correst bmi that will pass is 25.82 while 100.0 will fail
    fake_root = tk.Tk()
    result = BMICalculator.calculateBMI(70, 180, fake_root)
    assert result == 100.0

def testBMICalculatorPass():
    fake_root = tk.Tk()
    result = BMICalculator.calculateBMI(70, 180, fake_root)
    assert result == 25.82