#预处理，大量字段包含噪声”(该条评论已经被删除)“，已在表格中预先去除
from aip import AipNlp
import time
import xlrd
import xlwt 

fout = open("result.txt", "w", encoding = 'utf-8')

class Comment(object):
    def __init__(self, time, text, score):
        self.time = time
        self.text = text
        self.score = score
        
def Sentiment_Analysis(CommentList):
    #连接aipNLP账号
    APP_ID = 'XXXXX'
    API_KEY = 'XXXXX'
    SECRET_KEY = 'XXXXX'
    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    result = []
    for Comment in CommentList:
        #调用API进行情感分析
        try:
            temp = client.sentimentClassify(Comment.text)        
            #写结果
            fout.write(str(Comment.time) + '\n')
            fout.write(str(temp) + '\n')
            #计算综合情感值
            if temp['items'][0]['sentiment'] == 0:
                Comment.score = temp['items'][0]['confidence'] * (temp['items'][0]['sentiment'] - 1) * temp['items'][0]['negative_prob']
            if temp['items'][0]['sentiment'] == 2:
                Comment.score = temp['items'][0]['confidence'] * (temp['items'][0]['sentiment'] - 1) * temp['items'][0]['positive_prob']
            result.insert(0,Comment)
            fout.write(str(Comment.score) + '\n')
            fout.write('************' + '\n')
            time.sleep(0.2)   #{'error_code': 18, 'error_msg': 'Open api qps request limit reached'}
        except UnicodeEncodeError:
            continue
        except KeyError:
            continue
    return result

def read_excel():
    data = xlrd.open_workbook("Comments.xlsx", encoding_override = 'utf-8')
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    Time_List = [table.cell_value(rows,1) for rows in range(3,nrows)]
    Text_List = [table.cell_value(rows,5) for rows in range(3,nrows)]
    #创建CommentList
    Comment_List = []
    for index in range(0,len(Time_List)):
        Comment_List.append(Comment(Time_List[index], Text_List[index], 0))
    return Comment_List

def write_excel(result):
    wb = xlwt.Workbook()
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('My Worksheet')
    for i in range(len(result)):
        worksheet.write(i, 0, result[i].time)
        worksheet.write(i, 1, result[i].score)
        worksheet.write(i, 2, result[i].text)
    workbook.save('Result.xls')
    
def main():
    result = Sentiment_Analysis(read_excel())
    write_excel(result)
if __name__ == '__main__':
    main()