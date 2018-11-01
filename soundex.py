def get_soundex(token):
    temp=''
    token=token.upper()
    temp+=token[0]
    dic={'BFPV':1,'CGJKQSXZ':2,'DT':3,'L':4,'MN':5,'R':6,'AEIOUYHW':''}
    
    for char in token[1:]:
        for key in dic.keys():
            if char in key:
                code=str(dic[key])
                break
        if temp[-1]!=code:
            temp+=code
    temp=temp[:4].ljust(4,'0')
    return temp