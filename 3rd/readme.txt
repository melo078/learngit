利用之前做的统计结果（提交量前2万人的提交次数，status，cc,resolution三项数据所占百分比），使用r画图，
主要用到dist()求出欧式距离，再利用cmdscale(),hclust()分出簇，最后用qqplot2库画出散点图。