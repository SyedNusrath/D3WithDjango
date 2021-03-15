from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import numpy as np
import ast

def loadCharts(request):
    ObjectAndAccounts,ObjectAndAccounts2,ObjectAndAccounts3,file2,RequestTicketAverage ,RequestTimeAverage = getDatafromFiles()
    return render(request, 'barcharts.html',{'ObjectAndAccounts':ObjectAndAccounts, 'ObjectAndAccounts2':ObjectAndAccounts2, 
        'ObjectAndAccounts3':ObjectAndAccounts3, 
        'WindowsAndDomainAdmin':file2, 
        'RequestTimeAverage':RequestTimeAverage,'RequestTicketAverage':RequestTicketAverage, 
        })

def getDatafromFiles():
    ObjectAndAccounts = [{"name":"Total","value":557,"domain":"Domain Admin Percentage","percentages":1.0},{"name":"Vaulted","value":357.0,"domain":"Domain Admin Percentage","percentages":0.34}]
    ObjectAndAccounts2 = [{"name":"Total","value":386,"domain":"Domain Admin Percentage","percentages":1.0},{"name":"Vaulted","value":94.0,"domain":"Domain Admin Percentage","percentages":0.24}]
    ObjectAndAccounts3 = [{"name":"Total","value":557,"domain":"Domain Admin Percentage","percentages":1.0},{"name":"Vaulted","value":357.0,"domain":"Domain Admin Percentage","percentages":0.34}]
    df_per = [{"name":"Server Admin(Domain) Total","value":557,"domain":"Domain Admin Percentage","percentages":1.0},{"name":"Server Admin(Domain) Vaulted","value":428.0,"domain":"Domain Admin Percentage","percentages":0.35},{"name":"Server Admin (Local) Total","value":557.0,"domain":"Server Admin Percentage","percentages":1.0},{"name":"Server Admin (Local) Vaulted","value":428.0,"domain":"Server Admin Percentage","percentages":0.35},{"name":"WorkstationAdmin (Domain) Total","value":386.0,"domain":"Workstation Percentage","percentages":1.0},{"name":"WorkstationAdmin (Domain) Vaulted","value":94.0,"domain":"Workstation Percentage","percentages":0.2435},{"name":"WorkstationAdmin (Local) Total","value":386.0,"domain":"All  Admin Percentage","percentages":0.3388},{"name":"WorkstationAdmin (Local) Vaulted","value":94.0,"domain":"All  Admin Percentage","percentages":0.24}] 
    RequestTicketAverage = [{"name":"Domain Admin Total","value":35,"domain":"Domain Admin Percentage","percentages":1.0},{"name":"Domain Admin Vaulted","value":35.0,"domain":"Domain Admin Percentage","percentages":1.0}] 
    RequestTimeAverage = [{"name":"Server Admin(Domain) Total","value":557,"domain":"Domain Admin Percentage","percentages":1.0},{"name":"Server Admin(Domain) Vaulted","value":428.0,"domain":"Domain Admin Percentage","percentages":0.35},{"name":"Server Admin (Local) Total","value":557.0,"domain":"Server Admin Percentage","percentages":1.0},{"name":"Server Admin (Local) Vaulted","value":428.0,"domain":"Server Admin Percentage","percentages":0.35}] 
    return ObjectAndAccounts,ObjectAndAccounts2,ObjectAndAccounts3,df_per,\
           RequestTicketAverage,RequestTimeAverage