import csv
import sys
import math
import itertools
csv.field_size_limit(sys.maxsize);

# note: the local path on my machine is currently assigned to csvPath
csvPath = 'Desktop/January_Data/Transaction-Level_Merged_CompletePosttest.txt';
f = open(csvPath, 'rb')
counter = 0;
studentDict = {};

gradeableComponents = {"makingFractions_procedural": ["numline1"], 
                    "namingFractions_procedural": ["num1","den1","num2","den2"], 
                    "crossMultiplication_procedural": ["comparison_combobox_2"],
                    "ReducingFractions_conceptual": ["compBoxA","compBoxB","compBoxC","compBoxD"],
                    "transfer_equivalenceMultipleRepresentations": ["num1","den1","checkBox1","checkBox2","checkBox3","checkBox4","checkBox5","checkBox6"], 
                    "crossMultiplication_conceptual": ["compBoxA","compBoxB","compBoxC","compBoxD"], 
                    "estimatingFractions_procedural": ["numline1"], 
                    "comparingOrdering_conceptual": ["dropA", "dropD"],
                    "AddingFractions_procedural": ["numFinal","denFinal"], 
                    "ReducingFractions_procedural": ["numFinal","denFinal"], 
                    "transfer_findFractionBetweenTwoFractions": ["numFinal","denFinal"], 
                    "comparingOrdering_procedural": ["cj_1","cj_2","cj_3"], 
                    "transfer_integerMultiplicationOfFractions": ["numFinal","denFinal"], 
                    "addition_conceptual": ["dropA","dropC","dropD"], 
                    "naming_conceptual": ["dropA","dropB","dropC","dropD"], 
                    "transfer_relatePieceSizeToDenominator": ["compBox"] };


