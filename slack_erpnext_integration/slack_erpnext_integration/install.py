# Copyright (c) 2025, Slack ERPNext Integration and contributors
# For license information, please see license.txt

import frappe


def create_demo_webhook():
	"""Create a demo Slack webhook for testing"""
	if not frappe.db.exists("Slack Webhook URL", "Sales Update Channel"):
		webhook = frappe.get_doc({
			"doctype": "Slack Webhook URL",
			"webhook_name": "Sales Update Channel",
			"webhook_url": "YOUR_SLACK_WEBHOOK_URL
			"show_document_link": 1
		})
		webhook.insert()
		frappe.db.commit()
		return webhook.name
	return "Sales Update Channel"


def create_demo_notification():
	"""Create a demo Slack notification for Sales Order"""
	if not frappe.db.exists("Notification", "Slack - New Sales Order"):
		notification = frappe.get_doc({
			"doctype": "Notification",
			"name": "Slack - New Sales Order",
			"subject": '💰 New Order {{ doc.name }} - {{ doc.customer }} - {{ doc.currency }} {{ "{:,.0f}".format(doc.grand_total) }}',
			"document_type": "Sales Order",
			"event": "New",
			"enabled": 1,
			"channel": "Slack",
			"slack_webhook_url": "Sales Update Channel",
			"message": '''🎉 *NEW SALES ORDER RECEIVED!*

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 *Order #:* {{ doc.name }}
👤 *Customer:* {{ doc.customer }}
📅 *Date:* {{ doc.transaction_date }}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 *ITEMS ORDERED:*

{% for item in doc.items %}
• *{{ item.qty }}{{ item.uom }}* {{ item.item_name }} @ {{ doc.currency }} {{ '{:,.0f}'.format(item.rate) }} each
  _Subtotal: {{ doc.currency }} {{ '{:,.0f}'.format(item.amount) }}_
{% endfor %}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 *TOTAL AMOUNT: {{ doc.currency }} {{ '{:,.0f}'.format(doc.grand_total) }}*

{% if doc.delivery_date %}
🚚 *Delivery Date:* {{ doc.delivery_date }}
{% endif %}

{% if doc.po_no %}
📄 *Customer PO:* {{ doc.po_no }}
{% endif %}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
_Order Status: {{ doc.status }}_'''
		})
		notification.insert()
		frappe.db.commit()
		return notification.name
	return "Slack - New Sales Order"


def update_demo_notification():
	"""Update the demo notification with better message template"""
	if frappe.db.exists("Notification", "Slack - New Sales Order"):
		notification = frappe.get_doc("Notification", "Slack - New Sales Order")
		notification.subject = '💰 New Order {{ doc.name }} - {{ doc.customer }} - {{ doc.currency }} {{ "{:,.0f}".format(doc.grand_total) }}'
		notification.message = '''🎉 *NEW SALES ORDER RECEIVED!*

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 *Order #:* {{ doc.name }}
👤 *Customer:* {{ doc.customer }}
📅 *Date:* {{ doc.transaction_date }}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 *ITEMS ORDERED:*

{% for item in doc.items %}
• *{{ item.qty }}{{ item.uom }}* {{ item.item_name }} @ {{ doc.currency }} {{ '{:,.0f}'.format(item.rate) }} each
  _Subtotal: {{ doc.currency }} {{ '{:,.0f}'.format(item.amount) }}_
{% endfor %}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 *TOTAL AMOUNT: {{ doc.currency }} {{ '{:,.0f}'.format(doc.grand_total) }}*

{% if doc.delivery_date %}
🚚 *Delivery Date:* {{ doc.delivery_date }}
{% endif %}

{% if doc.po_no %}
📄 *Customer PO:* {{ doc.po_no }}
{% endif %}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
_Order Status: {{ doc.status }}_'''
		notification.save()
		frappe.db.commit()
		return "Updated successfully"
	return "Notification not found"
