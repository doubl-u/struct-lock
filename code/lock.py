#didnot start. the dictionary, and the unique key that is to be embeded in the encypted file has to be included.
#The decrypt function is not worked of in the key.py midlue either

import key
import al

def encrypt(content):
    content=content.replace("\t"," ")
    keys,code = key.key(False)
    txt = ""
    for a in content:
        txt += list(keys.keys())[list(keys.values()).index(a)]
    
    k_positions,cr,kr = al.structure(len(txt),len(code))
    #print(f"\ncontent = {txt}\n\ncode = {code}\n{len(code)}")
    ls=[]
    text = ""
    for a in range(1,k_positions[-1]+1):
        if a in k_positions:
            text+=code[0]
            code=code[1:]
        else:
            text+=txt[0]
            txt=txt[1:]
    text+=code
    text+=txt
    return text

def decrypt(content):
    text = ""
    txt = ""
    code = ""
    l = len(test)
    
    #to find what is the length of the code and text in the message, and uses that info to calculate the possible structure that can must have been used
    keys, len_code = key.key(content)
    len_txt = len(content)-len_code
    k_positions,cr,kr = al.structure(len_txt,len_code)
    #reversed coz otherwise when a needed part of the string is extracted, the other needed indexes after it would change  
    k_positions.sort(reverse=True)

    # In this format, after the structured layout, the left over keys are placed afterwards and then the remaining content. In the extraction, it needs to be extracted in the reverse order
    txt += content[-cr:]
    code += content[k_positions[0]:-cr]
    content=content[:k_positions[0]]
    
    # The positions specified are the keys, and the rest are content
    for a in range(k_positions[0],0,-1):
        if a in k_positions:
            code=content[a-1]+code
        else:
            txt=content[a-1]+txt

    #print(f"\ncontents = {txt}\n\ncode = {code}\n{len(code)}")
    
    # actual dectription process
    keys, len_code = key.key(code)
    for a in txt:
        text += keys[a]
    #print(text)
    return text


if __name__ == "__main__":
	test = "0123456789"*10
    a=encrypt(test)
    print(test,"=",decrypt(a))