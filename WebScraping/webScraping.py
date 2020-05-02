import re
import requests


def get_number_of_infected_people():
    page = requests.get('https://www.worldometers.info/coronavirus/country/us/')
    pattern = r'United States Coronavirus: (\d{0,3}, {0,1}\d{1,}) Cases and (\d{0,3}, {0,1}\d{1,})'
    obj = re.search(pattern, page.text)
    results = [obj.group(1), obj.group(2)]
    return results


with open('currentStatus.txt', 'r') as f:
    saved_data = f.readline()

current_data = get_number_of_infected_people()

if saved_data != str(current_data):
    with open('currentStatus.txt', 'w') as f:
        f.write(str(current_data))
    print(f'{current_data[0]} infected people and {current_data[1]} deaths')
else:
    print('nothing changed')



