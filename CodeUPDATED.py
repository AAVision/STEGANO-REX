#!/usr/bin/env python
# coding:UTF-8


import cv2
#docopt is like argparse
import docopt
import numpy as np
import hashlib 
import os
from PIL import Image
import random
import string


class SteganographyException(Exception):
    pass

def decodee(levell,in_f,out_f):
    level = levell
    in_img = cv2.imread(in_f)
    try:
        steg = Code(in_img,int(level))
        try:
            raw = steg.decode_binary()
        except :
            return "Error!"
        with open(out_f, "wb") as f:
            f.write(raw)
            return "Done"
    except :
        return "Error!"
    
        
        

def encod(in_f,file,levell,out):
    lossy_formats = ["jpeg", "jpg","png"]
        #Handling lossy format
    in_img = cv2.imread(in_f)
    out, out_ext = out.split(".")
    if out_ext in lossy_formats:
        out = out + ".png"
        print("Output file changed to ", out)

    image = Image.open(file)
    image = image.convert('RGB')
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(15)))
    image.save(str(result_str)+'.webp', 'webp')
    data = open(str(result_str)+'.webp', "rb").read()
        #\x1c\n\xec\xa5U\xce\t\x98N\x1c\xac\xff\xd9'
    level = levell
    steg = Code(in_img,int(level))
    res = steg.encode_binary(data)
    cv2.imwrite(out, res)
    if os.path.exists(str(result_str)+".webp"):
        os.remove(str(result_str)+".webp")
        print("DELETED")
    else:
        print("The file does not exist")


def encodee_text(in_f,file,levell,out):
    formats = ["pdf", "docx"]
        #Handling lossy format
    in_img = cv2.imread(in_f)
    out, out_ext = out.split(".")
    if out_ext in formats:
        out = out + ".pdf"
        print("Output file changed to ", out)

    level = levell
    steg = Code(in_img,int(level))
    res = steg.encode_text(data)
    cv2.imwrite(out, res)



def decodee_text(levell,in_f,out_f):
    level = levell
    in_img = cv2.imread(in_f)
    try:
        steg = Code(in_img,int(level))
        try:
            raw = steg.decode_text()
        except :
            return "Error!"
        print(str(raw))
    except :
        return "Error!"


