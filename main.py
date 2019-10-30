import kivy
from datepicker import CalendarWidget
import sqlite_stuff

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
	date_purchase = ObjectProperty(None, allownone=False)
	name = ObjectProperty(None, allownone=False)
	cost = ObjectProperty(None, allownone=False)
	category = ObjectProperty(None, allownone=False)
	means = ObjectProperty(None, allownone=False)
	pob = ObjectProperty(None, allownone=False)
	comments = ObjectProperty(None, allownone=True)
	submit_button = Button()

	def is_submit_disabled(self):
		print("Checking if button is disabled...")
		required_fields = [
			self.date_purchase.text,
			self.name.text,
			self.cost.text,
			self.category.text,
			self.means.text,
			self.pob.text
			]

		for field in required_fields:
			if not field:
				return True

		return False 


	def btn(self):
		if self.is_submit_disabled():
			self.submit_button.disabled = True
		else:
			expense = Expense(
				self.date_purchase.text,
				self.name.text,
				self.cost.text,
				self.category.text,
				self.means.text,
				self.pob.text,
				self.comments.text
				)
			sqlite_stuff.create_expense(expense)
			self.date_purchase.text = ""
			self.name.text = ""
			self.cost.text = ""
			self.category.text = ""
			self.means.text = ""
			self.pob.text = ""
			self.comments.text = ""

	def cal(self):
		print("Hi!")
		# TODO: add calendar widget, prefilled with today's date! (Tal)
		cal_widget = CalendarWidget()

class Expense:
	def __init__(self, date_purchase, name, cost, category, means, pob, comments):
		self.date_purchase = date_purchase
		self.name = name
		self.cost = cost
		self.category = category
		self.means = means
		self.pob = pob
		self.comments = comments
	def __str__(self):
		return " Date of Purchase: {} Name of Expense: {} Amount Spent: {} Category: {} Means: {} Place of Purchase: {} Comments: {}".format(self.date_purchase, self.name, self.cost, self.category, self.means, self.pob, self.comments)

class MyApp(App):
	def build(self):
		return MyGrid()

if __name__ == "__main__":
	MyApp().run()
