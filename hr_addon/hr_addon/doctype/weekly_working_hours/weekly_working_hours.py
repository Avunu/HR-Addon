# Copyright (c) 2022, Jide Olayinka and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class WeeklyWorkingHours(Document):
	#pass
	def autoname(self):
		""""""
		coy = frappe.db.sql("select abbr from tabCompany where name=%s", self.company)[0][0]
		if self.employee:
			self.name = make_autoname(coy+'-.YYYY.-'+self.employee+'.####')
		else:
			self.name = make_autoname(coy+'-.YYYY.-.####')
		self.title_hour= self.name

