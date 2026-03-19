
def calculateBMI(height, weight, root,tk):
    if height <= 0 or weight <= 0:
        inputWarning=tk.Label(root, text="Height/Weight must be greater than zero.", font=("Helvetica", 10), fg="red")
        inputWarning.grid(column=1, row=8)
        root.after(2000, lambda: inputWarning.grid_forget())
        return 
        
    bmi_value = 703 * (weight / (height**2))
    bmi_label = tk.Label(root, text=f"Your BMI: {round(bmi_value, 2)}", font=("Helvetica", 12, "bold"), justify="center")
    bmi_label.grid(column=1, row=8)
    return round(bmi_value, 2)

def openHomeScreen():
    from my_package.vars import changeScreen
    changeScreen(3)
    
def setup(root, tk):
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)
    weight_var = tk.IntVar()
    height_var = tk.IntVar()
    bmi_header = tk.Label(root, text="BMI Calculator", font=("Helvetica", 16),justify="center")
    bmi_header.grid(column=1, row=0)
    disclaimer1 = tk.Label(root, text="DISCLAIMER: For accurate health info,", font=("Helvetica", 10), fg="red")
    disclaimer1.grid(column=1, row=1, sticky="s")
    disclaimer2 = tk.Label(root, text="PLEASE speak to your doctor.", font=("Helvetica", 10), fg="red")
    disclaimer2.grid(column=1, row=2, sticky="n")
    tk.Label(root, text="Enter weight (lbs):").grid(column=1, row=3)
    tk.Entry(root, textvariable=weight_var).grid(column=1, row=4)
    tk.Label(root, text="Enter height (inches):").grid(column=1, row=5)
    tk.Entry(root, textvariable=height_var).grid(column=1, row=6)
    calculate_btn = tk.Button(
        root, 
        text="Calculate BMI", 
        command=lambda: calculateBMI(height_var.get(), weight_var.get(), root,tk)
    )
    backBtn = tk.Button(root, text="Back to Home", command=lambda: openHomeScreen(),justify="center")
    backBtn.grid(column=1, row=9)
    calculate_btn.grid(column=1, row=7)
    return [bmi_header, disclaimer1, disclaimer2, backBtn, calculate_btn]

if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    root.title("T&X Fitness")
    root.geometry("500x850")
    setup(root, tk)
    root.mainloop() 