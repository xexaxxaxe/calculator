import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("380x560")
window.resizable(False, False)
window.configure(bg="#F8F5FA")

display = tk.Entry(
    window,
    font=("Arial", 30, "bold"),
    bg="#EAF7FF",
    fg="#4A4A5A",
    insertbackground="#4A4A5A",
    justify="right",
    bd=0
)

display.pack(
    padx=20,
    pady=(25, 15),
    ipady=18,
    fill="x"
)

button_frame = tk.Frame(
    window,
    bg="#F8F5FA"
)

button_frame.pack(
    padx=20,
    fill="both",
    expand=True
)


def add_to_display(value):
    display.insert(tk.END, value)


def clear_display():
    display.delete(0, tk.END)


def delete_last():
    current = display.get()

    if current:
        display.delete(len(current) - 1, tk.END)


def calculate():
    try:
        expression = display.get()

        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")
        expression = expression.replace("−", "-")

        result = eval(expression)

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Нельзя делить на 0")

    except:
        display.delete(0, tk.END)
        display.insert(0, "Ошибка")


def create_button(
    text,
    row,
    column,
    command,
    bg="#FFFFFF",
    fg="#555566"
):
    button = tk.Button(
        button_frame,
        text=text,
        command=command,
        font=("Arial", 18, "bold"),
        bg=bg,
        fg=fg,
        activebackground="#E8DDF8",
        activeforeground="#555566",
        bd=0,
        relief="flat",
        cursor="hand2"
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5,
        sticky="nsew"
    )


for i in range(4):
    button_frame.columnconfigure(i, weight=1)

for i in range(5):
    button_frame.rowconfigure(i, weight=1)


create_button(
    "C", 0, 0,
    clear_display,
    "#FFD6E5",
    "#C94F7C"
)

create_button(
    "⌫", 0, 1,
    delete_last,
    "#E5F5FF",
    "#4A91B8"
)

create_button(
    "÷", 0, 2,
    lambda: add_to_display("÷"),
    "#CDEEFF",
    "#3685B5"
)

create_button(
    "×", 0, 3,
    lambda: add_to_display("×"),
    "#CDEEFF",
    "#3685B5"
)


create_button("7", 1, 0, lambda: add_to_display("7"))
create_button("8", 1, 1, lambda: add_to_display("8"))
create_button("9", 1, 2, lambda: add_to_display("9"))

create_button(
    "−", 1, 3,
    lambda: add_to_display("−"),
    "#CDEEFF",
    "#3685B5"
)


create_button("4", 2, 0, lambda: add_to_display("4"))
create_button("5", 2, 1, lambda: add_to_display("5"))
create_button("6", 2, 2, lambda: add_to_display("6"))

create_button(
    "+", 2, 3,
    lambda: add_to_display("+"),
    "#CDEEFF",
    "#3685B5"
)


create_button("1", 3, 0, lambda: add_to_display("1"))
create_button("2", 3, 1, lambda: add_to_display("2"))
create_button("3", 3, 2, lambda: add_to_display("3"))

create_button(
    "=", 3, 3,
    calculate,
    "#F4BBD0",
    "#A63F68"
)


create_button("0", 4, 0, lambda: add_to_display("0"))
create_button(".", 4, 1, lambda: add_to_display("."))
create_button("(", 4, 2, lambda: add_to_display("("))
create_button(")", 4, 3, lambda: add_to_display(")"))


window.mainloop()
