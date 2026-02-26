import tkinter as tk
from frontend import BMICalculator
def testBMICalculatorFail():
    #this will fail height less than 0 will fail
    fake_root = tk.Tk()
    result = BMICalculator.calculateBMI(-10, 180, fake_root)
    assert result == False
    # this fails weight less than 0 will fail
    result = BMICalculator.calculateBMI(70, -10, fake_root) 
    assert result == False

def testBMICalculatorPass():
    fake_root = tk.Tk()
    result = BMICalculator.calculateBMI(70, 180, fake_root)
    assert result == 25.82