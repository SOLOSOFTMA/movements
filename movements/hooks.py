# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "movements"
app_title = "Movements"
app_publisher = "Ahmed Ragheb"
app_description = "Fleet Management and Online Hotel and AirPlane Booking system"
app_icon = "octicon octicon-location"
app_color = "yellow "
app_email = " ahmedragheb75@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/movements/css/movements.css"
# app_include_js = "/assets/movements/js/movements.js"

# include js, css files in header of web template
# web_include_css = "/assets/movements/css/movements.css"
# web_include_js = "/assets/movements/js/movements.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "movements.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "movements.install.before_install"
# after_install = "movements.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "movements.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"movements.tasks.all"
# 	],
# 	"daily": [
# 		"movements.tasks.daily"
# 	],
# 	"hourly": [
# 		"movements.tasks.hourly"
# 	],
# 	"weekly": [
# 		"movements.tasks.weekly"
# 	]
# 	"monthly": [
# 		"movements.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "movements.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "movements.event.get_events"
# }

