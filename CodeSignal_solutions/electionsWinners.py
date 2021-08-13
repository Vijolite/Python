#Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.
#The winner of the election must secure strictly more votes than any other candidate. If two or more candidates receive the same (maximum) number of votes, assume there is no winner at all.

def electionsWinners(votes, k):
    for i in range(len(votes)):
        if i==0:
            m=votes[i]
            m_nr=1
        else:
            if votes[i]==m:
                m_nr+=1
            elif votes[i]>m:
                m=votes[i]
                m_nr=1
    c=0
    if k==0:
        if m_nr==1:
            c=1
        else:
            c=0
    else:
        for i in range(len(votes)):
            if votes[i]+k>m:
                c+=1
    return c
