# -*- coding: utf-8 -*-
# Copyright (c) 2018, Ahmed Ragheb and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Bookingdetails(Document):
	pass

@frappe.whitelist()
def get_terminal_list(airport):

	name_list=[]
	list=frappe.get_list(
					'Terminal Table',
					filters={'parent': airport},
					fields=['name'],
				   );
	if list:
		for i in range(len(list)):
			name_list.append(list[i].name) 
	return name_list

