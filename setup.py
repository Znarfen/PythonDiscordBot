
f = open("settings.txt", "r")
text = (f.read()).split('\n')

line1 = text[0].split(' ')
token = line1[1]
# Get the token from settings.txt

line2 = text[1].split(' ')
prefix = line2[1]
# Get the prefix from settings.txt

try:
    line3 = text[2].split(' ')
    # Gets number_of_responses from settings.txt
    responses = int(line3[1])
    # See if number_of_responses is an int

except:
    responses = 1
    # If not responses = 1