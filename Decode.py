from PIL import Image
imgFile = input('Enter image file: ')
#tell user it is working
print("Loading...")
img = Image.open(imgFile)
imgSizeX = img.size[0]
imgSizeY = img.size[1]
pixels = img.load()
#initialize textLength - used to store secret text length
secretTextLength = ''
#initialize secretTextASCII - used to store ASCII code of secret text
secretTextASCII = ''

#RETRIEVE TEXT LENGTH FROM FIRST 11 PIXELS
for i in range(11):
    #retrieves rgb values at specified x-y pixel and stores into r,g,b variables
    r,g,b = img.getpixel((imgSizeX-i-1,imgSizeY-1))
    #change to binary values then to string values
    r = str(bin(r))
    g = str(bin(g))
    b = str(bin(b))
    #R Value
    r = r[-1] #get LSB and store into r
    #G Value
    g = g[-1] #get LSB and store into g
    #B Value
    b = b[-1] #get LSB and store into b

    #store new bits into variable text length
    #we have to insert bits in the right order
    secretTextLength = b+g+r + secretTextLength
secretTextLength = int(secretTextLength,2)


#RETRIEVE TEXT INSIDE RGB VALUES OF IMAGE PIXELS
#THIS LOOP JUST TO FINISH BOTTOM ROW
for i in range(imgSizeX-11):
    
    r,g,b = img.getpixel((imgSizeX-i-12,imgSizeY-1))
    #change to binary values then to string values
    r = str(bin(r))
    g = str(bin(g))
    b = str(bin(b))
    #R Value
    r = r[-1] #get LSB and store into r
    #G Value
    g = g[-1] #get LSB and store into g
    #B Value
    b = b[-1] #get LSB and store into b

    secretTextASCII = b+g+r + secretTextASCII


#FINISH RETRIEVING TEXT INSIDE RGB VALUES OF IMAGE PIXELS
for j in range(imgSizeY-1): #subtract 1 because we did the bottom row
    for i in range(imgSizeX):
        r,g,b = img.getpixel((imgSizeX-i-1,imgSizeY-j-2))
        #change to binary values then to string values
        r = str(bin(r))
        g = str(bin(g))
        b = str(bin(b))
        #R Value
        r = r[-1] #get LSB and store into r
        #G Value
        g = g[-1] #get LSB and store into g
        #B Value
        b = b[-1] #get LSB and store into b

        secretTextASCII = b+g+r + secretTextASCII

#use this to alter so we can secret text
shiftedSecretTextASCII = secretTextASCII
shiftedSecretTextASCII = int(shiftedSecretTextASCII,2)

#create a list to store the text retrieved
secretText = []
#starting from high and going low
#for example, if secretTextLength is 40, that means there are 5 letters
#we divide by 8 to see exactly how many letters there are
#then convert it to an integer
#then we reverse the range so it goes from 4 down to 0
for i in reversed(range(int(secretTextLength))):
    #if it's the last 8 bits we need, we dont have to do mod 256
    if(i==0):
        secretText.extend([chr(shiftedSecretTextASCII)])
    #mod 256 accesses the last 8 bits
    else:
        #add to the list the letters retrieved
        secretText.extend([chr(shiftedSecretTextASCII%256)])
        shiftedSecretTextASCII = shiftedSecretTextASCII >> 8
#get length of secret text
lenthOfSecretText = len(secretText)
#reverses secret text list
secretText = secretText[::-1]

#print all contents in the list
print('secretText: ')
for i in range(lenthOfSecretText):
    print(secretText[i],end="")
print(' ')

