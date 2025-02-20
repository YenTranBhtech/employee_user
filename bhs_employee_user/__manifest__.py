{
    'name': "Auto create user from employee",
    'version': '1.0',
    'description': """
       Automatically create a new user from a new employee 
    """,
    'author': 'Bac Ha Software',
    'company': 'Bac Ha Software',
    'maintainer': 'Bac Ha Software',
    'website': "https://bachasoftware.com",
    'category': 'Human Resources',
    'depends': ['hr', 'hr_recruitment'],
    'data': [
        'views/hr_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'application': True
}
