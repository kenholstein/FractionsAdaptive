import csv

csvPath = 'AllTutors/FractionsAdaptive/FractionsAdaptiveDecember 2014/prereqV5.2.3_pset1.csv';
csvPath2 = 'AllTutors/FractionsAdaptive/FractionsAdaptiveDecember 2014/prereqV5.2.3_pset2.csv';

f = open(csvPath, 'rb')
largePool = open(csvPath2, 'rb')
allProblemNames_part1 = [];
allProblemNames_part2 = [];

selection_algorithm='prerequisites';

counter = 0;

#note: writing to file in append mode
with open("AllTutors/FractionsAdaptive/FractionsAdaptiveDecember 2014/package.xml", "a") as text_file:
    text_file.write('<?xml version="1.0" encoding="UTF-8"?>');
    text_file.write('\n <Package name="Fractions_Adaptive_December2014" label="Fractions_Adaptive" description="Fractions_Adaptive">');
    text_file.write('\n \t <Problems>');
    try:
        reader = csv.reader(f, delimiter=',');
        for row in reader: 
            if counter > 0:     # skip first (header) row
                    num_duplicates = int(row[4]);
                    
                    #string cleaning for prerequisite structure
                    problemNodeName = "".join(str(row[2]).split());
                    problemLevelSkill = "".join(str(row[1]).split());
                    problemParentList = str(row[3]).replace(";", ",");
                    problemParentList = "".join(problemParentList.split());
                    swfFileName = "".join(str(row[5]).split());
                    brdFileName = "".join(str(row[6]).split());
                            
                    if num_duplicates > 1:
                        for i in range(1,num_duplicates+1):
                            problemName = str(row[0]) + "_duplicate" + str(i);
                            allProblemNames_part1.append(problemName);
                            
                            text_file.write('\n \t \t <Problem name="' + problemName + '" label="' + problemLevelSkill + '" selection_features="' + problemParentList + '" description="' + problemNodeName + '" problem_file="' + brdFileName + '" student_interface="' + swfFileName + '" tutor_flag="tutor"></Problem>' );
                    else:
                        problemName = str(row[0]);
                        allProblemNames_part1.append(problemName);
                        text_file.write('\n \t \t <Problem name="' + problemName + '" label="' + problemLevelSkill + '" selection_features="' + problemParentList + '" description="' + problemNodeName + '" problem_file="' + brdFileName + '" student_interface="' + swfFileName + '" tutor_flag="tutor"></Problem>' );
                        
            counter = counter + 1;
        
    finally:
        f.close();

        
    #full-randomization phase (problem set 2)
    counter=0;
    try:
        reader2 = csv.reader(largePool, delimiter=',');
        for row in reader2: 
            if counter > 0:     # skip first (header) row
                    num_duplicates = int(row[4]);
                    
                    #string cleaning for prerequisite structure
                    problemNodeName = "".join(str(row[2]).split());
                    problemLevelSkill = "".join(str(row[1]).split());
                    problemParentList = str(row[3]).replace(";", ",");
                    problemParentList = "".join(problemParentList.split());
                    swfFileName = "".join(str(row[5]).split());
                    brdFileName = "".join(str(row[6]).split());

                    if num_duplicates > 1:
                        for i in range(1,num_duplicates+1):
                            problemName = str(row[0]) + "_duplicate" + str(i);
                            allProblemNames_part2.append(problemName);
                            
                            text_file.write('\n \t \t <Problem name="' + problemName + '" label="' + problemLevelSkill + '" selection_features="' + problemParentList + '" description="' + problemNodeName + '" problem_file="' + brdFileName + '" student_interface="' + swfFileName + '" tutor_flag="tutor"></Problem>' );
                    else:
                        problemName = str(row[0]);
                        allProblemNames_part2.append(problemName);
                        text_file.write('\n \t \t <Problem name="' + problemName + '" label="' + problemLevelSkill + '" selection_features="' + problemParentList + '" description="' + problemNodeName + '" problem_file="' + brdFileName + '" student_interface="' + swfFileName + '" tutor_flag="tutor"></Problem>' );
                        
            counter = counter + 1;
        
    finally:
        largePool.close();


    text_file.write('\n \t </Problems>');
    text_file.write('\n \t <ProblemSets>');
    
    text_file.write('\n \t \t <ProblemSet name="Fractions_Adaptive December2014 Part1" label="Fractions Tutor: Part 1" description="Fractions_Adaptive" selection_algorithm="' + selection_algorithm + '" max_count="1000" max_repeat="1" initial_sequence="0">');
    text_file.write('\n \t \t \t <Problems>');
    for probName in allProblemNames_part1:
        text_file.write('\n \t \t \t \t <Problem name="' + probName + '"/>');    
    text_file.write('\n \t \t \t </Problems>');
    text_file.write('\n \t \t <Skills></Skills><Categories></Categories></ProblemSet>');

    text_file.write('\n \t \t <ProblemSet name="Fractions_Adaptive December2014 Part2" label="Fractions Tutor: Part 2" description="Fractions_Adaptive" selection_algorithm="' + selection_algorithm + '" max_count="1000" max_repeat="1" initial_sequence="0">');
    text_file.write('\n \t \t \t <Problems>');
    for probName in allProblemNames_part2:
        text_file.write('\n \t \t \t \t <Problem name="' + probName + '"/>');    
    text_file.write('\n \t \t \t </Problems>');
    text_file.write('\n \t \t <Skills></Skills><Categories></Categories></ProblemSet>');    
    
    text_file.write('</ProblemSets><Assets></Assets>');
    text_file.write('\n </Package>');