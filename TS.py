# -*- coding:utf-8 -*-
import tushare as ts
import datetime
# import tables

# ts.get_hist_data('600000') #一次性获取全部日k线数据
# ts.get_today_all()
dfcode = ts.get_stock_basics()
fdate = dfcode['timeToMarket']
for code in dfcode.index:
 d = fdate.loc[code]
 ds = str(d)
 if len(ds) > 7:
    stodate = ds[0:4]+'-'+ds[4:6]+'-'+ds[6:8]
    ttmarket = datetime.datetime.strptime(stodate, '%Y-%m-%d')
    nowday = datetime.datetime.strptime('2017-07-03', '%Y-%m-%d')
    delta = nowday - ttmarket
    df = ts.get_h_data(code, '2017-07-03', '2017-07-03')
    while delta.days >= 1000 :
        dend = ttmarket + datetime.timedelta(1000)
        sdend = dend.strftime('%Y-%m-%d')
        sdstart = ttmarket.strftime('%Y-%m-%d')
        dfget = ts.get_h_data(code,start=sdstart, end=sdend)
        df = df.append(dfget)
        ttmarket = dend + datetime.timedelta(1)
        delta = nowday - ttmarket
    dfget = ts.get_h_data(code,ttmarket.strftime('%Y-%m-%d'),nowday.strftime('%Y-%m-%d'))
    df = df.append(dfget)
    df = df.drop('2017-07-03')
    df = df.sort_index()
    df.to_pickle('c:/temp/{}.pkl'.format(code))
    # df.to_hdf('c:/temp/{}.h5'.format(code),'table',append=True)


