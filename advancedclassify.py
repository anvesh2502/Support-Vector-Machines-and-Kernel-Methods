from pylab import *

class matchrow :

    def __init__(self,row,allnum=False) :

       if allnum :
           self.data=[float(row[i]) for i in range(len(row)-1)]
       else :
           self.data=row[0:len(row)-1]
       self.match=int(row[len(row)-1])

def loadmatch(f,allnum=False) :

        rows=[]
        for line in file(f) :
            rows.append(matchrow(line.split(','),allnum))
        return rows

def lineartrain(rows) :

    averages={}
    counts={}

    for row in rows :
        # Get the class of this point
        cl=row.match

        averages.setdefault(cl,[0.0]*(len(row.data)))
        counts.setdefault(cl,0)

        # Add this point to the averages
        for i in range(len(row.data)) :
            averages[cl][i]+=float(row.data[i])

        counts[cl]+=1

    # Divide sums by counts to get the averages
    for cl,avg in averages.items() :
        for i in range(len(avg)) :
            avg[i]/=counts[cl]

    return averages

def dotproduct(v1,v2) :

    return sum([v1[i]*v2[i] for i in range(len(v1))])


# Method to determine the class

     # class=sign((X-(M1+M2)/2).(M0-M1))



def dpclassify(point,avgs) :

    b=(dotproduct(avgs[1],avgs[1])-dotproduct(avgs[0],avgs[0]))/2
    y=dotproduct(point,avgs[0])-dotproduct(point,avgs[1])+b

    if y>0 : return 0
    return 1


def yesno(v) :

    if v=='yes' : return 1
    elif v=='no' : return -1
    return 0

def matchcount(interest1,interest2) :

    l1=interest1.split(':')
    l2=interest2.split(':')
    x=0
    for v in l1 :
        if v in l2 : x+=1
    return x



def milesdistance(a1,a2) :
    return 0        





def plotagematches(rows) :

    xdm,ydm=[r.data[0] for r in rows if r.match==1],[r.data[1] for r in rows if r.match==1]
    xdn,ydn=[r.data[0] for r in rows if r.match==0],[r.data[1] for r in rows if r.match==0]

    plot(xdm,ydm,'go')
    plot(xdn,ydn,'ro')

    show()
