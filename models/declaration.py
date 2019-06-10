from odoo import fields, models, api, _
from odoo.exceptions import UserError
from datetime import datetime
from dateutil.relativedelta import relativedelta
from email.utils import formataddr
from datetime import date
import calendar
import odoo.addons.decimal_precision as dp
import urllib


class declaration(models.Model):
    _name = 'declaration'
    
    name = fields.Char("Sequence No", readonly=True, copy=False, default='/')
    pan_no = fields.Char('Pan', states={'open': [('readonly', False)]})
    date_of_joining = fields.Date('Date of Joining',readonly="True")
    emp_name = fields.Char('Employee Name',required=True,copy=False,readonly="True")
    emp_code = fields.Char('Employee Code',readonly="True")
    due_date=fields.Date('Due Date',readonly="True")
    declaration_version_id = fields.Many2one('version.declaration','Declaration version',readonly="True")
    house_rent_paid_per_month=fields.Float('House Rent Paid',  copy=False, readonly=True, states={'open': [('readonly', False)]},help="Landlord's PAN is mandatory when House Rent Paid is more than Rs. 100000.00")
    full_name_of_landlord=fields.Char('Full Name of Landlord', copy=False, readonly=True, states={'open': [('readonly', False)]})
    street1=fields.Char('Street 1', copy=False, readonly=True, states={'open': [('readonly', False)]})
    street2=fields.Char('Street 2', copy=False, readonly=True, states={'open': [('readonly', False)]})
    city=fields.Char('City', copy=False, readonly=True, states={'open': [('readonly', False)]})
    country_id = fields.Many2one('res.country', copy=False, readonly=True, states={'open': [('readonly', False)]}, string='Country')
    states=fields.Many2one('res.country.state',string='State', copy=False, readonly=True, states={'open': [('readonly', False)]})
    state = fields.Selection([('open', 'Open'),('submit','Submitted'),('done','Done')],default='open',string='Status')
    zip_code=fields.Char('Zip Code', copy=False, readonly=True, states={'open': [('readonly', False)]})
    pan_of_landlord=fields.Char('PAN of Landlord',size=10, copy=False, readonly=True, states={'open': [('readonly', False)]})
    check=fields.Boolean('check', copy=False, readonly=True, states={'open': [('readonly', False)]})
    employee_id=fields.Many2one('hr.employee','Emp', copy=False, readonly=True, states={'open': [('readonly', False)]})
    city_metro=fields.Selection([('metro','Metro'),('non_metro','Non Metro')],string='Is City Metro',default='non_metro',copy=False, readonly=True, states={'open': [('readonly', False)]})
    submit_date = fields.Datetime("Submit Date", readonly=True)
    submit_by = fields.Many2one("res.users", string="Submit By", readonly=True)
    email = fields.Char('Email',copy=False, states={'open': [('readonly', False)]})
    mobile = fields.Char('Mobile',copy=False, states={'open': [('readonly', False)]})
    
    @api.multi
    def search_current_date(self):
        lst=[]
        today_date = datetime.today().strftime("%d-%m-%y")
        date = datetime.today() + relativedelta(years=1)
        current_year = date.strftime("%Y")
        my_date = date.today()
        day_name = calendar.day_name[my_date.weekday()]
        lst.append(today_date)
        lst.append(current_year)
        lst.append(day_name)
        return lst


    
    @api.depends('medi_self','medi_sen','details41')
    def _calc_medi(self):
        for decl in self:
            medi_self = decl.medi_self
            medi_sen = decl.medi_sen
            by_co = decl.details41
            details12 = 0.0
            if by_co >= medi_self:
                by_co -= medi_self
                details12 = 0.0
            else:
                details12 = medi_self - by_co
                by_co = 0.0
            details31 = by_co < medi_sen and medi_sen - by_co or 0.0
            decl.update({'details12':min(details12, 25000.0),
                            'details31':min(details31, 50000.0)})
            
    medi_self=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    medi_sen=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details12=fields.Float('Details', compute="_calc_medi", copy=False, readonly=True)
    details31=fields.Float('Details', compute="_calc_medi", copy=False, readonly=True)
    details41=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})

    details=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details1=fields.Float('Detailptoducts', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details2=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details3=fields.Date('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details4=fields.Char('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details5=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details6=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details7=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details8=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details9=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details10=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details11=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    type_disability=fields.Selection([('normal', 'Normal (Maximum limit - Rs 75,000/-)'),('severe', 'Severe (Maximum limit - Rs 1,25,000/-)')], string="Disability type",  copy=False, readonly=True, states={'open': [('readonly', False)]})
    details13=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details14=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details15=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details16=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details17=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    type_treatment=fields.Selection([('med_treat', 'Non-Senior Citizen(Maximum limit-40,000/-)'),
                                    ('med_treat_sen', 'Senior Citizen(Maximum limit-1,00,000/-)'),
                                    ], string="Medical treatment towards", copy=False, readonly=True, states={'open': [('readonly', False)]})
    details18=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details19=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    
#     ****************CONSTRUCTION OF HOUSING PROPERTY (U/S 24 b)**************

    @api.depends('details20','details23','details25','details27','pre_emi_interest_paid')
    def _total_24b(self):
        for decl in self:
            tot = -decl.details20 -decl.details23 -decl.details27 -decl.pre_emi_interest_paid
            tot += decl.details25 * 0.7
            if tot < 0.00:
                decl.update({'details181':max(tot,-200000.0)})
            else:
                decl.update({'details181':min(tot,200000.0)})
            
    details181=fields.Float('Details', compute="_total_24b", copy=False, readonly=True)
    details191=fields.Char('Details',size=10, copy=False, readonly=True, states={'open': [('readonly', False)]})
    
    lender_name=fields.Char('Details',size=100, copy=False, readonly=True, states={'open': [('readonly', False)]})
    lender_name2=fields.Char('Details',size=100, copy=False, readonly=True, states={'open': [('readonly', False)]})
    
    pan_no_lender2=fields.Char('Details',size=10, copy=False, readonly=True, states={'open': [('readonly', False)]})
    
    other_pan_no_lender1=fields.Char('Details',size=10, copy=False, readonly=True, states={'open': [('readonly', False)]})
    other_lender_name=fields.Char('Details',size=100, copy=False, readonly=True, states={'open': [('readonly', False)]})
    other_lender_name2=fields.Char('Details',size=100, copy=False, readonly=True, states={'open': [('readonly', False)]})
    other_pan_no_lender2=fields.Char('Details',size=10, copy=False, readonly=True, states={'open': [('readonly', False)]})
    
    details20=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details21=fields.Char('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details22=fields.Selection([('yes','Yes'),('no', 'No')],string="Please Fill INCOME FROM HOUSE PROPERTY Tab field 2.A", copy=False, readonly=True, states={'open': [('readonly', False)]})
    details23=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details24=fields.Selection([('yes','Yes'),('no', 'No')],string="Please Fill INCOME FROM HOUSE PROPERTY Tab field 2.J", copy=False, readonly=True, states={'open': [('readonly', False)]})
    details25=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details26=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details27=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    pre_emi_interest_paid=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    
    #*******************************************
    
    details28=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details29=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details30=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details32=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details33=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details34=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details35=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details36=fields.Date('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    to_date1=fields.Date('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    to_date2=fields.Date('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details37=fields.Char('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details38=fields.Char('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details39=fields.Char('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details40=fields.Char('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    employer_name2=fields.Char('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    employer_address2=fields.Char('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    tan1=fields.Char('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    pan1=fields.Char('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    remark1 = fields.Text('Remarks', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details228=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details229=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details230=fields.Float('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    details236=fields.Date('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    tan2=fields.Char('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    pan2=fields.Char('Details', copy=False, readonly=True, states={'open': [('readonly', False)]})
    remark2 = fields.Text('Remarks', copy=False, readonly=True, states={'open': [('readonly', False)]})
    
    
    
    @api.onchange('details22')
    def _onchange_details22(self):
        if self.details22:
            if self.details22 == 'no':
                self.details20 = 0.00
                self.pre_emi_interest_paid = 0.00
                
    @api.onchange('details24')
    def _onchange_details24(self):
        if self.details24:
            if self.details24 == 'no':
                self.details23 = 0.00
                self.details27 = 0.00
    
    @api.model
    def create(self, vals):
        res = super(declaration, self).create(vals)
        if vals['details22']:
            if vals['details22']=='no':
                vals['details20'] = 0.00
                vals['pre_emi_interest_paid'] = 0.00
        if vals['details24']:
            if vals['details24']=='no':
                vals['details23'] = 0.00
                vals['details27'] = 0.00
        if vals['pan_of_landlord']:
            if len(vals['pan_of_landlord']) != 10:
                raise UserError(_('Please fill 10 digit PAN of Landlord Number!'))
        if vals['details191']:
            if len(vals['details191']) != 10:
                raise UserError(_('Please fill 10 digit PAN of Lender/Financier!'))
        return res
    
    @api.multi
    def write(self, vals):
        if 'due_date' not in vals:
            current_date = datetime.now().strftime('%Y-%m-%d')
            if self.due_date<current_date:
                raise UserError(_('You can not edit this form because your due date is expire!'))
        if vals.has_key('details22'):
            if vals['details22']=='no':
                vals['details20'] = 0.00
                vals['pre_emi_interest_paid'] = 0.00
        if vals.has_key('details24'):
            if vals['details24']=='no':
                vals['details23'] = 0.00
                vals['details27'] = 0.00
        if vals.has_key('pan_of_landlord'):
            if vals['pan_of_landlord'] and len(vals['pan_of_landlord']) != 10:
                raise UserError(_('Please fill 10 digit PAN of Landlord Number!'))
        if vals.has_key('details191'):
            if vals['details191'] and len(vals['details191']) != 10:
                raise UserError(_('Please fill 10 digit PAN of Lender/Financier!'))
        return super(declaration, self).write(vals)

    @api.multi
    def button_submit(self):
        if self.due_date:
            current_date = datetime.now().strftime('%Y-%m-%d')
            if self.due_date<current_date:
                raise UserError(_('You can not edit this form because your due date is expire!'))
        today = datetime.today()
        fin_date = datetime(today.year, 04, 01).strftime('%Y-%m-%d')
        if self.date_of_joining:
            if self.date_of_joining >= fin_date and not ((self.remark1 or self.remark2) or (self.details28 or self.details228)):
                raise UserError(_('Please Fill Remarks or Income from Previous Employer for Employer Details 1 or Employer Details 2!'))
        return self.write({'state': 'submit','submit_date':datetime.now(),'submit_by':self._uid})
        
    @api.multi
    def button_reopen(self):
        if self.due_date:
            current_date = datetime.now().strftime('%Y-%m-%d')
            if self.due_date<current_date:
                raise UserError(_('You can not edit this form because your due date is expire!'))
        return self.write({'state': 'open'})
    
    @api.multi
    def button_done(self):
        if self.due_date:
            current_date = datetime.now().strftime('%Y-%m-%d')
            if self.due_date<current_date:
                raise UserError(_('You can not edit this form because your due date is expire!'))
        return self.write({'state': 'done'})
        
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        context = self._context or {}
        if self._uid==1 or self.user_has_groups('verts_v10_isgec_investment_dec.declaration_manager_group'):
            return super(declaration, self).search(args, offset, limit, order, count=count)
        elif self.user_has_groups('verts_v10_isgec_investment_dec.declaration_user_group'):
            employee_ids = self.env['hr.employee'].search([('user_id','=',self._uid)])
            if not employee_ids:
                return []
            ids=[]
            for each in employee_ids:
                self._cr.execute("SELECT id FROM declaration WHERE employee_id=%s"%each.id)
                declarion_ids = self._cr.fetchall()
                for decl in declarion_ids:
                    ids.append(decl[0])
            if ids:
                args.append((('id','in',ids)))        
            return super(declaration, self).search(args, offset, limit, order, count=count)    
        
    @api.onchange('house_rent_paid_per_month')
    def _onchange_house_rent_paid_per_month(self):
        if self.house_rent_paid_per_month > 100000.00:
            raise UserError(_('If Rent Paid Annually is Above of Rs.1 Lakhs, PAN No. of Landlord is Mandatory.'))
        
     
    urlgen = fields.Char('Attach Investment proof',compute='_urlGen')
    
    @api.one
    @api.depends('emp_code', 'due_date', 'declaration_version_id')
    def _urlGen(self):
        index = (self.emp_code or '') + '_' + (self.declaration_version_id.fiscal_year or '')
        args = {"AthHandle" : "J_INVESTMENT_DECLARATION",
                "Index": index, "AttachedBy" : self.emp_code, "ed" : "y"}
        url = "http://192.9.200.146/Attachment/Attachment.aspx?{}".format(urllib.urlencode(args))
        self.urlgen = url
        
        
    @api.multi
    def action_open_url(self):
        self.ensure_one()
        if not self.emp_code:
            raise UserError(_('Employee code is not set!'))
        return {
            'name': _("Submit Investment Proof"),
            'type': 'ir.actions.act_url',
            'url': self.urlgen,
            'target': 'new',
        }
        
        
        
        
        
        
        