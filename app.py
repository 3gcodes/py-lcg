import tornado.ioloop
import tornado.web
import os.path

# I don't like this style of import so let's find a better way later.
# for now this works though.
from handlers.MainHandler import *

application = tornado.web.Application(
	[
    	(r"/", MainHandler)
	],
	template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static")
)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()