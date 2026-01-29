# This is a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end and Replace vowels (a, e, i, o, u) with special symbols (@, #, $, %, &).
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove the last letter and append it to the beginning and # Replace vowels (a, e, i, o, u) with special symbols (@, #, $, %, &).

# This program is asked first, whether you want to code or decode

c="******************* SECRET CODE LANGUAGE TRANSLATOR *******************".center(140)
print(c)
ask=input("What you want to do 'ENCODE' OR 'DECODE' : ")

if(ask=="ENCODE"):
    inputs=input("Enter Your Message : ")
    import random
    inputsIntoLowerCase=inputs.lower()
    inputSplits=inputsIntoLowerCase.split() 
    encodeWords=[]
    randomList1=["zvxb","bxbe","xxwb","hxwb","uiqu","qxyi","oxqp","zwim","qqiu","ioqp","ihqi"]
    randomList2=["hphg","jhhd","uyqx","xuyn","nxhw","xoiy","xlim","lkla","nfjk","jlcl"]
    for item in inputSplits:
        if(len(item)>=3):
            word=random.choice(randomList1)+item[3:]+item[:3]+random.choice(randomList2)
            word=word.replace("a","@").replace("e","#").replace("i","$").replace("o","%").replace("u","&")
            encodeWords.append(word)
        else:
            s=item[::-1]
            encodeWords.append(s)
    finalEncodeWords=" ".join(encodeWords)
    print(finalEncodeWords)
elif(ask=="DECODE"):
    inputs=input("Enter Your Message : ")
    inputsIntoLowerCase=inputs.lower()
    inputSplits=inputsIntoLowerCase.split() 
    decodeWords=[]
    for item in inputSplits:
        if(len(item)>=3):
            word=item[4:-4]
            word=word[-3:]+word[:-3]
            word=word.replace("@","a").replace("#","e").replace("$","i").replace("%","o").replace("&","u")
            decodeWords.append(word)
        else:
            s=item[::-1]
            decodeWords.append(s)
    finalDecodeWords=" ".join(decodeWords)
    print(finalDecodeWords)

