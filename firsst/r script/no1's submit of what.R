library(RODBC)
channel=odbcConnect("mysqlodbc", uid="root", pwd="")
no100=sqlFetch(channel,"n1what100")
library(metricsgraphics)
library(RColorBrewer)
no100 %>%
  mjs_plot(x=num, y=what, width=2000, height=2000) %>%
  mjs_bar() %>%
  mjs_axis_x(xax_format = 'plain')

