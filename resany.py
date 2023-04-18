#------------ welcome to my project code --------------------------------------------

#-------------------- importing the modules ------------------------------------
import mysql.connector
from tkinter import *
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
#-------------------- modules imported -------------------------------------------

#--------------------- defin ing functions -----------------------------------------------------

#------------------------linereader function definition------------------------------
def line_reader(p):
    c,k=0,0
    for j in range(len(p)):
        try:
            if (p[j]=='M' or p[j]=='F') and type(eval(p[j+1]))==int:
                k+=j
                break
            else:
                continue
        except:
            continue
    for i in range(1,k):
        if (p[i]=='M' or p[i]=='F') and (p[i+1]).isnumeric==True:
            break
        else:
            c+=1
            if c==1:
                continue
            else:
                p[1]=p[1]+' '+p[i]
    for x in range(2,c+1):
        del p[2]
    if p[-1]=='PASS':
        p.append('NULL')
        p.append('NULL')
    elif len(p)==20:
        p.append('NULL')
    return p

#---------------End of Linereader definiton----------------------------------------------------------------
#-----------------------PI Calculator--------------------------------------------------------

#-----------------subject wise--------------------------------------------------------
def subpi(subject,table,db):
    mydb = mysql.connector.connect(
           host="localhost",
           user="root",
           passwd="",
           )

    my = mydb.cursor()
    my.execute('USE '+db)
    t=table
    my.execute(" select count(*) from "+t+" ;")
    sub=subject

    for x in my:
        no_s=x[0]

    my.execute(" select count(*) from "+t+" where "+sub+" = 'A1';")

    for x in my:
      a1=x[0]

    my.execute(" select count(*) from "+t+" where "+sub+" = 'A2';")

    for x in my:
      a2=x[0]

    my.execute(" select count(*) from "+t+" where "+sub+" = 'B1';")

    for x in my:
      b1=x[0]

    my.execute(" select count(*) from "+t+" where "+sub+" = 'B2';")

    for x in my:
      b2=x[0]

    my.execute(" select count(*) from "+t+" where "+sub+" = 'c1';")

    for x in my:
      c1=x[0]

    my.execute(" select count(*) from "+t+" where "+sub+" = 'c2';")

    for x in my:
      c2=x[0]

    my.execute(" select count(*) from "+t+" where "+sub+" = 'd1';")

    for x in my:
      d1=x[0]

    my.execute(" select count(*) from "+t+" where "+sub+" = 'd2';")

    for x in my:
      d2=x[0]
  
    pi=(8*a1 + 7*a2 + 6*b1 + 5*b2 + 4*c1 + 3*c2 + 2*d1 + 1*d2) * 100/(no_s * 8)
    print('PI =',pi)
    return pi


#---------------------------total pi---------------------------------------------


def totalpi(table,db):
    mydb = mysql.connector.connect(
           host="localhost",
           user="root",
           passwd="",
           )
    t=table
    my = mydb.cursor()
    my.execute('USE '+db)
    my.execute(" select count(*) from "+t+" ;")
    
    for x in my:
      no_s=x[0]

    
    sub=['grade_1','grade_2','grade_3','grade_4','grade_5']
    a1,a2,b1,b2,c1,c2,d1,d2=0,0,0,0,0,0,0,0

    for i in sub:
        my.execute(" select count(*) from "+t+" where "+i+" = 'A1' ;")
        for x in my:
            a1+=x[0]

    for i in sub:
        my.execute(" select count(*) from "+t+" where "+i+" = 'A2' ;")
        for x in my:
            a2+=x[0]

    for i in sub:
        my.execute(" select count(*) from "+t+" where "+i+" = 'B1' ;")
        for x in my:
            b1+=x[0]

    for i in sub:
        my.execute(" select count(*) from "+t+" where "+i+" = 'B2' ;")
        for x in my:
            b2+=x[0]

    for i in sub:
        my.execute(" select count(*) from "+t+" where "+i+" = 'C1' ;")
        for x in my:
            c1+=x[0]

    for i in sub:
        my.execute(" select count(*) from "+t+" where "+i+" = 'C2' ;")
        for x in my:
            c2+=x[0]

    for i in sub:
        my.execute(" select count(*) from "+t+" where "+i+" = 'D1' ;")
        for x in my:
            d1+=x[0]

    for i in sub:
        my.execute(" select count(*) from "+t+" where "+i+" = 'D2' ;")
        for x in my:
            d2+=x[0]

    pi=(8*a1 + 7*a2 + 6*b1 + 5*b2 + 4*c1 + 3*c2 + 2*d1 + 1*d2) * 100/(no_s * 40)
    print('PI =',pi)

