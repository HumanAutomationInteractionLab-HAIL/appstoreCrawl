# appstoreCrawl & SentimentAnalysis  
## 描述
-Crawl部分  
* CrawlAndCut是一个基于python，可抓取任意AppStore上app评论储存并切词的应用。
* CutOnly是一个基于python，可读取excel数据并切词的应用。
* 提供了样例评论表和样例结果。  
  
-SentimentAnalysis部分  
* 基于python和百度aipNLP接口，对抓取到的app评论进行情感分析并储存  
![](https://github.com/HumanAutomationInteractionLab-HAIL/appstoreCrawl/blob/master/SentimentAnalysis/SentimentAnalysisDemo.png)  
* 使用pyecharts库，自动绘制评论情感值随时间变化的动态曲线，以及对评论抽样后得到的评论表格  
* 曲线每次动态变化以app版本更新为界，表格位于图像下方  
![](https://github.com/HumanAutomationInteractionLab-HAIL/appstoreCrawl/blob/master/SentimentAnalysis/timeline.png)    
![](https://github.com/HumanAutomationInteractionLab-HAIL/appstoreCrawl/blob/master/SentimentAnalysis/table.png)  
  
## 使用说明  
-依赖安装  
* pip install -r requirements.txt  
  
-Crawl部分  
* CrawlAndCut在代码中将海尔智家的名字和id更改为所需app的名字与id。
* CutOnly运行后直接输入需要处理的表格名字（表格应置于工程文件夹中，表格默认为xlsx格式，若不然请微调代码）。
* 微调停用词列表从而因地制宜的享受切词。  
  
-SentimentAnalysis部分  
* 在百度智能云中创建自己的情感倾向分析应用  
* 在代码中的ID和KEY相应更改为自己的应用数据  
* 将Comments.xlsx更换为自己的评论数据（表格结构不同的excel表格，需要微调读取函数)  
  
## 代码贡献者  
Crawl部分：             李永康SocraLee   北京大学  
SentimentAnalysis部分： 郝瀚             北京邮电大学
