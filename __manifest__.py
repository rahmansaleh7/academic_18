{
    'name': "Academic Information System",

    'summary': """
        Course, Session & Attendee
    """,

    'description': """
        Academic Information System
        ===========================
        * Course, Session & Attendee
        * Instructor (inherit res.partner)
        * List, form, calendar, search, graph, pivot, kanban view
        * Group User/Manager, access rights, record rules
        * Wizard tambah peserta ke banyak session
        * Report PDF Session & terjemahan Bahasa Indonesia
    """,

    'author': "Iqbalasaleh [iqbalasaleh.com]",
    'website': "http://www.vitraining.com",

    'category': 'Education',
    'version': '18.0.1.0.0',

    'depends': [
        'base',
        'web',
        ],

    # always loaded
    'data': [
        'security/academic_security.xml',
        'security/ir.model.access.csv',
        'views/course.xml',
        'views/partner.xml',
        'views/session.xml',
        'views/attendee.xml',
        'wizard/create_attendee_view.xml',
        'report/session_report.xml',
        'views/menu.xml',
    ],
    "application": True,
    'license': 'LGPL-3',
}
