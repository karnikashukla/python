import mysql.connector;
from mysql.connector import Error;

try:
    con=mysql.connector.connect(host="localhost",database="python",user="root",password="mcalab");

    print("Connected..!!");


    def insert():
        ch='y';
        while ch=='y':
            rn=input("Enter roll no. : ");
            nm=input("Enter name : ");
            bd=input("Enter Birthdate : ");
            gender=input("Enter gender : ");
            sem=input("Enter Semester : ");
            py_mark=input("Enter Python marks : ");
            java_mark=input("Enter Java marks : ");
            php_mark=input("Enter PHP marks : ");

            queryinsert="insert into student(rollno,name,birthdate,gender,semester,python_marks,java_marks,php_marks) values (' ";
            queryinsert=queryinsert+rn+"',";
            queryinsert=queryinsert+"'"+nm+"',";
            queryinsert=queryinsert+"'"+bd+"',";
            queryinsert=queryinsert+"'"+gender+"',";
            queryinsert=queryinsert+sem+",";
            queryinsert=queryinsert+py_mark+",";
            queryinsert=queryinsert+java_mark+",";
            queryinsert=queryinsert+php_mark+")";

            print(queryinsert);

            cursor=con.cursor();

            result=cursor.execute(queryinsert);
            con.commit();
            print("Record inserted successfully..!"); 

            ch=input("Do you want to insert more records ?(y/n)");
        print("Bye..!!");


    def total():
        querytotal="update student set total_marks=python_marks+java_marks+php_marks";

        print(querytotal);

        cursor=con.cursor();

        result=cursor.execute(querytotal);

        con.commit();

        print("Total marks updated successfully..!");

    def percentage():
        queryper="update student set percentage=total_marks/3";

        print(queryper);

        cursor=con.cursor();

        result=cursor.execute(queryper);

        con.commit();

        print("Percentage updated successfully..!");

    def grade():
        
        
    
    
    def menu():
        print("1.Insert records.");
        print("2.calculate total.");
        print("3.calculate percentage.");
        print("4.calculate grade.");

    def getChoice():
        choice=int(input("Enter your choice : "));
        return choice;

    def main():
        while True:
            menu();
            c=getChoice();
            if c>4:
                return;
            else:
                select(c);
    def select(c):
        if c==1:
            insert();
        elif c==2:
            total();
        elif c==3:
            percentage();
        elif c==4:
            grade();
    main();
    print("Bye..!!");

        
        
except Error as e:
    print("Error : ",e);

finally:
    if(con.is_connected()):
        con.close();
        print("Connection disabled..!");
