library(RODBC)
channel=odbcConnect("mysqlodbc", uid="root", pwd="")
time_submit=sqlFetch(channel,"user_submit_times")
library(htmltools)
library(htmlwidgets)
library(metricsgraphics)
library(RColorBrewer)
time_submit2 %>%
mjs_plot(x=times, y=who, width=500, height=400) %>%
mjs_bar() %>%
mjs_axis_x(xax_format = 'plain')