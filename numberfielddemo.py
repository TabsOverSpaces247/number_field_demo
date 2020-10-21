"""
Program: numberfielddemo.py
Author: Serghie 10/15/20
Example from page 264-265

This GUI-based program is a simple Python GUI window that outputs the square root of an integer.

Check breezypythongui to see all methods and their attributes!

"""

from breezypythongui import EasyFrame
import math

""" NumberFieldDemo extends EasyFrame """

class NumberFieldDemo(EasyFrame):

	def __init__(self): 
		""" Sets up the window and the widgets. """
		EasyFrame.__init__(self, title = "Number Field Demo")

		# Label and field for the input
		""" addLabel() and addTextField() are methods
			inputField and outputField are variable names """

		self.addLabel(text = "An integer", row = 0, column = 0)
		self.inputField = self.addIntegerField(value = 0 , row = 0, column = 1, width = 10)
	
		# Label and field for the output
		self.addLabel(text = "Square Root", row = 1, column = 0)
		self.outputField = self.addFloatField(value = 0.0, row = 1, column = 1, state = "readonly", width = 8, precision = 2)

		""" The command refers to functions, and these functions must be defined."""

		# The command button
		self.addButton(text = "Compute", row = 2, column = 0, columnspan = 2, command = self.computeSqrt)

	# The event handling method for the button
	def computeSqrt(self):
		""" Inputs the integer, computes the square root and outputs the result."""
		try:
			number = self.inputField.getNumber()
			result = math.sqrt(number)
			self.outputField.setNumber(result)
		except ValueError:
			self.messageBox(title = "ERROR", message = "Please enter a positive whole number.")

def main():
	""" Instantiates and pops up the window. """
	NumberFieldDemo().mainloop()

# Global call to the main() function
main()