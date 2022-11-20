#### contains a single line ####
line = list() 
Ele = list()

##### contains all the tks #####
tks = dict() 
number = -1
fhand = open('/home/kawsar/Desktop/Class_Resource/4th year 1st semester/4131-Computer Simulation and Modeling/Computer Simulation Lab/Lab3_Critical_Path_method/input.txt')

#### slide the file line by line ####
for line in fhand: 
    Ele=(line.split(',')) 
    number += 1
    # print(Ele)
    
	#### creating the single task element ####
    for i in range(len(Ele)):
        tks[str(Ele[0])]= dict()
        tks[str(Ele[0])]['Activity'] = Ele[0]
        tks[str(Ele[0])]['Duration'] = Ele[1]
        Ele[-1]=Ele[-1].split('\n')[0];
        
        tks[str(Ele[0])]['Predecessor'] = Ele[2:]
        tks[str(Ele[0])]['ES'] = 0
        tks[str(Ele[0])]['EF'] = 0
        tks[str(Ele[0])]['LS'] = 0
        tks[str(Ele[0])]['LF'] = 0
        tks[str(Ele[0])]['ST'] = 0
        tks[str(Ele[0])]['isCritical'] = False
        
# for task in tks:
#     print(tks[task])
    

# =============================================================================
# FORWARD PASS
# =============================================================================

#### Slides all the tks ####
for taskFW in tks: 
    #### checks if it's the first task ####
    if('-' in tks[taskFW]['Predecessor']): 
        tks[taskFW]['ES'] = 0
        tks[taskFW]['EF'] = (tks[taskFW]['Duration'])
    else: #### not the first task ####
        for k in tks.keys():
            #### slides all the dependency in a single task ####
            for dep in tks[k]['Predecessor']: 
                #### if the task k has only one dependency ####
                if(dep != '-' and len(tks[k]['Predecessor']) == 1): 
                    tks[k]['ES'] = int(tks[dep]['EF']) 
                    tks[k]['EF'] = int(tks[k]['ES']) + int(tks[k]['Duration']) 
                elif(dep !='-'):
                #### put the maximum value of ES for the depend of a task ####
                    if(int(tks[dep]['EF']) > int(tks[k]['ES'])):
                        tks[k]['ES'] = int(tks[ dep]['EF']) 
                        tks[k]['EF'] = int(tks[k]['ES']) + int(tks[k]['Duration']) 
        
aList = list() #list of task keys
for element in tks.keys():
    aList.append(element)

bList = list() #reversed list of task keys
while len(aList) > 0:
    bList.append(aList.pop())
# print(bList)


# =============================================================================
# BACKWARD PASS
# =============================================================================
for taskBW in bList:
    #### check if it's the last task ####
    if(bList.index(taskBW) == 0):  
        tks[taskBW]['LF']=tks[taskBW]['EF']
        tks[taskBW]['LS']=tks[taskBW]['ES']
        
    for dep in tks[taskBW]['Predecessor']: #slides all the dependency in a single task
        #### check if it's NOT the last task ####
        if(dep != '-'): 
            #### check if the the dependency is already analyzed ####
            if(tks[dep]['LF'] == 0): 
                tks[dep]['LF'] = int(tks[taskBW]['LS']) 
                tks[dep]['LS'] = int(tks[dep]['LF']) - int(tks[dep]['Duration']) 
                tks[dep]['ST'] = int(tks[dep]['LF']) - int(tks[dep]['EF'])
            #### put the minimun value of LF for the depend of a task ####
            if(int(tks[dep]['LF']) > int(tks[taskBW]['LS']) ): 
                tks[dep]['LF'] = int(tks[taskBW]['LS']) 
                tks[dep]['LS'] = int(tks[dep]['LF']) - int(tks[dep]['Duration']) 
                tks[dep]['ST'] = int(tks[dep]['LF']) - int(tks[dep]['EF'])


             
# =============================================================================
# PRINTING  
# =============================================================================
print('Acitivity, Duration, ES, EF, LS, LF, ST, isCritical')
for task in tks:
    if(tks[task]['ST'] == 0):
        tks[task]['isCritical'] = True
    print(str(tks[task]['Activity']) +', '\
			+str(tks[task]['Duration']) +', '+str(tks[task]['ES']) +', '\
			+str(tks[task]['EF']) +', '+str(tks[task]['LS']) +', '+\
			str(tks[task]['LF']) +', '+str(tks[task]['ST']) +', '+\
			str(tks[task]['isCritical']))
