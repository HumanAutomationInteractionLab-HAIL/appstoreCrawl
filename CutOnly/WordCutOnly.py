# -*- coding: utf-8 -*-
import jieba
import xlrd
def readInAndHandle(stopwords):
    data=xlrd.open_workbook("Comments.xlsx",encoding_override='utf-8')
    table=data.sheets()[0]
    nrows = table.nrows  # 获取行号
    ncols = table.ncols  # 获取列号

    for i in range(3, nrows):  # 前三行为表头
        alldata = table.row_values(i)  # 循环拿到excel表中每一行，即所有数据
        result = str(alldata[5])  # 取出表中第二列数据
        print(result)
        handleAndWrite(result,stopwords)

def handleAndWrite(comment,stopWords):
    with open('D:/WordsOf海尔智家.txt','a',encoding='utf-8')as file:
        commentWord=jieba.cut(comment)
        strToWrite=''
        for word in commentWord:
             if word not in stopWords:
                  if word != '\t':
                     strToWrite += word
                     strToWrite += " "
        file.write(strToWrite)
    file.close()
def main():
    stopwords = [line.strip() for line in open('StopwordOfBaidu.txt', encoding='UTF-8').readlines()]
    readInAndHandle(stopwords)
if __name__ == '__main__':
    main()