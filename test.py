import tkinter as tk
root = tk.Tk()
root.attributes('-type', 'dock')
root.geometry('200x200')
tk.Entry(root).pack()
root.focus_force()
root.mainloop()