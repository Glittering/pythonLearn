#Web.py

##固定框架

import web
urls = (
    '/','class'
)

app = web.application(urls, globals())

class :

if __name__ = "__main__":
    app.run()

##请求处理

open(r'/index','r').read()	打开并读取一个文件

web.input()	获取请求

web.ctx.env()	获取请求头

##响应处理

+ render.index("参数")	模板文件读取
+ model.select("sql")	结果数据获取
+ web.seeother("/")	URL 跳转

使用模板 render = web.template.render('templates')
同级目录下创建templates文件夹
在templates里放html网页，例如：hello2.html
引用：render.hello2()
	模板比open好，可以传参数。 在hello2.html的第一行 写  $def with(变量)	引用变量：$变量名
