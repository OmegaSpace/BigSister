'''module to handle SQL database intergration'''

import sqlite3

class MembersDatabase(object):

	def __init__(self, database_name):
		self.database_name = database_name
		self.conn = None

	def _connect_to_db(self):
		self.conn = sqlite3.connect(self.database_name)

	def create_table(self):
		try:
			c = self.conn.cursor()
			c.execute('''CREATE TABLE members
							(bangor_id text, surname text, forename text, email text, mobile text, school text,study_year int)''')
			self.conn.commit()
			c.close()

		except sqlite3.Error as e:
			print(("Error: " + e.args[0]))

	def add_member(self, bangor_id, surname, forename, email, mobile, school, study_year):
		c = self.conn.cursor()
		if not self.validate_user(bangor_id):
			c.execute('''INSERT INTO members VALUES (?,?,?,?,?,?,?)''', (bangor_id, surname, forename, email, mobile, school, study_year))
		self.conn.commit()
		c.close()

	def remove_member(self, bangor_id):
		c = self.conn.cursor()
		if self.validate_user(bangor_id):
			c.execute('''DELETE FROM members WHERE bangor_id=?''', (bangor_id,))
		else:
			print('Member not removed')
		self.conn.commit()
		c.close()

	def validate_user(self, bangor_id):
		c = self.conn.cursor()
		c.execute('''SELECT surname FROM members WHERE bangor_id=?''', (bangor_id,))
		valid = c.fetchone()
		if valid is None:
			return False
		else:
			return True
		c.close()

	def print_members(self):
		c =self.conn.cursor()
		c. execute('''SELECT * FROM members''')
		membership = c.fetchall()
		c.close()
		return membership

	def return_name(self, bangor_id):
		c = self.conn.cursor()
		c.execute('''SELECT forename FROM members WHERE bangor_id=?''', (bangor_id,))
		name = c.fetchone()
		if name is None:
			return False
		else:
			return name

	def _close_connection(self):
		self.conn.close()
