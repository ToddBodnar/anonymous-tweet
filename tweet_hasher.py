import random
import re
import string
    
    
class dateTrimmer(object):
    def trim(date):
        return 0

class lazyDateTrimmer(dateTrimmer):
    def trim(date):
        return date;

class tweet_hasher(object):
    def __init__(self,forceWordSize = False,dateTrimmer = lazyDateTrimmer, matchCases = False):
        self.forceWordSize = forceWordSize
        self.matchCases = matchCases
        self.dateTrimmer = dateTrimmer
        self.wordConversion = {}
        self.wordSet = set()
        self.firstDate = 999999
        self.userConversion = {}
        self.userSet = set()
        ##straight convert the front of urls
        self.wordSet.add("t")
        self.wordSet.add("co")
        self.wordConversion["t"] = "t"
        self.wordConversion["co"] = "co"
    
    def __randomString(self,word):    
        length = random.randint(3,10)
        if self.forceWordSize:
            length = len(word)
        ##see https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
        text = "".join(random.choice(string.ascii_lowercase) for _ in range(length))
        return text
        
    def __copyCase(self,oldWord,newWord):
        if not self.matchCases | self.forceWordSize:
            return newWord
        result = ""
        for itr in range(len(oldWord)):
            if oldWord[itr].isupper():
                result = result + newWord[itr].upper()
            else:
                result = result + newWord[itr]
        return result
    
    def train(self,user,text,date):
        if(user not in self.userConversion):
            newUserId = random.randint(1, 10000000000)
            while newUserId in self.userSet:
                newUserId = random.randint(1, 10000000000)
            self.userConversion[user] = newUserId
            self.userSet.add(newUserId)
        
        for keyword in re.split("[^a-zA-Z]",text):
            if(keyword == ''):
                continue
            if(keyword.lower() not in self.wordConversion):
                newString = self.__randomString(keyword)
                while newString in self.wordSet:
                    newString = self.__randomString(keyword)
                self.wordConversion[keyword.lower()] = newString
                self.wordSet.add(newString)
    
    def convert(self,user,text,date):
        newUser = self.userConversion[user]
        newDate = self.dateTrimmer.trim(date)
        newText = ""
        for keyword in re.split("([^a-zA-Z])",text):
            if(keyword == ''):
                continue
            if keyword.lower() in self.wordConversion:
                newText = newText + self.__copyCase(keyword,self.wordConversion[keyword.lower()])
            else:
                newText = newText + keyword
        return {"user":newUser,"text":newText, "date":date}
        
    def print(self):
        print("New User Set")
        print(self.userSet)
        print("User Conversion Table")
        print(self.userConversion)  
        print("New Word Set")
        print(self.wordSet)
        print("Word Conversion Table")
        print(self.wordConversion)

t = tweet_hasher(forceWordSize = True, matchCases = True)

t.train(12,"this is a test!",0)
t.train(12,"also a #test",12)
t.train(23,"Something else? ;)",23)    

print(t.convert(12,"this is a test!",0))
print(t.convert(12,"also a #test",12))
print(t.convert(23,"Something else? ;)",23))
