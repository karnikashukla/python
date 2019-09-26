class Method:
    count = 0;
    def __init__(self):
        print("Constructor __init__() called.");
        Method.count=Method.count+1;
    @classmethod
    def method1(cls,nm):
        print("Inside class method.");
        cls.name=nm;
        
    @staticmethod
    def method2():
        print("Inside static method.");

    def show(self):
        print("Name = ",self.name);
        print("Object count = ",Method.count);

#

name=input("Enter your name : ");
m1=Method();
m1.method1(name);
m1.method2();
m1.show();
name1=input("Enter your name : ");
m2=Method();
m2.method1(name1);
m2.method2();
m2.show();
