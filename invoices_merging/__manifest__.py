# Copyright 2017 techmatic systems Business and IT Consulting Services Hyd
#   (https://www.techmaticsys.com)
# Copyright 2025 Techmatic Systems Pvt Ltd, Odoo Official Partner (https://www.odoo.com/partners/techmatic-systems-india-private-limited-14930407?grade_id=3&)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


{
    "name": "Account Invoices Merging",
    "category": "Services",
    "summary": "Merging invoices in draft",
    "author": "Techmatic Systems",
    "website": "https://www.techmaticsys.com",
    "license": "LGPL-3",
    "depends": ["account"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/invoice_merge_view.xml",
    ],
    'images': ["static/description/icon.png"
    ],
    "installable": True,
}
