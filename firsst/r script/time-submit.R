library(dygraphs)
dygraph(who, main = "times") %>% dyRangeSelector(dateWindow = c("1997-01-01", "2015-01-01"))

