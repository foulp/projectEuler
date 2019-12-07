# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:08:31 2016

@author: timothee.boulet
"""

alphabet = [chr(letter) for letter in range(ord('A'), ord('Z')+1)]

lower = list(range(97,123)) #a à z
lower = [bin(letter)[2:] for letter in lower]

f = open('C:\\Users\\timothee.boulet\\Desktop\\ProjectEuler\\Probleme59_cipher.txt', "r")

text=f.read().split(',')
text=[bin(int(letter))[2:] for letter in text]

def xor(a,b):
    lena=len(a)
    lenb=len(b)
    diff=lena-lenb
    if diff<0:
        a=abs(diff)*'0'+a
    elif diff>0:
        b=abs(diff)*'0'+b
    result=''
    for a,b in zip(a,b):
        if a!=b:
            result+='1'
        else:
            result+='0'
    return result

def decypher(text, key):
    """ key must be length 3"""
    result=[]
    for i, letter in enumerate(text):
        if i%3==0:
            decrypt=xor(letter, key[0])
            result.append(chr(int(decrypt,2)))
        if i%3==1:
            decrypt=xor(letter, key[1])         
            result.append(chr(int(decrypt,2)))
        if i%3==2:
            decrypt=xor(letter, key[2])
            result.append(chr(int(decrypt,2)))
    return ''.join(result)



forbidden=['#', 'µ', '¤', '§', '\\', '[', ']', '\\', '{', '}' ]
mandatory=['the', 'and', 'to', 'be', 'of']
for i,letter1 in enumerate(lower):
    for j,letter2 in enumerate(lower):
        for k,letter3 in enumerate(lower):
            test=decypher(text, [letter1, letter2, letter3])
            if all(carac not in test for carac in forbidden):
                if all(word in test for word in mandatory):
                    print(i,j,k)
#6,14,3
test=decypher(text, [lower[6], lower[14], lower[3]])              
ascii=[ord(letter) for letter in test]
print(sum(ascii))                