class Code():
    def __init__(self, im,level):
        self.image = im
        #get height and width from the shape of image
        self.height, self.width, self.nbchannels = im.shape
        #size = width * height
        self.size = self.width * self.height
        
        
        if level==1:
            self.maskONEValues = [1,2]
            self.maskONE = self.maskONEValues.pop(0)
            self.maskZEROValues = [254,253]
            self.maskZERO = self.maskZEROValues.pop(0)
        
        elif level==2:
            self.maskONEValues = [1,2,4,8]
            self.maskONE = self.maskONEValues.pop(0)
            self.maskZEROValues = [254,253,251,247]
            self.maskZERO = self.maskZEROValues.pop(0)
        
        elif level==3:
            self.maskONEValues = [1,2,4,8,16,32]
            self.maskONE = self.maskONEValues.pop(0)
            self.maskZEROValues = [254,253,251,247,239,223]
            self.maskZERO = self.maskZEROValues.pop(0)
            
       
        
        
        elif level ==4:
            self.maskONEValues = [1,2,4,8,16,32,64,128]
       
            self.maskONE = self.maskONEValues.pop(0) #Will be used to do bitwise operations
        
            self.maskZEROValues = [254,253,251,247,239,223,191,127]
       
            self.maskZERO = self.maskZEROValues.pop(0)
        
        self.curwidth = 0  # Current width position
        self.curheight = 0 # Current height position
        self.curchan = 0   # Current channel position
        self.count = 0
        self.counterrr=0
        #channels are 3 RGB
       
    def put_binary_value(self, bits): #Put the bits of the image
      
        for c in bits: #Iterate over all bits chml lal yamen
            val = list(self.image[self.curheight,self.curwidth]) #Get the pixel value as a list (val is now a 3D array)
            #Get the pixel value as a list
            #if the bit to be encoded is '0'
           


            if int(c) == 1: #if bit is set, mark it in image
            	
                val[self.curchan] = int(val[self.curchan]) | self.maskONE
                #print(val[self.curchan])#OR with maskONE
            else:
             
                val[self.curchan] = int(val[self.curchan]) & self.maskZERO
               
            
            #Update image
            self.image[self.curheight,self.curwidth] = tuple(val)
           

            self.next_slot() #Move "cursor" to the next space
        
    def next_slot(self):#Move to the next slot were information can be taken or put
        if self.curchan == self.nbchannels-1: #Next Space is the following channel
            self.curchan = 0
            if self.curwidth == self.width-1: #Or the first channel of the next pixel of the same line
                self.curwidth = 0
                if self.curheight == self.height-1:#Or the first channel of the first pixel of the next line
                    self.curheight = 0
                    if self.maskONE == int(max(self.maskONEValues)): #final mask, indicating all bits used up
                        raise SteganographyException("No available slot remaining (image filled)")
                    else: #Or instead of using the first bit start using the second and so on..
                        self.maskONE = self.maskONEValues.pop(0)
                        self.maskZERO = self.maskZEROValues.pop(0)
                else:
                    self.curheight +=1
            else:
                self.curwidth +=1
        else:
            self.curchan +=1

       
    def read_bit(self): #Read a single bit int the image
        val = self.image[self.curheight,self.curwidth][self.curchan]
        val = int(val) & self.maskONE
        self.next_slot()
        #Check if corresp bitmask and val have same set bit
        if val > 0:
            return "1"
        else:
            return "0"
    
    def read_byte(self):
        return self.read_bits(8)
    
    def read_bits(self, nb): #Read the given number of bits
        bits = ""
        for i in range(nb):
            bits += self.read_bit()
        #65300
        return bits

    def byteValue(self, val):
        return self.binary_value(val, 8)
        
    def binary_value(self, val, bitsize): #Return the binary value of an int as a byte
        binval = bin(val)[2:]
        if len(binval) > bitsize:
            raise SteganographyException("binary value larger than the expected size")
        while len(binval) < bitsize:
            binval = "0"+binval
        #print(binval)
        return binval

    def encode_text(self, txt):
        l = len(txt)
        #print(l)
        binl = self.binary_value(l, 16) #Length coded on 2 bytes so the text size can be up to 65536 bytes long
      
        self.put_binary_value(binl) #Put text length coded on 4 bytes
        for char in txt: #And put all the chars
            c = ord(char)
           
            self.put_binary_value(self.byteValue(c))
        return self.image
       
    def decode_text(self):
        ls = self.read_bits(16) #Read the text size in bytes
        l = int(ls,2)
        i = 0
        unhideTxt = ""
        while i < l: #Read all bytes of the text
            tmp = self.read_byte() #So one byte
            i += 1
            unhideTxt += chr(int(tmp,2)) #Every chars concatenated to str
        return unhideTxt

    def encode_image(self, imtohide):
        w = imtohide.width
        h = imtohide.height
        if self.width*self.height*self.nbchannels < w*h*imtohide.channels:
            raise SteganographyException("Carrier image not big enough to hold all the datas to steganography")
        binw = self.binary_value(w, 16) #Width coded on to byte so width up to 65536
        binh = self.binary_value(h, 16)
        self.put_binary_value(binw) #Put width
        self.put_binary_value(binh) #Put height
        for h in range(imtohide.height): #Iterate the hole image to put every pixel values
            for w in range(imtohide.width):
                for chan in range(imtohide.channels):
                    val = imtohide[h,w][chan]
                    self.put_binary_value(self.byteValue(int(val)))
        return self.image

                    
    def decode_image(self):
        width = int(self.read_bits(16),2) #Read 16bits and convert it in int
        height = int(self.read_bits(16),2)
        unhideimg = np.zeros((width,height, 3), np.uint8) #Create an image in which we will put all the pixels read
        for h in range(height):
            for w in range(width):
                for chan in range(unhideimg.channels):
                    val = list(unhideimg[h,w])
                    print("val:",val)
                    val[chan] = int(self.read_byte(),2) #Read the value
                    print("val[chan]:",val)
                    unhideimg[h,w] = tuple(val)
                    print("unhideimg[h,w]:",val)
        return unhideimg
    
    def encode_binary(self, data):
    
        l = len(data)
     
        
        if self.width*self.height*self.nbchannels < l+64:
            raise SteganographyException("Carrier image not big enough to hold all the datas to steganography")
        self.put_binary_value(self.binary_value(l, 64)) #put bin(52598,64)
        for byte in data:
        
            byte = byte if isinstance(byte, int) else ord(byte) # Compat py2/py3
            self.put_binary_value(self.byteValue(byte))
        return self.image

    def decode_binary(self):
        l = int(self.read_bits(64), 2)
        print(l)
        output = b""
        for i in range(l):
            output += bytearray([int(self.read_byte(),2)])
        return output

if __name__=="__main__":
    main()

