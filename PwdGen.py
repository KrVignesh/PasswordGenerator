from tkinter import *
from tkinter import messagebox
from pathlib import Path
import random
import webbrowser					 
							

# -----FUNCTIONS
def disptotal():
	global charCount
	global gp
	global character
	global number
	global symbol
	gp = ""
	total = charCount.get()
	lett = ("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
	character = charVar.get()
	number = digVar.get()
	symbol = symVar.get() 
	#To check if entered value is integer
	try:
		total = int(total)
	except:
		pass
	if isinstance(total, int) != True:
		messagebox.showerror(title = "ERROR", message = "Enter an integer Value")

	elif total == 0:
		messagebox.showwarning(title = "Zero Not Zero", message = "All available infinite integers, yet you chose '0' \nNOTE : minimum recommended character is 10")

	elif (character & number & symbol == 1):
		for i in range(0,int(total)):
			gp += random.choice(lett)
		output.insert(END, gp)
	
	elif (character & number == 1) & (symbol == 0):
		for i in range(0,int(total)):
			gp += random.choice(lett[0:62])
		output.insert(END, gp)
	
	elif (character & symbol == 1) & (number == 0):
		for i in range(0,int(total)):
			gp += random.choice(lett[10:94])
		output.insert(END, gp)
	
	elif (character == 1) & (number & symbol == 0):
		for i in range(0,int(total)):
			gp += random.choice(lett[10:62])
		output.insert(END, gp)
	
	elif (character == 0) & (number & symbol == 1):
		for i in range(0,int(total)):
			gp += random.choice(lett[0:10] + lett[62:94])
		output.insert(END, gp)
	
	elif (character == 0) & (number == 1) & (symbol == 0):
		for i in range(0,int(total)):
			gp += random.choice(lett[0:10])
		output.insert(END, gp)
	
	elif (character & number == 0) & (symbol == 1):
		for i in range(0,int(total)):
			gp += random.choice(lett[62:94])
		output.insert(END, gp)

	else:
		messagebox.showerror("Error", "select at least one checkbox")

# -----copy
def cpy():
	window.clipboard_clear()
	window.clipboard_append(gp)
	window.update()
	messagebox.showinfo(title = "Message", message = "Generated password is copied to the clipboard.\n\nNOTE : For security reason copied password will be removed after closing this app")

# -----clear
def clr():
	output.delete(1.0, END)
	charCount.delete(0, END)
	charVar.set(0)
	digVar.set(0)
	symVar.set(0)

# -----save
def save():
	global saveEntry
	global savewin
	savewin = Toplevel()
	savewin.config(background = bColor)
	saveLabel = Label(savewin, text = "Enter a unique name to identify this password", font=bodyFont, fg = fColor, bg = bColor) 
	saveLabel.pack()
	saveEntry = Entry(savewin, bg = bColor, relief = "sunken") 
	saveEntry.pack()
	saveSubmit = Button(savewin, text = "Save", cursor = "hand2", font = optionFont, command = write, relief = "solid", fg = fColor, bg = bColor, highlightthickness = 1, highlightbackground = "white")
	saveSubmit.pack()

def write():
	uDir = str(Path.home())
	uName = saveEntry.get()
	file = open(uDir + "/Documents/password.txt", "a")
	file.write(str(uName) + " : ")
	file.write(str(gp))
	file.write("\n-----End-----\n")
	file.close()
	messagebox.showinfo(title = "Success", message = "Password saved successfully in \n /user/Documents/password.txt")
	savewin.destroy()

# -----links
def ghlink():
	webbrowser.open(r"https://github.com/KrVignesh")
def twlink():
	webbrowser.open(r"https://twitter.com/KrVigneshVictor")
def maillink():
	webbrowser.open("mailto:krvigneshchn17@gmail.com")
	
# -----about
def about():
	abtwin = Toplevel()
	abtwin.config(background = bColor)
	abtwin.title("ABOUT - Password Generator")
	abtLabel = Label(abtwin, text = "This app Password Generator is created using Python.\n For more details, issues, suggestions \nvisit :", font = ("Courier 10 Pitch","12"), fg = fColor, bg = bColor)
	abtLabel.pack()
	abtgit = Button(abtwin, text = "Github", command = ghlink, fg = "white", bg = "black", cursor = "hand2", relief = "solid", font = optionFont, highlightthickness = 1, highlightbackground = "white")
	abtgit.pack(side = LEFT)
	abttwitter = Button(abtwin, text = "Twitter", command = twlink, fg = "white", bg = "#1DA1F2", cursor = "hand2", relief = "solid", font = optionFont, highlightthickness = 1, highlightbackground = "white")
	abttwitter.pack(side = LEFT, padx = 20)
	abtmail = Button(abtwin, text = "Email", command = maillink, fg = "white", bg = "#D54B3D", cursor = "hand2", relief = "solid", font = optionFont, highlightthickness = 1, highlightbackground = "white")
	abtmail.pack(side = LEFT)

# -----help
def hlp():
	hlpwin = Toplevel()
	hlpwin.config(background = bColor)
	hlpwin.title("HELP - Password Generator")
	hlpLabel = Label(hlpwin, text = "Random English Letters includes : a-z, A-Z \n\nDigits includes : 0-9 \n\nSymbols include : !\"#$%&'()*+,-./:;<=>?@[\\]^_`|{}~ \n  ", font = bodyFont, fg = fColor, bg = bColor)	
	hlpLabel.pack()

# -----Color & fonts
bColor = "#ae00ff"
fColor = "white"
bodyFont = ("Courier 10 Pitch","14", "bold")
optionFont = ("Courier 10 Pitch", "12", "italic")

# -----GUI
# -----create main window
window = Tk()
window.config(background = bColor)
window.title("Password Generator")

# -----heading
title = Label(window, text = "PASSWORD GENERATOR", anchor = "center", font=("Free Mono","30", "bold"), fg = fColor, bg = bColor)
title.grid(column = 0, row = 0, columnspan = 4, pady = 20)

# -----get number of character in password
charLabel = Label(window, text = "How many character do you need in Password\n(Enter integer numbers)", font=bodyFont, fg = fColor, bg = bColor)
charLabel.grid(column = 0, row = 1, pady = 10, padx = 20, sticky = E)

charCount = Entry(window, relief = "sunken", justify = "center", borderwidth = 4, bg = bColor)
charCount.grid(column = 1, row = 1)

# -----things to be included in password
incLabel = Label(window, text = "Password should include", font=bodyFont, fg = fColor, bg = bColor)
incLabel.grid(column = 0, row = 2, pady = 10, sticky = E)

charVar = BooleanVar()
incChar = Checkbutton(window, text = "Random English Letters", variable = charVar, font = optionFont, cursor = "hand2", bg = bColor, fg = fColor, highlightthickness = 0, selectcolor = bColor, activebackground = bColor)
incChar.grid(column = 1, row = 2)

digVar = BooleanVar()
incDigits = Checkbutton(window, text = "Digits", variable = digVar, font = optionFont, cursor = "hand2", bg = bColor, fg = fColor, highlightthickness = 0, selectcolor = bColor, activebackground = bColor)
incDigits.grid(column = 2, row = 2)

symVar = BooleanVar()
incSym = Checkbutton(window, text = "Symbols", variable = symVar, font = optionFont, cursor = "hand2",  bg = bColor, fg = fColor, highlightthickness = 0, selectcolor = bColor, activebackground = bColor)
incSym.grid(column = 3, row = 2)

# -----Generate - button
Submit = Button(window, text = "Generate", cursor = "hand2", font = optionFont, command = disptotal, relief = "solid", fg = fColor, bg = bColor, highlightthickness = 1, highlightbackground = "white")
Submit.grid(column = 1, row = 4, pady = 10)

# -----clear all - button
clear = Button(window, text = "Clear All",command = clr, font = optionFont, cursor = "hand2", relief = "solid", fg = fColor, bg = bColor, highlightthickness = 1, highlightbackground = "white")
clear.grid(column = 2, row = 4, pady = 10)

#-----generated password
pwdLabel = Label(window, text = "Generated Password", font= bodyFont, fg = fColor, bg = bColor)
pwdLabel.grid(column = 0, row = 5, pady = 10, sticky = E)

# -----output
output = Text(window, width = 60, height = 5, borderwidth = 4, relief = "ridge", bg = bColor)
output.grid(column = 1, row = 5, columnspan = 3, pady = 20, padx = 10)

# -----Copy generated password to clipboard - button
copy = Button(window, text = "Copy",command = cpy, font = optionFont, cursor = "hand2", relief = "solid", fg = fColor, bg = bColor, highlightthickness = 1, highlightbackground = "white")
copy.grid(column = 1, row = 6, pady = 10, columnspan = 1)

# -----save generated password to a file - button
store = Button(window, text = "Save",command = save, font = optionFont, cursor = "hand2", relief = "solid", fg = fColor, bg = bColor, highlightthickness = 1, highlightbackground = "white")
store.grid(column = 2, row = 6, pady = 10, columnspan = 1)

# -----about - button
abt = Button(window, text = "About",command = about, font = optionFont, cursor = "hand2", relief = "solid", fg = fColor, bg = bColor, highlightthickness = 1, highlightbackground = "white")
abt.grid(column = 2, row = 7, pady = 5)

# -----help - button
more = Button(window, text = "Help",command = hlp, font = optionFont, cursor = "hand2", relief = "solid", fg = fColor, bg = bColor, highlightthickness = 1, highlightbackground = "white")
more.grid(column = 3, row = 7)

# -----quit - button
exit = Button(window, text = "Quit",command = window.destroy, font = optionFont, cursor = "hand2", relief = "solid", fg = fColor, bg = bColor, highlightthickness = 1, highlightbackground = "white")
exit.grid(column = 4, row = 7, padx = 5)

window.mainloop()