class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str= ""
        for sent in strs:
            encode_str+= f"{len(sent)}#{sent}"
        return encode_str

    def decode(self, s: str) -> List[str]:
        decode_list =[]
        i=0

        while i < len(s):

            j=i
            while s[j] != '#':
                j+=1
            
            length = int(s[i:j])

            i = j+1
            sent = s[i:i+length]
            decode_list.append(sent)
            i+=length
        
        return decode_list