import requests
import json
import pprint
try:
    result = requests.get('https://www.idx.co.id/umbraco/Surface/Helper/GetStockChart?indexCode=SRTG&period=1W')
    if result.status_code == 200:
        data = json.loads(result.text)
        pprint.pprint(data)
        print(data['ChartData'])
        #print(result.status_code)
        #print(result.text)
        chart_data = data['ChartData']

        f = open('data.csv', 'w')
        f.write('#Tanggal' Value\n')')
        for d in chart_data:
            tanggal = d['Date']
            value = d['Close']
            print(tanggal, ';', value)
            f.write('{};{}\n'.format(tanggal, value))
            f.close()
except Exception as ex:
    print(ex)