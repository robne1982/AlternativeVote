import csv

# Setup
strPath = r'C:\avcode\final.csv'

#############################################################################################################
# functions
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False



def round_of_av(lstScores, intRound):
    # Track votes in here
    intVotetracker = []

    print '============================================================================================'
    print ' ROUND ' + str(intRound)

    print ' --------------------------------'
    
    # loop over all rows, which are candidates
    for i in range(0,len(lstScores)):
        # loop over the contents of the row, counting votes of 1
        intWincount = 0
        for j in range(0,len(lstScores[i-1])):
            # score 1's
            if str(lstScores[i][j]).strip() == '1':
                intWincount+=1
        # track this candidates score
        intVotetracker.append(intWincount)

    print "The votes are "
    for i in range(0 , len(intVotetracker)):
        print lstScores[i][0] + " : " + str(intVotetracker[i])

    print ' --------------------------------'    
    
    # Wrok out what to remove...
    intMinValue = min(intVotetracker)
    intRemovals = []
    for i in range(0,len(intVotetracker)):
        if (intVotetracker[i]==intMinValue):
            # these are the candidates to remove...
            intRemovals.append(i)

    print "Therefore there are " + str(len(intRemovals)) + " removals"

    if len(intRemovals) == len(lstScores):
        print ' Dead heat'
        
        quit()
        
    # Do the deleting....
    for offset, index in enumerate(intRemovals):
      index -= offset
      print lstScores[index][0]
      del lstScores[index]
      
    print ' --------------------------------'
  
    # Do the reordering of votes
    # Loop over the columns
    #print len(lstScores[0])
    for i in range(1,len(lstScores[0])-1):
        # and now through rows for that columns...
        #print len(lstScores)-1

        # Loop over the voters choices and find the lowest
        # we only need set that one to 1 - the other numbers don't matter
        intVoterMinimum = 999
        #print len(lstScores)-1
        for j in range(0,len(lstScores)):
            if is_int(lstScores[j][i]):
                #print int(lstScores[j][i])
                if int(lstScores[j][i]) < intVoterMinimum:
                    #print  'temp = ' + str((lstScores[j][i]))
                    intVoterMinimum = int(lstScores[j][i])

        #print intVoterMinimum
        
        # loop again and set it to 1 - realise this could be faster!
        for j in range(0,len(lstScores)):
            if is_int(lstScores[j][i]):
                if int(lstScores[j][i]) == intVoterMinimum:
                    #print 'switch ' + str(lstScores[j][i])
                    lstScores[j][i] = 1
                    break

    print "The new vote list is as follows"
    for row in lstScores:
        print row

    print ' --------------------------------'  

    return lstScores


##############################################################################

###### MAIN ###########
    
# Read the data
with open(strPath) as fileCsv:
    objReader = csv.reader(fileCsv, delimiter=',')
    i=1
    lstScores = list()
    for row in objReader:
        if(i==1):
            lstNames = row
            i+=1
        else:
            lstScores.append(row)
            i+=1

# Write some info about the starting position

print '============================================================================================'
print 'Before round 1 there are ' + str(len(lstScores)) + ' candidates '
print ' and we have ' + str(len(lstNames)-1) + ' goats voting'
print '============================================================================================'

# Call a round of AV...
intRound = 1
intLastCount = 9999999
while len(lstScores) > 1:
    lstScores = round_of_av(lstScores,intRound)
    intRound+=1
    if (len(lstScores) ==intLastCount):
        print ' Dead heat'
    intLastCount = len(lstScores)
    if(len(lstScores)==1):
        print '============================================================================================'
        print ' The winner is declared : ' + str(lstScores[0][0])
        print '============================================================================================'

