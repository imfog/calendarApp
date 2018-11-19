#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import calendar
import datetime as dt

class Month:
	#static Contstants
	ROWS    = 3
	COLUMNS = 4 #12 months
	ACT_BG  = '#b1dcfb'
	ACT_FG  = 'black'
	SLCT_BG = '#003eff'
	SLCT_FG = 'white'

	def __init__(self, tk_parent, stringVar_):
		self.notifyStrVar = stringVar_
		self.slected_label = None
		self.displayMonths = []
		for i in range(1,13):
			self.displayMonths.append(calendar.month_name[i][0:3])

		#Label Row
		label = tk.Label(master=tk_parent, text="Month Picker", bg="white", fg="black", relief=tk.RAISED)
		label.grid(row = 0, column = 0, sticky="new", columnspan=self.COLUMNS)

		#Grid months
		for i in range(self.ROWS):
			for j in range(self.COLUMNS):
				label_ = tk.Label(master=tk_parent, text = self.displayMonths[i*self.COLUMNS + j],bg = "white", relief=tk.RAISED)
				label_.grid(row=i+1, column=j, sticky="news")
				label_.bind("<Enter>", lambda event: event.widget.configure(background=self.ACT_BG, foreground=self.ACT_FG))
				label_.bind("<Leave>", lambda event: event.widget.configure(background="white"))
				label_.bind("<1>", self.clicked)

		font = tkFont.Font()
		maxwidth = max(font.measure(text) for text in self.displayMonths)
		for i in range(self.COLUMNS):
			tk_parent.grid_columnconfigure(i, minsize=maxwidth, weight=1)

		for j in range(1,self.ROWS+1):
			tk_parent.grid_rowconfigure(j, weight=1)

	def clicked(self, event):
		label = event.widget
		if label == self.slected_label:
			return

		#Clear selection on current label
		if self.slected_label:
			self.slected_label.configure(background= "white", foreground="black")
			self.slected_label.bind("<Enter>", lambda event: event.widget.configure(background=self.ACT_BG, foreground=self.ACT_FG))
			self.slected_label.bind("<Leave>", lambda event: event.widget.configure(background="white"))

		self.slected_label = label

        #Show new selection
		label.configure(background=self.SLCT_BG, foreground=self.SLCT_FG)
		label.unbind("<Enter>")
		label.unbind("<Leave>")

		text = label["text"]

		#notify the String variable
		self.notifyStrVar.set(calendar.month_name[self.displayMonths.index(text) + 1])

if __name__ == "__main__":
	root = tk.Tk()
	strvar = tk.StringVar()
	root.geometry("300x200")
	root.columnconfigure(0,weight=1)
	root.rowconfigure(0,weight=1)
	frame = tk.Frame(root)
	month = Month(frame, strvar)
	#frame.grid(sticky="news")
	#frame.grid_remove()
	frame.grid(sticky="news")
	root.mainloop()