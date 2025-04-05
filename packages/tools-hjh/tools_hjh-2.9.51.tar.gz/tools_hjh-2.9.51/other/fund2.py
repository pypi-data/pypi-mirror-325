# coding:utf-8
import sys
from tools_hjh import DBConn
from tools_hjh import Log
from tools_hjh import ThreadPool
from tools_hjh import Tools
from tools_hjh import HTTPTools
import json
import time
import datetime
from dateutil.relativedelta import relativedelta
from tools_hjh.Chrome import ChromePool
import numpy as np
import math

stop_flag = False
page_num = None

date = Tools.locatdate()
log = Log('U:/MyFiles/MyPy/log/fund/' + date + '.log')

host = 'https://'

chrome_path = r'D:\MyApps\CentBrowser\App\chrome.exe'
chromedriver_path = r'D:\MyApps\CentBrowser\chromedriver.exe'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'text',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'dnt': '1',
    'pragma': 'no-cache',
    'sec-ch-ua': 'x86;v=99, Windows;v=10, Surface Laptop Studio;v=1',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Referer':'http://fundf10.eastmoney.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    'cookie':'qgqp_b_id=5b3011884880cd251f1bc065e16256ae; emshistory=%5B%22513100%22%5D; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; HAList=ty-103-NQ00Y-%u5C0F%u578B%u7EB3%u6307%u5F53%u6708%u8FDE%u7EED%2Cty-100-NDX100-%u7EB3%u65AF%u8FBE%u514B100%2Cty-133-USDCNH-%u7F8E%u5143%u79BB%u5CB8%u4EBA%u6C11%u5E01%2Cty-1-512690-%u9152ETF%2Cty-1-513100-%u7EB3%u6307ETF%2Cty-105-NVDA-%u82F1%u4F1F%u8FBE%2Cty-1-600900-%u957F%u6C5F%u7535%u529B%2Cty-1-000001-%u4E0A%u8BC1%u6307%u6570; st_si=04690614705089; st_asi=delete; EMFUND0=null; EMFUND7=07-18%2022%3A48%3A53@%23%24%u62DB%u5546%u4E2D%u8BC1%u767D%u9152%u6307%u6570%28LOF%29A@%23%24161725; EMFUND8=07-19%2002%3A43%3A47@%23%24%u6613%u65B9%u8FBE%u5929%u5929%u7406%u8D22%u8D27%u5E01A@%23%24000009; EMFUND9=07-29 10:05:57@#$%u534E%u590F%u6210%u957F%u6DF7%u5408@%23%24000001; st_pvi=99805886133314; st_sp=2024-04-24%2009%3A56%3A14; st_inirUrl=http%3A%2F%2Fquote.eastmoney.com%2Fsh513100.html; st_sn=4; st_psi=20240729100557782-112200305282-3955411629'
}

try:
    sys_argv_1 = sys.argv[1]
except:
    sys_argv_1 = 'download'
try:
    sys_argv_2 = int(sys.argv[2])
except:
    sys_argv_2 = -1  # 获取条数
try:
    sys_argv_3 = sys.argv[3]
except:
    sys_argv_3 = 1
    
thread_num = 4


def main(): 
    db = DBConn('sqlite', db='U:/MyFiles/MyPy/data/fund.db')
    createDatabase(db, rebuild=False)

    # get_fund_main(db, HTTPTools)
    # chrome = ChromePool(1, chrome_path, chromedriver_path, is_display_picture=False, is_hidden=True)
    # chrome.close()
    # get_fund_dv(db, HTTPTools, page_size=9999, begin_code='000000', code=None, name_like='%国泰纳斯达克100指数%')
    # get_fund_dv(db, HTTPTools, page_size=9999, begin_code='000000', code=None, name_like='%纳斯达克%')
    # get_fund_dv(db, HTTPTools, page_size=9999, begin_code='000000', code=None, name_like='%纳指%')
    get_fund_dv(db, HTTPTools, page_size=9999, begin_code='000000', code=None, name_like='%%')
    get_zf(db)
    get_val(db)
    get_hc(db)
    get_nh(db)
    get_xp(db)


