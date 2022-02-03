class Game:

    def __init__(self, name, console):

        self.name = name
        self.console = console
        


    def Search(self):

        from urllib import response
        from aiohttp import request
        import requests

        response = requests.get("https://www.pricecharting.com/api/products?t=c0b53bce27c1bdab90b1605249e600dc43dfd1d5&q=Super Mario nds")
        response = response.json()

        print(response)

G = Game("Super mario", "nds")
G.Search

