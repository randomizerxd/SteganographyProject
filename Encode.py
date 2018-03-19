#here's how you do the project
#if my picture is 100x100 pixels and I am using the
#first 11 pixels (starting from bottom right) to specify
#my secret text length
#Let's say my secret text is "abc", the string-to-binary converter
#will convert the string to the ascii characters. These are 8 bit representations
#of the characters in the alphabet. So when we go searching for the ascii characters in the image,
#we will need to collect 8 bits and then convert that to a letter. My secret text length is 3. 0b11
from PIL import Image
imgFile = input('Enter image file: ')
img = Image.open(imgFile)
imgSizeX = img.size[0]
imgSizeY = img.size[1]
#access the pixels and define them with rgb values
pixels = img.load()

#asks user for secret text
secretText = input("Please enter the secret text: ")


#converts text to binary string - ASCII code
secretTextASCII = ''.join('{:08b}'.format(ord(c)) for c in secretText)
#convert binary string to binary number
secretTextASCII = int(secretTextASCII,2)
#temp variable used for the shifting
shiftedSecretTextASCII = secretTextASCII

#gets secret text length
secretTextLength = len(secretText)
#to get bit length, multiply by 8
secretTextLength = secretTextLength * 8
#temp variable used for the shifting
shiftedSecretTextLength = secretTextLength

#STORE TEXT LENGTH IN FIRST 11 PIXELS
for i in range(11):
    r,g,b = img.getpixel((imgSizeX-i-1, imgSizeY-1)) #x changes but y stays
    
    #R VALUE
    if(r%2 == 0):
        if (shiftedSecretTextLength%2 == 1):
            r = r + 1
    if(r%2 == 1):
        if(shiftedSecretTextLength%2 == 0):
            r = r - 1
    shiftedSecretTextLength = shiftedSecretTextLength >> 1 #logical shift right. brings in a 0
    
    #G VALUE
    if(g%2 == 0):
        if (shiftedSecretTextLength%2 == 1):
            g = g + 1
    if(g%2 == 1):
        if(shiftedSecretTextLength%2 == 0):
            g = g - 1
    shiftedSecretTextLength = shiftedSecretTextLength >> 1 #logical shift right. brings in a 0
    
    #B VALUE
    if(b%2 == 0):
        if (shiftedSecretTextLength%2 == 1):
            b = b + 1
    if(b%2 == 1):
        if(shiftedSecretTextLength%2 == 0):
            b = b - 1
    shiftedSecretTextLength = shiftedSecretTextLength >> 1 #logical shift right. brings in a 0

    #write the possibly new rgb values back to the pixel
    pixels[imgSizeX-i-1, imgSizeY-1] = (r,g,b)

#STORE TEXT INSIDE RGB VALUES OF IMAGE PIXELS
#THIS LOOP JUST TO FINISH BOTTOM ROW
for i in range(imgSizeX-11): #offset by 11 to go from next pixel to pixel 0 the specific pixel
    r,g,b = img.getpixel((imgSizeX-i-12, imgSizeY-1))
    
    #R VALUE
    if(r%2 == 0):
        if (shiftedSecretTextASCII%2 == 1):
            r = r + 1
    if(r%2 == 1):
        if(shiftedSecretTextASCII%2 == 0):
            r = r - 1
    shiftedSecretTextASCII = shiftedSecretTextASCII >> 1 #logical shift right. brings in a 0
    
    #G VALUE
    if(g%2 == 0):
        if (shiftedSecretTextASCII%2 == 1):
            g = g + 1
    if(g%2 == 1):
        if(shiftedSecretTextASCII%2 == 0):
            g = g - 1
    shiftedSecretTextASCII = shiftedSecretTextASCII >> 1 #logical shift right. brings in a 0
    
    #B VALUE
    if(b%2 == 0):
        if (shiftedSecretTextASCII%2 == 1):
            b = b + 1
    if(b%2 == 1):
        if(shiftedSecretTextASCII%2 == 0):
            b = b - 1
    shiftedSecretTextASCII = shiftedSecretTextASCII >> 1 #logical shift right. brings in a 0

    #write the possibly new rgb values back to the pixel
    pixels[imgSizeX-i-12, imgSizeY-1] = (r,g,b)

#FINISH STORING TEXT INSIDE RGB VALUES OF IMAGE PIXELS
for j in range(imgSizeY-1): #subtract 1 because we did the bottom row
    for i in range(imgSizeX):
        r,g,b = img.getpixel((imgSizeX-i-1,imgSizeY-j-2))#subtract 2 from y because we are starting at row 98
        
        #R VALUE
        if(r%2 == 0):
            if (shiftedSecretTextASCII%2 == 1):
                r = r + 1
        if(r%2 == 1):
            if(shiftedSecretTextASCII%2 == 0):
                r = r - 1
        shiftedSecretTextASCII = shiftedSecretTextASCII >> 1 #logical shift right. brings in a 0
    
        #G VALUE
        if(g%2 == 0):
            if (shiftedSecretTextASCII%2 == 1):
                g = g + 1
        if(g%2 == 1):
            if(shiftedSecretTextASCII%2 == 0):
                g = g - 1
        shiftedSecretTextASCII = shiftedSecretTextASCII >> 1 #logical shift right. brings in a 0
    
        #B VALUE
        if(b%2 == 0):
            if (shiftedSecretTextASCII%2 == 1):
                b = b + 1
        if(b%2 == 1):
            if(shiftedSecretTextASCII%2 == 0):
                b = b - 1
        shiftedSecretTextASCII = shiftedSecretTextASCII >> 1 #logical shift right. brings in a 0

        #write the possibly new rgb values back to the pixel
        pixels[imgSizeX-i-1, imgSizeY-j-2] = (r,g,b)


img.save("output.png")






