from tkinter import *

class Calculator(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('312x324')
        self.title('Fun coding by Peter!')
        self.resizable(False, False)
        self.iconbitmap('user_target_person_man_icon_193936.ico')
        self.expression = ''

        self.create_widgets()

    def btn_clear(self):
        self.expression = ""
        self.input_text.set("")

    def btn_click(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def btn_equal(self):
        self.result = str(eval(self.expression))
        self.input_text.set(self.result)
        self.expression = ""

    def create_widgets(self):
        self.input_text = StringVar()
        self.input_frame = Frame(self, width=300, height=50, bd=0,
                                 highlightbackground="white", highlightcolor="whitesmoke", highlightthickness=0.5)
        self.input_frame.pack(side=TOP)

        self.input_field = Entry(self.input_frame, font=('Trebuchet MS', 18),
                                 textvariable=self.input_text, width=50, bg="#D9D9D9", bd=0, justify=RIGHT, fg='black')
        self.input_field.grid(column=0, row=0)
        self.input_field.pack(ipady=10)

        self.button_frame = Frame(self, width=300, height=350, bg="whitesmoke")
        self.button_frame.pack()

        self.clear_button = Button(self.button_frame,  text="Clear", fg="black", width=21,
                                   height=3, bd=0, bg='#D9D9D9', cursor="hand2", justify=LEFT, command=self.btn_clear)
        self.clear_button.grid(row=0, column=0, columnspan=2, padx=1, pady=1)

        self.division_button = Button(self.button_frame, text='/', fg='black', width=10, height=3,
                                      bd=0, bg='#D9D9D9', cursor='hand2', command=lambda: self.btn_click('/'))
        self.division_button.grid(row=0, column=2, padx=1, pady=1)

        self.multiplication_button = Button(self.button_frame, text='*', fg='black', width=10, height=3,
                                            bd=0, bg='#D9D9D9', cursor='hand2', command=lambda: self.btn_click('*'))
        self.multiplication_button.grid(row=0, column=3, padx=1, pady=1)

        self.minus_button = Button(self.button_frame, text='-', fg='black', width=10, height=3,
                                   bd=0, bg='#D9D9D9', cursor='hand2', command=lambda: self.btn_click('-'))
        self.minus_button.grid(row=1, column=3, padx=1, pady=1)

        self.seven_button = Button(self.button_frame,  text="7", fg="black", width=10,
                                   height=3, bd=0, bg='#F2F2F2', cursor="hand2", justify=LEFT, command=lambda: self.btn_click(7))
        self.seven_button.grid(row=1, column=0, padx=1, pady=1)

        self.eight_button = Button(self.button_frame, text='8', fg='black', width=10, height=3,
                                   bd=0, bg='#F2F2F2', cursor='hand2', command=lambda: self.btn_click(8))
        self.eight_button.grid(row=1, column=1, padx=1, pady=1)

        self.nine_button = Button(self.button_frame, text='9', fg='black', width=10, height=3,
                                  bd=0, bg='#F2F2F2', cursor='hand2', command=lambda: self.btn_click(9))
        self.nine_button.grid(row=1, column=2, padx=1, pady=1)

        self.plus_button = Button(self.button_frame, text='+', fg='black', width=10, height=3,
                                  bd=0, bg='#D9D9D9', cursor='hand2', command=lambda: self.btn_click('+'))
        self.plus_button.grid(row=2, column=3, padx=1, pady=1)

        self.for_button = Button(self.button_frame,  text="4", fg="black", width=10,
                                 height=3, bd=0, bg='#F2F2F2', cursor="hand2", justify=LEFT, command=lambda: self.btn_click(4))
        self.for_button.grid(row=2, column=0, padx=1, pady=1)

        self.five_button = Button(self.button_frame, text='5', fg='black', width=10, height=3,
                                  bd=0, bg='#F2F2F2', cursor='hand2', command=lambda: self.btn_click(5))
        self.five_button.grid(row=2, column=1, padx=1, pady=1)

        self.six_button = Button(self.button_frame, text='6', fg='black', width=10, height=3,
                                 bd=0, bg='#F2F2F2', cursor='hand2', command=lambda: self.btn_click(6))
        self.six_button.grid(row=2, column=2, padx=1, pady=1)

        self.one_button = Button(self.button_frame,  text="1", fg="black", width=10,
                                 height=3, bd=0, bg='#F2F2F2', cursor="hand2", justify=LEFT, command=lambda: self.btn_click(1))
        self.one_button.grid(row=3, column=0, padx=1, pady=1)

        self.two_button = Button(self.button_frame, text='2', fg='black', width=10, height=3,
                                 bd=0, bg='#F2F2F2', cursor='hand2', command=lambda: self.btn_click(2))
        self.two_button.grid(row=3, column=1, padx=1, pady=1)

        self.three_button = Button(self.button_frame, text='3', fg='black', width=10, height=3,
                                   bd=0, bg='#F2F2F2', cursor='hand2', command=lambda: self.btn_click(3))
        self.three_button.grid(row=3, column=2, padx=1, pady=1)

        self.dot_button = Button(self.button_frame, text='.', fg='black', width=10, height=3,
                                 bd=0, bg='#D9D9D9', cursor='hand2', command=lambda: self.btn_click('.'))
        self.dot_button.grid(row=3, column=3, padx=1, pady=1)

        self.zero_button = Button(self.button_frame,  text="0", fg="black", width=21,
                                  height=3, bd=0, bg='#F2F2F2', cursor="hand2", justify=LEFT, command=lambda: self.btn_click(0))
        self.zero_button.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

        self.equal_button = Button(self.button_frame,  text="=", fg="black", width=21,
                                   height=3, bd=0, bg='#D9D9D9', cursor="hand2", justify=LEFT, command=lambda: self.btn_equal())
        self.equal_button.grid(row=4, column=2, columnspan=2, padx=1, pady=1)


if __name__ == "__main__":
    calculator = App()
    calculator.mainloop()
