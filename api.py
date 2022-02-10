import requests

class Games:
    def __init__(self, game = "1872564715g45h5r2111hguk", platform = ""):
        self.game = game
        self.platform = platform

    def search(self): # Wear info is taken
        
        try:
            response = requests.get("https://www.pricecharting.com/api/products?t=c0b53bce27c1bdab90b1605249e600dc43dfd1d5&q=" + self.game + " " + self.platform) # api + key words
            response = response.json()
            response = (response["products"])
            return_object = str()

            if len(response) > 5: # set a maximum for results
                top = 5
            if len(response) < 5:
                top = len(response)

            for i in range(0, top):
                
                try:
                    return_object += "Name:                           " + (response[i])['product-name'] + "\n"
                    return_object += "Console/Platform:     " + (response[i])['console-name']
                    return_object += "\n\n"
          
                except:
                    return_object = return_object
                    print("er")

            return(return_object)
        
        except:
            try:
                response = requests.get("https://www.pricecharting.com/api/products?t=c0b53bce27c1bdab90b1605249e600dc43dfd1d5&q=pokemonX 3ds")
                return("Could not locate the game!")
            except:
                return("Could not conect to API!")

testing = False

if testing == True:
    wow = Games("pokemon") # Note to user: works bether with one word. (It takes the last word as the console/platform)
    print(wow.search())