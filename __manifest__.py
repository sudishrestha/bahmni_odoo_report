
# -*- coding: utf-8 -*-
{
'name':'NepalEhr Odoo Report',
'description':'Report Section',
'author':'Possible Health',
'application': True,
   

    'category': 'possibleReport',
    'version': '0.1',

    # any module necessary for this one to work correctly
   'depends':  ['base','sale','bahmni_insurance_odoo', "mail", "bahmni_atom_feed", "bahmni_account", "account","purchase"],

    # always loaded
    'data': [
        'views/reporting_menu.xml',
        'views/report_extended.xml'
  
    ],
}
