import requests

api = 'https://findvulnsapichux.herokuapp.com/api'

brand = input('[+] Enter brand name: ')
vers = input("[+] Enter brand's version: ")

payload = { 'product': brand, 'version': vers }

def request_api(brand, vers):
    response = requests.post(api, data=payload)
    parsed = response.json()
    return parsed

dict_results = request_api(brand, vers)
results = dict_results['Results']
for result in results:
    print('\n')
    print(result)