
####scrapy练习--爬取汽车之家的图片

&nbsp;
&nbsp;

#####2018-3-12
提取到异步加载的帖子评论数。这就是单独请求一个链接，带上帖子号就能给你返回需要的数据

帖子图片是下滑才加载，还没找到更好的方法来提取图片链接···

&nbsp;
&nbsp;
-----------------------
&nbsp;
&nbsp;

 能力不够，解决不了汽车之家这个图片加载问题,只好用 selenium 来模拟web浏览器来爬去了。    
 

&nbsp;
&nbsp;

--------------------
&nbsp;
selenium:

    selenium 是一套完整的web应用程序测试系统，包含了测试的录制（selenium IDE）,编写及运行（Selenium Remote Control）和测试的并行处理（Selenium Grid）。Selenium的核心Selenium Core基于JsUnit，完全由JavaScript编写，因此可以用于任何支持JavaScript的浏览器上。

    selenium可以模拟真实浏览器，自动化测试工具，支持多种浏览器，爬虫中主要用来解决JavaScript渲染问题。