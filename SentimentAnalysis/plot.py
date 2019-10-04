from pyecharts.charts import Line, Timeline
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import xlrd
import time

#比较时间先后
def compare_time(t1, t2):
    time1 = time.mktime(time.strptime(t1,"%Y-%m-%d %H:%M:%S")) 
    time2 = time.mktime(time.strptime(t2,"%Y-%m-%d %H:%M:%S"))
    if time1 >= time2:
    	return True
    return False

#导入数据
def read_xlsx(filename):
	data = xlrd.open_workbook(filename, encoding_override = 'utf-8')
	table = data.sheets()[0]
	nrows = table.nrows
	Time_List = [table.cell_value(rows,0) for rows in range(0,nrows)]
	Score_List = [table.cell_value(rows,1) for rows in range(0,nrows)]
	Comment_List = [table.cell_value(rows,2) for rows in range(0,nrows)]
	#app版本信息七麦数据无法直接导出，此处手动录入
	Update_List = ['2019-09-29 00:00:00', '2019-09-15 00:00:00', '2019-09-07 00:00:00', '2019-08-26 00:00:00', '2019-08-12 00:00:00', '2019-07-02 00:00:00', '2019-06-19 00:00:00', '2019-06-06 00:00:00', '2019-06-03 00:00:00', '2019-05-31 00:00:00', '2019-04-22 00:00:00', '2019-03-20 00:00:00', '2019-03-08 00:00:00', '2019-01-31 00:00:00', '2019-01-02 00:00:00', '2018-12-14 00:00:00', '2018-11-21 00:00:00', '2018-11-03 00:00:00', '2018-11-01 00:00:00', '2018-10-15 00:00:00', '2018-09-23 00:00:00', '2018-09-12 00:00:00', '2018-08-06 00:00:00', '2018-07-14 00:00:00', '2018-07-02 00:00:00', '2018-06-15 00:00:00', '2018-05-25 00:00:00', '2018-05-15 00:00:00', '2018-04-28 00:00:00', '2018-04-13 00:00:00', '2018-03-19 00:00:00', '2018-02-08 00:00:00', '2018-01-23 00:00:00', '2018-01-02 00:00:00', '2017-12-11 00:00:00', '2017-08-25 00:00:00', '2017-08-07 00:00:00', '2017-07-20 00:00:00', '2017-06-01 00:00:00', '2017-05-19 00:00:00', '2017-04-07 00:00:00', '2017-03-14 00:00:00', '2017-03-07 00:00:00', '2017-01-17 00:00:00', '2016-12-12 00:00:00', '2016-11-29 00:00:00', '2016-10-28 00:00:00', '2016-09-20 00:00:00', '2016-08-04 00:00:00', '2016-07-14 00:00:00', '2016-06-02 00:00:00', '2016-03-17 00:00:00', '2016-03-07 00:00:00', '2016-02-03 00:00:00', '2015-12-22 00:00:00', '2015-12-09 00:00:00', '2015-10-27 00:00:00', '2015-09-24 00:00:00', '2015-09-10 00:00:00']
	Update_List.reverse()
	return Time_List, Score_List, Comment_List, Update_List

def draw_Timeline(Time_List, Score_List, Update_List):
	#生成时间线对象
	t1 = Timeline(init_opts=opts.InitOpts(width = '1750px', height = '700px', theme = ThemeType.LIGHT))
	temp_Time_List = []
	temp_Score_List = []
	#配置时间轴参数
	t1.add_schema(axis_type = 'time', symbol_size = [10,10], is_auto_play = True,
						 width = '1000px', height = '200px', pos_bottom = '-120px', pos_left = '350px')

	for update_time in Update_List:
		for index in range(0,len(Time_List)):
			#判断每一条评论的时间处于的版本区间
			if compare_time(update_time, Time_List[index]):
				temp_Time_List.append(Time_List[index])
				temp_Score_List.append(Score_List[index])
			else:
				break
		#绘制折线并添加到时间线中
		line = (
			Line(init_opts=opts.InitOpts(theme = ThemeType.LIGHT, width = '2000px', height = '300px'))
			.add_xaxis(temp_Time_List)
			.add_yaxis("横轴：评论时间 , 纵轴：情绪值", temp_Score_List, is_smooth = True, is_symbol_show = False)
			.set_global_opts(
				yaxis_opts=opts.AxisOpts(name="情感值"),
				xaxis_opts=opts.AxisOpts(name="时间"),
				legend_opts=opts.LegendOpts(is_show = False)
				)
				)
		t1.add(line, update_time)
		temp_Time_List = []
		temp_Score_List = []
	return t1

def draw_Table(Time_List, Score_List, Comment_List, Update_List):
	#绘制评论表格
	table = Table()
	headers = ["评论时间", "情绪值", "评论内容"]
	rows = []
	for index in range(0,1800,30):
		temp = [Time_List[index], Score_List[index], Comment_List[index]]
		rows.append(temp)
	table.add(headers, rows).set_global_opts(
	    title_opts=ComponentTitleOpts(title="时间-情绪-评论文本 抽样数据")
	)
	return table

def main():
	file = 'result.xls'
	time_list, score_list, comment_list, update_list = read_xlsx(file)
	draw_Timeline(time_list, score_list, update_list).render("海尔智家.html")
	draw_Table(time_list, score_list, comment_list, update_list).render("table.html")

if __name__ == '__main__':
    main()
