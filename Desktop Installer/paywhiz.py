# -*- coding: utf-8 -*-
#!/usr/bin/env python

import time, sys
import pyodbc
import xlrd
from xlrd import XLRDError
import logging
LOG_FILENAME = 'Paywhiz Import.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
import Tkinter, tkFileDialog
root = Tkinter.Tk()
root.withdraw()

print "Please select excel file to upload!"
time.sleep(2)
path = tkFileDialog.askopenfilename()
path = path.encode('utf-8')
print "path == > ",path
logging.info(path)
if not path:
    print "File not selected. Please try again!"
    time.sleep(2)
    exit()
#db_file = r'''C:\Program Files\Sinewave\Paywhiz\TAXBASE.MDB'''
user = 'admin'
odbc_url = 'DRIVER={Driver do Microsoft Access (*.mdb)};UID=%s;PWD=%s;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL={MS Access};DriverId=25;DBQ=%s;'

db_file = r'''D:\Paywhiz\Taxbase.mdb'''
password = 'T!5b)2^M'
odbc_conn_str = odbc_url % (user, password, db_file)
conn = pyodbc.connect(odbc_conn_str)
cursor = conn.cursor()

payroll_file = r'''D:\Paywhiz\Payroll.mdb'''
pwd = u'1Wu§Ãèû'
payroll_conn_str = odbc_url % (user, pwd, payroll_file)
pconn = pyodbc.connect(payroll_conn_str)
pcursor = pconn.cursor()

#path = 'Investment Declaration Test Data and Issue Tracker.xlsx'
try:
    
    workbook = xlrd.open_workbook(path)
except XLRDError:
    print "Invalid Excel file!!!"
    logging.info("Invalid Excel file!!!")
    time.sleep(3)
    exit()
worksheet = workbook.sheet_by_index(0)
offset = 1
rows = []
for i, row in enumerate(range(worksheet.nrows)):
    if i <= offset:  # (Optionally) skip headers
        continue
    r = []
    for j, col in enumerate(range(worksheet.ncols)):
        r.append(worksheet.cell_value(i, j))
    rows.append(r)

print 'Importing %d records.' % (len(rows), )
user_input = raw_input("Continue?:(y/n) ")
if user_input not in ('y', 'Y'):
    print "Exiting.."
    time.sleep(1.5)
    exit()	
