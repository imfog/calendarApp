#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

#Global Constants
UP_ARROW_CODE = 'f700'
DOWN_ARROW_CODE = 'f701'

class TimePicker:
	# static class defaults
	MIN_HOURS    = 0
	MAX_HOURS    = 24
	MIN_MINUTES  = 0
	MAX_MINUTES  = 60

	def __init__(self, tk_parent, row_ = 0, column_ = 0):
		self.curr_hour           = tk.IntVar()
		self.curr_minutes        = tk.IntVar()
		self.curr_min_hour       = self.MIN_HOURS
		self.curr_min_minutes    = self.MIN_MINUTES
		#expected format is {"hr":IntVar(), "min":IntVar()}
		self.update_target_feild = None #set the current time to the target variable

		#initialize frame
		time_frame = tk.Frame(master=tk_parent, bg="azure", colormap="new")
		time_frame.grid(row = row_, column=column_)

		#intilaze label
		label = tk.Label(master=time_frame, text="Time Picker, 24hr (HH:MM)", bg="white", fg="black", relief=tk.RAISED)
		label.grid(row=0, column = 0, columnspan=2)

		#style and create the buttons
		style = ttk.Style()
		style.layout('U.TButton', (
			[('Button.focus', {'children': [('Button.uparrow', None)]})]))
		style.layout('D.TButton', (
			[('Button.focus', {'children': [('Button.downarrow', None)]})]))

		hrArrowUp = ttk.Button(time_frame, style='U.TButton', command=self.onHourArrowUp)
		hrArrowUp.grid(row=1, column = 0, ipady=10, ipadx=10)

		minArrowUp = ttk.Button(time_frame, style='U.TButton', command=self.onMinArrowUp)
		minArrowUp.grid(row=1, column = 1, ipady=10, ipadx=10)

		hrArrowDown = ttk.Button(time_frame, style='D.TButton', command=self.onHourArrowDown)
		hrArrowDown.grid(row=3, column = 0, ipady=10, ipadx=10)

		minArrowDown = ttk.Button(time_frame, style='D.TButton', command=self.onMinArrowDown)
		minArrowDown.grid(row=3, column = 1, ipady=10, ipadx=10)

		#Text Entry:
		hrEntry = tk.Entry(master=time_frame, textvariable=self.curr_hour, validate="key", justify=tk.CENTER, width=3, bg = "white")
		hrEntry['validatecommand'] = (hrEntry.register(self.validateHourEntry), '%S', '%P','%d')
		
		#Bind this Entry
		hrEntry.bind('<Up>', self.onHourArrowUp)
		hrEntry.bind('<Down>', self.onHourArrowDown)
		hrEntry.grid(row=2, column=0)

		#Minutes Text Entry
		minEntry = tk.Entry(master=time_frame, textvariable=self.curr_minutes, validate="key", justify=tk.CENTER, width=3, bg = "white", state="readonly")
		minEntry['validatecommand'] = (minEntry.register(self.validateMinutesEntry), '%S', '%P','%d')

		#Bind this entry
		minEntry.bind('<Up>', self.onMinArrowUp)
		minEntry.bind('<Down>', self.onMinArrowDown)
		minEntry.grid(row=2, column=1)

	#clears the current time values
	def _clear(self):
		self.curr_hour.set(0)
		self.curr_min.set(0)

	#set min time
	def setMinTime(self, hour=0, minutes=0):
		self.curr_min_hour    = 0
		self.curr_min_minutes = 0

	#set the target update text-feild
	def updateTarget(self, target_feild):
		self.update_target_feild = target_feild

	def onHourArrowUp(self, event=None):
		val = 0
		exception = False
		try:
			val = self.curr_hour.get()
		except:
			self.curr_hour.set(0)
			exception = True

		if val < self.MAX_HOURS and not exception:
			val += 1
			self.curr_hour.set(val)

		if(self.update_target_feild):
			self.update_target_feild["hr"].set(val)

	def onMinArrowUp(self, event=None):
		val = 0
		exception = False
		try:
			val = self.curr_minutes.get()
		except:
			self.curr_minutes.set(0)
			exception = True
		if val < self.MAX_MINUTES and not exception:
			val+= 1
			self.curr_minutes.set(val)
		if(self.update_target_feild):
			self.update_target_feild["min"].set(val)

	def onHourArrowDown(self, event=None):
		val = 0
		exception = False
		try:
			val = self.curr_hour.get()
		except:
			self.curr_hour.set(0)
			exception = True

		if val > self.curr_min_hour and not exception:
			val-=1
			self.curr_hour.set(val)

		if(self.update_target_feild):
			self.update_target_feild["hr"].set(val)

	def onMinArrowDown(self, event=None):
		val = 0
		exception = False
		try:
			val = self.curr_minutes.get()
		except:
			self.curr_minutes.set(0)
			exception = True

		if val > self.curr_min_minutes and not exception:
			val -= 1
			self.curr_minutes.set(val)
		if(self.update_target_feild):
			self.update_target_feild["min"].set(val)

	def validateHourEntry(self, incomingEdit, inStr, acttyp):
		hex_val = ":".join("{:02x}".format(ord(c)) for c in incomingEdit)
		if hex_val == UP_ARROW_CODE or hex_val == DOWN_ARROW_CODE:
			return False
		if acttyp != '0':
			if not inStr.isdigit():
				return False

			k = int(inStr)
			if k < self.curr_min_hour or k > self.MAX_HOURS:
				return False
		return True

	def validateMinutesEntry(self, incomingEdit, inStr, acttyp):
		hex_val = ":".join("{:02x}".format(ord(c)) for c in incomingEdit)
		if hex_val == UP_ARROW_CODE or hex_val == DOWN_ARROW_CODE:
			return False
		if acttyp != '0':
			if not inStr.isdigit():
				return False

			k = int(inStr)
			if k < self.curr_min_minutes or k > self.MAX_MINUTES:
				return False
		return True	

if __name__ == "__main__":
	root = tk.Tk()
	root.title("Testing 123")
	timePicker = TimePicker(root)
	root.mainloop()

