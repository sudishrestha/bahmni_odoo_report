
# -*- coding: utf-8 -*-
{
'name':'NepalEhr Odoo Report',
'description':'Report Section',
'author':'Possible Health',
'application': True,
   

    'category': 'possibleReport',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
       
        'views/sale_analysis_view.xml',
       
   
    ],
}
