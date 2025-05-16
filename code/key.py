
#have to finish the program for the encrypting version and decrypting.

from random import shuffle

def key(content=False,mode = 0):
    if mode == 0:
        special_characters = {"00":" ", "01":"!", "02":"\"", "03":"#", "04":"$", "05":"%", "06":"&", "07":"\'", "08":"(", "09":")", "10":"*", "11":"+", "12":",", "13":"-", "14":".", "15":"/",
                              "26":":", "27":";", "28":"<", "29":"=", "30":">", "31":"?", "32":"@",
                              "59":"[", "60":"\\", "61":"]", "62":"^", "63":"_", "64":"`",
                              "91":"{", "92":"|", "93":"}", "94":"~",
                              "95":"\n"}

        digits = {"16":"0", "17":"1", "18":"2", "19":"3", "20":"4", "21":"5", "22":"6", "23":"7", "24":"8", "25":"9"}

        upper_case = {"33":"A", "34":"B", "35":"C", "36":"D", "37":"E", "38":"F", "39":"G", "40":"H", "41":"I", "42":"J", "43":"K", "44":"L", "45":"M", "46":"N", "47":"O", "48":"P", "49":"Q", "50":"R", "51":"S", "52":"T", "53":"U", "54":"V", "55":"W", "56":"X", "57":"Y", "58":"Z"}

        lower_case = {"65":"a", "66":"b", "67":"c", "68":"d", "69":"e", "70":"f", "71":"g", "72":"h", "73":"i", "74":"j", "75":"k", "76":"l", "77":"m", "78":"n", "79":"o", "80":"p", "81":"q", "82":"r", "83":"s", "84":"t", "85":"u", "86":"v", "87":"w", "88":"x", "89":"y", "90":"z"}
    
    all_characters = {**special_characters ,**digits ,**upper_case ,**lower_case}
    
    all_characters_reversed=dict(zip(all_characters.values(),all_characters.keys()))

    length = len(all_characters.keys())
    
    key_length = len(list(all_characters.keys())[0])
    #length of each encrypted key needs to be the same

    if not content:
        ls = []
        en_key = {}
        code=""
        for a in range(0,length):
            b = ""
            if a<10:
                b = "0"
            b+=str(a)
            ls.append(str(all_characters[b]))
        shuffle(ls)
        
        c=[]
        for a in ls:
            code+=a
        keys=dict(zip(all_characters.values(),ls))
        return keys, code
   
    else:
        ls = []
        for a in content:
            ls.append(all_characters[all_characters_reversed[a]])
            #all_characters_reversed[a] finds the key for the character and then reassigns it to its original character,
            # "r34*i" > [43,54,66,09,01] > "hello"
        keys=dict(zip(all_characters.values(),ls))
        return keys,len(list(all_characters.values()))

if __name__=='__main__':
    j,k=key(False)
    #print(j,"\n\n",key(k))

    #In this test, key(false) returns a randomly generated key dictionary 
    #and its keys as a single string (to be implmented in the encrypted message)
