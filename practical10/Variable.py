class Person:
    count=0;
    def __init__(self):
        print("Constructor __init__() called.");
        Person.count=Person.count+1;
        #print("Constructor count = ",Person.count);
    def set(self,nm,ag):
        self.name=nm;
        self.age=ag;
    def show(self):
        print("Name : ",self.name);
        print("Age : ",self.age);
        print("Constructor count = ",Person.count);

#

p1=Person();
p1.set("karnika",22);
p1.show();
p2=Person();
p2.set("abc",26);
p2.show();
