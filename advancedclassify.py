from pylab import *
import json
import urllib2

google_api_key="AIzaSyDLyGWie8q3Reltbcz8VM1LsDyx3AvaL8M"
google_maps_url="https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}"


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
    lat1,long1=getlocation(a1)
    lat2,long2=getlocation(a2)
    latdiff=69.1*(lat2-lat1)
    longdiff=53.0*(long2-long1)
    return (latdiff**2+longdif**2)**0.5



loc_cache={}

def getlocation(address) :

    l=[]

    for c in address :
        if c==' ':
            l.append('+')
        else :
            l.append(c)

    address=''.join(l)



    if address in loc_cache : return loc_cache[address]

    try :
        json_data=urllib2.urlopen(google_maps_url.format(address,google_api_key)).read()
    except :
        print google_maps_url.format(address,google_api_key)

        return


    try :
     lat_long=json.loads(json_data)['results'][0]['geometry']['location']
    except  :
        print 'Error fetching map data'
        return
    loc_cache[address]=(float(lat_long['lat']),float(lat_long['lng']))
    return loc_cache[address]






def plotagematches(rows) :

    xdm,ydm=[r.data[0] for r in rows if r.match==1],[r.data[1] for r in rows if r.match==1]
    xdn,ydn=[r.data[0] for r in rows if r.match==0],[r.data[1] for r in rows if r.match==0]

    plot(xdm,ydm,'go')
    plot(xdn,ydn,'ro')

    show()
