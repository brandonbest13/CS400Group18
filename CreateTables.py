##Create Tables.py


import pymysql


db = pymysql.connect(host='academic-mysql.cc.gatech.edu', user='cs4400_Team_18', passwd='hPwvUzZA', db='cs4400_Team_18')
cur = db.cur1sor()
AdmiTable = """
CREATE TABLE Admin
    {Username           VARCHAR(10)         NOT NULL
    Password            VARCHAR(15)         NOT NULL
    PRIMARY KEY(Username) };
"""

StudTable = """
CREATE TABLE Students
    {GT_Email           VARCHAR             NOT NULL
    Year                CHAR(2)
    Major               VARCHAR
    Username            VARCHAR(10)         NOT NULL
    Password            VARCHAR(15)         NOT NULL
    PRIMARY KEY(Username)
    UNIQUE(GT_Email)
    FOREIGN KEY(Major)REFERENCES Major(Major_Name) };
"""

DeptTable = """
CREATE TABLE Department
    {Dept_Name          VARCHAR             NOT NULL
    PRIMARY KEY(Dept_Name) };
"""

MajoTable = """
CREATE TABLE Major
    {Major_Name         VARCHAR             NOT NULL
    D_Name              VARCHAR             NOT NULL
PRIMARY KEY(Major_Name)
FOREIGN KEY(D_Name) REFERENCES Department (Dept_Name)   };
"""

ProjTable = """
CREATE TABLE Project
    {Est_Num_Students       INT
    Name                VARCHAR             NOT NULL
    Adv_Name            VARCHAR             NOT NULL
    Adv_Email           VARCHAR             NOT NULL
    Description         VARCHAR
    Desig_Name          VARCHAR
    PRIMARY KEY(Name)
    FOREIGN KEY(Desig_Name) REFERENCES Designation (Name) };
"""

CateTable = """
CREATE TABLE Category
    {CatName               VARCHAR             NOT NULL
    PRIMARY KEY(CatName) };
"""

DesiTable = """

CREATE TABLE Designation
    {Name               VARCHAR             NOT NULL
    PRIMARY KEY(Name) };
"""

CourTable = """
CREATE TABLE Course
    {Course_Num         VARCHAR             NOT NULL
    Course_Name         VARCHAR             NOT NULL
    Instructor          VARCHAR             NOT NULL
    Est_Num_Students    INT
    Designation_Name    VARCHAR
    PRIMARY KEY(Course_Num)
    UNIQUE(Name)
    FOREIGN KEY (Designation_Name) REFERENCES Designation (Name) };
"""

ApplTable = """
CREATE TABLE Application
    {Date               DATE
    Status              VARCHAR             NOT NULL
    S_Username          INT                 NOT NULL
    P_Name              VARCHAR             NOT NULL
    PRIMARY KEY(S_Username,P_Name)
    FOREIGN KEY(S_Username) REFERENCES Students (Username)
    FOREIGN KEY(P_Name) REFERENCES Project (Name) };
"""

PisCTable = """
CREATE TABLE Proj_Is_Cat
    {Category       VARCHAR         NOT NULL
    P_Name          VARCHAR         NOT NULL
    PRIMARY KEY(Category, P_Name)
    FOREIGN KEY(P_Name) REFERENCES Project (Name) };
"""

CisCTable = """
CREATE TABLE Course_Is_Cat
    {Category       VARCHAR         NOT NULL
    Course_Num      VARCHAR         NOT NULL
    PRIMARY KEY(Category, Course_Num)
    FOREIGN KEY(Course_Num) REFERENCES Course (Course_Num)
    FOREIGN KEY(Category) REFERENCES Category (CatName) };
"""

RequTable = """

CREATE TABLE Requirements
    {Requirement    VARCHAR             NOT NULL
    P_Name          VARCHAR             NOT NULL
    PRIMARY KEY(Requirement, P_Name)
    FOREIGN KEY(P_Name) REFERENCES Project(Name)
    FOREIGN KEY(Category) REFERENCES Category (CatName) };
"""
tables = [AdmiTable, StudTable, DeptTable, MajoTable, ProjTable, CateTable, DesiTable, CourTable, ApplTable, PisCTable, CisCTable, RequTable]
for table in tables:
    cur.execute(table)
db.commit()
cur.close()
db.close()