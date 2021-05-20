#!/usr/bin/env python
# coding:UTF-8
"""Code.py
only for lossy files jpg and png and jpeg




Usage:
  Code.py encode -i <input> -o <output> -f <file> -l <level>
  Code.py decode -i <input> -o <output> -l <level>
  Code.py mes -i <input> -o <output> -f <file> 
  Code.py dmes -i <input> 

Options:
  -h, --help                Show this help
  --version                 Show the version
  -f,--file=<file>          File to hide
  -i,--in=<input>           Input image (carrier)
  -o,--out=<output>         Output image (or extracted file)
  -l,--level = <level>

"""

import cv2
#docopt is like argparse
import docopt
import numpy as np
import hashlib 
import os


class SteganographyException(Exception):
    pass


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
        #Mask used to put one ex:1->00000001, 2->00000010 .. associated with OR bitwise
        #Bitwise operators are used to change individual bits in an operand. A single byte of computer memory-when viewed as 8 bits-can signify the true/false status of 8 flags
        #bchel awal 0 aa chml so btzeh + bchel awal chi b array
            self.maskONE = self.maskONEValues.pop(0) #Will be used to do bitwise operations
        
            self.maskZEROValues = [254,253,251,247,239,223,191,127]
        #bze7 awal 0 aa yamen lal chml + bchel awal chi b array
        #Mak used to put zero ex:254->11111110, 253->11111101 .. associated with AND bitwise
            self.maskZERO = self.maskZEROValues.pop(0)
        
        self.curwidth = 0  # Current width position
        self.curheight = 0 # Current height position
        self.curchan = 0   # Current channel position
        self.count = 0
        self.counterrr=0
        #channels are 3 RGB
        #print("first:",self.image[379,379])
        #print("EE:",self.curheight)
        #print("VV:",self.curwidth)
    def put_binary_value(self, bits): #Put the bits of the image
        #print("boss:",self.image[self.curheight,self.curwidth])
        for c in bits: #Iterate over all bits chml lal yamen
            val = list(self.image[self.curheight,self.curwidth]) #Get the pixel value as a list (val is now a 3D array)
            #Get the pixel value as a list
            #if the bit to be encoded is '0'
           


            if int(c) == 1: #if bit is set, mark it in image
            	#Else if bit is not set, reset it in image
                #print("first")
                #print(val[self.curchan])
                val[self.curchan] = int(val[self.curchan]) | self.maskONE
                #print(val[self.curchan])#OR with maskONE
            else:
                #print("second")
                #print(val[self.curchan])
                val[self.curchan] = int(val[self.curchan]) & self.maskZERO
                #print(val[self.curchan])
                #print("curchan:",int(val[self.curchan]))
                #print("mask0:",self.maskZERO)
                #print("sum::",val[self.curchan])
                #print("after222:",val[self.curchan]) #AND with maskZERO
            
            #Update image
            self.image[self.curheight,self.curwidth] = tuple(val)
            #print("2:",val[self.curchan])

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

        #print('maskONE: ',self.maskONE)
        #print('maskZERO: ',self.maskZERO)
        #print('curwidth: ',self.curwidth)

        #print('curheight: ',self.curheight)
        #print('curchan: ',self.curchan)
        #print('curchan: ',self.curchan)
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
        #print(binl)
        self.put_binary_value(binl) #Put text length coded on 4 bytes
        for char in txt: #And put all the chars
            c = ord(char)
            #print(c)
            #print(self.byteValue(c))
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
        #file
        l = len(data)
        #print(l)
        #exmaple l=52598 if image 2.jpg
        
        if self.width*self.height*self.nbchannels < l+64:
            raise SteganographyException("Carrier image not big enough to hold all the datas to steganography")
        self.put_binary_value(self.binary_value(l, 64)) #put bin(52598,64)
        for byte in data:
            #bhwel mn number to ascii ex: (b=>98, 1=>48)
            byte = byte if isinstance(byte, int) else ord(byte) # Compat py2/py3
            self.put_binary_value(self.byteValue(byte))
        return self.image

    def decode_binary(self):
        l = int(self.read_bits(64), 2)
        output = b""
        for i in range(l):
            output += bytearray([int(self.read_byte(),2)])
        return output

    
    
def main():
    args = docopt.docopt(__doc__, version="0.2")
    in_f = args["--in"]
    out_f = args["--out"]
    os.system('optimize-images ' +in_f)
    in_img = cv2.imread(in_f)
    lossy_formats = ["jpeg", "jpg","png"]
    
    
    

    if args['encode']:
        #Handling lossy format
        out_f, out_ext = out_f.split(".")
        if out_ext in lossy_formats:
            out_f = out_f + ".png"
            print("Output file changed to ", out_f)

        data = open(args["--file"], "rb").read()
        #\x1c\n\xec\xa5U\xce\t\x98N\x1c\xac\xff\xd9'
        level = args['--level']
        steg = Code(in_img,int(level))
        res = steg.encode_binary(data)
        cv2.imwrite(out_f, res)
        #os.system('optimize-images ' +out_f)
        #os.system('picopt ' +out_f)

    elif args["decode"]:
        level = args['--level']
        steg = Code(in_img,int(level))
        raw = steg.decode_binary()
        with open(out_f, "wb") as f:
            f.write(raw)

    elif args["mes"]:
    	result = hashlib.sha512(args["--file"].encode())
    	#result.hexdigest()
    	test = steg.encode_text(args["--file"])
    	cv2.imwrite(out_f, test)
    	print("Done!")

    elif args["dmes"]:
    	outtext = steg.decode_text()
    	print(outtext)

if __name__=="__main__":
    main()

