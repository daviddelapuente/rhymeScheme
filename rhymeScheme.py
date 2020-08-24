import nltk
nltk.download('cmudict')

#this function takes 2 strings, and return True if one of them is sufix of the other
def isSufix(s1,s2):
    if(len(s1)>=len(s2)):
        for i in range(len(s2)):
            if (s2[len(s2)-1-i]!=s1[len(s1)-1-i]):
                return False
    else:
        for i in range(len(s1)):
            if(s1[len(s1)-1-i]!=s2[len(s2)-1-i]):
                return False
    return True

#this function was taken from https://github.com/kevin-brown/rhyme-detect
def possible_phones(word):
    phone_dictionary = nltk.corpus.cmudict.dict()
    if word not in phone_dictionary:
        return []
    return phone_dictionary[word]

phone_dictionaryOPT = nltk.corpus.cmudict.dict()
def possible_phones_OPT(word):
    if word not in phone_dictionaryOPT:
        return []
    return phone_dictionaryOPT[word]

def first_score(phones1,phones2):
    if(len(phones1)==0 or len(phones2)==0):
        return 0
    phones1=phones1[::-1]
    phones2=phones2[::-1]
    if len(phones1)>len(phones2):
        phones1,phones2=phones2,phones1
    hit=0
    total=0
    for i in range(len(phones1)):
        if phones1[i]==phones2[i]:
            if hasDigit(phones1[i]):
                hit+=2
                total+=2
            else:
                hit+=1
                total+=1
        else:
            total+=1
    return hit/total
    
def hasDigit(s):
    for char in s:
        if char.isdigit():
            return True
    return False

def rhyme_score(first_word,second_word):
    return getScore(first_word,second_word,possible_phones)

def rhyme_scoreOPT(first_word, second_word):
    return getScore(first_word,second_word,possible_phones_OPT)

#this function was inspired by word_similarity from https://github.com/kevin-brown/rhyme-detect
def getScore(first_word, second_word,dicrtionaryFunction):
    #first we filter some border cases like empty strings
    if(first_word==None or second_word==None):
        return 0
    if(len(first_word)==0 or len(second_word)==0):
        return 0
    if (isSufix(first_word,second_word)):
        return 0
    

    #this build the phonemas
    first_phones = dicrtionaryFunction(first_word)
    second_phones = dicrtionaryFunction(second_word)
    if not first_phones or not second_phones:
        return 0

    #we invert the array
    first_range = first_phones[0][::-1]
    second_range = second_phones[0][::-1]

    #we put the smaller array in first_range
    if len(first_range) > len(second_range):
        first_range, second_range = second_range, first_range

    hits = 0
    total = len(first_range)

    c1=[]
    b=False
    for i in range(len(first_range)):
        phone=first_range[i]
        if(hasDigit(phone)):
            b=True
        c1.append(phone)
        if(not phone[-1].isdigit() and b):
            break

    c2=[]
    b=False
    for i in range(len(second_range)):
        phone=second_range[i]
        if(hasDigit(phone)):
            b=True
        c2.append(phone)
        if(not phone[-1].isdigit() and b):
            break
    
    score1=first_score(c1,c2)
    return score1

def word_similarity(first_word, second_word, start_phone=None, end_phone=None):
    first_phones = possible_phones(first_word)
    second_phones = possible_phones(second_word)

    if not first_phones or not second_phones:
        return 0

    first_phones = first_phones[0]
    second_phones = second_phones[0]

    first_range = first_phones[start_phone:end_phone]
    second_range = second_phones[start_phone:end_phone]

    first_range = first_range[::-1]
    second_range = second_range[::-1]

    if len(first_range) > len(second_range):
        first_range, second_range = second_range, first_range

    hits = 0
    total = len(first_range)

    for idx, phone in enumerate(first_range):
        other_phone = second_range[idx]

        if phone == other_phone:
            hits += 1

            # Phones with emphasis are better matches, weight them more
            if phone[-1].isdigit():
                hits += 1
                total += 1

    return hits / total