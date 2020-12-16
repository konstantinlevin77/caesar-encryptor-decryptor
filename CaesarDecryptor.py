import os
class CaesarDecryptor():
    
    def __init__(self,code):
        
        if len(str(code)) != 3:
            raise Exception("Decryption code must have 3 digits")
        
        self.code = [int(digit) for digit in str(code)]
        
    
    def _decrypt_digit(self,digit,code):
        
        ASCII = ord(digit)
        
        ASCII = ASCII - code
        
        return chr(ASCII)
    
    
    def decrypt_text(self,text):
        chars = []
        for index,char in enumerate(text):
            
            chars.append(self._decrypt_digit(char,self.code[index%3]))
        
        return "".join(chars)
    
    
    def decrypt_text_file(self,text_path):
        
        with open(text_path,encoding="UTF-8",mode="r") as F:
            
            text = F.read()
        
        decrypted_text = self.decrypt_text(text)
        
        decrypted_text_name = "decrypted_"+os.path.split(text_path)[1]
        
        with open(decrypted_text_name,encoding="UTF-8",mode="w") as F:
            
            F.write(decrypted_text)
            
        print("Your decrypted text saved as {}".format(decrypted_text_name))
        

test = CaesarDecryptor(476)
test.decrypt_text_file("encrypted_orijinal_metin.txt")
            

            
        