for row in rows:
    emp_code = False
    ecode = row[1]
    ASS_YR = row[2]
    sel_qry = "select PAYEE_CODE from EMPLOYEE_MASTER1 where TOKEN_NO = '%s'" % (ecode,)
    pcursor.execute(sel_qry)
    data = pcursor.fetchall()
    if data:
        emp_code = data[0][0]
    else:
        msg = "\n\n\n\Employee  Data not found for employee %s : %s  for Assessment Year %s." % (ecode, row[3], ASS_YR)
        logging.info(msg)
        print msg
        time.sleep(1.5)
        continue	        
    msg = "\n\n\n\nImporting Data for employee %s : %s  for Assessment Year %s." % (emp_code, row[3], ASS_YR)
    logging.info(msg)
    print msg
    time.sleep(1)

    lic_amt = row[5]
    post_off = row[6]
    ppf = row[8]
    ulip_amt = row[9]
    nsc_amt = row[10]
    hlrp_amt = row[11]
    elss = row[12]
    tution = row[13]
    pension = row[14]
    mf = row[15]
    sukanya = row[16]

    ins_qry = "insert into CHAPTERVIIIA ([GROUP], [CODE], [ASS_YR], [VIIIA_CODE], [VIIIA_DESP], [VIIIA_INVESTMENT], [VIIIA_ELIGIBLE], [EMP_CODE]) values "

    if lic_amt:
        sel_qry = "select VIIIA_INVESTMENT from CHAPTERVIIIA where ASS_YR = '%s' and VIIIA_CODE = 'VIIIA_LIC' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry + "('00001','00001','%s','VIIIA_LIC','Life Insurance Premium',%f,%f,'%s')" % (ASS_YR, lic_amt, lic_amt,emp_code)
            cursor.execute(query)
            msg = "LIC amount %f updated for emp code %s." % (lic_amt,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "LIC Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)
    if post_off:
        sel_qry = "select VIIIA_INVESTMENT from CHAPTERVIIIA where ASS_YR = '%s' and VIIIA_CODE = 'VIIIA_OTH2' and VIIIA_INVESTMENT = %f and EMP_CODE = '%s'" % (ASS_YR, post_off, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry + "('00001','00001','%s','VIIIA_OTH2','Post Office saving',%f,%f,'%s')" % (ASS_YR, post_off, post_off,emp_code)
            cursor.execute(query)
            msg = "Post Office saving %f updated for emp code %s." % (post_off,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "Post Office saving Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (emp_code, ASS_YR, data[0][0])
            print msg
            logging.info(msg)		
    if ppf:
        sel_qry = "select VIIIA_INVESTMENT from CHAPTERVIIIA where ASS_YR = '%s' and VIIIA_CODE = 'VIIIA_PPF' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry + "('00001','00001','%s','VIIIA_PPF','Public Provident Fund',%f,%f,'%s')" % (ASS_YR, ppf, ppf,emp_code)
            cursor.execute(query)
            msg = "PPF %f updated for emp code %s." % (ppf,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "PPF Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)
			
    if ulip_amt:
        sel_qry = "select VIIIA_INVESTMENT from CHAPTERVIIIA where ASS_YR = '%s' and VIIIA_CODE = 'VIIIA_ULIP' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry + "('00001','00001','%s','VIIIA_ULIP','Unit Linked Insurance Premium',%f,%f,'%s')" % (ASS_YR, ulip_amt, ulip_amt,emp_code)
            cursor.execute(query)
            msg = "ULIP %f updated for emp code %s." % (ulip_amt,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "ULIP Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)

    if nsc_amt:
        sel_qry = "select VIIIA_INVESTMENT from CHAPTERVIIIA where ASS_YR = '%s' and VIIIA_CODE = 'VIIIA_NSC_ND' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry + "('00001','00001','%s','VIIIA_NSC_ND','N.S.C. (New Deposits)',%f,%f,'%s')" % (ASS_YR, nsc_amt, nsc_amt,emp_code)
            cursor.execute(query)
            msg = "N.S.C. (New Deposits): %f updated for emp code %s." % (nsc_amt,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "N.S.C. (New Deposits) Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)
    if hlrp_amt:
        sel_qry = "select VIIIA_INVESTMENT from CHAPTERVIIIA where ASS_YR = '%s' and VIIIA_CODE = 'VIIIA_REP_HL' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry + "('00001','00001','%s','VIIIA_REP_HL','Instalment or Part Payment for Purchase or Construction of residential house Property for repayment of loans',%f,%f,'%s')" % (ASS_YR, hlrp_amt, hlrp_amt,emp_code)
            cursor.execute(query)
            msg = "House Property for repayment of loans: %f updated for emp code %s." % (hlrp_amt,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "House Property for repayment of loans Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)

    if elss:
        sel_qry = "select VIIIA_INVESTMENT from CHAPTERVIIIA where ASS_YR = '%s' and VIIIA_CODE = 'VIIIA_OTH2' and VIIIA_INVESTMENT = %f and EMP_CODE = '%s'" % (ASS_YR, elss, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry + "('00001','00001','%s','VIIIA_OTH2','ELSS',%f,%f,'%s')" % (ASS_YR, elss, elss,emp_code)
            cursor.execute(query)
            msg = "ELSS: %f updated for emp code %s." % (elss,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "ELSS Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)

    if tution:
        sel_qry = "select VIIIA_INVESTMENT from CHAPTERVIIIA where ASS_YR = '%s' and VIIIA_CODE = 'VIIIA_EDU_EXP' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry + "('00001','00001','%s','VIIIA_EDU_EXP','Tuition Fees',%f,%f,'%s')" % (ASS_YR, tution, tution,emp_code)
            cursor.execute(query)
            msg = "Tuition Fees: %f updated for emp code %s." % (tution,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "Tuition Fees Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)

    if mf:
        sel_qry = "select VIIIA_INVESTMENT from CHAPTERVIIIA where ASS_YR = '%s' and VIIIA_CODE = 'VIIIA_MUTUAL' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry + "('00001','00001','%s','VIIIA_MUTUAL','Mutual Fund',%f,%f,'%s')" % (ASS_YR, mf, mf,emp_code)
            cursor.execute(query)
            msg = "Mutual Fund : %f updated for emp code %s." % (mf,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "Mutual Fund Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)

    if pension:
        sel_qry = "select VIIIA_INVESTMENT from CHAPTERVIIIA where ASS_YR = '%s' and VIIIA_CODE = 'VIIIA_80CCC' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry + "('00001','00001','%s','VIIIA_80CCC','Deduction in respect of contribution to certain pension funds',%f,%f,'%s')" % (ASS_YR, pension, pension,emp_code)
            cursor.execute(query)
            msg = "Pension funds: %f updated for emp code %s." % (pension,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "Pension funds Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)

    if sukanya:
        sel_qry = "select VIIIA_INVESTMENT from CHAPTERVIIIA where ASS_YR = '%s' and VIIIA_CODE = 'VIIIA_OTH2' and VIIIA_INVESTMENT = %f and EMP_CODE = '%s'" % (ASS_YR, sukanya, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry + "('00001','00001','%s','VIIIA_OTH2','SUKANYA SAMRIDHHI YOJANA',%f,%f,'%s')" % (ASS_YR, sukanya, sukanya,emp_code)
            cursor.execute(query)
            msg = "SUKANYA SAMRIDHHI YOJANA: %f updated for emp code %s." % (sukanya,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "SUKANYA SAMRIDHHI YOJANA Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)

#	Chapter VI table		
######################	
    ins_qry_2 = "insert into CHAPTERVIA ([GROUP], [CODE], [ASS_YR], [VIA_CODE], [VIA_DESP], [VIA_PAYMENT], [VIA_ELIGIBLE], [VIA_DEDUCTION], [EMP_CODE], [VIA_AMOUNT1], [VIA_BOOL], [NO_MONTHS]) values "		
    nps = row[17]
    medi = row[18]
    medi_senior = row[19]
    disability_type = row[20]
    handi = row[21]
    medi_2wards = row[22]
    treatment = row[23]
    saving = row[25]
    rgess = row[26]
    ccd2 = row[27]
    VI80ee = row[28]
    VI80e = row[29]
    if nps:
        sel_qry = "select VIA_PAYMENT from CHAPTERVIA where ASS_YR = '%s' and VIA_CODE = 'VIA_80CCD(1B)' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry_2 + "('00001','00001','%s','VIA_80CCD(1B)','Additional deduction for National Pension System Contribution.',%f,%f,%f, '%s', 0,0,12)" % (ASS_YR, nps, nps, nps,emp_code)
            cursor.execute(query)
            msg = "ELSS: %f updated for emp code %s." % (elss,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "NPS Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)
    if medi or medi_senior:
        medi = medi or 0.0
        medi_senior = medi_senior or 0.0
        via_bool = medi_senior and -1 or 0
        VIA_PAYMENT = medi
        VIA_ELIGIBLE = medi + medi_senior
        VIA_DEDUCTION = medi + medi_senior
        VIA_AMOUNT1 = medi_senior
        sel_qry = "select VIA_PAYMENT from CHAPTERVIA where ASS_YR = '%s' and VIA_CODE = 'VIA_80D' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry_2 + "('00001','00001','%s','VIA_80D','Deduction in respect of Medical Insurance Premia',%f,%f,%f, '%s', %f,%d,12)" % (ASS_YR, VIA_PAYMENT, VIA_ELIGIBLE, VIA_DEDUCTION,emp_code,VIA_AMOUNT1, via_bool)
            cursor.execute(query)
            msg = "Medical Insurance: %f updated for emp code %s." % (medi,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "Medical Insurance Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)

    if handi:
        via_bool = 0
        via_bool2 = -1
        if not disability_type:
            disability_type = "Normal"
        hlimit = 75000.0
        if disability_type == "Severe":
            hlimit = 125000.0
            via_bool = -1
            via_bool2 = 0
        VIA_DEDUCTION = min(handi, hlimit)
        sel_qry = "select VIA_PAYMENT from CHAPTERVIA where ASS_YR = '%s' and VIA_CODE = 'VIA_80DD' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = "insert into CHAPTERVIA ([GROUP], [CODE], [ASS_YR], [VIA_CODE], [VIA_DESP], [VIA_PAYMENT], [VIA_ELIGIBLE], [VIA_DEDUCTION], [EMP_CODE], [VIA_AMOUNT1], [VIA_BOOL], [VIA_BOOL2], [NO_MONTHS]) values ('00001','00001','%s','VIA_80DD','Deduction in respect of maintenance including medical treatment of handicapped dependent',%f,%f,%f, '%s', 0,%d,%d,12)" % (ASS_YR, handi, VIA_DEDUCTION, VIA_DEDUCTION,emp_code,via_bool,via_bool2)
            cursor.execute(query)
            msg = "medical treatment of handicapped dependent: %f updated for emp code %s." % (handi,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "medical treatment of handicapped dependent Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)

    if treatment:
        dic1 = {'Non-Senior Citizen' : 1, 'Senior Citizen':2, 'Super Senior Citizen':3}
        if not medi_2wards:
            medi_2wards = 'Non-Senior Citizen'
        undertaking=dic1.get(medi_2wards, 1)
        VIA_DEDUCTION = min(treatment, 60000.00)
        sel_qry = "select VIA_PAYMENT from CHAPTERVIA where ASS_YR = '%s' and VIA_CODE = 'VIA_80DDB' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = "insert into CHAPTERVIA ([GROUP], [CODE], [ASS_YR], [VIA_CODE], [VIA_DESP], [VIA_PAYMENT], [VIA_ELIGIBLE], [VIA_DEDUCTION], [EMP_CODE], [VIA_AMOUNT1], [VIA_BOOL], [NO_MONTHS], [Undertaking2]) values ('00001','00001','%s','VIA_80DDB','Deduction towards Medical Treatment etc.',%f,%f,%f, '%s', 0,0,12,%d)" % (ASS_YR, treatment, VIA_DEDUCTION, VIA_DEDUCTION,emp_code,undertaking)
            cursor.execute(query)
            msg = "Deduction towards Medical Treatment: %f updated for emp code %s." % (treatment,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "Deduction towards Medical Treatment Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)
    if saving:
        VIA_DEDUCTION = min(saving, 10000.00)
        sel_qry = "select VIA_PAYMENT from CHAPTERVIA where ASS_YR = '%s' and VIA_CODE = 'VIA_80TTA' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry_2 + "('00001','00001','%s','VIA_80TTA','Deduction in respect of interest on deposites in savings account',%f,%f,%f, '%s', 0,0,12)" % (ASS_YR, saving, VIA_DEDUCTION, VIA_DEDUCTION,emp_code)
            cursor.execute(query)
            msg = "Savings account: %f updated for emp code %s." % (saving,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "savings account Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)
    if rgess:
        rgess = rgess / 2
        VIA_DEDUCTION = min(rgess, 25000.00)
        sel_qry = "select VIA_PAYMENT from CHAPTERVIA where ASS_YR = '%s' and VIA_CODE = 'VIA_80CCG' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry_2 + "('00001','00001','%s','VIA_80CCG','Deduction in respect of investment made under an equity savings',%f,%f,%f, '%s', 0,0,12)" % (ASS_YR, rgess, VIA_DEDUCTION, VIA_DEDUCTION,emp_code)
            cursor.execute(query)
            msg = "RGESS: %f updated for emp code %s." % (rgess,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "RGESS Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)
    if ccd2:
        sel_qry = "select VIA_PAYMENT from CHAPTERVIA where ASS_YR = '%s' and VIA_CODE = 'VIA_80CCD(2)' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry_2 + "('00001','00001','%s','VIA_80CCD(2)','Deduction in respect of employer s contribution to pension scheme of Central Government u/s 80CCD(2)',%f,%f,%f, '%s', 0,0,12)" % (ASS_YR, ccd2, ccd2, ccd2,emp_code)
            cursor.execute(query)
            msg = "VIA_80CCD(2): %f updated for emp code %s." % (ccd2,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "VIA_80CCD(2) Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)
    if VI80ee:
        VIA_DEDUCTION = min(VI80ee, 50000.00)
        sel_qry = "select VIA_PAYMENT from CHAPTERVIA where ASS_YR = '%s' and VIA_CODE = 'VIA_80EE' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry_2 + "('00001','00001','%s','VIA_80EE','Deduction in respect of interest on loan taken for residential house property.',%f,%f,%f, '%s', 0,0,12)" % (ASS_YR, VI80ee, VIA_DEDUCTION, VIA_DEDUCTION,emp_code)
            cursor.execute(query)
            msg = "VIA_80EE: %f updated for emp code %s." % (VI80ee,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "VIA_80EE Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)
    if VI80e:
        sel_qry = "select VIA_PAYMENT from CHAPTERVIA where ASS_YR = '%s' and VIA_CODE = 'VIA_80E' and EMP_CODE = '%s'" % (ASS_YR, emp_code)
        cursor.execute(sel_qry)
        data = cursor.fetchall()
        if not data:
            query = ins_qry_2 + "('00001','00001','%s','VIA_80E','Deduction in respect of interest on loan taken for higher education',%f,%f,%f, '%s', 0,0,12)" % (ASS_YR, VI80e, VI80e, VI80e,emp_code)
            cursor.execute(query)
            msg = "VIA_80E: %f updated for emp code %s." % (VI80e,emp_code)
            print msg
            logging.info(msg)
        else:
            msg = "VIA_80E Details already exists for emp code %s for Assesment year %s. Amount declared is : %f." % (ASS_YR, emp_code, data[0][0])
            print msg
            logging.info(msg)
#	House Property
#    prop_type = row[28]	
    address = row[30] or ''
    city = row[31] or ''
    income_prop = row[32] or 0.0
    interest_oth = row[33] or 0.0
    interest_self = row[34] or 0.0
    preemi_interest = row[35] or 0.0
    rent = row[36] or 0.0
    ins_qry_3 = "insert into HOUSE_PROPERTY ([GROUP], [CODE], [ASS_YR], [HOUSE_SNO], [HOUSE_OWNER_PER], [HOUSE_RENT_SO], [HOUSE_RENT_VALUE], [HOUSE_ANNUAL_VALUE], [HOUSE_INTEREST], [HOUSE_COLLECTIONCHARGES], [HOUSE_SELFOCC_ACTINT], [HOUSE_PRE_CONST_INT], [EMP_CODE], [HOUSE_DETAIL1], [HOUSE_DETAIL2]) values "
	
    if income_prop or interest_self:
        # 30% of income from property allowed	
        HOUSE_COLLECTIONCHARGES = income_prop * 0.3
        query = ins_qry_3 + "('00001','00001','%s', 1, 100, 'S', 0, 0, %f,%f,%f,%f, '%s', '%s', '%s')" % (ASS_YR, interest_self, HOUSE_COLLECTIONCHARGES, interest_self, preemi_interest,emp_code, address, city)
        cursor.execute(query)
        msg = "House property details updated for emp code %s." % (emp_code,)
        print msg
        logging.info(msg)

    if rent:
        sno = income_prop and 2 or 1
        query = ins_qry_3 + "('00001','00001','%s',%d, 100, 'R', %f,%f,0,0,0, 0, '%s', '%s', '%s')" % (ASS_YR, sno, rent, rent, emp_code, address, city)
        cursor.execute(query)
        msg = "Rented property details updated for emp code %s." % (emp_code,)
        print msg
        logging.info(msg)

#	Previous Empl. Income
    employer_name = row[41] or 0.0
    employer_addr = row[42] or 0.0
    prev_income = row[43] or 0.0
    prev_tds = row[44] or 0.0
    prev_pf = row[45] or 0.0
    no_mnth = row[46] or 0
    no_mnth = int(no_mnth)
    ins_qry_4 = "insert into SALARY ([GROUP], [CODE], [EMP_CODE], [Sal_summ_sno], [Sal_summ_car_mths], [Sal_summ_desc],[Ass_yr], [Sal_summ_employer], [Sal_summ_Emp_add], [Sal_summ_oth],	[Sal_summ_taxable_pr_stdded], [Sal_For_HRA],[Sal_summ_tds], [Sal_summ_pf], [Sal_summ_sal_mon],[Sal_summ_hra_rec_mon],[Sal_summ_exp_pay_mon]) values "

    if prev_income:
        query = ins_qry_4 + "('00001','00001', '%s', 2, 12, 'Salary', '%s', '%s', '%s', %f, %f, %f, %f, %f, %d, %d, %d)" % (emp_code, ASS_YR, employer_name, employer_addr, prev_income, prev_income, prev_income, prev_tds,prev_pf,no_mnth,no_mnth,no_mnth)
        cursor.execute(query)
        msg = "Previous Employer details updated for emp code %s." % (emp_code,)
        print msg
        logging.info(msg)
conn.commit()
conn.close()
pconn.close()
print "\n\n\nImport Done. Please check log file '%s' for details." % LOG_FILENAME
time.sleep(5)
exit()
#################################