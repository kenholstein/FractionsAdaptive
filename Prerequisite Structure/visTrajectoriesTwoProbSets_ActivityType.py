import csv
from random import randrange
from matplotlib.pylab import *
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import copy
import sys

#csvPath = 'AllTutors/FractionsAdaptive/FractionsAdaptiveNovember2014/prereqUrbanPathways.csv';
csvPath = 'Desktop/December_Data/prereqV5.2.3_pset1.csv';
csvPath2 = 'Desktop/December_Data/prereqV5.2.3_pset2.csv';

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
            problem_j_Name = problem_j_Name.split('_')[1];
            episodeTrajectory.append(problem_j_Name);


        
                
                        
                                
                                        
                                                
                                                        
                                                                
                                                                                
    #replace problem_type names with numeric labels in output matrix
    for z in range(0,len(episodeTrajectory)):
        if "".join(episodeTrajectory[z].split()) == 'SM':
            trajectoryMatrix[z,v] = 1;
        elif "".join(episodeTrajectory[z].split()) == 'IR':
            trajectoryMatrix[z,v] = 2;
        elif "".join(episodeTrajectory[z].split()) == 'fluency':
            trajectoryMatrix[z,v] = 3;
                    
   # for m in range(0,len(episodeTrajectory)):
    #    if trajectoryMatrix[m,v] == 0:
     #       print "".join(episodeTrajectory[m].split()) == 'IR' or "".join(episodeTrajectory[z].split()) == 'SM' or "".join(episodeTrajectory[z].split()) == 'fluency';
      #      print "".join(episodeTrajectory[m].split());
            


# make a color map of fixed colors
cmap = colors.ListedColormap(['magenta', 'yellow','green',])
bounds=[0.5,1.5,2.5,3.5]
norm = colors.BoundaryNorm(bounds, cmap.N)

# tell imshow about color map so that only set colors are used
img = plt.imshow(trajectoryMatrix, interpolation='nearest', origin='lower',
                    cmap=cmap, norm=norm)

# make a color bar
cbar = plt.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=[1, 2, 3])

cbar.set_ticklabels(["SM","IR","F"]);

#plt.savefig('redwhite.png')

plt.show()

sum_SM = 0.0;
sum_IR = 0.0;
sum_F = 0.0;
for t in range(0,numTrajectories):
    sum_SM += list(trajectoryMatrix[:,t]).count(1);
    sum_IR += list(trajectoryMatrix[:,t]).count(2);
    sum_F += list(trajectoryMatrix[:,t]).count(3);
    
avg_SM = sum_SM/numTrajectories;
avg_IR = sum_IR/numTrajectories;
avg_F = sum_F/numTrajectories;

print "avg_SM: " + str(avg_SM) + "\n" + "avg_IR: " + str(avg_IR) + "\n" + "avg_F: "+ str(avg_F);