try:
    reader = csv.reader(f, delimiter='\t');
    for row in reader: 
        if counter > 0:     # skip first (header) row
            
            #assign values to relevant variables for each DataShop transaction
            problemName = row[14];
            problemSetName = row[13];
            studentID = row[3];
            thisSelection = row[20];
            thisAction = row[22];
            thisInput = row[24];
            attemptNum = row[0]; #row number in original data file
            if attemptNum == "": attemptNum = 1;
            
        
            if problemSetName == "Fractions Adaptive December Pretest" or problemSetName == "Fractions Adaptive December Posttest":
                if studentID not in studentDict:
                    #set default values for interface components within selected test items
                    studentDict[studentID] = {"makingFractions_procedural": {"Fractions Adaptive December Pretest": [], "Fractions Adaptive December Posttest": [] }, 
                    "namingFractions_procedural": {"Fractions Adaptive December Pretest": [], "Fractions Adaptive December Posttest": [] }, "crossMultiplication_procedural": {"Fractions Adaptive December Pretest": [], "Fractions Adaptive December Posttest": [] }, 
                    "ReducingFractions_conceptual": {"Fractions Adaptive December Pretest": [], "Fractions Adaptive December Posttest": [] }, 
                    "transfer_equivalenceMultipleRepresentations": {"Fractions Adaptive December Pretest": [ ["checkBox1",0,"default value",1], ["checkBox2",0,"default value",1], ["checkBox3",1,"default value",1], ["checkBox4",0,"default value",1], ["checkBox5",0,"default value",1], ["checkBox6",0,"default value",1] ], "Fractions Adaptive December Posttest": [ ["checkBox1",0,"default value",1], ["checkBox2",0,"default value",1], ["checkBox3",1,"default value",1], ["checkBox4",0,"default value",1], ["checkBox5",0,"default value",1], ["checkBox16",0,"default value",1] ] }, 
                    "crossMultiplication_conceptual": {"Fractions Adaptive December Pretest": [], "Fractions Adaptive December Posttest": [] }, "estimatingFractions_procedural": {"Fractions Adaptive December Pretest": [], "Fractions Adaptive December Posttest": [] }, 
                    "comparingOrdering_conceptual": {"Fractions Adaptive December Pretest": [], "Fractions Adaptive December Posttest": [] }, 
                    "AddingFractions_procedural": {"Fractions Adaptive December Pretest": [], "Fractions Adaptive December Posttest": [] }, "ReducingFractions_procedural": {"Fractions Adaptive December Pretest": [], "Fractions Adaptive December Posttest": [] }, 
                    "transfer_findFractionBetweenTwoFractions": {"Fractions Adaptive December Pretest": [], "Fractions Adaptive December Posttest": [] }, 
                    "comparingOrdering_procedural": {"Fractions Adaptive December Pretest": [ ["cj_1",0,"default value",1], ["cj_2",0,"default value",1], ["cj_3",1,"default value",1] ], "Fractions Adaptive December Posttest": [ ["cj_1",0,"default value",1], ["cj_2",0,"default value",1], ["cj_3",1,"default value",1] ] }, 
                    "transfer_integerMultiplicationOfFractions": {"Fractions Adaptive December Pretest": [], "Fractions Adaptive December Posttest": [] }, "addition_conceptual": {"Fractions Adaptive December Pretest": [], "Fractions Adaptive December Posttest": [] }, 
                    "naming_conceptual": {"Fractions Adaptive December Pretest": [], "Fractions Adaptive December Posttest": [] }, "transfer_relatePieceSizeToDenominator": {"Fractions Adaptive December Pretest": [], "Fractions Adaptive December Posttest": [] } };
                
                
                #update studentDict[studentID] with grades
                
                if problemName == "makingFractions_procedural":
                    if thisSelection=="numline1" and thisAction=="AddPoint":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='5/7'),thisInput,attemptNum]);
                    
                if problemName == "namingFractions_procedural":
                    if thisSelection=="num1" and thisAction=="UpdateTextField":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='3'),thisInput,attemptNum]);
                    if thisSelection=="den1" and thisAction=="UpdateTextField":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='7'),thisInput,attemptNum]);
                    if thisSelection=="num2" and thisAction=="UpdateTextField":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='4'),thisInput,attemptNum]);
                    if thisSelection=="den2" and thisAction=="UpdateTextField":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='7'),thisInput,attemptNum]);
                    
                if problemName == "crossMultiplication_procedural":
                    if thisSelection=="comparison_combobox_2" and thisAction=="UpdateComboBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='<'),thisInput,attemptNum]);
                    
                if problemName == "ReducingFractions_conceptual":
                    if thisSelection=="compBoxA" and thisAction=="UpdateComboBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='divide'),thisInput,attemptNum]);
                    if thisSelection=="compBoxB" and thisAction=="UpdateComboBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='common factor'),thisInput,attemptNum]);
                    if thisSelection=="compBoxC" and thisAction=="UpdateComboBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='common factors'),thisInput,attemptNum]);
                    if thisSelection=="compBoxD" and thisAction=="UpdateComboBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='one'),thisInput,attemptNum]);
                    
                if problemName == "transfer_equivalenceMultipleRepresentations":
                    if thisSelection=="num1" and thisAction=="UpdateTextField":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='1'),thisInput,attemptNum]);
                    if thisSelection=="den1" and thisAction=="UpdateTextField":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='4'),thisInput,attemptNum]);
                    if thisSelection=="checkBox1" and thisAction=="UpdateCheckBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='Equivalent?: true'),thisInput,attemptNum]);
                    if thisSelection=="checkBox2" and thisAction=="UpdateCheckBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='Equivalent?: true'),thisInput,attemptNum]);
                    if thisSelection=="checkBox3" and thisAction=="UpdateCheckBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='Equivalent?: false'),thisInput,attemptNum]);
                    if thisSelection=="checkBox4" and thisAction=="UpdateCheckBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='Equivalent?: true'),thisInput,attemptNum]);
                    if thisSelection=="checkBox5" and thisAction=="UpdateCheckBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='Equivalent?: true'),thisInput,attemptNum]);
                    if thisSelection=="checkBox6" and thisAction=="UpdateCheckBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='Equivalent?: true'),thisInput,attemptNum]);
                    
                if problemName == "crossMultiplication_conceptual":
                    if thisSelection=="compBoxA" and thisAction=="UpdateComboBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='numerators'),thisInput,attemptNum]);
                    if thisSelection=="compBoxB" and thisAction=="UpdateComboBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=="the original fractions' denominators"),thisInput,attemptNum]);
                    if thisSelection=="compBoxC" and thisAction=="UpdateComboBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='denominators'),thisInput,attemptNum]);
                    if thisSelection=="compBoxD" and thisAction=="UpdateComboBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='numerators'),thisInput,attemptNum]);
                    
                if problemName == "estimatingFractions_procedural":
                    if thisSelection=="numline1" and thisAction=="AddPoint":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(float(thisInput)<=0.7 and float(thisInput)>=0.5),thisInput,attemptNum]);
                                                
                if problemName == "comparingOrdering_conceptual":
                    if thisSelection=="dropA" and thisAction=="SetChildren":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='option4'),thisInput,attemptNum]);
                    if thisSelection=="dropD" and thisAction=="SetChildren":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='option3'),thisInput,attemptNum]);

                # note that not all equivalent sums are currently accepted as input
                if problemName == "AddingFractions_procedural":
                    if thisSelection=="numFinal" and thisAction=="UpdateTextField":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='19' or thisInput=='38'),thisInput,attemptNum]);
                    if thisSelection=="denFinal" and thisAction=="UpdateTextField":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='30' or thisInput=='60'),thisInput,attemptNum]);
                    
                if problemName == "ReducingFractions_procedural":
                    if thisSelection=="numFinal" and thisAction=="UpdateTextField":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='1'),thisInput,attemptNum]);
                    if thisSelection=="denFinal" and thisAction=="UpdateTextField":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='5'),thisInput,attemptNum]);
                    
                if problemName == "transfer_findFractionBetweenTwoFractions":
                    if thisSelection=="numFinal" and thisAction=="UpdateTextField":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,thisInput,thisInput,attemptNum]);                #need to grade these together, later
                    if thisSelection=="denFinal" and thisAction=="UpdateTextField":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,thisInput,thisInput,attemptNum]);
                    
                if problemName == "comparingOrdering_procedural":
                    if thisSelection=="cj_1" and thisAction=="SetOrder":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='frac1_3;frac1_2;frac1_1'),thisInput,attemptNum]);
                    if thisSelection=="cj_2" and thisAction=="SetOrder":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='frac2_3;frac2_1;frac2_2'),thisInput,attemptNum]);
                    if thisSelection=="cj_3" and thisAction=="SetOrder":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='frac3_1;frac3_2;frac3_3'),thisInput,attemptNum]);
                    
                if problemName == "transfer_integerMultiplicationOfFractions":
                    if thisSelection=="numFinal" and thisAction=="UpdateTextField":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,thisInput,thisInput,attemptNum]);               #need to grade these together, later
                    if thisSelection=="denFinal" and thisAction=="UpdateTextField":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,thisInput,thisInput,attemptNum]);
                                    
                if problemName == "addition_conceptual":
                    if thisSelection=="dropA" and thisAction=="SetChildren":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='option8'),thisInput,attemptNum]);
                    if thisSelection=="dropC" and thisAction=="SetChildren":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='option6'),thisInput,attemptNum]);
                    if thisSelection=="dropD" and thisAction=="SetChildren":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='option7'),thisInput,attemptNum]);
                                        
                if problemName == "naming_conceptual":
                    if thisSelection=="dropA" and thisAction=="SetChildren":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='option2'),thisInput,attemptNum]);
                    if thisSelection=="dropB" and thisAction=="SetChildren":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='option4'),thisInput,attemptNum]);
                    if thisSelection=="dropC" and thisAction=="SetChildren":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='option5'),thisInput,attemptNum]);
                    if thisSelection=="dropD" and thisAction=="SetChildren":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='option3'),thisInput,attemptNum]);
                                
                if problemName == "transfer_relatePieceSizeToDenominator":
                    if thisSelection=="compBox" and thisAction=="UpdateComboBox":
                        studentDict[studentID][problemName][problemSetName].append([thisSelection,int(thisInput=='Circle A shows the fraction with a larger denominator.'),thisInput,attemptNum]);


        counter = counter + 1;
        
