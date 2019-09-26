import datetime;

class Person:
    def __init__(self):
        print("__init__() method.");

    def get(self):
        self.name=input("Enter your name : ");
        self.bdate=input("Enter your birthdate : ");
        self.gender=input("Enter your gender : ");

    def show(self):
        print("Person name : ",self.name);
        print("Person gender : ",self.gender);
       # datetime.today();
        #self.age=bdate.year-today.year;
        #print("Person age : ",self.age);


#


class Student(Person):
    def __init__(self):
        print("");
    def get(self):
           super().get();
           self.semester=int(input("Enter your semester : "));
           self.py_marks=int(input("Enter python marks : "));
           self.j_marks=int(input("Enter java marks : "));
           self.php_marks=int(input("Enter php marks : "));

    def calc_total(self):
            self.total = self.py_marks+self.j_marks+self.php_marks;

    def calc_per(self):
            self.per=(self.total/3);

    def Grade(self):
        if self.per>=70:
            self.grade="Distinction";
        elif self.per>=60:
           self. grade="First class";
        elif self.per>=50:
            self.grade="Second class";
        elif self.per>=35:
            self.grade="Pass class";
        else :
            self.grade="FAIL";


    def Show(self):
        super().show();
        #print("Student name  : ",self.name);
        print("Student semester : ",self.semester);
        print("Total marks : ",self.total);
        print("Percentage : ",self.per);
        print("Grade : ",self.grade);

#

class Employee(Person):
        def __init__(self,salary,da,hra):
            self.salary=salary;
            self.da=da;
            self.hra=hra;

        def get(self):
            super().get();
            self.salary=int(input("Enter Salary : "));

        def da(self):
            if self.gender == 'f' || self.gender = "female" :
                self.da=self.salary*0.80;
            else
                self.da=self.salary*0.70;

        def hra(self):
            if self.gender == 'f' || self.gender = "female" :
                self.hra=self.salary*0.10;
            else
                self.hra=self.salary*0.15;

        def total_Sal(self):
            self.bonus=self.salary*0.50;
            self.sal=self.da+self.hra+self.bonus;
        
        def show(self):
            

#


p1.Person();
p1.get();
p1.show();
s1=Student();
s1.get();
s1.calc_total();
s1.calc_per();
s1.Grade();
s1.Show();
