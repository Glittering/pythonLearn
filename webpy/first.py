import web
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        return open(r'jingYuan/index.html', 'r').read()

if __name__ == "__main__":
    app.run()
