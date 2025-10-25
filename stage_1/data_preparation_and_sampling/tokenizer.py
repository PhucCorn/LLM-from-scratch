import re

class TokenizerV1:
    def __init__(self,vocab):
        self.string2idtoken = vocab
        self.idstoken2string = {v:k for k,v in vocab.items()}

    def encode(self,text):
        tokens = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        tokens = [item.strip() for item in tokens if item.strip()]
        ids_token = [self.string2idtoken[tokens[i]] if tokens[i] in self.string2idtoken else self.string2idtoken["<|unk|>"] for i in range(len(tokens))]
        return ids_token
    
    def decode(self,ids_token):
        text = ' '.join([self.idstoken2string[ids_token[i]] for i in range(len(ids_token))])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
    

if __name__ == "__main__":
    with open("../../data/the-verdict.txt",'r') as f:
        text = f.read()
    words_set = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    words_set = [item.strip() for item in words_set if item.strip()]
    words_set = list(set(words_set))
    words_set.sort()
    words_set += ["<|unk|>","<|endoftext|>"]
    vocab = {words_set[i]:i for i in range(len(words_set))}
    tokenizer = TokenizerV1(vocab)
    sample_text = "The verdict -- what is the verdict?"
    encoded = tokenizer.encode(sample_text)
    print("Sample text: ", sample_text)    
    print("Encoded: ", encoded)
    print("Decoded: ", tokenizer.decode(encoded))