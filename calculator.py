from tkinter import *

# - Budowa apki
window = Tk()

# tytuł i rozmiar okna
window.title('Fun coding by Peter!')
window.geometry('312x324')
window.resizable(False, False)

# Ikona
window.iconbitmap('user_target_person_man_icon_193936.ico')

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")
 
def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
 
    expression = ""
 
expression = ""

input_text = StringVar()
input_frame = Frame(window, width=300, height=50, bd=0,
                    highlightbackground="white", highlightcolor="whitesmoke", highlightthickness=0.5)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('Trebuchet MS', 18),
                    textvariable=input_text, width=50, bg="#D9D9D9", bd=0, justify=RIGHT, fg='black')
input_field.grid(column=0, row=0)
input_field.pack(ipady=10)

button_frame = Frame(window, width=300, height=350, bg="whitesmoke")
button_frame.pack()

clear_button = Button(button_frame,  text="Clear", fg="black", width=21,
                      height=3, bd=0, bg='#D9D9D9', cursor="hand2", justify=LEFT, command=lambda: btn_clear())
clear_button.grid(row=0, column=0, columnspan=2, padx=1, pady=1)

division_button = Button(button_frame, text='/', fg='black', width=10, height=3,
                         bd=0, bg='#D9D9D9', cursor='hand2', command=lambda: btn_click('/'))
division_button.grid(row=0, column=2, padx=1, pady=1)

multiplication_button = Button(button_frame, text='*', fg='black', width=10, height=3,
                               bd=0, bg='#D9D9D9', cursor='hand2', command=lambda: btn_click('*'))
multiplication_button.grid(row=0, column=3, padx=1, pady=1)

minus_button = Button(button_frame, text='-', fg='black', width=10, height=3,
                      bd=0, bg='#D9D9D9', cursor='hand2', command=lambda: btn_click('-'))
minus_button.grid(row=1, column=3, padx=1, pady=1)

#############

seven_button = Button(button_frame,  text="7", fg="black", width=10,
                      height=3, bd=0, bg='#F2F2F2', cursor="hand2", justify=LEFT, command=lambda: btn_click(7))
seven_button.grid(row=1, column=0, padx=1, pady=1)

eight_button = Button(button_frame, text='8', fg='black', width=10, height=3,
                      bd=0, bg='#F2F2F2', cursor='hand2', command=lambda: btn_click(8))
eight_button.grid(row=1, column=1, padx=1, pady=1)

nine_button = Button(button_frame, text='9', fg='black', width=10, height=3,
                     bd=0, bg='#F2F2F2', cursor='hand2', command=lambda: btn_click(9))
nine_button.grid(row=1, column=2, padx=1, pady=1)

plus_button = Button(button_frame, text='+', fg='black', width=10, height=3,
                     bd=0, bg='#D9D9D9', cursor='hand2', command=lambda: btn_click('+'))
plus_button.grid(row=2, column=3, padx=1, pady=1)

###############

for_button = Button(button_frame,  text="4", fg="black", width=10,
                    height=3, bd=0, bg='#F2F2F2', cursor="hand2", justify=LEFT, command=lambda: btn_click(4))
for_button.grid(row=2, column=0, padx=1, pady=1)

five_button = Button(button_frame, text='5', fg='black', width=10, height=3,
                     bd=0, bg='#F2F2F2', cursor='hand2', command=lambda: btn_click(5))
five_button.grid(row=2, column=1, padx=1, pady=1)

six_button = Button(button_frame, text='6', fg='black', width=10, height=3,
                    bd=0, bg='#F2F2F2', cursor='hand2', command=lambda: btn_click(6))
six_button.grid(row=2, column=2, padx=1, pady=1)

#################

one_button = Button(button_frame,  text="1", fg="black", width=10,
                    height=3, bd=0, bg='#F2F2F2', cursor="hand2", justify=LEFT, command=lambda: btn_click(1))
one_button.grid(row=3, column=0, padx=1, pady=1)

two_button = Button(button_frame, text='2', fg='black', width=10, height=3,
                    bd=0, bg='#F2F2F2', cursor='hand2', command=lambda: btn_click(2))
two_button.grid(row=3, column=1, padx=1, pady=1)

three_button = Button(button_frame, text='3', fg='black', width=10, height=3,
                      bd=0, bg='#F2F2F2', cursor='hand2', command=lambda: btn_click(3))
three_button.grid(row=3, column=2, padx=1, pady=1)

dot_button = Button(button_frame, text='.', fg='black', width=10, height=3,
                    bd=0, bg='#D9D9D9', cursor='hand2', command=lambda: btn_click('.'))
dot_button.grid(row=3, column=3, padx=1, pady=1)

#####################

zero_button = Button(button_frame,  text="0", fg="black", width=21,
                      height=3, bd=0, bg='#F2F2F2', cursor="hand2", justify=LEFT, command=lambda: btn_click(0))
zero_button.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

equal_button = Button(button_frame,  text="=", fg="black", width=21,
                      height=3, bd=0, bg='#D9D9D9', cursor="hand2", justify=LEFT, command=lambda: btn_equal())
equal_button.grid(row=4, column=2, columnspan=2, padx=1, pady=1)


window.mainloop()
