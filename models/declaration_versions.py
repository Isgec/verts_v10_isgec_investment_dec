from odoo import fields, models, api, _
from odoo.exceptions import UserError


class version_declaration(models.Model):
    _name = 'version.declaration'
    _inherit = ['mail.thread']
    
    name = fields.Char('Version Name',required=True, help="Version such 2017 May or 2018 Feb.")
    due_date=fields.Date('Due Date' ,required=True)
    fiscal_year = fields.Char('Fiscal year',required=True, help="Fiscal year for which declarations to be made.")
    state = fields.Selection([('draft', 'Draft'),('open','Open'),('close','Close'),('cancel', 'Cancelled')],string='Cancel', default='draft', track_visibility='onchange')
#     _sql_constraints = [
#         ('issue_number_uniq', 'unique(name)', 'Version Number must be unique !!'),
#     ]
    @api.multi
    def button_close(self):
        return self.write({'state': 'close'})
    
    @api.multi
    def button_update_due_date(self):
        declaration_pool = self.env['declaration']
        declaration_ids=declaration_pool.search([('declaration_version_id','=',self.id)])
        for rec in declaration_ids:
            rec.update({'due_date': self.due_date})
        return True
        
    @api.multi
    def button_cancel(self):
        return self.write({'state': 'cancel'})
    
    @api.multi
    def button_open(self):
        employee_pool = self.env['hr.employee']
        employee_ids=employee_pool.search([])
        for emp in employee_ids:
            self.env['declaration'].create({'due_date': self.due_date,
                                            'declaration_version_id':self.id,
                                            'check':True,
                                            'employee_id':emp.id,
                                            'emp_name':emp.name,
                                            'name':emp.name,
                                            'emp_code':emp.emp_code,
                                            #'pan_no':emp.pan_no,
                                            'date_of_joining':emp.date_of_joining,
                                            'pan_of_landlord':'',
                                            'details22':'',
                                            'details24':'',
                                            'details191':0})
        return self.write({'state': 'open'})
    
    @api.multi
    def new_employee(self):
        employee_pool = self.env['hr.employee']
        declaration_pool = self.env['declaration']
        employee_ids=employee_pool.search([])
        for emp in employee_ids:
            declaration_ids=declaration_pool.search([('employee_id','=',emp.id),('declaration_version_id','=',self.id)])
            if not declaration_ids:
                self.env['declaration'].create({'due_date': self.due_date,
                                            'declaration_version_id':self.id,
                                            'check':True,
                                            'employee_id':emp.id,
                                            'emp_name':emp.name,
                                            'name':emp.name,
                                            'emp_code':emp.emp_code,
                                            'email':emp.work_email,
                                            'mobile':emp.mobile_phone,
                                            #'pan_no':emp.pan_no,
                                            'date_of_joining':emp.date_of_joining,
                                            'pan_of_landlord':'',
                                            'details22':'',
                                            'details24':'',
                                            'details191':0})
        return True
    
    @api.model
    def create(self, vals):
        if 'name' in vals and vals['name']:
            version = self.search([('name','=', vals['name'])])
            if version:
                raise UserError(_('You can not create same version name!')) 
        res = super(version_declaration, self).create(vals)
        return res
     
    @api.multi
    def write(self, vals):
        if 'name' in vals and vals['name']:
            version = self.search([('name','=', vals['name'])])
            if version:
                raise UserError(_('You can not update same version name!')) 
        return super(version_declaration, self).write(vals)
     
    
    
    
    
    
    
         
    
    
