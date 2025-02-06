from tornado.options import define, options
import tornado.ioloop
import tornado.web
import server.database as db
import server.website as website
from server.certificates.passwords import cookie_secret
from server.websocket_server import WebSocketHandler

# hardcode some initial values for database
# TODO: add user interface for that...
db.load_database()
try:
	db.register_course("Numerik")
	db.register_course("Stochastik")
except:
	pass
db.make_user_tutor(0,"wandeln")
db.make_user_admin("wandeln")

# Tornado Application
def make_app(debug=False):
	settings = dict(
		static_path="server/static",
		template_path="server/template",
		include_version=False,
		cookie_secret=cookie_secret,
		xsrf_cookies=True,
		debug=debug,
		login_url="/login")
	return tornado.web.Application([
		(r"/logout", website.LogoutHandler),
		(r"/login", website.LoginHandler),
		(r"/home", website.HomeHandler),
		(r"/course/(.*)", website.CourseHandler),
		(r"/course_tutor/(.*)", website.CourseTutorHandler),
		(r"/course_csv/(.*)", website.CourseCSVHandler),
		(r"/exercise/(.*)/(.*)", website.ExerciseHandler),
		(r"/exercise_tutor/(.*)/(.*)/(.*)", website.ExerciseTutorHandler),
		(r"/websocket", WebSocketHandler),
		(r"(.*)", website.HomeHandler),  # WebSocket endpoint => runs on same port as webserver
	],
	default_handler_class=website.My404Handler,**settings),tornado.web.Application([
		("(.*)", website.HTTPRedirectHandler),  # http redirects directly to secure https connection
	],**settings)

if __name__ == "__main__":
	define("https_port", default=443, help="run https server on the given port", type=int)
	define("http_port", default=80, help="run http server on the given port", type=int)
	define("debug", default=False, help="run server in debug mode", type=bool)
	options.parse_command_line()
	
	HTTPSapp,HTTPapp = make_app(debug=options.debug)
	#settings = dict( ssl_options={"certfile":"server/certificates/crt.pem","keyfile":"server/certificates/key.pem"})
	settings = dict( ssl_options={"certfile":"/etc/letsencrypt/live/cg2-04.informatik.uni-bonn.de/fullchain.pem","keyfile":"/etc/letsencrypt/live/cg2-04.informatik.uni-bonn.de/privkey.pem"})
	HTTPSserver = tornado.httpserver.HTTPServer(HTTPSapp,**settings)
	HTTPSserver.listen(options.https_port)
	HTTPserver = tornado.httpserver.HTTPServer(HTTPapp)
	HTTPserver.listen(options.http_port)
	
	tornado.ioloop.IOLoop.current().start()
