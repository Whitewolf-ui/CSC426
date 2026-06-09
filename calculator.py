import tkinter as tk

# ---------------- Functions ---------------- #
expression = ""

def press(value):
    global expression
    expression += str(value)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def equal():
    global expression
    try:
        result = str(eval(expression.replace("^", "**")))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# ---------------- Window ---------------- #
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("500x700")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

equation = tk.StringVar()

# ---------------- Display ---------------- #
display = tk.Entry(
    root,
    textvariable=equation,
    font=("Arial", 28),
    justify="right",
    bd=10,
    relief=tk.RIDGE,
    bg="white"
)

display.pack(fill="both", padx=15, pady=20, ipady=20)

# ---------------- Button Frame ---------------- #
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(expand=True, fill="both")

buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", "%", "^", "="]
]

for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        if text == "=":
            cmd = equal
            color = "#4CAF50"
        elif text == "C":
            cmd = clear
            color = "#FF5722"
        else:
            cmd = lambda t=text: press(t)
            color = "#333333"

        button = tk.Button(
            frame,
            text=text,
            font=("Arial", 22, "bold"),
            bg=color,
            fg="white",
            command=cmd,
            relief=tk.RAISED,
            bd=4
        )

        button.grid(
            row=r,
            column=c,
            sticky="nsew",
            padx=5,
            pady=5
        )

# Make buttons resize evenly
for i in range(5):
    frame.rowconfigure(i, weight=1)

for i in range(4):
    frame.columnconfigure(i, weight=1)

root.mainloop()