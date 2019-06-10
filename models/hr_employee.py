from odoo import api, fields, models, _

class hr_employee(models.Model):
    _inherit = 'hr.employee'
    
    emp_code = fields.Char(string='Employee Code')
    pan_no = fields.Char(string='PAN No')
    date_of_joining = fields.Date('Date of Joining')