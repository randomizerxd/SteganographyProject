Randy Baldwin

This is Steganography. We are able to encode an image with some secret text and then we are able to decode the image and retrieve the hidden secret text. Python 3 and the PILLOW library were used to make this happen. Encode.py and Decode.py are included. I was able to get the basic functionality of both the encoding and decoding, but I am missing one thing. I am not able to loop until the secret text length is 0. The encode and decode will loop through the entire picture. I know this isn't optimal, but I couldn't figure out how to do this. The output.png image has been embedded with the source code of both Encode.py and Decode.py. I wasn’t sure how exactly you wanted this done. I couldn’t find a convenient way to embed it with all of the formatting, so I ended up taking the indents and spaces away.. Yeah probably not right. I know. 

INSTRUCTIONS:
Run Encode.py with python3. It will ask you for an image name. Go ahead and type the image file name and then you will be prompted to type out your secret text. Type your secret text and then it will run. Since it's looping through the whole picture, it might take a while if it's a picture that has more pixels. Then when you want to decode, run Decode.py. It will ask for the image file name. Type it in. Then it will output the secret text retrieved. Encode takes in jpg or png and outputs a png file.