def createDatabase(db, rebuild=False):
    if rebuild:
        db.run('drop table if exists t_main')
        db.run('drop table if exists t_date_value')

    t_main = '''
        create table if not exists t_main(
            code char(9),
            name varchar(255),
            type varchar(255),
            primary key(code)
        )
    '''
    
    t_date_value = '''
        create table if not exists t_date_value(
            code char(9),
            date char(10),
            dwjz real,
            ljjz real,
            zf real,
            fh text,
            val real,
            hc real,
            hc1n real,
            hc3n real,
            nh1n real,
            nh3n real,
            nh5n real,
            xp1n real,
            xp3n real,
            xp5n real,
            primary key(code, date)
        )
    '''
    
    db.run(t_main)
    db.run(t_date_value)
    
    db.run('create index if not exists idx_val_code on t_date_value(code)')
    db.run('create index if not exists idx_val_date on t_date_value(date)')
    db.run('create index if not exists idx_zbd_val on t_date_value(val)')
    db.run('create index if not exists idx_zbd_hc on t_date_value(hc)')
    db.run('create index if not exists idx_zbd_nh5n on t_date_value(nh5n)')


def get_fund_main(db, rep):
    sql = 'insert or replace into t_main(code,name,type) values(?,?,?)'
    page = rep.get('http://fund.eastmoney.com/js/fundcode_search.js')
    page = page.encode('utf8')[3:].decode('utf8')
    page = page.replace('var r = ', '').replace(';', '')
    fund_list = json.loads(page)
    params = []
    for fund in fund_list:
        code = fund[0]
        name = fund[2]
        type_ = fund[3]
        params.append((code, name, type_))
    num = db.run(sql, params)
    log.info('get_fund_main', num)


def get_fund_dv(db, rep, page_size, begin_code='000000', code=None, name_like=''):
    
    if page_size == '' or page_size == -1 or page_size == 0 or page_size == None or page_size == 'all':
        page_size = 9999
            
    sql = "insert into t_date_value(code,date,dwjz,ljjz,fh) select ?,?,?,?,? where not exists(select 1 from t_date_value where code = ? and date = ?)"
    vals_all = []

    def get_fund_dv_one(code, rep, page_size=9999, times=1):
        try:
            idx = 1
            timestamp = str(int(time.time() * 1000))
            url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery18306743973867400965_1722217638986&fundCode=' + code + '&pageIndex=' + str(idx) + '&pageSize=' + str(page_size) + '&startDate=&endDate=&_=' + timestamp
            page = rep.get(url, headers=headers)
            page = page.replace('jQuery18306743973867400965_1722217638986', '').strip()
            page = page.split('"LSJZList":')[1].split(',"FundType"')[0]
            rss = json.loads(page)
            
            if page_size == 9999 and len(rss) > 0:
                exists_count = db.run('select count(1) from t_date_value where code = ?', (code,)).get_rows()[0][0]
                get_min_date = rss[-1]['FSRQ']
                get_max_date = rss[0]['FSRQ']
                try:
                    db_min_date = db.run('select min(date) from t_date_value where code = ?', (code,)).get_rows()[0][0]
                except:
                    db_min_date = '1949-10-01'
                if db_min_date == None:
                    db_min_date = '1949-10-01'
                try:
                    db_max_date = db.run('select max(date) from t_date_value where code = ?', (code,)).get_rows()[0][0]
                except:
                    db_max_date = '2999-01-01'
                if db_max_date == None:
                    db_max_date = '1949-10-01'
                                        
                if int(exists_count) == len(rss) and get_min_date == db_min_date and get_max_date == db_max_date:
                    log.info('get_fund_dv_one', code, 'exists', times)
                    return
                elif get_min_date < db_min_date and int(exists_count) > 0:
                    num = db.run('delete from t_date_value where code = ?', (code,))
                    log.info('get_fund_dv_one', code, 'delete', num, times)
                elif get_min_date == db_min_date and get_max_date > db_max_date:
                    num = len(rss) - int(exists_count)
                elif int(exists_count) == 0:
                    num = len(rss)
                elif get_min_date > db_min_date:
                    raise Exception('get_min_date_error')
                    
            if len(rss) == 0:
                log.info('get_fund_dv_one', code, 0, times)
                return
            
            for rs in reversed(rss):
                date_ = rs['FSRQ']
                dwjz = rs['DWJZ']
                if dwjz == '':
                    dwjz = None
                ljjz = rs['LJJZ']
                if ljjz == '':
                    ljjz = None
                zf = rs['JZZZL']
                if zf == '':
                    zf = 0
                fh = rs['FHSP']
                if fh == '':
                    fh = None
     
                vals_all.append((code, date_, dwjz, ljjz, fh, code, date_))

            log.info('get_fund_dv_one', code, len(rss), times)
                    
        except Exception as _:
            if times <= 99:
                # log.warning('get_fund_dv_one', code, times, _)
                # time.sleep(1)
                times = times + 1
                get_fund_dv_one(code, rep, page_size, times)
            else:
                log.error('get_fund_dv_one', code, times, _)
    
    if code is not None:
        get_code_sql = '''
            select code from t_main 
            where code = ?
        '''
        funds = db.run(get_code_sql, (begin_code,)).get_rows()
    else:
        get_code_sql = '''
            select code from t_main 
            where 1=1
            and type not in('货币型-普通货币')
            and code >= ?
            and name like ?
            order by code
        '''
        funds = db.run(get_code_sql, (begin_code, name_like)).get_rows()
    
    if thread_num == 1:
        for fund in funds:
            code = fund[0]
            get_fund_dv_one(code, rep, page_size)
            num = db.run(sql, vals_all)
            log.info('get_fund_dv', code, num)
            vals_all.clear()
    else:
        tp = ThreadPool(thread_num)
        for fund in funds:
            if len(vals_all) >= 1000000:
                tp.wait()
                num = db.run(sql, vals_all)
                log.info('get_fund_dv', num)
                vals_all.clear()
            else:
                code = fund[0]
                tp.run(get_fund_dv_one, (code, rep, page_size))
        tp.wait()
        num = db.run(sql, vals_all)
        log.info('get_fund_dv', num)
        vals_all.clear()


