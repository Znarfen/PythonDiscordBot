
f = open("setup.txt", "r")
text = (f.read()).split('\n')

line1 = text[0].split(' ')
token = line1[1]

line2 = text[1].split(' ')
prefix = line2[1]

try:
    line3 = text[2].split(' ')
    responses = int(line3[1])

except:
    responses = 1

