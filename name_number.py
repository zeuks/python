alphabet = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
'r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
'R','S','T','U','V','W','X','Y','Z']

number_list = []
alpha_list = []
loop = 0
code = 0

while True:
    name = input("What is the name?(type 'stop' to continue): ")
    if name == "stop":
        break
    else:
        for x in name:
            number_list.append(alphabet.index(x))
        print ("Your secret code: '%s'" % (str(number_list).strip('[]')))
        number_list = []

print ("Type '111' when you want to stop." )

while True:
    loop += 1
    code = int(input("Input the secret number for letter number %s: " % (loop)))
    if code == 111:
        break
    else:
        alpha_list.append(alphabet[code])

print ("Your name: %s" % (''.join(alpha_list)))
