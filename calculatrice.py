import tkinter as tk
import tkinter.messagebox as mb

class Calculatrice():

# -------------------------------- MAIN WINDOW --------------------------------
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Calculatrice')
        self.root.config(bg='#FFFFFF')
        self.grid_format()
        
        self.entry(0, 0)
        
        self.allclear_button('AC', 1, 0)
        self.bracket_button('(', 1, 1)
        self.bracket_button(')', 1, 2)
        self.remove_button('<', 1, 3)
        
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
        self.root.mainloop()
        
# ----------------------------- CREATING WIDGETS ------------------------------
        
    def grid_format(self):
        for column in range(0, 4, 1):
            self.root.grid_columnconfigure(column, minsize=75)
       
        for row in range(1, 6, 1):
            self.root.grid_rowconfigure(row, minsize=75)
        
    def entry(self, x, y):
        """ Creates an input field and puts a number zero in it """
        self.entry = tk.Entry(self.root, justify='right', relief=tk.FLAT, font=('Verdana', 20))
        self.entry.insert(0, '0')
        self.entry.grid(row=x, column=y, columnspan=5, sticky='we', padx=2, pady=2)
    
    def number_button(self, symbol, x, y):
        """ Creates a button entering a digit or a dot """
        self.button = tk.Button(self.root, text=symbol, bg='#FFFFFF', relief=tk.FLAT, font=('Verdana', 15), 
                                command=lambda : self.click_number_button(symbol))
        self.button.grid(row=x, column=y, sticky='wens', padx=2, pady=2)
        
    def operation_button(self, symbol, x, y):
        """ Creates an operation button """
        self.button = tk.Button(self.root, text=symbol, bg='#CFCFCF', relief=tk.FLAT, font=('Verdana', 15), 
                                command=lambda : self.click_operation_button(symbol))
        self.button.grid(row=x, column=y, sticky='wens', padx=2, pady=2)
    
    def bracket_button(self, symbol, x, y):
        """ Creates a bracket button """
        self.button = tk.Button(self.root, text=symbol, bg='#CFCFCF', relief=tk.FLAT, font=('Verdana', 15), 
                                command=lambda : self.click_bracket_button(symbol))
        self.button.grid(row=x, column=y, sticky='wens', padx=2, pady=2)    
    
    def result_button(self, symbol, x, y):
        self.button = tk.Button(self.root, text=symbol, bg='#4890E1', relief=tk.FLAT, font=('Verdana', 15), 
                                command=self.calculate)
        self.button.grid(row=x, column=y, sticky='wens', padx=2, pady=2)

    def remove_button(self, symbol, x, y):
        self.button = tk.Button(self.root, text=symbol, bg='#CFCFCF', relief=tk.FLAT, font=('Verdana', 15), 
                                command=self.click_remove_button)
        self.button.grid(row=x, column=y, sticky='wens', padx=2, pady=2)
    
    def allclear_button(self, symbol, x, y):
        self.button = tk.Button(self.root, text=symbol, bg='#CFCFCF', relief=tk.FLAT, font=('Verdana', 15), 
                                command=self.click_allclear_button)
        self.button.grid(row=x, column=y, sticky='wens', padx=2, pady=2)

# ------------------------------- PROGRAM LOGIC -------------------------------

    def click_allclear_button(self):
        """ Clears the entry field """
        self.entry.delete(0, tk.END)
        self.entry.insert(0, '0')
    
    def click_remove_button(self):
        """ Removes the last entered character """
        self.string = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.string[0:-1])
    
    def click_number_button(self, symbol):
        """ Enters digits
        
        The starting zero is replaced by the entered digit. The starting zero 
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
        
    def click_bracket_button(self, symbol):
        """ Enters brackets 
        
        An opening bracket is entered only after the operation character, 
        or after another opening bracket or at the beginning, otherwise an error 
        message is displayed. A closing bracket is entered only after 
        a number character and only if the number of opening brackets does not 
        exceed the number of closing brackets, including the entered one.
        """
        
        self.string = self.entry.get()
        if self.string == '0' and symbol == '(':
            self.string = self.string[1:]
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, symbol)
        elif self.string[-1] not in '+-*/(' and symbol == '(' :
            mb.showerror('Attention!', 'Enter an operation symbol (+, -, * or /)')
        elif self.string.count('(') <= self.string.count(')') and symbol == ')':
            mb.showerror('Attention!', 'Excessive closing bracket')
        else:
            self.entry.insert(tk.END, symbol)
        
    def click_operation_button(self, symbol):
        """ Enters operation characters
        
        Enters an operation character after a number or a bracket. If an operation 
        character is enterd after another operation character, the previous one 
        is deleted. Negative numbers can be entered only at the beginning of 
        an expression or after an opening bracket.
        """
        
        self.string = self.entry.get()
        if self.string != '0' and self.string[-1] in '+-*/':
            self.string = self.string[:-1]
        elif self.string == '0' and symbol == '-':
            self.string = ''
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.string + symbol)

    def calculate(self):
        """ Calculates the entered expression and outputs the result """
        self.string = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, eval(self.string))
    
# -----------------------------------------------------------------------------

calculatrice = Calculatrice()
calculatrice.run()