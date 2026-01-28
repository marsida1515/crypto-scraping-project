import requests
from bs4 import BeautifulSoup
url = "https://www.coindesk.com/"
response = requests.get(url)
print(f"Statusi i kërkesës: {response.status_code}")

url = "https://www.coindesk.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

titujt = soup.find_all('h3')

print("Lajmet e fundit mbi Kripto:")
for i, titull in enumerate(titujt[:5], 1): 
    print(f"{i}. {titull.get_text().strip()}")

api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
api_response = requests.get(api_url)
data = api_response.json() 

cmimi_btc = data['bitcoin']['usd']
print(f"\nÇmimi aktual i Bitcoin: ${cmimi_btc}")

import csv
filename = "lajmet_kripto.csv"
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Nr", "Titulli", "Cmimi BTC"]) 
    
    for i, titull in enumerate(titujt[:5], 1):
        writer.writerow([i, titull.get_text().strip(), cmimi_btc])

print(f"Të dhënat u ruajtën me sukses në skedarin: {filename}")