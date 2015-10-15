library(RODBC)
channel=odbcConnect("mysqlodbc", uid="root", pwd="")
no2_time_submit=sqlFetch(channel,"no1b")
library(zoo)
library(xts)
ss.data<-as.POSIXct(no2_time_submit$when)
ss<-xts(no2_time_submit[1,],ss.data)
dygraph(ss, main = "times") %>% dyRangeSelector(dateWindow = c("2000-10-01", "2015-01-01"))

