library(RODBC)
channel=odbcConnect("mysqlodbc", uid="root", pwd="")
won1=sqlFetch(channel,"wontfix4")
library(zoo)
library(xts)
qq.data<-as.POSIXct(won1$when)
qqq<-xts(won1[,2],qqq.data)
library(dygraphs)
dygraph(ss, main = "times") %>% dyRangeSelector(dateWindow = c("2000-10-01", "2015-01-01"))