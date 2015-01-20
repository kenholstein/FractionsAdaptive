#for each file in a given folder, print all rows (excluding the first )to same output file

import os
import sys
import csv

csv.field_size_limit(sys.maxsize);

dataPathName = "Desktop/January_Data/";
#dataFolderName = "Individual Schools/Transaction_Level/"; 
dataFolderName = "Individual Schools/Student-Problem_Level/";
#targetFileName = "Transaction_Level_Merged.txt"; 
targetFileName = "Student-Problem-Level_Merged.txt";
#sampleFileName = "Hoover_Transactions.txt" 
sampleFileName ='Hoover_ProblemLevel.txt';

with open(dataPathName + targetFileName, "wb") as new_CSV:
    csvPath0 = dataPathName + dataFolderName + sampleFileName;
    f0 = open(csvPath0, 'rb');
    reader0 = csv.reader(f0, delimiter='\t');
    w0 = csv.writer(new_CSV, delimiter='\t');
    counter0 = 0;
    for row0 in reader0:
        if counter0 == 0:
           w0.writerow(row0);
        else:
            break;
        counter0+=1;
    print counter0;
    f0.close();


    for filename in os.listdir(dataPathName + dataFolderName):
        if ".txt" in filename:
            csvPath = dataPathName + dataFolderName + filename;
            f = open(csvPath, 'rb')
            counter = 0;    
            try:
                reader = csv.reader(f, delimiter='\t');
                for row in reader:
                    if counter > 0:     # skip first (header) row
                        w0.writerow(row);        
                    counter = counter + 1;
            finally:
                f.close();