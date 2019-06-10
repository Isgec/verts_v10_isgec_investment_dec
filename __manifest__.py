# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011-2015 Verts Services India Pvt. Ltd. (<http://www.verts.co.in>)
#    Copyright (C) 2004-2010 OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name': 'verts_v10_isgec_investment_dec',
    'version': '1.0',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Generic Modules/Others',
    'description': """
        
        
    """,
    'author': 'Verts Services India Pvt. Ltd.',
    'website': 'www.verts.co.in',
    'depends': ['base','hr'],
    'init_xml': [],
    'data': [
             'security/security.xml',
             'views/declaration_version_view.xml',
             'views/declaration_view.xml',
             'views/employee_view.xml',
             'security/ir.model.access.csv',
             'wizard/declartion_details_wizard_view.xml',
             'views/menu_view.xml',
             'views/declaration_report_view.xml',
             'views/declaration_report_template_view.xml',
             'views/report_declaration_form12b.xml',
             'views/res_user_view.xml',
             'views/sequence_view.xml',
             
             
    ],
    'demo_xml': [],
    'test': [
    ],
    'qweb' : [
    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
