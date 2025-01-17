{
    'name': 'POS Boleta Button',
    'version': '1.0',
    'author': 'Aly',
    'category': 'Point of Sale',
    'summary': 'Agrega un botón "Boleta" en la pantalla de pagos del POS',
    'depends': ['point_of_sale'],
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_boleta_button/static/src/js/BoletaButton.js',
            'pos_boleta_button/static/src/xml/BoletaButton.xml',
        ],
    },
    'installable': True,
    'application': False,
}
