import re

class TokenizerV1:
    def __init__(self,vocab):
        self.string2idtoken = vocab
        self.idstoken2string = {v:k for k,v in vocab.items()}

    def encode(self,text):
        tokens = re.split(r'([{,.:;_-+=~!@#$%^&*<>?|\s+}])', text)
        ids_token = [self.string2idtoken[tokens[i]] for i in range(len(tokens))]
        return ids_token
    
    def decode(self,ids_token):
        text = ' '.join([self.idstoken2string[ids_token[i]] for i in range(len(ids_token))])
        return text
    

if __name__ == "__main__":
    with open('vocab.txt','r') as f:
        text = f.read()
    
    