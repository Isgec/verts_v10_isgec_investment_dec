from odoo import api,fields,models,_
from datetime import datetime
import xlwt 
import StringIO
import cStringIO
import base64


class declaration_details_wizard(models.TransientModel):
    _name='declaration.details.wizard'
    declaration_version_id = fields.Many2one('version.declaration',string='Declaration version')
    
    def button_excel(self, data, context=None):
#         if context is None:
#             context = {}
#         data.update(self.read(['from_date','to_date'])[0])
#         from_date = data['from_date']
#         to_date = data['to_date']
        try:
            import xlwt
            from xlwt import *
        except Exception, e:
            raise wizard.except_wizard(_('User Error'), _('Please Install xlwt Library.!'))
        filename = 'Declaration Details.xls'
        string = 'Declaration Details.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        worksheet = wb.add_sheet(string)
        style_value = xlwt.easyxf('font: bold on ,colour_index 0x36;' "borders: top double , bottom double ,left double , right double;")
        style_header = xlwt.easyxf('font: bold on ,colour_index black;' "borders: top double , bottom double ,left double , right double;")
        style = XFStyle()
        fnt = Font()
        fnt.colour_index = 0x36
        fnt.bold = True
        fnt.width = 256 * 30
        style.font = fnt
        style1 = XFStyle()
        fnt = Font()
        fnt.colour_index = 0x86
        fnt.bold = True
        fnt.width = 256 * 30
        style1.font = fnt
       
        worksheet.write(0,0,'Sl.No',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,1,'EmpCode',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,2,'Financial Year',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,3,'Employee Name',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,4,'DECLARATION STATUS',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,5,'Mobile No.',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,6,'Email',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,7,'Date of Joining',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,8,'LIC Premium',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,9,'(Post office Savings(Cumulative time deposit/FD))',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        # worksheet.write(0,7,'FD',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,10,'(PPF)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,11,'Date of PPF Deposit',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,12,'A/c No. in which PPF is Deposited ',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,13,'(ULIP)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,14,'NSC',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,15,'Housing Loan Payment Principal',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,16,'ELSS',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,17,'(Sukanya Samriddhi Scheme)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,18,'Mutual Fund',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,19,'Tuition Fee',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,20,'Pension Fund',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        # worksheet.write(0,15,'Mutual Fund',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        # worksheet.write(0,16,'(Sukanya Samriddhi Scheme)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        # worksheet.write(0,17,'Employee Contribution to National Pension Scheme(NPS)-80CCD(1B)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,21,'Mediclaim Insurance (Self/Spoue/Childrens)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,22,'Medical Insurance Premium paid For Parents/Senior Citizen',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,23,'Disability type',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,24,'(80DD) (Payment on medical treatment of handicapped  dependents )',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,25,' Medical Treatment Towards',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,26,'(80DDB) (ACTUAL EXP., DED. UPTO 40,000 OR 60,000)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,27,'(80U)(Deduction for self suffering from permanent physical disability)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,28,'(80E)(INT. ON LOAN FOR HIGHER EDU.)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        # worksheet.write(0,24,'Donations',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        # worksheet.write(0,25,'Interest from Savings Bank A/C ',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,29,'(80CCG)Rajiv Gandhi Equity Saving Scheme (RGESS)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,30,'Employee Contribution to National Pension Scheme(NPS)-80CCD(1B)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,31,'Employer Contribution to NPS Account u/s-80CCD(2)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,32,'Interest from Savings Bank A/C ',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,33,'INCOME/LOSS(-) FORM HOUSE PROPERTY',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,34,'Self occupied residential property has been acquired or constructed before end of the Current Financial Year (No Benefit is available, if property is not completed/ Possession)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,35,'INTEREST FOR SELF OCCUPIED PROPERTY',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,36,'PRE EMI INTEREST PAID(for Self Occupied Property)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,37,'Lender Name1(Self Occupied Property)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,38,'PAN of Lender1/Financier (Mandatory)(Self Occupied Property)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,39,'Lender Name2(Self Occupied Property)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,40,'PAN of Lender2/Financier (Mandatory)(Self Occupied Property)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,41,'Property Situated at (place of said property)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,42,'City',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,43,'Other Property has been acquired or constructed before end of the Current Financial Year (No Benefit is available, if property is not completed/ Possession)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,44,'INTEREST FOR OTHERS PROPERTY ',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,45,'PRE EMI INTEREST PAID(Other Property)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,46,'INCOME FROM HOUSE PROPERTY',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,47,'Fair rent of same locality (per month) ',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,48,'Lender Name1(Other Property)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,49,'PAN of Lender1/Financier (Mandatory)(Other Property)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,50,'Lender Name2(Other Property)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,51,'PAN of Lender2/Financier (Mandatory)(Other Property)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,52,'House Rent Paid',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,53,'METRO',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,54,'PAN OF LANDLORD',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,55,'NAME OF LANDLORD',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        # worksheet.write(0,28,'(80EE) (ADDTIONAL DED. RS. 50,000/-)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        # worksheet.write(0,29,'INTT. ON LOAN FOR HIGHER EDU',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,56,'Address of property',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,57,'INCOME_PREV_EMPLOYER(01/04/2018 to date of leaving from previous employer)-1',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,58,'"TDS"_FROM PREV_EMPLOYER-1',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,59,'PF_FROM PREV_EMPLOYER-1',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,60,'Period of Employment(For Current Year only)-1',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,61,'Previous Employer Name1',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,62,'Previous Employer Address1',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,63,'TAN EMPLOYER-1',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,64,'PAN EMPLOYER-1',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,65,'REMARKS-1',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,66,'INCOME_PREV_EMPLOYER(01/04/2018 to date of leaving from previous employer)-2',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,67,'"TDS"_FROM PREV_EMPLOYER-2',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,68,'PF_FROM PREV_EMPLOYER-2',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,69,'Period of Employment(For Current Year only)-2',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,70,'Previous Employer Name2',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,71,'Previous Employer Address2',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,72,'TAN EMPLOYER-2',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,73,'PAN EMPLOYER-2',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,74,'REMARKS-2',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))



        # worksheet.write(0,31,'City',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        # worksheet.write(0,34,'INTEREST FOR SELF OCCUPIED PROPERTY',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
#         worksheet.write(0,40,'Status of Declaration upload',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
#         worksheet.write(0,41,'Date',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
#         worksheet.write(0,42,'REMOVED',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
#         worksheet.write(0,40,'MEDICLAIM REIMBUREMENT BY CO.',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))

        state='submit'
        
#        worksheet.write(0,12,'(Other)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
#         worksheet.write(0,13,'(Housing Loan Repayment)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
#        worksheet.write(0,17,'(80D)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
#        worksheet.write(0,19,'(80CCG)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
#        worksheet.write(0,21,'(80U)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
#        worksheet.write(0,34,'REMARKS',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        if self.declaration_version_id:
            self._cr.execute("""SELECT id FROM declaration
                    WHERE declaration_version_id = %s and state = %s""",(self.declaration_version_id.id,state))
            version_ids = self._cr.fetchall()
            b = 1
            dict1 = {'normal':'Normal','severe':'Severe'}
            dict2 = {'med_treat':'Non-Senior Citizen','med_treat_sen':'Senior Citizen','med_treat_sup_sen':'Super Senior Citizen'}
            cnt = 0
            for picking_id in version_ids:
                b+=1
                cnt+=1
                picking_obj=self.env['declaration'].browse(picking_id[0])
                landlord_address = str(picking_obj.street1 or ' ')+' '+str(picking_obj.street2 or '')+' '+str(picking_obj.city or '')+' '+str(picking_obj.states.name or '')+' '+str(picking_obj.zip_code or '')
                worksheet.write(b, 0, cnt)
                worksheet.write(b, 1, picking_obj.emp_code or '')
                worksheet.write(b, 2, picking_obj.declaration_version_id.fiscal_year or '')
                worksheet.write(b, 3, picking_obj.emp_name or '')
                worksheet.write(b, 4, picking_obj.state or '')
                worksheet.write(b, 5, picking_obj.mobile or '')
                worksheet.write(b, 6, picking_obj.email or '')
                if picking_obj.date_of_joining:
                    date_of_joining = datetime.strptime(picking_obj.date_of_joining, "%Y-%m-%d").strftime("%d-%m-%Y")
                    worksheet.write(b, 7, date_of_joining or '')
                worksheet.write(b, 8, picking_obj.details or '')
                worksheet.write(b, 9, picking_obj.details1 or '')
                # worksheet.write(b, 7,)
                worksheet.write(b, 10, picking_obj.details2 or '')
                if picking_obj.details3:
                    details3 = datetime.strptime(picking_obj.details3, "%Y-%m-%d").strftime("%d-%m-%Y")
                    worksheet.write(b, 11, details3 or '')
                worksheet.write(b, 12, picking_obj.details4 or '')
                worksheet.write(b, 13, picking_obj.details5 or '')
                worksheet.write(b, 14, picking_obj.details6 or '')
                worksheet.write(b, 15, picking_obj.details8 or '')
                worksheet.write(b, 16, picking_obj.details9 or '')
                worksheet.write(b, 17, picking_obj.details17 or '')
                worksheet.write(b, 18, picking_obj.details32 or '')
                worksheet.write(b, 19, picking_obj.details10 or '')
                worksheet.write(b, 20, picking_obj.details11 or '')
                # worksheet.write(b, 15, picking_obj.details32 or '')
                # worksheet.write(b, 16, picking_obj.details17 or '')
                # worksheet.write(b, 17, picking_obj.details33 or '')
                worksheet.write(b, 21, picking_obj.details12 or '')
                worksheet.write(b, 22, picking_obj.details31 or '')
                if not picking_obj.type_disability:
                    worksheet.write(b, 23)
                else:
                    worksheet.write(b, 23, dict1[picking_obj.type_disability])
                worksheet.write(b, 24, picking_obj.details13 or '')
                if not picking_obj.type_treatment:
                    worksheet.write(b, 25)
                else:
                    worksheet.write(b, 25, dict2[picking_obj.type_treatment or False])
                worksheet.write(b, 26, picking_obj.details18 or '')
                worksheet.write(b, 27, picking_obj.details15 or '')
                worksheet.write(b, 28, picking_obj.details14 or '')
                # worksheet.write(b, 24, )
                # worksheet.write(b, 25, picking_obj.details34 or '')
                worksheet.write(b, 29, picking_obj.details19 or '')
                worksheet.write(b, 30, picking_obj.details33 or '')
                worksheet.write(b, 31, picking_obj.details16 or '')
                worksheet.write(b, 32, picking_obj.details34 or '')
                worksheet.write(b, 33, picking_obj.details181 or '')
                worksheet.write(b, 34, picking_obj.details22 or '')
                worksheet.write(b, 35, picking_obj.details20 or '')
                worksheet.write(b, 36, picking_obj.pre_emi_interest_paid or '')
                worksheet.write(b, 37, picking_obj.lender_name or '')
                worksheet.write(b, 38, picking_obj.details191 or '')
                worksheet.write(b, 39, picking_obj.lender_name2 or '')
                worksheet.write(b, 40, picking_obj.pan_no_lender2 or '')
                worksheet.write(b, 41, picking_obj.details37 or '')
                worksheet.write(b, 42, picking_obj.details38 or '')
                worksheet.write(b, 43, picking_obj.details24 or '')
                worksheet.write(b, 44, picking_obj.details23 or '')
                worksheet.write(b, 45, picking_obj.details27 or '')
                worksheet.write(b, 46, picking_obj.details25 or '')
                worksheet.write(b, 47, picking_obj.details26 or '')
                worksheet.write(b, 48, picking_obj.other_lender_name or '')
                worksheet.write(b, 49, picking_obj.other_pan_no_lender1 or '')
                worksheet.write(b, 50, picking_obj.other_lender_name2 or '')
                worksheet.write(b, 51, picking_obj.other_pan_no_lender2 or '')
                worksheet.write(b, 52, picking_obj.house_rent_paid_per_month or 0.0)
                worksheet.write(b, 53, picking_obj.city_metro or '')
                worksheet.write(b, 54, picking_obj.pan_of_landlord or '')
                worksheet.write(b, 55, picking_obj.full_name_of_landlord or '')
                # worksheet.write(b, 28, picking_obj.details35 or '')
                # worksheet.write(b, 29, picking_obj.details14 or '')
                worksheet.write(b, 56, landlord_address or '')
                worksheet.write(b, 57, picking_obj.details28 or '')
                worksheet.write(b, 58, picking_obj.details29 or '')
                worksheet.write(b, 59, picking_obj.details30 or '')
                if picking_obj.details36 and picking_obj.to_date1:
                    details36 = datetime.strptime(picking_obj.details36, "%Y-%m-%d").strftime("%d-%m-%Y")
                    to_date1 = datetime.strptime(picking_obj.to_date1, "%Y-%m-%d").strftime("%d-%m-%Y")
                    worksheet.write(b, 60, (str(details36 or ' ')+ 'To' +str(to_date1 or ' ')) or ' ')
                elif picking_obj.details36:
                    details36 = datetime.strptime(picking_obj.details36, "%Y-%m-%d").strftime("%d-%m-%Y")
                    worksheet.write(b, 60, (str(details36 or ' ')+ 'To' +str(picking_obj.to_date1 or ' ')) or ' ')
                elif picking_obj.to_date1:
                    to_date1 = datetime.strptime(picking_obj.to_date1, "%Y-%m-%d").strftime("%d-%m-%Y")
                    worksheet.write(b, 60, (str(picking_obj.details36 or ' ')+ 'To' +str(to_date1 or ' ')) or ' ')
                worksheet.write(b, 61, picking_obj.details39 or '')
                worksheet.write(b, 62, picking_obj.details40 or '')
                worksheet.write(b, 63, picking_obj.tan1 or '')
                worksheet.write(b, 64, picking_obj.pan1 or '')
                worksheet.write(b, 65, picking_obj.remark1 or '')
                worksheet.write(b, 66, picking_obj.details228 or '')
                worksheet.write(b, 67, picking_obj.details229 or '')
                worksheet.write(b, 68, picking_obj.details230 or '')
                if picking_obj.details236 and picking_obj.to_date2:
                    details236 = datetime.strptime(picking_obj.details236, "%Y-%m-%d").strftime("%d-%m-%Y")
                    to_date2 = datetime.strptime(picking_obj.to_date2, "%Y-%m-%d").strftime("%d-%m-%Y")
                    worksheet.write(b, 69, (str(details236 or ' ')+ 'To' +str(to_date2 or ' ')) or '')
                elif picking_obj.details236:
                    details236 = datetime.strptime(picking_obj.details236, "%Y-%m-%d").strftime("%d-%m-%Y")
                    worksheet.write(b, 69, (str(details236 or ' ')+ 'To' +str(picking_obj.to_date2 or ' ')) or '')
                elif picking_obj.to_date2:
                    to_date2 = datetime.strptime(picking_obj.to_date2, "%Y-%m-%d").strftime("%d-%m-%Y")
                    worksheet.write(b, 69, (str(picking_obj.details236 or ' ')+ 'To' +str(to_date2 or ' ')) or '')
                worksheet.write(b, 70, picking_obj.employer_name2 or '')
                worksheet.write(b, 71, picking_obj.employer_address2 or '')
                worksheet.write(b, 72, picking_obj.tan2 or '')
                worksheet.write(b, 73, picking_obj.pan2 or '')
                worksheet.write(b, 74, picking_obj.remark2 or '')
                
                # worksheet.write(b, 31, picking_obj.details38 or '')
                # worksheet.write(b, 34, picking_obj.details20 or '')
                # worksheet.write(b, 40, picking_obj.details41 or '')

                

        fp = cStringIO.StringIO()
        wb.save(fp)
        out = base64.encodestring(fp.getvalue())
        view_report_status_id=self.env['view.report'].create({'file_name':out,'datas_fname':filename})
        return {
        'res_id'   :view_report_status_id.id,
        'name'     :'Declaration Details Report',
        'view_type':'form',
        'view_mode':'form',
        'res_model':'view.report',
        'view_id'  : False ,
        'type'     :'ir.actions.act_window',
    }
      
class view_report(models.TransientModel):
    _name = 'view.report'
    _rec_name = 'datas_fname'
    datas_fname=fields.Char('File Name', size=256)
    file_name=fields.Binary('Report')
    
