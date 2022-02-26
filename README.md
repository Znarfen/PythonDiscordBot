# **Read me**

## Teknologier

Detta pogram är helt gort i python. Förutom en textfil som används för att ändra instälningar på boten. Pogramet använder sig av bibloteket discord.py och requests.

## Hur det fungerar

Man kan skriva [prefix]help (om du inte ändrat prefixet är pefixet: >>) för att få en lista av de komandon som boten kan köra. (Vilket för tilfälet ändast är två komandon, help och search)

När man startar discord.py är pogramet i en funktion, on_message som har letar efter medelanden som någon nys har skrivit. Och om man skriver [prefix]search i din discordserver som boten är i kommer discord.py ta information ifrån api.py. I api.py hämtar den information från apin: https://www.pricecharting.com/api/products?t=c0b53bce27c1bdab90b1605249e600dc43dfd1d5&q=. Som hätas via klassen Game, i funktionen search. Efter det soterar den infromationen returnerar den en sträng med informationen till bot.py. I bot.py skriver den sedan ut infromationen in i discordserven.

## Installation

För att pogramet ska kunna köras måste man ha discord.py. Öppna CMD och skriv in: "pip install discord.py" för att instalera discord.py. Man måste även ha requests instalerat så att api:n ska fungera. Öppna CMD och skriv in: "pip install requests" för att instalera requests. 

Om man vill att pogramet ska kunna köras måste du ha en token till din discord bot. Du lägger nycken i settings.txt. Notera att det måste vara ett melanslag mellan token: och din nyckel.

I settings.txt kan du också ändra på prefixet som boten svarar på och number_of_responses som är hur många svar den skriver ut.

När du känner dig klar kan du starta bot.py vilket startar boten. Boten måste vara i din discord server för att kunna fungera.

## Att göra

Jag skulle vilja göra så att boten klarar av att spela hänga gubbe. Jag skulle även vilja komma på mer saker att göra med boten.

## Att bidra

Tyvär är detta ett skolarbet villket inebär att det inte tillåts några pull requests.
