import requests
from pprint import pprint

def SearchProject(keyword_search='เรือดำน้ำ'):

    url = 'https://opend.data.go.th/govspending/cgdcontract'

    token = 'SevD3VkzYrewkOOaS46jRFdeaMlSc0L7'

    parameters = {'api-key':token,
                  'year':2562,
                  'keyword':keyword_search,
                  'limit':50}

    r = requests.get(url,params=parameters)
    result = r.json()

    allproject = result['result']
    

    #print(type(allproject))
    print('Count: ' ,len(allproject))   #len() คือการนับค่าใน List / Dict
    #pprint(allproject[8])

    allbudget = []

    for pj in (allproject):
        print(pj['dept_name'])
        print(pj['sum_price_agree'])
        print(pj['project_name'])
        print(pj['transaction_date'])
        allbudget.append(int(pj['sum_price_agree'].replace(',','')))
        print('-----------')

    print('*******************************************')
    print('ค้นหาคำว่า: {} งบประมาณทั้งหมด: {:,d} บาท'.format((keyword_search),sum(allbudget)))
    print('*******************************************')

    
SearchProject('เรือดำน้ำ')

        

