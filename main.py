import requests

nofluffjobs_request = requests.get('https://nofluffjobs.com/pl/praca-zdalna/Python?criteria=city%3Dwarszawa%20%20seniority%3Dtrainee,junior&page=1')

print(nofluffjobs_request)