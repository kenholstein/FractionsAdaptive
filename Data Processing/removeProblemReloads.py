import csv

csvPath1 = 'Desktop/January_Data/Student-Problem-Level_Merged.txt';

f1 = open(csvPath1, 'rb');
counter = 0; 
studentDataSet = {};
targetFileName1 = "Student-Problem-Level_Merged_NoReloads.txt";

#note: writing to file in append mode
with open("Desktop/January_Data/" + targetFileName1, "wb") as new_CSV:
    w0 = csv.writer(new_CSV, delimiter='\t');
    try:
        reader1 = csv.reader(f1, delimiter='\t');
        
        for row1 in reader1:
            
            studID = row1[2];
            
            if counter == 0:
                w0.writerow(row1);
            else:
                if studID in studentDataSet.keys():
                    if str([row1[3], row1[4]]) not in studentDataSet[studID]:
                        studentDataSet[studID].append(str([row1[3], row1[4]]));
                        w0.writerow(row1);
                        print [row1[3], row1[4]];
                if studID not in studentDataSet.keys():
                    studentDataSet[studID] = [[row1[3], row1[4]]];
                    w0.writerow(row1);
                    print [row1[3], row1[4]];
                    
            counter = counter + 1;
        
    finally:
        f1.close();

print len(studentDataSet.keys());