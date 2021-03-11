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
    ObjectAndAccounts = [{"name":"Total Objects","value":399.0},{"name":"Failed Objects","value":137.0}]
    LicenseAndSales = [{'name': 'License Count X of 2200', 'value': 2161.0}, {'name': 'Percentage of License in Use', 'value': 0.9823}, {'name': 'Number of people whom have access to password vault ', 'value': 4060.0}, {'name': '# Sales', 'value': 3540}] 
    df_per = [{"name":"Domain Admin Total","value":35.0,"domain":"Domain Admin Percentage","percentages":1.0},{"name":"Domain Admin Vaulted","value":35.0,"domain":"Domain Admin Percentage","percentages":1.0},{"name":"Server Admin Total","value":1223.0,"domain":"Server Admin Percentage","percentages":0.35},{"name":"Server Admin Vaulted","value":428.0,"domain":"Server Admin Percentage","percentages":0.35},{"name":"Workstation Admin Total","value":386.0,"domain":"Workstation Percentage","percentages":0.2435},{"name":"Workstation Admin Vaulted","value":94.0,"domain":"Workstation Percentage","percentages":0.2435},{"name":"All Admin Total","value":1644.0,"domain":"All  Admin Percentage","percentages":0.3388},{"name":"All  Admin Vaulted","value":557.0,"domain":"All  Admin Percentage","percentages":0.3388}] 
    RequestTicketAverage = [{"name":"Accounts:","value":130315.0},{"name":"Sales:","value":3709.0}] 
    RequestTimeAverage = [{"name":"Average Time Open(Hrs) - Tasks","value":68.85},{"name":"Average Time Open(Hrs) -  Incidents","value":45.26},{"name":"Average OF ALL","value":66.04},{"name":"Average Time Open(Hrs) - ALL","value":66.04}] 
    passRetrivedAllvalues  = [{'name': 'Unique Users who pulled passwords in the last 7 Days ', 'value': 368.0}, {'name': 'Unique Accounts retrieved', 'value': 1912}, {'name': 'All Active user in the last 7 days ', 'value': 978.0}]
    passRetrivedTotal = [{"name":"Total # of pwds pulled in last 7 days","value":260884.0}]
    return ObjectAndAccounts,LicenseAndSales,df_per,\
           RequestTicketAverage,RequestTimeAverage,passRetrivedAllvalues,passRetrivedTotal