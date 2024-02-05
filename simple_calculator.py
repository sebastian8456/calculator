## Create a GUI-based simple calculator, 
# which can perform basic arithmetic operations.
from tkinter import *

root = Tk()

OPERATORS = ('÷','x','+','-', '%')

# Expand the window
root.geometry('350x500+150+300')
root.title('Calculator')

Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)


content = Frame(root)
content.grid(sticky='NSEW')
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=1)
content.columnconfigure(3, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)
content.rowconfigure(3, weight=1)
content.rowconfigure(4, weight=1)
content.rowconfigure(5, weight=1)


# Create the main screen
display = Label(content, text='Display', bg='#363636', fg='white', relief='raised', font=('Ariel', 32), anchor=E, padx=12)
display.grid(columnspan=4, sticky='NSEW')

# Functionality
# Have the buttons display text when clicked.

# StringVar automatically updates the display when its contents change.
stringvar = StringVar()
stringvar.set("0")
display.configure(textvariable=stringvar)


def clicked(digit):
    text = stringvar.get()
    if text.endswith(OPERATORS) and digit in OPERATORS:
        text = text[:-1] + digit
    elif text == '0' and digit.isdigit():
        text = digit
    elif digit in OPERATORS and text != '0':
        stringvar.set(str(evaluate(text)) + digit)
        return
    elif digit == 'C' or (text.endswith(OPERATORS) and digit in OPERATORS) or digit in OPERATORS and text == '0':
        stringvar.set('0')
        return
    else:
        text += digit
    stringvar.set(text)


def equals(stringvar=stringvar):
    text = stringvar.get()
    text = text.rstrip(''.join(OPERATORS))
    if text != '':
        stringvar.set(str(evaluate(text)))
        return
    
def evaluate(text):
    text = text.replace('x', '*')
    text = text.replace('÷', '/')
    result = eval(text)
    if str(result).endswith('.0'):
        result = int(str(result)[:-2])
    result = round(result, 2)
    return result
    
    
def plus_minus(stringvar=stringvar):
    text = stringvar.get()
    if text.startswith('-'):
        text = text[1:]
    else:
        text = str(evaluate(text))
        text = '-' + text
    stringvar.set(text)
    return



# Operation buttons
Button(content, text='=', command=equals, bg='Orange', activebackground='Orange', font=('Ariel', 16, 'bold')).grid(column=3, row=5, sticky='NSEW')
Button(content, text='÷', command=lambda: clicked('÷'), font=('Ariel', 16, 'bold')).grid(column=3, row=1, sticky='NSEW')
Button(content, text='x', command=lambda: clicked('x'), font=('Ariel', 16, 'bold')).grid(column=3, row=2, sticky='NSEW')
Button(content, text='-', command=lambda: clicked('-'), font=('Ariel', 16, 'bold')).grid(column=3, row=3, sticky='NSEW')
Button(content, text='+', command=lambda: clicked('+'), font=('Ariel', 16, 'bold')).grid(column=3, row=4, sticky='NSEW')

# Integer buttons
Button(content, text='7', command=lambda: clicked('7'), font=('Ariel', 16)).grid(column=0, row=2, sticky='NSEW')
Button(content, text='8', command=lambda: clicked('8'), font=('Ariel', 16)).grid(column=1, row=2, sticky='NSEW')
Button(content, text='9', command=lambda: clicked('9'), font=('Ariel', 16)).grid(column=2, row=2, sticky='NSEW')
Button(content, text='4', command=lambda: clicked('4'), font=('Ariel', 16)).grid(column=0, row=3, sticky='NSEW')
Button(content, text='5', command=lambda: clicked('5'), font=('Ariel', 16)).grid(column=1, row=3, sticky='NSEW')
Button(content, text='6', command=lambda: clicked('6'), font=('Ariel', 16)).grid(column=2, row=3, sticky='NSEW')
Button(content, text='1', command=lambda: clicked('1'), font=('Ariel', 16)).grid(column=0, row=4, sticky='NSEW')
Button(content, text='2', command=lambda: clicked('2'), font=('Ariel', 16)).grid(column=1, row=4, sticky='NSEW')
Button(content, text='3', command=lambda: clicked('3'), font=('Ariel', 16)).grid(column=2, row=4, sticky='NSEW')
Button(content, text='0', command=lambda: clicked('0'), font=('Ariel', 16)).grid(column=0, row=5, sticky='NSEW', columnspan=2)

# Misc buttons
Button(content, text='.', command=lambda: clicked('.'), font=('Ariel', 16, 'bold')).grid(column=2, row=5, sticky='NSEW')
Button(content, text='C', command=lambda: clicked('C'), font=('Ariel', 16, 'bold')).grid(column=0, row=1, sticky='NSEW')
Button(content, text='+/-', command=plus_minus, font=('Ariel', 16, 'bold')).grid(column=1, row=1, sticky='NSEW')
Button(content, text='%', command=lambda: clicked('%'), font=('Ariel', 16, 'bold')).grid(column=2, row=1, sticky='NSEW')


root.mainloop()
