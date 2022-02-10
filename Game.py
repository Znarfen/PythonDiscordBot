import requests

response = requests.get("https://www.pricecharting.com/api/products?t=c0b53bce27c1bdab90b1605249e600dc43dfd1d5&q=Super Mario nds")
response = response.json()
game = response['product-name']
platform = response['console-name']

print(game, platform)