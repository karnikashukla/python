class Student :
    def __init__(self):
        print("Constructor __init()__ called");
        
    def input(self):
        self.rno = int(input("Enter roll no .: "));
        self.c_marks=int(input("Enter c_marks : "));
        self.cpp_marks=int(input("Enter cpp_marks : "));
        self.python_marks=int(input("Enter python_marks : "));

    
    def calc_total(self):
        self.total_marks= self.c_marks + self.cpp_marks + self.python_marks;

    def calc_per(self):
        self.per=(self.total_marks/3);

    def grade(self):
         if self.per>=70:
            self.grade="Distinction";
         elif self.per>=60:
             self.grade="First class";
         elif self.per>=50:
             self.grade="Second class";
         elif self.per>=35:
             self.grade="Pass class";
         else:
             self.grade="FAIL";
       
    def display(self):
        print("Roll no : ",self.rno);
        #print("Name : ",self.name);
        print("Total marks : ",self.total_marks);
        print("Percentage : ",self.per);
        print("Grade ",self.grade);

stud1= Student();
stud1.input();
stud1.calc_total();
stud1.calc_per();
stud1.grade();
stud1.display();

stud2 = Student();
stud2.input();
stud2.calc_total();
stud2.calc_per();
stud2.grade();
stud2.display();
