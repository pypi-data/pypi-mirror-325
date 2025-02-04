{
    "name": "grupxarxa",
    "summary": """
        Odoo customization for Grup Xarxa
    """,
    "description": """
        - Remove remaining days widget
        - Hide date_rang_fy_id
    """,
    "author": "Coopdevs",
    "website": "https://git.coopdevs.org/coopdevs/odoo/odoo-addons/odoo-grupxarxa",  # noqa
    "category": "Uncategorized",
    "version": "16.0.0.1.0",
    "depends": ["account", "account_move_fiscal_year"],
    "data": [
        "views/account_views.xml"
    ],
}
