import os
class CaesarEncryptor():
    
    def __init__(self,code):
        
        if len(str(code)) != 3:
            raise Exception("Please use a 3 digit code.")
        
        self.code = [int(digit) for digit in str(code)]
        
        
    def _encrypt_digit(self,digit,code):
        
        ASCII = ord(digit)
        return chr(ASCII + code)
    
    
    def encrypt_text(self,text):
        chars = []
        for index,char in enumerate(text):
            chars.append(self._encrypt_digit(char,self.code[index%3]))
        
        return "".join(chars)
    
    
    def encrypt_text_file(self,text_path):
        
        with open(text_path,mode="r",encoding="UTF-8") as F:
            
            text = F.read()
            
        text_encrypted = self.encrypt_text(text)
        
        encrypted_file_name = "encrypted_"+os.path.split(text_path)[1]
        
        with open(encrypted_file_name,
                  mode="w",
                  encoding="UTF-8"
                  ) as F:
            
            F.write(text_encrypted)
        
        print("Your encrypted text saved as {}".format(encrypted_file_name))


