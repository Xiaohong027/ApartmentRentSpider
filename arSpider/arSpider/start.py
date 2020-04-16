from scrapy.cmdline import execute

# 爬取58同城数据,已完成
#execute(['scrapy', 'crawl', 'Spider_58tc'])

# 爬取我爱我家数据，已完成
#execute(['scrapy', 'crawl', 'Spider_5i5j'])

# 爬取58同城数据，已完成
# 勿忘记修改setting中的useragent为移动端
# 停用时注意修改setting中的useragent
#execute(['scrapy', 'crawl', 'Spider_58tc_mobile'])

# 爬取107房数据，已完成
# 注意打开管道中的经纬度字段
# 结束时关闭经纬度字段
# execute(['scrapy', 'crawl', 'Spider_107room'])

# 爬取房天下数据,已完成
# execute(['scrapy', 'crawl', 'Spider_fangtianxia'])

# 爬取列表网数据,已完成
# execute(['scrapy', 'crawl', 'Spider_liebiaowang'])

# 爬取安居客数据
execute(['scrapy', 'crawl', 'Spider_anjuke'])