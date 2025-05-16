from os import remove
from lock import encrypt
from lock import decrypt
		
    ###Controlable variables###

#assigns the file names
unlocked_file="file[].txt"
locked_file="file[locked].txt"
#switch to enter testing mode
testing = False


#cariable checking if the file exists
unlocked_file_exists=False
locked_file_exists=False

#checking is a unencrypted file exists
try:
    f=open(unlocked_file,"x")
    f.close()
except:
    unlocked_file_exists = True
else:
    remove(unlocked_file)
    if testing:
        print("unlocked_file_exists=False")
#checking is a encrypted file exists
try:
    f=open(locked_file,"x")
    f.close()
except:
    locked_file_exists = True
else:
    remove(locked_file)
    if testing:
        print("locked_file_exists=False")

#The function that encrypts and decrypts the file
def process(is_encrypting):
    with open(primary_file, mode = "r+") as before_file:
        content = before_file.read()
        print("Before processing = [",content,"]\n")
        if is_encrypting:
            c=encrypt(content)
        else:
            c=decrypt(content)
    with open(secondary_file,mode = "w") as after_file:
        after_file.write(c)
    with open(secondary_file,mode = "r") as after_file:
        print("After processing = [",after_file.read(),"]")

#running the function, deciding if the file has to encrypted or decrypted and not deleting the anything if they are in testing
if not unlocked_file_exists and not locked_file_exists:
    print("file does not exist")
elif unlocked_file_exists and locked_file_exists and not testing:
    print("Both files exists. [testing mode =",testing,"]")
elif unlocked_file_exists:
    primary_file=unlocked_file
    secondary_file=locked_file
    process(True)
    if not testing:
        remove(primary_file)
elif locked_file_exists:
    primary_file=locked_file
    secondary_file=unlocked_file
    process(False)
    if not testing:
        remove(primary_file)