# -*- coding: utf-8 -*-
# © 2018 Igor V. Kartashov
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": 'SETIR sale',
    "version": "9.0.1.0",
    "summary": "módulo extensiones para VAIMA",
    "description": """
		i-vk
		v9.0.1.0
	""",
    "author": "Igor V. Kartashov",
    "license": "AGPL-3",
    "website": "http://crm.setir.es",
    "category": "Sale",
    "depends": [
				'base',
				'crm',
				'sale',
				'website_quote',
                'mail',
				],
    "data": [
		#"views/setirSaleOrderForm.xml",
        #"security/ir.model.access.csv",
        ],
    "installable": True,
    "application": True,
	"auto_install": False,
    "price": 0.00,
    "currency": "EUR"
}