def get_zf(db):
    sql = 'update t_date_value set zf = ? where code = ? and date = ?'
    zfs = []

    def get_zf_one(db, code):
        rss = db.run('select date,dwjz,fh from t_date_value where code = ? and zf is null order by date', (code,)).get_rows()
        for rs in rss:
            date_ = rs[0]
            dwjz = float(rs[1])
            fh = rs[2]
            try:
                previous_dwjz = float(db.run('select dwjz from t_date_value where code = ? and date < ? order by date desc limit 1', (code, date_)).get_rows()[0][0])
            except:
                previous_dwjz = dwjz 
            
            if '每份基金份额分拆' in str(fh):
                fh_cf = float(fh.replace('每份基金份额分拆', '').replace('份', ''))
                zf = ((dwjz * fh_cf) - previous_dwjz) / previous_dwjz * 100
            elif '每份派现金' in str(fh):
                fh_xj = float(fh.replace('每份派现金', '').replace('元', ''))
                zf = ((dwjz + fh_xj) - previous_dwjz) / previous_dwjz * 100
            else:
                zf = (dwjz - previous_dwjz) / previous_dwjz * 100
                
            zfs.append((zf, code, date_))
            
        log.info('get_zf', code, len(rss))

    tp = ThreadPool(64)
    funds = db.run("select DISTINCT code from t_date_value order by code").get_rows()
    for fund in funds:
        if len(zfs) >= 1000000:
            tp.wait()
            num = db.run(sql, zfs)
            log.info('get_zf', num)
            zfs.clear()
        else:
            tp.run(get_zf_one, (db, fund[0]))
    tp.wait()
    num = db.run(sql, zfs)
    log.info('get_zf', num)
    zfs.clear()

    
def get_val(db):
    sql = 'update t_date_value set val = ? where code = ? and date = ?'
    vals = []   

    def get_val_one(db, code):
        rss = db.run('select date,zf from t_date_value where code = ? and val is null order by date', (code,)).get_rows()
        next_val = 1 
        for rs in rss:
            try:
                date_ = rs[0]
                zf = rs[1]
                try:
                    next_val_db = None
                    next_val_db = db.run('select val from t_date_value where code = ? and date < ? order by date desc limit 1', (code, date_)).get_rows()[0][0]
                except:
                    next_val_db = None
                if next_val_db is not None:
                    next_val = next_val_db
                val = round(float(next_val) * (1 + float(zf) / 100), 3)
                vals.append((val, code, date_))
                next_val = val
            except Exception as _:
                print(_, code, date_, next_val, zf)
            
        log.info('get_val', code, len(rss))

    tp = ThreadPool(64)
    funds = db.run("select DISTINCT code from t_date_value where val is null order by code").get_rows()
    for fund in funds:
        if len(vals) >= 1000000:
            tp.wait()
            num = db.run(sql, vals)
            log.info('get_val', num)
            vals.clear()
        else:
            tp.run(get_val_one, (db, fund[0]))
    tp.wait()
    num = db.run(sql, vals)
    log.info('get_val', num)
    vals.clear()


