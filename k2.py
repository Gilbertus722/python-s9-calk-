import logging
import math
import sys
from tkinter import *
from tkinter import messagebox, ttk

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.ERROR)

logger = logging.getLogger()

handler = logging.FileHandler('logfile.log')
logger.addHandler(handler)
file_log = logging.FileHandler("logfile.log")
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out), level=logging.DEBUG)


root = Tk() 
root.title("Калькуляторище")

bttn_list = ["7", "8", "9", "+", "*", "4", "5", "6", "-", "/", "1", "2", "3",  "=", "C", "0", ".", "±", "xⁿ" , "π", "sin", "cos", "(", ")","n!","√2","Exit" ]

r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1
        
calc_entry = Entry(root, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)


def calc(key):
    global memory
    if key == "=":

        str1 = "-+0123456789.*/)(" 
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "Хочу число!")
            messagebox.showerror("Нужны числа!")
            logging.error("Ошибка!")

        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Ошибочка!")
            messagebox.showerror("Неправильные данные!")
            logging.warning('Предупреждение')
            

    elif key == "C":
        calc_entry.delete(0, END)
        
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "π":
        calc_entry.insert(END, math.pi)
        
    elif key == "Exit":
        root.after(1,root.destroy)
        sys.exit
    
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
        
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
        
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
        
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
        
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
        
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

root.mainloop()