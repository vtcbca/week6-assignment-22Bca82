reate table result
                (
                Student_id int primary key,
                Student_name text,
                Sub_1 int,
                Sub_2 int,
                Sub_3 int,
                Sub_4 int,
                Sub_5 int
                )""")
print("Table created successfully")
#record inserting using list
record=[
        [1,'heer',60,89,45,52,65],
        [2,'pitu',75,90,68,78,65],
        [3,'ujjaval',56,45,40,42,45],
        [4,'pihu',82,70,84,66,89],
        [5,'harry',15,20,7,36,40],
        [6,'viha',45,50,60,52,51],
        [7,'mudhra',56,65,52,41,70],
        [8,'diya',20,25,15,35,45],
        [9,'jiya',56,89,65,75,69],
        [10,'foram',45,40,56,41,43]
       ]
cur.executemany("Insert Into result values(?,?,?,?,?,?,?)",record)
print("Record inserted successfull")
con.commit()

Question3. Dump table into csv file "result.csv".
Dump the Table using sqlite3
Ans:-
	.mode csv
	.header on
	.output result_file.csv
 	select * from result;
 	.quit

question4. Read result.csv file and Print Total Marks and Grade of each student.
	  Also Append Total Marks and Grade column into result.csv file.

import csv
filename="c://sqlite3//result_file.csv"
with open(filename,"r")as read_file:
    read=csv.reader(read_file)
    data=list(read)
    #copy the data of a csv file into data variable
    #condition for Total
    for i in range(len(data)):
        if i!=0:
            total=int(data[i][2])+int(data[i][3])+int(data[i][4])+int(data[i][5])+int(data[i][6])
            data[i].append(total)
        else:
            data[i].append('Total')

    #condition for Percentage
    for i in range(len(data)):
        if i!=0:
            percentage=int(data[i][7])/5
            data[i].append(percentage)
        else:
            data[i].append('Percentage')

    #condition for Grade
    for i in range(len(data)):
        if i!=0:
            if int(data[i][8])>80:
                data[i].append('A+')
            elif int(data[i][8])>70 and int(data[i][8])<80:
                data[i].append('A')
            elif int(data[i][8])>60 and int(data[i][8])<70:
                data[i].append('B')
            elif int(data[i][8])>50 and int(data[i][8])<60:
                data[i].append('C')
            elif int(data[i][8])>40 and int(data[i][8])<50:
                data[i].append('D')
            else:
                data[i].append('Fail')
        else:
            data[i].append('Grade')
            

#adding total in the csv file
with open(filename,"a",newline="")as write_file:
    write=csv.writer(write_file)
    write.writerows(data)
    print('Total,Percentage and Grader are successfully Append.')

with open(filename,"r")as read:
    r=csv.reader(read)
    for i in r:
        print(i)
    
Question5. List out Top 3 Student id and name with its percentage.

import csv
filename="c://sqlite3//result_file.csv"
with open(filename,"r")as read_file:
    read=csv.DictReader(read_file)
    record=list(read)
    record.sort(key= lambda x : x['Total'] , reverse = True)
    count=0
    print("Student Id\tStudent Name\tPercentage")
    for i in record:
        if count<3:
            print(i['Student_id'],"\t\t",i['Student_name'],"\t\t",i['Percentage'])
            count+=1
