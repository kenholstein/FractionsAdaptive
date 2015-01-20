import csv
from random import randrange
from matplotlib.pylab import *
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import copy

#csvPath = 'AllTutors/FractionsAdaptive/FractionsAdaptiveNovember2014/prereqUrbanPathways.csv';
csvPath ='Desktop/prereqV5.2.3_pset1.csv';
csvPath2 = 'Desktop/prereqV5.2.3_pset2.csv';

f = open(csvPath, 'rb')
largePool = open(csvPath2, 'rb')
counter = 0;    

trajectoryLength = 60;
numTrajectories = 100;

selectionPool = [];
selectionPool2 = [];

#initial pool of problems
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
                            
                for i in range(1,num_duplicates+1):
                    problemName = str(row[0]) + "_duplicate" + str(i);
                    selectionPool.append([problemName,problemNodeName,problemParentList,brdFileName]);  
                    
                                            
        counter = counter + 1;
        
finally:
    f.close();

counter=0;   
#large pool of problems  
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
                            
                for i in range(1,num_duplicates+1):
                    problemName = str(row[0]) + "_duplicate" + str(i);
                    selectionPool2.append([problemName,problemNodeName,problemParentList,brdFileName]);  
                    
                                            
        counter = counter + 1;
        
finally:
    largePool.close();
    
counter = 0;
#simulation of numTrajectories trajectories, each of length trajectoryLength
trajectoryMatrix = zeros((trajectoryLength,numTrajectories));
for v in range(0,numTrajectories):
    #generate single-episode trajectory

    brdNameHistory = [];
    prereqSatisfiedHistory = [];
    episodeSelectionPool = copy.deepcopy(selectionPool);
    validSelectionPool = [];
    episodeTrajectory = [];
    
    for j in range(0,trajectoryLength+1):  #plus 1 since we do not add to episode trajectory when switching between problem sets
        
        if validSelectionPool == [] and j>0:
            episodeSelectionPool = copy.deepcopy(selectionPool2);

        #update validSelectionPool based on prerequisite and problem-duplicate history
        for prob in list(validSelectionPool):
            if prob[3] in brdNameHistory:
                validSelectionPool.remove(prob);
        for problem in list(episodeSelectionPool):
            if ((set(problem[2].split(',')).issubset(prereqSatisfiedHistory) ) or (problem[2]=='')):
                validSelectionPool.append(problem);
                episodeSelectionPool.remove(problem); 

        if validSelectionPool != []:
           #randomly select problem from current selection pool
            problem_j_index = randrange(0,len(validSelectionPool));
            problem_j = validSelectionPool[problem_j_index];
            brdNameHistory.append(problem_j[3]);
            prereqSatisfiedHistory.append(problem_j[1]);
    
            #extract activity type and add to episode trajectory
            problem_j_Name = problem_j[0];
            problem_j_Name = problem_j_Name.split('_')[0];
            episodeTrajectory.append(problem_j_Name);
            
            
            
            
            

            
    #replace problem_type names with numeric labels in output matrix
    for z in range(0,len(episodeTrajectory)):
        if episodeTrajectory[z] == 'makingFractionsNL' or episodeTrajectory[z] == 'numberLine' or episodeTrajectory[z] == 'naming' or episodeTrajectory[z] == 'estimatingFractionsNL' or episodeTrajectory[z] == 'estimatingFractions' or episodeTrajectory[z] == 'namingFractionsNL':
            trajectoryMatrix[z,v] = 1;
        if episodeTrajectory[z] == 'orderingFractionsNL' or episodeTrajectory[z] == 'equivalentFractionsNL' or  episodeTrajectory[z] == 'comparisonDrill':
            trajectoryMatrix[z,v] = 2;
        if episodeTrajectory[z] == 'crossMultiplicationUnscaffolded' or episodeTrajectory[z] == 'crossMultiplicationScaffolded' or episodeTrajectory[z] == 'crossMultiplication':
            trajectoryMatrix[z,v] = 3;
        if episodeTrajectory[z] == 'fractionReduction' or episodeTrajectory[z] == 'reducingFractions':
            trajectoryMatrix[z,v] = 4;
        if episodeTrajectory[z] == 'commonDenominator':
            trajectoryMatrix[z,v] = 5;
        if episodeTrajectory[z] == 'addition':
            trajectoryMatrix[z,v] = 6;
 
    for q in range(0,len(episodeTrajectory)):
        if trajectoryMatrix[q,v] == 0:  print episodeTrajectory[q];
 

# custom cmap and bounds
cmap = colors.ListedColormap(['cyan', 'magenta', 'blue', 'yellow', 'black', 'red'])
bounds=[0.5,1.5,2.5,3.5,4.5,5.5,6.5]
norm = colors.BoundaryNorm(bounds, cmap.N)

# imshow set params and custom cmap
img = plt.imshow(trajectoryMatrix, interpolation='nearest', origin='lower',
                    cmap=cmap, norm=norm)

# color bar def'n
cbar = plt.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=[1, 2, 3, 4, 5, 6])

cbar.set_ticklabels(["Naming, Making, Estimating on NL","Ordering and Equivalence","Cross Multiplication","Reducing Fractions","Common Denominators","Addition"]);

plt.show()



sum_MakingNamingEstimating = 0.0;
sum_OrderingEquivalence = 0.0;
sum_CrossMultiplication = 0.0;
sum_FractionReduction = 0.0;
sum_CommonDenominator = 0.0;
sum_Addition = 0.0;
for t in range(0,numTrajectories):
    sum_MakingNamingEstimating += list(trajectoryMatrix[:,t]).count(1);
    sum_OrderingEquivalence += list(trajectoryMatrix[:,t]).count(2);
    sum_CrossMultiplication += list(trajectoryMatrix[:,t]).count(3);
    sum_FractionReduction += list(trajectoryMatrix[:,t]).count(4);
    sum_CommonDenominator += list(trajectoryMatrix[:,t]).count(5);
    sum_Addition += list(trajectoryMatrix[:,t]).count(6);
    
avg_MakingNamingEstimating = sum_MakingNamingEstimating/numTrajectories;
avg_OrderingEquivalence = sum_OrderingEquivalence/numTrajectories;
avg_CrossMultiplication = sum_CrossMultiplication/numTrajectories;
avg_FractionReduction = sum_FractionReduction/numTrajectories;
avg_CommonDenominator = sum_CommonDenominator/numTrajectories;
avg_Addition = sum_Addition/numTrajectories;

print "avg_MakingNamingEstimating: " + str(avg_MakingNamingEstimating) + "avg_OrderingEquivalence" + "\n" + str(avg_OrderingEquivalence) + "\n" + "avg_CrossMultiplication: " + str(avg_CrossMultiplication) + "\n" + "avg_FractionReduction: "+ str(avg_FractionReduction) + "\n" + "avg_CommonDenominator: " + str(avg_CommonDenominator) + "\n" + "avg_Addition: "+ str(avg_Addition);