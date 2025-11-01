{
    'name': "Digitec Galaxus PDF Document Style",
    'summary': "Report templates in Digitec Galaxus AG Style for Sales, Purchase, Delivery, and Invoice.",
    'description': """
- External layout (header/footer)
- Sale, Purchase, Delivery, and Invoice report templates
- Optional paperformat
- Toggles in Settings to enable/disable each template and reset to default Odoo behaviour
""",
    'author': 'Nathanael Lee',
    'website': 'https://erp-partner.ch',
    'category': 'Reporting',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'purchase',
        'product',
        'mail',
        'account',
        'stock',
        'sale_stock',
        'stock_delivery'
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'reports/sale_report_templates.xml',
        'reports/purchase_report_templates.xml',
        'reports/account_report_templates.xml',
        'reports/delivery_report_templates.xml',
        'reports/report_paperformats.xml',
        'reports/report_layouts.xml',
    ],
    'images': ['images/banner.png'],
    'installable': True,
    'application': False,
}