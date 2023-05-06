
import matplotlib.pyplot as pl
import matplotlib.style as style
import numpy as np

pl.scatter([1,2,3],[4,5,5])
pl.title("graph")
pl.ylabel("yaxis")
pl.xlabel("xaxis")
style.use("ggplot")
pl.legend()
pl.show 

x=np.arange(0.,10,0.1)
a=np.sin(x)
b=np.cos(x)
pl.plot(x,a,'b') #can add line color
pl.plot(x,b,'r')
pl.show

a1=['delhi','pune','mumbai','hyderabad']
b1=[237647,983698,564776,799785]
pl.bar(a1,b1,0.5,color=['green','red','k','m'])
pl.xlabel('cities')
pl.ylabel('population')
pl.show()
#can use .barh for horizontal graph

b2=[20,40,35,5]
houses=['h,','j','k','l']
pl.pie(b2,labels=houses,autopct="%1.1f%%")
pl.show()

a3=[24,26,32,16]
lab=['jay','janvi','sarita','sid'] #names of each part
color=['r','c','g','b'] #color of each part
expl=[0.2,0,0,0] #to make emphasis on part individually
pl.axis("equal") 
pl.pie(a3,labels=lab,explode=expl,colors=color,autopct="%1.1f%%")
pl.show()

val=[[5.,25.,45.,20.],[4.,23.,49.,17.],[6.,22.,47.,19.]]
x=np.arange(4)
pl.bar(x+0.00,val[0],color='b',width=0.25,label='range1')
pl.bar(x+0.25,val[1],color='g',width=0.25,label='range2')
pl.bar(x+0.50,val[2],color='r',width=0.25,label='range3')
pl.legend(loc='upper right')
pl.title("Multirange bar chart")
pl.xlabel=('X')
pl.ylabel=('Y')
pl.show()

