

#### Run removeProblemReloads.py before running this method! ###


import csv
import sys

csv.field_size_limit(sys.maxsize);

targetFileName1 = "Student-Problem-Level_Merged_NoReloads_CompletePosttest.txt";
targetFileName2 = "Transaction-Level_Merged_CompletePosttest.txt";

csvPath1 = 'Desktop/January_Data/Intermediate Data/Student-Problem-Level_Merged_NoReloads.txt';
csvPath2 = 'Desktop/January_Data/Intermediate Data/Transaction_Level_Merged.txt';

f1 = open(csvPath1, 'rb');
f2 = open(csvPath2, 'rb');
counter = 0; 
removalList = [];
studentDataSet = {};

#note: writing to file in append mode
with open("Desktop/January_Data/" + targetFileName1, "wb") as new_CSV:
    try:
        reader1 = csv.reader(f1, delimiter='\t');
        for row1 in reader1: 
            if counter > 0:     # skip first (header) row
                studID = row1[2];
                if "Posttest" in str(row1[3]):
                    if studID in studentDataSet.keys():
                        studentDataSet[studID] += 1;
                    else:
                        studentDataSet[studID] = 1;
                if studID not in studentDataSet.keys():
                    studentDataSet[studID] = 0;
                    
            counter = counter + 1;
            
        
        #build removalList
        for studID in studentDataSet.keys():
            if studentDataSet[studID] < 16 or "Test" in studID:
                removalList.append(studID);
        
        f1.close();
        f1 = open(csvPath1, 'rb');
        w0 = csv.writer(new_CSV, delimiter='\t');
        reader2 = csv.reader(f1, delimiter='\t');
        studentDataSet = [];
        counter=0;
        for row2 in reader2:
            if counter == 0:
                w0.writerow(row2);
            if counter > 0:
                if row2[2] not in removalList:
                    w0.writerow(row2);
                    
                    if row2[2] not in studentDataSet: studentDataSet.append(row2[2])
                    
            counter = counter+1;
    finally:
        f1.close();
            
with open("Desktop/January_Data/" + targetFileName2, "wb") as new_CSV2:
    try:
        w1 = csv.writer(new_CSV2, delimiter='\t');
        reader3 = csv.reader(f2, delimiter='\t');
        counter=0;
        for row3 in reader3:
            if counter == 0:
                w1.writerow(row3[0:25]);
            if counter > 0:
                if row3[3] not in removalList:
                    w1.writerow(row3[0:25]);
                    if row3[3] not in studentDataSet: studentDataSet.append(row3[3])
            counter = counter+1;

    finally:
        f2.close();
        

print removalList;
print len(studentDataSet);