def get_hc(db):
    codes = []
    rs_list = []        
    hc_sql = 'update t_date_value set hc = ?, hc1n = ?, hc3n = ? where code = ? and date = ?'

    def get_hc_one(db, code):
        rows = db.run('select date,val from t_date_value where hc is null and code = ?', (code,)).get_rows()
        for row in rows:
            date_now = row[0]
            date_1n_old = (datetime.datetime.strptime(date_now, '%Y-%m-%d') - relativedelta(years=1)).strftime('%Y-%m-%d')
            date_3n_old = (datetime.datetime.strptime(date_now, '%Y-%m-%d') - relativedelta(years=3)).strftime('%Y-%m-%d')
            val = row[1]
            max_val = db.run('select max(val) from t_date_value where date <= ? and code = ?', (date_now, code)).get_rows()[0][0]
            max_1n_val = db.run('select max(val) from t_date_value where date <= ? and date >= ? and code = ?', (date_now, date_1n_old, code)).get_rows()[0][0]
            max_3n_val = db.run('select max(val) from t_date_value where date <= ? and date >= ? and code = ?', (date_now, date_3n_old, code)).get_rows()[0][0]
            val = float(val)
            max_val = float(max_val)
            max_1n_val = float(max_1n_val)
            max_3n_val = float(max_3n_val)
            hc = round((max_val - val) / max_val * 100, 3)
            hc1n = round((max_1n_val - val) / max_1n_val * 100, 3)
            hc3n = round((max_3n_val - val) / max_3n_val * 100, 3)
            rs_list.append((hc, hc1n, hc3n, code, date_now))
        codes.append(code)
        log.info('get_hc', code, len(rows))
    
    tp = ThreadPool(64)
    funds = db.run("select DISTINCT code from t_date_value where hc is null order by code").get_rows()
    for fund in funds:
        if len(rs_list) >= 1000000:
            tp.wait()
            num = db.run(hc_sql, rs_list)
            log.info('get_hc', num)
            rs_list.clear()
            codes.clear()
        else:
            tp.run(get_hc_one, (db, fund[0]))
    tp.wait()
    num = db.run(hc_sql, rs_list)
    log.info('get_hc', num)
    rs_list.clear()
    codes.clear()


def get_nh(db):
            
    codes = []
    rs_list = []        
    nh_sql = 'update t_date_value set nh1n = ?, nh3n = ?, nh5n = ? where code = ? and date = ?'

    def get_nh_one(db, code):
        rows = db.run('select date,val from t_date_value where (nh5n is null or nh5n = -1) and code = ?', (code,)).get_rows()
        for row in rows:
            date_now = row[0]
            date_future_1 = (datetime.datetime.strptime(date_now, '%Y-%m-%d') + relativedelta(years=1)).strftime('%Y-%m-%d')
            date_future_3 = (datetime.datetime.strptime(date_now, '%Y-%m-%d') + relativedelta(years=3)).strftime('%Y-%m-%d')
            date_future_5 = (datetime.datetime.strptime(date_now, '%Y-%m-%d') + relativedelta(years=5)).strftime('%Y-%m-%d')
            val = row[1]
            val = float(val)
            try:
                val_future_1 = db.run('select val from t_date_value where date >= ? and code = ? order by date limit 1', (date_future_1, code)).get_rows()[0][0]
                val_future_1 = float(val_future_1)
                hn1n = round((val_future_1 - val) / val * 100, 3)
            except:
                hn1n = -1
            try:
                val_future_3 = db.run('select val from t_date_value where date >= ? and code = ? order by date limit 1', (date_future_3, code)).get_rows()[0][0]
                val_future_3 = float(val_future_3)
                hn3n = round((val_future_3 - val) / val * 100 / 3, 3)
            except:
                hn3n = -1
            try:
                val_future_5 = db.run('select val from t_date_value where date >= ? and code = ? order by date limit 1', (date_future_5, code)).get_rows()[0][0]
                val_future_5 = float(val_future_5)
                hn5n = round((val_future_5 - val) / val * 100 / 5, 3)
            except:
                hn5n = -1
            
            rs_list.append((hn1n, hn3n, hn5n, code, date_now))
        codes.append(code)
        log.info('get_nh', code, len(rows))
    
    tp = ThreadPool(16)
    funds = db.run("select DISTINCT code from t_date_value where nh5n is null order by code").get_rows()
    for fund in funds:
        if len(rs_list) >= 1000000:
            tp.wait()
            num = db.run(nh_sql, rs_list)
            log.info('get_nh', num)
            rs_list.clear()
            codes.clear()
        else:
            tp.run(get_nh_one, (db, fund[0]))
    tp.wait()
    num = db.run(nh_sql, rs_list)
    log.info('get_nh', num)
    rs_list.clear()
    codes.clear()

    
