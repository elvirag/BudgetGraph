import sqlite3

def connect():

	conn = sqlite3.connect('expenses_db.sqlite')
	cur = conn.cursor()

	return conn, cur

def create_table():
	conn, cur = connect()

	cur.execute('pragma encoding')

	cur.execute("""CREATE TABLE IF NOT EXISTS expenses (
	    Expense_id INTEGER PRIMARY KEY,
	    Date_purchase DATE NOT NULL,
	    Name Varchar(256) NOT NULL,
	    Cost REAL NOT NULL,
	    Category Varchar(256) NOT NULL,
	    Means Varchar(256) NOT NULL,
	    Buisness Varchar(256) NOT NULL,
	    Comments Varchar(1024)
	);
	""")

	conn.commit()
	conn.close()



def create_expense(expense):
	conn, cur = connect()

	cur.execute(
		"""INSERT INTO expenses (Date_purchase, Name, Cost, Category, Means, Buisness, Comments)
		VALUES( "{}", "{}", {}, "{}", "{}", "{}", "{}");
		""".format(expense.date_purchase, expense.name, expense.cost, expense.category, expense.means, expense.pob, expense.comments)
	)

	conn.commit()
	conn.close()

create_table()