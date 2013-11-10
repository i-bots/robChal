import json
import pygtk
pygtk.require("2.0")
import gtk

tasks = json.load(open("aufgaben.json"))

statechecks=[]

BORDER=5
SPACING=5

class Window:
	def __init__(self):
		self.createWindow()
		self.parse()
		self.win.show_all()
		
	def createWindow(self):
		self.win=gtk.Window()
		self.win.set_title("Irgendwas")
		self.win.connect("delete-event", self.delete)
		self.win.set_icon_from_file("icon")
		self.win.set_size_request(500,700)
		self.vbox=gtk.VBox(spacing=SPACING)
		self.vbox.set_border_width(BORDER)
		self.win.add(self.vbox)
		
		image=gtk.Image()
		image.set_from_file("challenge-logo")
		self.vbox.pack_start(image,False,True,0)
		
		finbutton=gtk.Button("Fertig")
		self.vbox.pack_end(finbutton,False,True,0)
		finbutton.connect("clicked",self.onDone)
		
	def parse(self):
		for task in tasks:
			if task["type"]=="check":
				button=gtk.CheckButton(task["name"]+" "+str(task["options"]))
				self.vbox.pack_start(button,False,False,0)
				statechecks.append((button,task["options"]))
				
			elif task["type"]=="choice":
				combo=gtk.combo_box_new_text()
				frame=gtk.Frame(task["name"])
				frame.add(combo)
				for i in task["options"]:
					combo.append_text(i)
				combo.set_active(0)
				self.vbox.pack_start(frame,False,False,0)
				statechecks.append([combo])
	
	def delete(self, widget, data=None):
		gtk.main_quit()
		return False
	
	def onDone(self,widget,data=None):
		points=0
		for i in statechecks:
			state=i[0].get_active()
			if type(state)==bool:
				if state:
					points+=i[1][1]
				else:
					points+=i[1][0]
			else:
				model=i[0].get_model()
				selection=i[0].get_active()
		print(points)
			
app=Window()
gtk.main()
