import numpy as np
import pandas as pd
from datetime import date

SERVICE_ITEMS = []
PRICES = []
DATES = []
EXPENSE_TYPES = []

def add_expense(service_item, price, date, expense_type):
    SERVICE_ITEMS.append(service_item)
    PRICES.append(price)
    DATES.append(date)
    EXPENSE_TYPES.append(expense_type)

option = -1
while(option != 0):
    print('식비 계산기 작동 :')
    print('1. 식비 입력')
    print('2. 지출 보고서 보기')
    print('0. 나가기')
    option = int(input('옵션을 고르세요 : '))
    print()
    
    if option == 0:
        print('qq')
        break
    elif option == 1:
        expense_type = '(식비)'
    elif option == 2:
        expense_report = pd.DataFrame()
        expense_report['지출 내역'] = SERVICE_ITEMS
        expense_report['비용'] = PRICES
        expense_report['날짜'] = DATES
        expense_report['지출 항목'] = EXPENSE_TYPES
        expense_sum = expense_report['비용'].sum()
        temp_df = pd.DataFrame([['-', '총합: '+str(expense_sum), '-', '-']], columns=['지출 내역', '비용', '날짜', '지출 항목'])
        expense_report = pd.concat([expense_report, temp_df])
        expense_report.to_csv('expenses.csv')
        print(expense_report)
    else:
        print('wrong input')   
        
    if option == 1:
        service_item = input('지출 항목을 넣으세요 '+expense_type+':\n')
        price = float(input('지출 비용을 넣으세요 :\n'))
        today = date.today()
        add_expense(service_item, price, today, expense_type)
        print()     