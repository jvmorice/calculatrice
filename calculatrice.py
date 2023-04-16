import tkinter as tk
import tkinter.messagebox as mb

class Calculatrice():

# -------------------------------- MAIN WINDOW --------------------------------

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Calculatrice')
        self.root.resizable(False, False)
        self.root.bind('<Key>', self.press_key)

        self.entry_font = ('Verdana', 20)
        self.button_font = ('Verdana', 15)

        self.main_frame()
        self.entry_field(0, 0)

        self.string = ''

        self.allclear_button('AC', 1, 0)
        self.bracket_button('(', 1, 1)
        self.bracket_button(')', 1, 2)
        self.remove_button('⌫', 1, 3)

        self.number_button('7', 2, 0)
        self.number_button('8', 2, 1)
        self.number_button('9', 2, 2)
        self.operation_button('/', 2, 3)

        self.number_button('4', 3, 0)
        self.number_button('5', 3, 1)
        self.number_button('6', 3, 2)
        self.operation_button('*', 3, 3)

        self.number_button('1', 4, 0)
        self.number_button('2', 4, 1)
        self.number_button('3', 4, 2)
        self.operation_button('-', 4, 3)

        self.number_button('0', 5, 0)
        self.number_button('.', 5, 1)
        self.result_button('=', 5, 2)
        self.operation_button('+', 5, 3)

    def run(self):
        """Call the window and keep it open."""
        self.root.mainloop()

# ----------------------------- CREATING WIDGETS ------------------------------

    def main_frame(self):
        """Create a frame and set its parameters."""
        self.frame = tk.Frame(self.root, padx=30, pady=30, bg='#FFFFFF')
        for col in range(0, 4, 1):
            self.frame.columnconfigure(col, minsize=75, weight=1)
        for row in range(1, 6, 1):
            self.frame.rowconfigure(row, minsize=75, weight=1)
        self.frame.pack()

    def entry_field(self, row, col):
        """Create an input field and puts a number zero in it."""
        self.entry = tk.Entry(self.frame, justify='right', relief=tk.FLAT,
                              font=self.entry_font)
        self.entry.insert(0, '0')
        self.entry.grid(row=row, column=col, columnspan=5,
                        sticky='we', padx=2, pady=2)

    def allclear_button(self, symbol, row, col):
        """Create the button clearing the entry field."""
        self.button = tk.Button(self.frame, text=symbol, bg='#CFCFCF',
                                relief=tk.FLAT, font=self.button_font,
                                command=self.click_allclear_button)
        self.button.grid(row=row, column=col, sticky='wens', padx=2, pady=2)

    def remove_button(self, symbol, row, col):
        """Create the backspace button."""
        self.button = tk.Button(self.frame, text=symbol, bg='#CFCFCF',
                                relief=tk.FLAT, font=self.button_font,
                                command=self.click_remove_button)
        self.button.grid(row=row, column=col, sticky='wens', padx=2, pady=2)

    def bracket_button(self, symbol, row, col):
        """Create a bracket button."""
        self.button = tk.Button(self.frame, text=symbol, bg='#CFCFCF',
                                relief=tk.FLAT, font=self.button_font,
                                command=lambda:
                                    self.click_bracket_button(symbol))
        self.button.grid(row=row, column=col, sticky='wens', padx=2, pady=2)

    def number_button(self, symbol, row, col):
        """Create a button entering a digit or a dot."""
        self.button = tk.Button(self.frame, text=symbol, bg='#FFFFFF',
                                relief=tk.FLAT, font=self.button_font,
                                command=lambda:
                                    self.click_number_button(symbol))
        self.button.grid(row=row, column=col, sticky='wens', padx=2, pady=2)

    def operation_button(self, symbol, row, col):
        """Create an operation button."""
        self.button = tk.Button(self.frame, text=symbol, bg='#CFCFCF',
                                relief=tk.FLAT, font=self.button_font,
                                command=lambda:
                                    self.click_operation_button(symbol))
        self.button.grid(row=row, column=col, sticky='wens', padx=2, pady=2)

    def result_button(self, symbol, row, col):
        """Create the button calculating the entered expression."""
        self.button = tk.Button(self.frame, text=symbol, bg='#4890E1',
                                relief=tk.FLAT, font=self.button_font,
                                command=self.calculate)
        self.button.grid(row=row, column=col, sticky='wens', padx=2, pady=2)

