{
    'name': 'POS Alert Zero Price',
    'version': '1.0',
    'author': 'Aly',
    'category': 'Point of Sale',
    'summary': 'Alerta al seleccionar un producto con precio S/ 0.0 en POS',
    'depends': ['point_of_sale'],
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_alert_zero_price/static/src/js/models.js',
        ],
    },
    'installable': True,
    'application': False,
}
