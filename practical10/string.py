class String:
    
    def __init__(self,st="hey"):
        print("Constructor __init__() called.");
        self.str=st;
    
    def set(self,st="hello"):
        #print("Parameterized Constructor set called.");
        self.str=st;
    def get(self):
        #print("Constructor get called.");
        return(self.str);
    def Length(self):
        self.l=len(self.str);
        return self.l;
    def Join(self,s2):
        self.str=self.str+s2.str;

    def Compare(self,s2):
        if(self.str==s2.str):
            return True;
        else:
            return False;
    def Reverse(self):
        self.str=self.str[::-1];
        return self.str;
    def Check_pali(self):
        self.str1=self.str[::-1];
        if(self.str==self.str1):
            return True;
        else:
            return False;

    def Search(self):
        self.s=input("Enter word to search : ");
        self.n=self.s in s1.str;
        if self.n==1:
            return True;
        else:
            return False;
#

s1=String();
print("s1= ",s1.get());
s2=String("ddu");
print("s2= ",s2.get());
tmp=input("Enter string : ");
s1.set(tmp);
print("s1= ",s1.get());
#tmp2=input("Enter string : ");
s1.Join(s2);
print("Length of s1 = ",s1.Length());
print("Length of s2 = ",s2.Length());
print("Joining two strings : ",s1.get());
s1.set("madam");
print("Comaparision of two strings : ",s1.Compare(s2));
print("Reverse string is : ",s1.Reverse());
print("Palindrome = ",s1.Check_pali());
print("Search word in s1 : ",s1.Search());