# ------------------------------- PROGRAM LOGIC -------------------------------

    def click_allclear_button(self):
        """Clear the entry field and place an initial zero in it."""
        self.entry.delete(0, tk.END)
        self.entry.insert(0, '0')

    def click_remove_button(self):
        """Remove the last entered character.

        If all characters are removed, an initial zero is placed in the field.
        """
        self.string = self.entry.get()
        self.string = self.string[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.string)
        if len(self.string) == 0:
            self.entry.insert(0, '0')

    def click_bracket_button(self, symbol):
        """Enter brackets.

        If an opening bracket is entered after a digit, the multiplication sign
        is placed before the bracket.
        If an opening bracket is entered after the dot, the dot is deleted and
        the multiplication sign is placed between the digit and the bracket.
        If a closing bracket is entered right after the opening one,
        the input of the closing bracket is blocked.
        A closing bracket can be entered only if the number of opening brackets
        does not exceed the number of closing brackets, including the
        entered one.
        """
        self.string = self.entry.get()
        if self.string == '0' and symbol == '(':
            self.string = self.string[1:] + symbol
        elif self.string[-1].isdigit() and symbol == '(':
            self.string = self.string + '*' + symbol
        elif self.string[-1] == '.' and symbol == '(':
            self.string = self.string[:-1] + '*' + symbol
        elif self.string[-1] == '(' and symbol == ')':
            self.string = self.string
        elif self.string.count('(') > self.string.count(')') and symbol == ')':
            self.string = self.string + symbol
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.string)

    def click_number_button(self, symbol):
        """Enter digits.

        The initial zero is replaced by the entered digit. The initial zero
        is saved, if the second character is a dot. If a dot is entered
        after an operation character, a zero is inserted before it, for example
        '5*.2' is replaced by '5*0.2'.
        """
        self.string = self.entry.get()
        if self.string == '0' and symbol != '.':
            self.string = self.string[1:]
        elif self.string[-1] in '+-*/' and symbol == '.':
            self.string = self.string + '0'
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.string + symbol)


    def click_operation_button(self, symbol):
        """Enter operation characters.

        Enter an operation character after a number or a bracket. If an operation
        character is entered after another operation character, the previous one
        is deleted. Negative numbers can be entered only at the beginning of
        an expression or after an opening bracket. If an operation character is
        entered after the dot, the dot is deleted, for example '5.+' is
        replaced by '5+'.
        """
        self.string = self.entry.get()
        if self.string != '0' and self.string[-1] in '+-*/':
            self.string = self.string[:-1]
        elif self.string == '0' and symbol == '-':
            self.string = ''
        elif self.string[-1] == '.':
            self.string = self.string[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.string + symbol)

    def calculate(self):
        """Calculate the entered expression and outputs the result."""
        self.string = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, eval(self.string))

    def press_key(self, event):
        """Link keys with the main window.

        Keys: operation keys, number keys, dot, brackets, backspace, enter.
        """
        if event.char.isdigit() or event.char == '.':
            self.click_number_button(event.char)
        elif event.char in '+-*/':
            self.click_operation_button(event.char)
        elif event.char in '()':
            self.click_bracket_button(event.char)
        elif event.char == '\x08':
            self.click_remove_button()
        elif event.char == '\r':
            self.calculate()

# -----------------------------------------------------------------------------


calculatrice = Calculatrice()
calculatrice.run()
