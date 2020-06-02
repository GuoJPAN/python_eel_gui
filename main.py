import eel

# 初始化定义html文件所在文件夹
eel.init('web')


@eel.expose  # 使用装饰器,类似flask里面对路由的定义
def print_content(str):
    content = '你好！我来自Python的字符串；' + '这家伙前端送来的→' + str
    return (content)


# 测试调用js中的函数,同样需要使用回调函数
js_return = eel.js_fun('python传过去的参数')(lambda x: print(x))

# 启动的函数调用放在最后,port=0表示使用随机端口,size=(宽,高)
eel.start('main.html', port=0, size=(600, 300))
