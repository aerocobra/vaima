# -*- coding: utf-8 -*-
# © 2018 Igor V. Kartashov
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": 'VAIMA extentions',
    "version": "11.0.1.0",
    "summary": "módulo extensiones para VAIMA",
    "description": """
		i-vk
		v11.0.1.0
	""",
    "author": "Igor V. Kartashov",
    "license": "AGPL-3",
    "website": "http://alfeta.com",
    "category": "Sale",
    "depends": [
				'base',
				'crm',
				'sale',
				'website',
				'website_quote',
				'website_sale',
                'mail',
				],
    "data": [
		"views/vaimaWebsiteSaleProduct.xml",
		"reports/vaimaOfertaReport.xml",
		"reports/vaimaReportDeliverySlipBase.xml",
		"reports/vaimaReportDeliverySlipPrice.xml",
		],
    "installable": True,
    "application": True,
	"auto_install": False,
    "price": 0.00,
    "currency": "EUR"
}