def get_xp(db):
            
    codes = []
    rs_list = []        
    xp_sql = 'update t_date_value set xp1n = ?, xp3n = ?, xp5n = ? where code = ? and date = ?'

    def get_xp_one(db, code):
        rows = db.run('select date from t_date_value where (xp5n is null or xp5n = -1) and code = ?', (code,)).get_rows()
        for row in rows:
            date_now = row[0]
            date_before_1 = (datetime.datetime.strptime(date_now, '%Y-%m-%d') + relativedelta(years=-1)).strftime('%Y-%m-%d')
            date_before_3 = (datetime.datetime.strptime(date_now, '%Y-%m-%d') + relativedelta(years=-3)).strftime('%Y-%m-%d')
            date_before_5 = (datetime.datetime.strptime(date_now, '%Y-%m-%d') + relativedelta(years=-5)).strftime('%Y-%m-%d')
            try:
                zfs_before_1 = db.run('select zf from t_date_value where date > ? and date <= ? and code = ? order by date', (date_before_1, date_now, code)).get_rows()
                zfs_before_1 = [c[0] for c in zfs_before_1]
                year_rate = sum(zfs_before_1)
                day_standard_deviation = np.std(zfs_before_1) * math.sqrt(365)
                if day_standard_deviation == 0:
                    xp1n = -1
                else:
                    xp1n = round(year_rate / day_standard_deviation, 3)
            except Exception as _:
                xp1n = -1
            try:
                zfs_before_3 = db.run('select zf from t_date_value where date > ? and date <= ? and code = ? order by date', (date_before_3, date_now, code)).get_rows()
                zfs_before_3 = [c[0] for c in zfs_before_3]
                year_rate = sum(zfs_before_3)
                day_standard_deviation = np.std(zfs_before_3) * math.sqrt(365 * 3)
                if day_standard_deviation == 0:
                    xp3n = -1
                else:
                    xp3n = round(year_rate / day_standard_deviation, 3)
            except Exception as _:
                xp3n = -1
            try:
                zfs_before_5 = db.run('select zf from t_date_value where date > ? and date <= ? and code = ? order by date', (date_before_5, date_now, code)).get_rows()
                zfs_before_5 = [c[0] for c in zfs_before_5]
                year_rate = sum(zfs_before_5)
                day_standard_deviation = np.std(zfs_before_5) * math.sqrt(365 * 5)
                if day_standard_deviation == 0:
                    xp5n = -1
                else:
                    xp5n = round(year_rate / day_standard_deviation, 3)
            except Exception as _:
                xp5n = -1
            
            rs_list.append((xp1n, xp3n, xp5n, code, date_now))
        codes.append(code)
        log.info('get_xp', code, len(rows))
    
    tp = ThreadPool(16)
    funds = db.run("select DISTINCT code from t_date_value where xp5n is null order by code").get_rows()
    for fund in funds:
        if len(rs_list) >= 1000000:
            tp.wait()
            num = db.run(xp_sql, rs_list)
            log.info('get_xp', num)
            rs_list.clear()
            codes.clear()
        else:
            tp.run(get_xp_one, (db, fund[0]))
    tp.wait()
    num = db.run(xp_sql, rs_list)
    log.info('get_xp', num)
    rs_list.clear()
    codes.clear()


def find_name(db, name):
    sql = '''
        select replace(date,'-','/'),nh3n from t_date_value t where code = 'NDX' order by date
    '''
    rss = db.run(sql).get_rows_2()
    for rs in rss:
        print(rs)

    
if __name__ == '__main__':
    main()

