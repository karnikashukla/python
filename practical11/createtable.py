import mysql.connector;
from mysql.connector import Error;

try:
    con=mysql.connector.connect(host="localhost",database="python",user="root",password="mcalab");

    print("Connected..!!");

    querycreatetable="create table Student (name varchar(20) not null ,";
    querycreatetable=querycreatetable+"birthdate date ,gender char(1),";
    querycreatetable=querycreatetable+"semester int(1),python_marks decimal,";
    querycreatetable=querycreatetable+"java_marks decimal,php_marks decimal,";
    querycreatetable=querycreatetable+"total_marks decimal,percentage decimal,";
    querycreatetable=querycreatetable+"grade char(1))";

    print(querycreatetable);

    cursor=con.cursor();

    result=cursor.execute(querycreatetable);

    print("Table created successfully..!");
except Error as e:
    print("Error : ",e);
