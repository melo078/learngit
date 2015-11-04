ss=read.table("D:\\di105.txt",header=T)
ss=ss[,-1]
s=dist(ss,method='euclidean')
model1=hclust(s,method='ward.D')
result=cutree(model1,k=20)
mds=cmdscale(s,k=2,eig=T)
x = mds$points[,1]
y = mds$points[,2]
library(ggplot2)
p=ggplot(data.frame(x,y),aes(x,y,label = colnames(ss[1])))
p+geom_point(size=2,alpha=1,aes(colour=factor(result)))


