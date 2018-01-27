alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
'r','s','t','u','v','w','x','y','z']
alphabet2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
'R','S','T','U','V','W','X','Y','Z']

name1 = input("Input full name for person #1: ")
name2 = input("Input full name for person #2: ")
print("Caculating...")

sum1 = 0
sum2 = 0
itemnumb1 = 0
itemnumb2 = 0
for word in name1:
    if word in alphabet:
        itemnumb1 = alphabet.index(word)
        sum1 += itemnumb1
    elif word in alphabet2:
        itemnumb1 = alphabet2.index(word)
        sum1 += itemnumb1
    else:
        sum1 += 0

for word in name2:
    if word in alphabet:
        itemnumb2 = alphabet.index(word)
        sum2 += itemnumb2
    elif word in alphabet2:
        itemnumb2 = alphabet2.index(word)
        sum2 += itemnumb2
    else:
        sum2 += 0

result = (sum1 + sum2) % 101
result2 = ""

#★☆
if result < 20:
    result2 = "★☆☆☆☆"
elif result < 40:
    result2 = "★★☆☆☆"
elif result < 60:
    result2 = "★★★☆☆"
elif result < 80:
    result2 = "★★★★☆"
else:
    result2 = "★★★★★"

print ("%s percent" % (result))
print (result2)
