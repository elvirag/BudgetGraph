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

	date_purchase = ObjectProperty(None)
	name = ObjectProperty(None)
	cost = ObjectProperty(None)
	category = ObjectProperty(None)
	pob = ObjectProperty(None)
	comments = ObjectProperty(None)

	def btn(self):
		expense = Expense(
			self.date_purchase.text,
			self.name.text,
			self.cost.text,
			self.category.text,
			self.pob.text,
			self.comments.text
			)
		sqlite_stuff.create_expense(expense)
		self.date_purchase.text = ""
		self.name.text = ""
		self.cost.text = ""
		self.category.text = ""
		self.pob.text = ""
		self.comments.text = ""

	def cal(self):
		print("Hi!")
		# TODO: add calendar widget, prefilled with today's date! (Tal)
		cal_widget = CalendarWidget()

class Expense:
	def __init__(self, date_purchase, name, cost, category, pob, comments):
		self.date_purchase = date_purchase
		self.name = name
		self.cost = cost
		self.category = category
		self.pob = pob
		self.comments = comments
	def __str__(self):
		return " Date of Purchase: {} Name of Expense: {} Amount Spent: {} Category: {} Place of Purchase: {} Comments: {}".format(self.date_purchase, self.name, self.cost, self.category, self.pob, self.comments)

class MyApp(App):
	def build(self):
		return MyGrid()

if __name__ == "__main__":
	MyApp().run()
