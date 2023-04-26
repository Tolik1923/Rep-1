from PIL import Image
import binascii

text = "DAnville was born on 17 August 1709, the son of Louis de La Rochefoucauld, Marquis de Roye, a distant cousin of the Dukes of La Rochefoucauld and Marthe Ducasse. He married Marie-Louise-Nicole de La Rochefoucauld, daughter of Alexandre, Duke de La Rochefoucauld. Alexandre had no surviving sons and exceptionally gained the permission of the Pope and the French King to hand the ducal title through the female line, but one of the conditions was that his daughter must marry a La Rochefoucauld. Jean-Baptiste de La Rochfoucauld de Roye was created Duc DAnville on 15 February 1732, a few days before the marriage. He was an officer in the galley corps (corps des galères), transferring into the French navy in 1734, and he was appointed lieutenant general of in January 1745.[1] DAnville and Marie-Louise-Nicole had three daughters and one son, Louis Alexandre, who succeeded to the title Duc DAnville in 1746 on his fathers death. And on his grandfathers death in 1762, he became Duc de La Rochefoucauld."

def read_img(name):
    extracted_bin = []
    with Image.open(name) as img:
        width, height = img.size
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                extracted_bin.append(pixel[2]&1)

    data = "".join([str(x) for x in extracted_bin])
    return data 

def write_img(bin_text, name):
    i = 0
    with Image.open(name) as img:
        width, height = img.size
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                if(i < len(bin_text)):
                    pixel[2] = pixel[2] & ~1 | int(bin_text[i])
                    i+=1
                if(i == len(bin_text)):
                    i = 0
                    pixel[2] = pixel[2] & ~1 | int(bin_text[i])
                img.putpixel((x,y), tuple(pixel))
        img.save("secret_img.png", "PNG")

def decode_BW(name):
    data = read_img(name)
    i = 0
    with Image.open(name) as img:
        width, height = img.size
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                if (data[i] == "1"):
                    for n in range(0,3):
                        pixel[n] = 255
                if (data[i] == "0"):
                    for n in range(0,3):
                        pixel[n] = 0
                i += 1
                img.putpixel((x,y), tuple(pixel))
        img.save("decode_img.png", "PNG")




def decode_binary (data):
    binary = ""
    for i in range (0, len(data)):
        if (i % 8) == 0:
            binary += ' '
            binary += data[i]
        else:
            binary += data[i]

    for i in range (0, (len(data) % 7)):
        binary += data[i]

    binary_values = binary.split()
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character

    return ascii_string

def code_in_binary(text):
    bin_text = ''.join(format(ord(i), '08b') for i in text)
    return bin_text

def read_img_3(name):
    extracted_bin = []
    with Image.open(name) as img:
        width, height = img.size
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                for n in range(0,3):
                    extracted_bin.append(pixel[n]&1)

    data = "".join([str(x) for x in extracted_bin])
    return data 

def write_img_3(bin_text, name):
    i = 0
    with Image.open(name) as img:
        width, height = img.size
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                for n in range(0,3):
                    if(i < len(bin_text)):
                        pixel[n] = pixel[n] & ~1 | int(bin_text[i])
                        i+=1
                    if(i == len(bin_text)):
                        i = 0
                        pixel[n] = pixel[n] & ~1 | int(bin_text[i])
                img.putpixel((x,y), tuple(pixel))
        img.save("secret.png", "PNG")





#data = read_img("propala.png")
#ascii_string = decode_binary(data)

#bin_text =  code_in_binary(text)
#write_img(bin_text, "propala.png")
#data = read_img("secret_img.png")
#ascii_string = decode_binary(data)

#bin_text =  code_in_binary(text)
#write_img_3(bin_text, "propala.png")
#data = read_img_3("secret.png")
#ascii_string = decode_binary(data)

#data = read_img("BW.png")
#write_img(data, "propala.png")
#decode_BW("secret_img.png")





#print (ascii_string)







