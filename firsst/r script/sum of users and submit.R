library(RODBC)
channel=odbcConnect("mysqlodbc", uid="root", pwd="")
user_submit=sqlFetch(channel,"user_submit111")
library(metricsgraphics)
library(RColorBrewer)
user_submit%>%
mjs_plot(x=number, y=num, width=600, height=500) %>%
mjs_point(color_accessor=carb) %>%
mjs_labs(x="sum of submit", y="times")