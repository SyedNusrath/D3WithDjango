from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import numpy as np
import ast

def loadCharts(request):
    ObjectAndAccounts,LicenseAndSales,file2,RequestTicketAverage ,RequestTimeAverage,passRetrivedAllvalues,passRetrivedTotal= getDatafromFiles()
    return render(request, 'barcharts.html',{'ObjectAndAccounts':ObjectAndAccounts,'LicenseAndSales':LicenseAndSales,'WindowsAndDomainAdmin':file2,
                                             'RequestTimeAverage':RequestTimeAverage,'RequestTicketAverage':RequestTicketAverage,
                                             'passRetrivedAllvalues': passRetrivedAllvalues,'passRetrivedTotal': passRetrivedTotal})

def getDatafromFiles():
    file1 = pd.read_excel(r'static/file1.xlsx')

    # chart 1
    ObjectAndAccounts = file1.iloc[:2,:2].to_json(orient='records')
    # chart 2
    ls = ast.literal_eval(file1.iloc[7:10,:2].to_json(orient='records'))
    ls.append({'name': '# Sales', 'value': 3540})
    LicenseAndSales = str(ls)

    file2 = pd.read_excel(r'static/files2.xlsx')
    # chart 3
    file2.index = pd.RangeIndex(start=1, stop=len(file2.index) +1, step=1)
    df_new = file2[file2.index % 3 != 0]
    newdf = file2[file2.index % 3 == 0].reset_index(drop=True)
    newdf = pd.DataFrame(np.repeat(newdf.values,2,axis=0))
    df_per = pd.concat([df_new.reset_index(drop=True),newdf.reset_index(drop=True)],axis=1,ignore_index=False)
    df_per.columns=['name','value','domain','percentages']

    # chart 4
    passRetrived = ast.literal_eval(file1.iloc[6:7,:2].to_json(orient='records'))
    passRetrived.append({'name': 'Unique Accounts retrieved', 'value': 1912})
    passRetrived.append(ast.literal_eval(file1.iloc[2:3,3:].rename(columns={"Unnamed: 3": "name", "Unnamed: 4": "value"}).to_json(orient='records'))[0])
    passRetrivedAllvalues = str(passRetrived)
    
    # chart 5
    passRetrivedTotal = file1.iloc[3:4,3:].rename(columns={"Unnamed: 3": "name", "Unnamed: 4": "value"}).to_json(orient='records')

    RequestTicketAverage = pd.read_excel(r'static/RequestTicketAverage.xlsx')
    RequestTimeAverage = pd.read_excel(r'static/RequestTimeAverage.xlsx')
    # passRetrived = pd.read_excel(r'static/passRetrived.xlsx')
    # passRetrivedAllvalues = passRetrived.iloc[:-1].to_json(orient='records')
    # passRetrivedTotal = passRetrived.iloc[-1].to_json()
    return ObjectAndAccounts,LicenseAndSales,df_per.to_json(orient='records'),\
           RequestTicketAverage.to_json(orient='records'),RequestTimeAverage.to_json(orient='records'),passRetrivedAllvalues,passRetrivedTotal