finally:
    f.close();
    

    
#iterate over all students, problems, and test-types in studentDict, and for each:
#     replace the pre and post test lists with the grade on the max primary key value
for studID in studentDict.keys():
    for probName in studentDict[studID].keys():
        for testType in studentDict[studID][probName].keys():
            tempFinalResponse = [];
            for gradeComponent in gradeableComponents[probName]:
                tempSelInput = [];
                tempGreatest = 0;
        
                for transactionInstance in studentDict[studID][probName][testType]:                                                                               
                    if transactionInstance[0]==gradeComponent and int(transactionInstance[3])>tempGreatest:
                        tempSelInput = [transactionInstance[0],transactionInstance[1],transactionInstance[2]];
                        tempGreatest = int(transactionInstance[3]);
                #append temporary [selection,input] list to temporary final response list
                tempFinalResponse.append(tempSelInput);
                
            #grade "transfer_findFractionBetweenTwoFractions"
            if probName == "transfer_findFractionBetweenTwoFractions" and tempFinalResponse[0]:
                if not(tempFinalResponse[0][1].isdigit() and tempFinalResponse[1][1].isdigit()):
                    tempFinalResponse[0][1] = 0;
                    tempFinalResponse[1][1] = 0;
                else:
                    if float(tempFinalResponse[1][1]) != 0:
                        frac1 = (float(tempFinalResponse[0][1])/float(tempFinalResponse[1][1]));
                        tempFinalResponse[0][1] = int( frac1>=0.258714 and frac1<=0.6  );
                    else:
                        tempFinalResponse[0][1] = 0;
                    tempFinalResponse[1][1] = tempFinalResponse[0][1];
            #grade transfer multiplication question
            if probName == "transfer_integerMultiplicationOfFractions" and tempFinalResponse[0]: 
                #statements below are structured to prevent type errors   
                if not(tempFinalResponse[0][1].isdigit() and tempFinalResponse[1][1].isdigit()):
                    tempFinalResponse[0][1] = 0;
                    tempFinalResponse[1][1] = 0;
                elif tempFinalResponse[0][1]=="6" and tempFinalResponse[1][1]=="11":
                    tempFinalResponse[0][1] = 1;
                    tempFinalResponse[1][1] = 1;
                else:
                    tempFinalResponse[0][1] = 0;
                    tempFinalResponse[1][1] = 0;

                                
            tempFinalResponse = list(itertools.chain(*tempFinalResponse));
            studentDict[studID][probName][testType] = [studID] + [testType] + [probName] + tempFinalResponse;
            
            #write to output file in append mode
            outFile = open('Desktop/January_Data/January_Data_Cleaned_Graded.csv', 'a')
            wr = csv.writer(outFile, quoting=csv.QUOTE_NONNUMERIC)
            wr.writerow(studentDict[studID][probName][testType]);
            
