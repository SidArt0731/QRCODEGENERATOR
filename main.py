from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
import qrcode #pip install it


class Function(ScreenManager):
	def generate_qr_code(self , root):
		if self.ids.link_text.text != "" and self.ids.image_name.text != "":
			code = qrcode.QRCode(version=1.0 , box_size= 15 , border=4)
			code.add_data(self.ids.link_text.text)
			code.make(fit=True)
			img = code.make_image(fill = "Black" , back_color = "White")
			img.save(f"{self.ids.image_name.text}.png")
			Snackbar(text = "QR code generated" , font_size = 40).show()
			
		else:
			Snackbar(text = "Enter something in text sections" , font_size = 40).show()
			
		
	def view_image(self , root):
		if self.ids.link_text.text != "" and self.ids.image_name.text != "":
			self.ids.img_.source = f"{self.ids.image_name.text}.png"
			root.current = "image" #changing screen
			
		else:
			Snackbar(text = "Enter something in text sections" , font_size = 40).show()
			
		
	def make_another(self , root):
		self.ids.link_text.text = ""
		self.ids.image_name.text = ""
		root.current = "first" #going to main screen
		

class Main(MDApp):
	
	def __init__(self,**kwargs):
		Builder.load_file("layout.kv")
		super().__init__(**kwargs)
	
	def build(self):
		return Function()
		
	def show_data(self , obj):
		
		about_us = "This app creates QR codes.\n\nCreated by Siddharth Soni.\n\nContact: sidsoni0731@gmail.com"
		
		close_button = MDFlatButton(text = "close", on_release = self.close_dialog)
		self.dialog = MDDialog(title = "QR code generator", text = about_us, size_hint = (0.7 , 1), buttons = [close_button])
		
		self.dialog.open()
		
	def close_dialog(self , obj):
		self.dialog.dismiss()
		
	def show_themepicker(self):
		picker = MDThemePicker()
		picker.open()
		

Main().run()