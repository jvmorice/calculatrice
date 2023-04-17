"""Just another calculator in Python."""

import tkinter as tk


class Calculatrice():

# -------------------------------- MAIN WINDOW --------------------------------

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Calculatrice')
        self.root.resizable(False, False)

        self.string = ''
        self.control = ''

        self.entry_font = ('Verdana', 20)
        self.button_font = ('Verdana', 15)

        self.main_frame()
        self.entry_field(0, 0)

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
        self.root.bind('<Key>', self.press_key)
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

    def display(self, string):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.string)

    def is_result(self):
        """Verify if the number in the entry is a result of a calculation."""
        if self.control == '*':
            self.string = '0'
            self.control = ''

    def click_allclear_button(self):
        """Clear the entry field and place an initial zero in it."""
        self.string = '0'
        self.display(self.string)

    def click_remove_button(self):
        """Remove the last entered character.

        If all characters are removed, an initial zero is placed in the field.
        """
        self.string = self.entry.get()
        self.string = self.string[:-1]
        if len(self.string) == 0:
            self.string = '0'
        self.display(self.string)

    def click_bracket_button(self, symbol):
        """Enter brackets, do auto-replacements to avoid errors."""
        self.string = self.entry.get()
        self.is_result()
        if self.string == '0' and symbol == '(':
            self.string = self.string[1:] + symbol
        elif self.string[-1].isdigit() and symbol == '(':
            self.string = self.string + '*' + symbol
        elif self.string[-1] == '.' and symbol == '(':
            self.string = self.string[:-1] + '*' + symbol
        elif self.string[-1] == ')' and symbol == '(':
            self.string = self.string + '*' + symbol
        elif self.string[-1] == '.' and symbol == ')':
            self.string = self.string[:-1] + symbol
        elif self.string[-1] in '(+-*/' and symbol == ')':
            self.string = self.string
        elif self.string.count('(') == self.string.count(')') and symbol == ')':
            self.string = self.string
        else:
            self.string = self.string + symbol
        self.display(self.string)

    def click_number_button(self, symbol):
        """Enter digits, do auto-replacements to avoid errors."""
        self.string = self.entry.get()
        self.is_result()
        if self.string == '0' and symbol.isdigit():
            self.string = self.string[1:]
        elif self.string[-1] == '0' and symbol == '.':
            self.string = self.string
        elif self.string[-1] == '.' and symbol == '.':
            self.string = self.string.rstrip('.')
        elif self.string[-1] in '(+-*/' and symbol == '.':
            self.string = self.string + '0'
        elif self.string[-1] == ')' and symbol == '.':
            self.string = self.string + '*0'
        elif self.string[-1] == ')' and symbol.isdigit():
            self.string = self.string + '*'
        self.string = self.string + symbol
        self.display(self.string)

    def click_operation_button(self, symbol):
        """Enter operation characters, do auto-replacements to avoid errors."""
        self.string = self.entry.get()
        self.is_result()
        if self.string == '0' and symbol == '-':
            self.string = self.string[1:] + symbol
        elif self.string == '0' and symbol != '-':
            self.string = self.string + symbol
        elif len(self.string) > 1 and self.string[-1] in '+-*/':
            self.string = self.string[:-1] + symbol
        elif self.string == '-':
            self.string = self.string
        elif self.string[-1] == '.':
            self.string = self.string[:-1] + symbol
        elif self.string[-1] == '(' and symbol != '-':
            self.string = self.string
        else:
            self.string = self.string + symbol
        self.display(self.string)

    def calculate(self):
        """Calculate the entered expression and output the result."""
        self.string = self.entry.get()
        if self.string[-1].isdigit() or self.string[-1] == ')':
            try:
                eval(self.string)
                if eval(self.string) * 10 % 10 == 0:
                    self.string = int(eval(self.string))
                else:
                    self.string = eval(self.string)
            except ZeroDivisionError:
                self.string = 'Division by zero'
            except (NameError, SyntaxError):
                self.string = 'Error'
        self.display(self.string)
        self.control = '*'

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