#---------------------------End of pi function definition----------------------------
'''
Now the main game begins
'''
def main():
    while 1:
       a=input('\nAre you using it for the first time? (y/n): ')
       if a=='y':
            db=input('Name your database: ')    
            mydb = mysql.connector.connect(
                   host="localhost",
                   user="root",
                   passwd="")
            my = mydb.cursor()
            try:
                my.execute("CREATE DATABASE "+db)
                my.execute("USE "+db)
                
            except:
                print("Database already exists!")
                my.execute("USE "+db)
            break
       elif a=='n':
          try:
              db=input('Enter the name of your database:')
              mydb = mysql.connector.connect(
                 host="localhost",
                 user="root",
                 passwd="",)
              my = mydb.cursor()
              my.execute("USE "+db)
              break
          except:
              print('Database does not exist')
       else:
          print('you must enter in y or n.....')
    
    while 1:
        m=mydb.cursor()
        b=input('\nDo you want to create a new table? (if yes press y or press any key to continue): ')
        if b=='y':
          print('\nSelect the result text file from browse menu')
          a = askopenfilename()
          print(a)
          f=open(a)
          lines=f.readlines()
          lin = 0
          with open(a, 'r') as f:
                for l in f:
                    lin += 1
                    for i in range(0,lin):
                        j=lines[i]
                        p=j.split()
                        try:
                            if type(eval(p[0]))==int:
                                a1=line_reader(p)
                                a1=tuple(a1)
                            elif len(p)==0:
                                continue
                            else:
                                continue
                        except:
                            continue


          
          while 1:
              tname=input('Enter new table name: ')
              try:
                  m.execute("CREATE TABLE "+tname+" (ROLL_NO INT(20) PRIMARY KEY,NAME_OF_CANDIDATE VARCHAR(50) NOT NULL,SEX CHAR(2),SUB1_CD VARCHAR(4),MARKS_1 INT(4) , GRADE_1 VARCHAR(5) ,SUB2_CD VARCHAR(4) , MARKS_2 INT(4) , GRADE_2 VARCHAR(5) ,SUB3_CD VARCHAR(4) , MARKS_3 INT(4) , GRADE_3 VARCHAR(5) ,SUB4_CD VARCHAR(4) , MARKS_4 INT(4) , GRADE_4 VARCHAR(5) ,SUB5_CD VARCHAR(4) , MARKS_5 INT(4) , GRADE_5 VARCHAR(5) ,RESULT VARCHAR(5) , COMP1_SUB_CD VARCHAR(4) , COMP2_SUB_CD VARCHAR(4) )")
                  break
              except:
                  inp=input('Table already exists, Do you want to overwrite it?(y/n):')
                  if inp == 'y':
                    m.execute("DROP TABLE "+tname)
                    m.execute("CREATE TABLE "+tname+" (ROLL_NO INT(20) PRIMARY KEY,NAME_OF_CANDIDATE VARCHAR(50) NOT NULL,SEX CHAR(2),SUB1_CD VARCHAR(4),MARKS_1 INT(4) , GRADE_1 VARCHAR(5) ,SUB2_CD VARCHAR(4) , MARKS_2 INT(4) , GRADE_2 VARCHAR(5) ,SUB3_CD VARCHAR(4) , MARKS_3 INT(4) , GRADE_3 VARCHAR(5) ,SUB4_CD VARCHAR(4) , MARKS_4 INT(4) , GRADE_4 VARCHAR(5) ,SUB5_CD VARCHAR(4) , MARKS_5 INT(4) , GRADE_5 VARCHAR(5) ,RESULT VARCHAR(5) , COMP1_SUB_CD VARCHAR(4) , COMP2_SUB_CD VARCHAR(4) )")
                    mydb.commit()
                    break
                  elif inp == 'n':
                    continue
                  else:
                    print("You should have entered in 'y' or 'n'")
                      
          print("Table created now entering values.....")
          for i in range(0,lin):
              j=lines[i]
              p=j.split()
              try:
                  if type(eval(p[0]))==int:
                      a1=line_reader(p)             
                      cmd_1='INSERT INTO '+tname+'(ROLL_NO,NAME_OF_CANDIDATE,SEX,SUB1_CD,MARKS_1,GRADE_1,SUB2_CD,MARKS_2,GRADE_2,SUB3_CD,MARKS_3,GRADE_3,SUB4_CD, MARKS_4,GRADE_4,SUB5_CD,MARKS_5,GRADE_5,RESULT,COMP1_SUB_CD,COMP2_SUB_CD)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                      m.execute(cmd_1,tuple(a1))
                      mydb.commit()
                  elif len(p)==0:
                      continue
                  else:
                      continue
              except:
                  continue   
          mydb.commit()  
          print('\nYour newly created table')
          print()
   
          m.execute("SELECT * FROM "+tname)
          for i1 in m:
                print(i1)
          break
        else:
           l=[]
           while 1:
               tname=input('\nEnter table name: ')
               
               choice_1=input('Want to view the contents? (if yes press y or press any key): ')
               if choice_1=='y':
                    try:
                      x=0
      
                      my.execute("SELECT * FROM "+tname)
                      for i in my:
                         print(i)
                      break
                    except:
                      print('Table does not exist')
               else:
                   break
           break
    mydb.commit()
    mydb.close()
    
    #----------pi part---------------------------------------------------------------------------------------
  
    while 1:
        inp=input('\nDO YOU WANT TO CHECK PI (y,n):')
        print()
        if inp=='y':
            try:                
                table=tname
                print('\nTOTAL PI')
                totalpi(table,db)
                print('\nFor English')
                p1=subpi('grade_1',table,db)
                print('\nFor Hindi')
                p2=subpi('grade_2',table,db)
                print('\nFor Mathematics')
                p3=subpi('grade_3',table,db)
                print('\nFor Science')
                p4=subpi('grade_4',table,db)
                print('\nFor Social Science')
                p5=subpi('grade_5',table,db)

                print('\nThank you for using this software, Hope your day goes well..........')

                
                x=['English','Hindi','Mathematics','Science','Social Science']
                y=[p1,p2,p3,p4,p5]
                plt.bar(x,y)
                plt.title('PI variation with subject')
                plt.xlabel('Subjects')
                plt.ylabel('Performance Index')
                plt.show()

                
                break
            except:
                print('ENTER DATA CORRECTLY!')
        elif inp=='n':
            print('OK BYE')
            break
        else:
            print("Enter either 'y' or 'n'  ")
            
    print('\nThank you for using this software, Hope your day goes well..........')


# main()
root = Tk()
root.title('RESULT ANALYSIS SOFTWARE')
titl = Label(root, text='RESULT ANALYSIS SOFTWARE')
titl.grid(row=0,column=0,columnspan=20)
titl.config(font=('arial',20,'underline'),bg='white')

titl = Label(root, text='                           MADE BY  PRASUN KUMAR DAS')
titl.grid(row=2,column=0,columnspan=20)
titl.config(font=('arial',10),bg='white')

b= Button(root, text="LETS GET STARTED", command=main,bg='orange')
b.grid(row=3,column=1,columnspan=20)
b.config(font=('helvetica', 15, 'bold'))

titl = Label(root, text='THANK YOU FOR USING OUR PROGRAM')
titl.grid(row=4,column=0,columnspan=20)
titl.config(font=('arial',10),bg='white')











