def Menu():
    print("MENU");
    print("1.Find string length");
    print("2.Join strings");
    print("3.Compare strings");
    print("4.Reverse string");
    print("5.Check string Palindrome");
    print("6.Search word");

def Length(str):
    l=len(str);
    return l;

#Menu();

def Join():
    str1=input("Enter one string : ");
    str2=input("Enter another string : ");
    join=str1+str2;
    return join;

def Compare(str1,str2):
    if(str1==str2):
        res="same";
        return res;
    else:
        res="Not same";
        return res;

def Reverse(str1):
    s=str1[::-1];
    return s;

def Palindrome(str1):
    str2=str1[::-1];
    if(str1==str2):
        res="Palindrome";
        return res;
    else:
        res="Not Palindrome.";
        return res;

def Search(str1,s):
    n=s in str1;
    if n==1:
        res="found";
        return res;
    else:
        res="not found";
        return res;

def getChoice():
    ch=int(input("Enter your choice : "));
    return ch;

def Choice(ch):
    if ch==1:
        str=input("Enter any String : ");
        l=Length(str);
        print("Length of String is ",l);
    elif ch==2:
        j=Join();
        print("After joining two strings : ",j);
    elif ch==3:
        str1=input("Enter one string : ");
        str2=input("Enter another string : ");
        c=Compare(str1,str2);
        print("String comparision result : ",c);
    elif ch==4:
        str1=input("Enter a string : ");
        res=Reverse(str1);
        print("Reverse of a given string is : ",res);
    elif ch==5:
        str1=input("Enter a string : ");
        res=Palindrome(str1);
        print("String is ",res);
    elif ch==6:
        str1=input("Enter one string : ");
        s=input("Enter a word to search in the string : ");
        res=Search(str1,s);
        print("A word is ",res);
        


def Main():
    while True:
        Menu();
        ch=getChoice();
        if ch>=7:
            return;
        else:
            Choice(ch);

Main();
