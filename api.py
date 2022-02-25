import requests
import setup

class Games:
    def __init__(self, game = "1872564715g45h5r2111hguk", platform = ""):
        self.game = game
        self.platform = platform

    def search(self): # Wear info is taken
        
        try:
            api = "https://www.pricecharting.com/api/products?t=c0b53bce27c1bdab90b1605249e600dc43dfd1d5&q="
            response = requests.get(api + self.game + " " + self.platform)
            # api + key words

            response = response.json()
            response = (response["products"])
            return_object = str()

            num = setup.responses

            if len(response) > num: # set a maximum for results
                top = num
            if len(response) < num: # if the number of responses < the maximum
                top = len(response)

            for i in range(0, top): # list all results in a str object
                
                try:
                    Name = "Name:                           "
                    Console = "Console/Platform:     "

                    return_object += Name + response[i]['product-name'] + "\n"
                    return_object += Console + response[i]['console-name']
                    return_object += "\n\n"
          
                except:
                    return_object = return_object
                    print("er")

            return(return_object)
        
        except:
            # test if its wrong with the api or conection
            try:
                api = "https://www.pricecharting.com/api/products?t=c0b53bce27c1bdab90b1605249e600dc43dfd1d5&q=pokemonX 3ds"
                response = requests.get(api)
                return("Could not locate the game!")
            except:
                return("Could not conect to API!")

testing = False

if testing == True:
    wow = Games("pokemonX") 
    # Note to user: works bether with one word.
    # (It takes the last word as the console/platform)

    print(wow.search())