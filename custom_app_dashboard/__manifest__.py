{
    'name': 'App Dashboard for Odoo Community',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',
    'category': 'Tools',
    'summary': 'Modern App Dashboard for Odoo Community',
    'description': """
App Dashboard for Odoo Community

A modern dashboard-style application launcher designed for Odoo Community Edition.

Features:
- Modern application dashboard
- Responsive design for Desktop, Tablet and Mobile
- Navbar integration
- Fast access to installed applications
- Mobile-friendly interface
- Lightweight and easy to deploy
- Odoo Community Edition compatible
""",
    'author': 'GTMTechsol.com',
    'maintainer': 'GTMTechsol.com',
    'website': 'https://gtmtechsol.com',
    'depends': ['web'],
    'data': [
        'views/dashboard_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_app_dashboard/static/src/js/app_dashboard.js',
            'custom_app_dashboard/static/src/js/navbar_patch.js',
            'custom_app_dashboard/static/src/xml/navbar_patch.xml',
            'custom_app_dashboard/static/src/xml/app_dashboard.xml',
            'custom_app_dashboard/static/src/scss/app_dashboard.scss',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
