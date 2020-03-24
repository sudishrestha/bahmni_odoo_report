
# -*- coding: utf-8 -*-
{
'name':'NepalEhr Odoo Report',
'description':'Report Section',
'author':'Possible Health',
'application': True,
   

    'category': 'possibleReport',
    'version': '0.1',

    # any module necessary for this one to work correctly
   'depends':  ['base','sale','sales_team', 'account', 'procurement', 'report', 'web_tour'],

    # always loaded
    'data': [
        'views/reporting_menu.xml',
         'report/sale_report_views.xml',
        'report/sale_report_templates.xml',
        'report/invoice_report_templates.xml',

       
   
    ],
}
