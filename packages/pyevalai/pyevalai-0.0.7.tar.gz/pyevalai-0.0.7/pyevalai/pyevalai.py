# test of websocket client for ai_grader in jupyter notebook
# connects with grading_server2.py

import tornado.ioloop
import tornado.websocket
import threading
import time
import getpass
from IPython.display import display, Markdown
import ipywidgets as widgets
import json
import warnings
import cloudpickle
import base64
import inspect
from .utils import CustomEncoder,custom_decoder

webs = None # websocket
ioloop = None # tornado ioloop
log_screen = None # for logging of debug information
current_screen = None # for output of current active cell
exercise_screen = {} # for output of specific exercise (dict keys correspond to exercise names)
test_function = {} # functions that should be evaluated
connect_condition = threading.Condition()

def print_log(s):
	if log_screen is not None: log_screen.append_display_data(Markdown(s))

def get_screen(screen=None):
	if type(screen) is str: screen = exercise_screen.get(screen)
	if screen is None or screen=="None": screen = current_screen
	return screen

def clear_screen(screen=None):
	screen = get_screen(screen)
	#screen.clear_output()
	screen.outputs=[]
	#time.sleep(0.1) # seems to be necessary, otherwise messages shortly after this call might be cleared as well

def print_md(s,screen=None):
	screen = get_screen(screen)
	if screen is not None: screen.append_display_data(Markdown(s))

def print_danger(s,screen=None):
	print_md(f"""<div class="alert alert-block alert-danger">{s}</div>""")

def print_warn(s,screen=None):
	print_md(f"""<div class="alert alert-block alert-warning">{s}</div>""")

def print_ok(s,screen=None):
	print_md(f"""<div class="alert alert-block alert-success">{s}</div>""")

def set_current_screen():
	global current_screen
	current_screen = widgets.Output()
	display(current_screen)

def show(s):
	display(Markdown(s))
	return s

def start_client(url="localhost"):
	global ioloop,webs
	# Create a new IOLoop for the client thread

	# WebSocket connection callback
	def on_connect(future):
		global webs, connect_condition
		with connect_condition:
			try:
				webs = future.result()  # This gives us the websocket to write messages
			except:
				webs=None
			connect_condition.notify()
		#print_log("WebSocket client ready")
		#webs.write_message("Hello from client!")

	def on_message(message):
		global webs
		# if message is None => connection closed
		if message is None:
			ioloop.stop()
			print_danger("WebSocket disconnected! login again!")
			return
		
		#print_log(f"Received message from server: {message}")
		msg = json.loads(message)
		
		if msg["type"]=="clear":
			clear_screen(msg.get("screen"))
		
		if msg["type"]=="md":
			print_md(msg["value"],msg.get("screen"))
		
		if msg["type"]=="error":
			print_danger(msg["value"],msg.get("screen"))
		
		if msg["type"]=="warn":
			print_warn(msg["value"],msg.get("screen"))
		
		if msg["type"]=="success":
			print_ok(msg["value"],msg.get("screen"))
		
		if msg["type"]=="test_input":
			msg = json.loads(message, object_hook=custom_decoder) # decode json
			name = msg["name"]
			input_args = msg["args"]
			input_kwargs = msg["kwargs"]
			try:
				output_value = test_function[name](*input_args,**input_kwargs)
			except Exception as e:
				output_value = None
				print(e)
			
			# encode output_value...
			response = {"type":"test_result","value":output_value}
			json_payload = json.dumps(response, cls=CustomEncoder)
			webs.write_message(json_payload)
		
		return
		

	# Connect to the WebSocket server and use the on_connect callback
	stop_client()
	
	ioloop = tornado.ioloop.IOLoop()
	ws_req = tornado.httpclient.HTTPRequest(f"wss://{url}/websocket", validate_cert=True) # certificate sollte auf jeden Fall validiert werden!
	future = tornado.websocket.websocket_connect(ws_req,on_message_callback=on_message)
	future.add_done_callback(on_connect)
	
	# Start the IOLoop for the client thread
	ioloop.start()
	print_log("connection closed")
	ioloop = None
	webs=None

def stop_client():
	global ioloop, webs
	webs = None
	if ioloop is not None:
		try:
			ioloop.stop()
			ioloop = None
		except:
			print_log("stop_client error")

def start(url="localhost:1234"):
	global webs, connect_condition
	# Start the client in a separate thread
	for i in range(3): # try at most 3 times to connect
		try:
			client_thread = threading.Thread(target=start_client,args=(url,))
			client_thread.daemon = True  # Ensure the thread exits when the main program exits
			client_thread.start()
			
			start_time = time.time()
			with connect_condition:
				while webs is None and time.time()-start_time<3: # could be done more elegantly with condition variable
					connect_condition.wait(1)
			
			if webs is not None: # connection succeeded
				return
			
			print_log("connection failed ... retry")
		except:
			print_log("could not connect ... retry in 1s")
			time.sleep(1)

def send(msg):
	if webs is None:
		print_danger("WebSocket disconnected! login again!")
		return
	webs.write_message(msg)

def login(url="localhost:1234",username=None,password=None):
	global webs, log_screen
	log_screen = widgets.Output()
	display(log_screen)
	
	start(url)
	if username is None:
		username = input("Username: ")
	if password is None:
		password = getpass.getpass(prompt="Passwort: ")
	
	set_current_screen()
	
	send({"type":"auth","username":username,"password":password})

def enter_course(name):
	set_current_screen()
	send({"type":"enter_course","course":name})

def register_exercise(name,exercise,solution,points,tests=[],ex_type="text",n_tries=None,deadline=None):
	set_current_screen()
	
	send({"type":"register_ex",
	   "name":name,
	   "exercise":exercise,
	   "solution":solution,
	   "points":points,
	   "ex_type":ex_type,
	   "tests":tests,
	   "n_tries":n_tries,
	   "deadline":deadline})

def remove_exercise(name):
	set_current_screen()
	send({"type":"remove_ex", "name":name})

def test_text(question,yes_points=None,no_points=None):
	return [{"type":"text",
		 "question":question,
		 "yes_points":yes_points,
		 "no_points":no_points}]

def test_code(question,unit_test):
	serialized_test = cloudpickle.dumps(unit_test)
	encoded_test = base64.b64encode(serialized_test).decode('utf-8')
	return [{"type":"code",
		 "question":question,
		 "encoded_test":encoded_test}]

def handin_exercise(name,solution):
	global test_function, current_screen, exercise_screen
	set_current_screen()
	
	if webs is None:
		print_danger("WebSocket disconnected! login again!")
		return
	
	clear_screen()
	exercise_screen[name] = current_screen
	
	if type(solution) != str:
		test_function[name] = solution
		solution = inspect.getsource(solution)
	
	send({"type":"handin_ex",
	   "ex_name":name,
	   "solution":solution})
