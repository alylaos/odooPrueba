{
    'name': 'Invoice Sales Channel',
    'version': '1.0',
    'author': 'Aly',
    'category': 'Accounting',
    'summary': 'Agrega un campo Canal de ventas a las facturas',
    'depends': ['account'],
    'data': [
        'data/sales_channel_data.xml',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
}
