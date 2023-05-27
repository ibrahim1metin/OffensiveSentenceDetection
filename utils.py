import string
def sortDictByValues(dictionary:dict):
    keys=list(dictionary.keys())
    values=list(dictionary.values())
    for i in range(len(values)):
        for j in range(len(keys)-i-1):
            if(values[j]>values[j+1]):
                values[j],values[j+1]=values[j+1],values[j]
                keys[j],keys[j+1]=keys[j+1],keys[j]
    return {k:v for k,v in zip(keys,values)}
def clean_text(text:str):
    wordss=text.split()
    for i in wordss:
        if(i.find('@')==-1):
            wordss.remove(i)
    table = str.maketrans('','', string.punctuation)
    wordss=[word.translate(table) for word in wordss]
    ss=[word.lower() for word in wordss if word.isalpha()]
    return ss