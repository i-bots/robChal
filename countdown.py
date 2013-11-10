import gtk
import pango
from datetime import timedelta as time

COWNTDOWN=[1,20]

def fill(string,length):
	if len(string)<length:
		string+="0"
		string=fill(string,length)
	if len(string)>=length:
		return string

class app:
	def __init__(self):
		self.window=gtk.Window()
		gtk.timeout_add(10,self.subtract)
		self.window.set_size_request(800,500)
		
		self.text=gtk.Label()
		self.text.modify_font(pango.FontDescription("sans 60"))
		
		self.time=COWNTDOWN[0]*60+COWNTDOWN[1]
		
		self.window.add(self.text)
		self.window.show_all()
		
	def subtract(self,data=None):
		
		self.text.set_text(
		str(time(seconds=self.time))[3:10]
		)
		
		self.time-=0.01
		
		if self.time > 0:
			return True
		else:
			return False

root=app()
gtk.main()
