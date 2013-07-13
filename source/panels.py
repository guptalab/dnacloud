# -*- coding: utf-8 -*-
import sys
from PIL import Image
from PIL import PngImagePlugin
import barcodeGenerator
import math
import os
import sqlite3 
import sqlite3 as lite
import wx
import extraModules
import multiprocessing
import time

CHUNK_SIZE = 1000000
if hasattr(sys, "frozen"):
        PATH = os.path.dirname(sys.executable)
else:
        PATH = os.path.dirname(os.path.abspath(__file__))
#print PATH , "panels"

BARCODE_HEIGHT = 96
BARCODE_WIDTH = 470
PREF_DISCLAIMER = "Disclaimer : Please note that this details will be used to identify user of the DNA strings by Bio Companies hence these are mandatory to be filled."

SOFTWARE_DETAILS = "\n\n  Version 1.0\n\n  www.guptalab.org/dnacloud\n\n  Report bugs at dnacloud@guptalab.org"

class encodePanel(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent = parent,style = wx.TAB_TRAVERSAL)
		
		self.vBox1 = wx.BoxSizer(wx.VERTICAL)
#This is the adjustment of the Basic BUI text and textCtrl panels along with save to DataBase and Discard Button Options
		head = wx.StaticText(self ,label = "Encode file into DNA String",style = wx.CENTER)
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.vBox1.Add(head ,flag = wx.EXPAND | wx.TOP | wx.LEFT , border = 10)
		line1 = wx.StaticLine(self, size=(1000,1) , style = wx.ALIGN_CENTRE)
		self.vBox1.Add(line1, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 10)
		
		self.hBox1 = wx.BoxSizer(wx.HORIZONTAL)
		self.butChoose = wx.Button(self , label = "Choose File",size = (100,30))
		self.hBox1.Add(self.butChoose,flag = wx.EXPAND | wx.LEFT , border = 10)
		path = wx.StaticText(self, label = "Select any File from you File System")
		self.hBox1.Add(path,flag = wx.ALIGN_CENTER_VERTICAL | wx.LEFT , border = 20)
		self.vBox1.Add(self.hBox1)

		head =  wx.StaticText(self,label = "Details(approx.)")
		font = wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.vBox1.Add(head,flag = wx.TOP | wx.LEFT,border =20)

		line2 = wx.StaticLine(self, size=(1000,1) , style = wx.ALIGN_CENTRE)
		self.vBox1.Add(line2, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 10)

		self.hBox = wx.BoxSizer(wx.HORIZONTAL)                        
		path = wx.StaticText(self, label = "File Selected : ",style = wx.ALIGN_CENTRE)
		self.txt = wx.TextCtrl(self,name = "hBox",size = (500,25),style= wx.TE_READONLY)
		self.hBox.Add(path,2 ,flag = wx.EXPAND )
		self.hBox.Add(self.txt, 8, flag = wx.EXPAND | wx.RIGHT , border = 20)
		self.vBox1.Add(self.hBox,flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 5)

		self.hBox2 = wx.BoxSizer(wx.HORIZONTAL)
		content1 = wx.StaticText(self, label = "Lenght Of DNA String : " , style = wx.ALIGN_CENTRE)
		self.txt2 = wx.TextCtrl(self,name = "hBox3",size = (300,25),style= wx.TE_READONLY)
		self.hBox2.Add(content1, 2, flag = wx.EXPAND)
		self.hBox2.Add(self.txt2, 8, flag = wx.EXPAND | wx.RIGHT , border = 20)
		self.vBox1.Add(self.hBox2,flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 5)
		
		self.hBox3 = wx.BoxSizer(wx.HORIZONTAL)
		content1 = wx.StaticText(self, label = "No of DNA Chunks : " , style = wx.ALIGN_CENTRE)
		self.txt3 = wx.TextCtrl(self,name = "hBox3",size = (300,25),style= wx.TE_READONLY)
		self.hBox3.Add(content1, 2, flag = wx.EXPAND)
		self.hBox3.Add(self.txt3, 8, flag = wx.EXPAND | wx.RIGHT , border = 20)
		self.vBox1.Add(self.hBox3,flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 5)
		
		self.hBox4 = wx.BoxSizer(wx.HORIZONTAL)
		content1 = wx.StaticText(self, label = "Length of each DNA Chunk : ", style = wx.ALIGN_CENTRE)
		self.txt4 = wx.TextCtrl(self,name = "hBox4",size = (300,25),style= wx.TE_READONLY)
		self.hBox4.Add(content1, 2, flag = wx.EXPAND)
		self.hBox4.Add(self.txt4, 8, flag = wx.EXPAND | wx.RIGHT , border = 20)
		self.vBox1.Add(self.hBox4,flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 5)
		
		self.hBox5 = wx.BoxSizer(wx.HORIZONTAL)
		content1 = wx.StaticText(self, label = "File Size(Bytes) : " , style = wx.ALIGN_CENTRE)
		self.txt5 = wx.TextCtrl(self,name = "hBox5",size = (300,25),style= wx.TE_READONLY)
		self.hBox5.Add(content1, 2, flag = wx.EXPAND)
		self.hBox5.Add(self.txt5, 8, flag = wx.EXPAND | wx.RIGHT , border = 20)
		self.vBox1.Add(self.hBox5,flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 5)
#There is nothing like self.txt1
		"""
		head =  wx.StaticText(self,label = "Encoded DNA String")
		font = wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.vBox1.Add(head,flag = wx.TOP | wx.LEFT,border =20)
		
		line3 = wx.StaticLine(self, size=(1000,1) , style = wx.ALIGN_CENTRE)
		self.vBox1.Add(line3, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 10)
		
		self.hBox9 = wx.BoxSizer(wx.HORIZONTAL)
		content1 = wx.StaticText(self, label = "DNA String : ", style = wx.ALIGN_CENTRE) 
		self.but9 = wx.Button(self,label = "View DNA String")
		content1.SetFont(font)
		self.hBox9.Add(content1 ,flag = wx.LEFT ,border = 20)
		self.hBox9.Add(self.but9 ,flag = wx.EXPAND | wx.LEFT , border = 180)
		self.vBox1.Add(self.hBox9 ,flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 5)

		self.hBox10 = wx.BoxSizer(wx.HORIZONTAL)
		content1 = wx.StaticText(self, label = "DNA String List with Error Checks : ", style = wx.ALIGN_CENTRE)
		self.but10 = wx.Button(self,label = "View DNA Chunks")
		font = wx.Font(9 , wx.DEFAULT, wx.NORMAL, wx.BOLD)
		content1.SetFont(font)
		self.hBox10.Add(content1 ,flag = wx.LEFT ,border = 20)
		self.hBox10.Add(self.but10 ,flag = wx.EXPAND)
		self.vBox1.Add(self.hBox10 ,flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 5)
		"""
		self.hBox11 = wx.BoxSizer(wx.HORIZONTAL)
		self.saveBut = wx.Button(self,label = "Encode  your  File",size = (200,40))
		self.discardBut = wx.Button(self,label = "Reset  file  Selected",size = (200,40))
		self.hBox11.Add(self.saveBut, flag = wx.EXPAND | wx.LEFT  , border = 20)
		self.hBox11.Add(self.discardBut, flag = wx.EXPAND | wx.LEFT ,border = 20)
		self.vBox1.Add(self.hBox11 ,flag = wx.TOP | wx.BOTTOM ,border = 10)                

		"""
		self.clearDB = wx.Button(self,label = "Clear Database")
		self.hBox11.Add(self.clearDB ,flag = wx.EXPAND)
		
		head =  wx.StaticText(self,label = "© QR Code generated for given User Details")
		font = wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.vBox1.Add(head,flag = wx.TOP | wx.LEFT,border =20)
		
		line3 = wx.StaticLine(self, size=(1000,1) , style = wx.ALIGN_CENTRE)
		self.vBox1.Add(line3, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 10)
		
		img = wx.EmptyImage(240,240)
		self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY,wx.BitmapFromImage(img))
		self.vBox1.Add(self.imageCtrl,flag = wx.EXPAND | wx.LEFT | wx.BOTTOM , border = 25)
		"""
		self.dummyhBox = wx.BoxSizer(wx.VERTICAL)
                self.vBox1.Add(self.dummyhBox, 2, wx.EXPAND)
		line3 = wx.StaticLine(self, size=(1000,1) , style = wx.ALIGN_CENTRE)
		self.vBox1.Add(line3, flag = wx.EXPAND)
                
		self.hBox12 = wx.BoxSizer(wx.HORIZONTAL)
		self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY,wx.Image(name = PATH + '/../icons/DNAicon.png').ConvertToBitmap())
		self.hBox12.Add(self.imageCtrl,flag = wx.EXPAND | wx.LEFT | wx.TOP , border = 25)
		self.v1Box= wx.BoxSizer(wx.VERTICAL)
		head =  wx.StaticText(self,label = "DNA-CLOUD")
		font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD,underline = True)
		head.SetFont(font)
		self.v1Box.Add(head,flag = wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.LEFT,border = 25)
                head =  wx.StaticText(self,label = SOFTWARE_DETAILS)
		font = wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.v1Box.Add(head,flag = wx.LEFT | wx.EXPAND , border = 20)
		self.hBox12.Add(self.v1Box)
		self.vBox1.Add(self.hBox12,flag = wx.ALIGN_BOTTOM)
		
		self.SetSizer(self.vBox1)
 
  
class decodePanel(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent = parent,style = wx.TAB_TRAVERSAL)
	
		self.vBox2 = wx.BoxSizer(wx.VERTICAL)
		head = wx.StaticText(self ,label = "Generate File from DNA String",style = wx.CENTER)
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.vBox2.Add(head ,flag = wx.EXPAND | wx.TOP | wx.LEFT , border = 10)

		line1 = wx.StaticLine(self, size=(1000,1) , style = wx.ALIGN_CENTRE)
		self.vBox2.Add(line1, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 10)

		
		self.hBox21 = wx.BoxSizer(wx.HORIZONTAL)
		path = wx.StaticText(self, label = "Please Write DNA String :", style = wx.ALIGN_CENTRE)
		self.txt21 = wx.TextCtrl(self,name = "hBox") 
                self.hBox21.Add(path, 2,flag = wx.EXPAND)
		self.hBox21.Add(self.txt21, 8,flag = wx.EXPAND | wx.RIGHT , border = 20)
		self.vBox2.Add(self.hBox21 , flag = wx.EXPAND)

		self.hBox22 = wx.BoxSizer(wx.HORIZONTAL)
		self.decodeBut = wx.Button(self,label = "Decode",size = (150,30))
		self.resetBut = wx.Button(self,label = "Reset",size = (150,30))
		self.hBox22.Add(self.decodeBut ,flag = wx.LEFT ,border = 20)
		self.hBox22.Add(self.resetBut ,flag = wx.EXPAND | wx.LEFT , border = 20)
		self.vBox2.Add(self.hBox22 ,flag = wx.EXPAND | wx.TOP | wx.ALIGN_CENTER, border = 15)   

		head = wx.StaticText(self ,label = "Generate File from already encoded files",style = wx.CENTER)
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.vBox2.Add(head ,flag = wx.EXPAND | wx.TOP | wx.LEFT, border = 20)
		line2 = wx.StaticLine(self, size=(1000,1) , style = wx.ALIGN_CENTRE)
		self.vBox2.Add(line2, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 10)
		
		"""			  
		self.cb = wx.ComboBox(self,size=(800,30) ,style=wx.CB_READONLY)
		self.vBox2.Add(self.cb,flag =  wx.TOP | wx.LEFT | wx.RIGHT , border = 10)
		"""
		self.hBox23 = wx.BoxSizer(wx.HORIZONTAL)                        
		path = wx.StaticText(self, label = "File Selected : ",style = wx.ALIGN_CENTRE)
		self.txt = wx.TextCtrl(self,name = "hBox",style= wx.TE_READONLY)
		self.hBox23.Add(path, 2, flag = wx.EXPAND)
		self.hBox23.Add(self.txt, 8, flag = wx.EXPAND | wx.RIGHT , border = 20)
		self.vBox2.Add(self.hBox23,flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 5)
		
		self.hBox24 = wx.BoxSizer(wx.HORIZONTAL)
		content1 = wx.StaticText(self, label = "Lenght Of DNA String(approx.) : " , style = wx.ALIGN_CENTRE)
		self.txt2 = wx.TextCtrl(self,name = "hBox3",style= wx.TE_READONLY)
		self.hBox24.Add(content1, 2, flag = wx.EXPAND)
		self.hBox24.Add(self.txt2, 8, flag = wx.EXPAND | wx.RIGHT , border = 20)
		self.vBox2.Add(self.hBox24,flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 10)
		
		self.hBox25 = wx.BoxSizer(wx.HORIZONTAL)
		content1 = wx.StaticText(self, label = "No of DNA Chunks(approx.) : " , style = wx.ALIGN_CENTRE)
		self.txt3 = wx.TextCtrl(self,name = "hBox3",style= wx.TE_READONLY)
		self.hBox25.Add(content1, 2, flag = wx.EXPAND)
		self.hBox25.Add(self.txt3, 8, flag = wx.EXPAND | wx.RIGHT , border = 20)
		self.vBox2.Add(self.hBox25,flag = wx.EXPAND | wx.TOP , border = 10)
		
		self.hBox26 = wx.BoxSizer(wx.HORIZONTAL)
		self.butChoose = wx.Button(self , label = "Select  .dna  File ",size = (200,40))
		self.hBox26.Add(self.butChoose,flag = wx.EXPAND | wx.LEFT , border = 20)
		self.decodeBut1 = wx.Button(self,label = "Decode  selected  File ",size = (200,40))
		self.hBox26.Add(self.decodeBut1,flag = wx.EXPAND | wx.LEFT , border = 20)
		self.vBox2.Add(self.hBox26,flag = wx.TOP , border = 15)
		
		"""
		head =  wx.StaticText(self,label = "© QR Code generated for given User Details")
		font = wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.vBox2.Add(head,flag = wx.TOP | wx.LEFT,border =20)	
		
		line3 = wx.StaticLine(self, size=(1000,1) , style = wx.ALIGN_CENTRE)
		self.vBox2.Add(line3, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 10)
		
		img = wx.EmptyImage(240,240)
		self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY,wx.BitmapFromImage(img))
		self.vBox2.Add(self.imageCtrl,flag = wx.EXPAND | wx.LEFT | wx.BOTTOM ,border =  25)
		"""
		self.dummyhBox = wx.BoxSizer(wx.VERTICAL)
                self.vBox2.Add(self.dummyhBox, 2, wx.EXPAND)
		line3 = wx.StaticLine(self, size=(1000,1) , style = wx.ALIGN_CENTRE)
		self.vBox2.Add(line3, flag = wx.EXPAND)
		
		self.hBox27 = wx.BoxSizer(wx.HORIZONTAL)
		self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY,wx.Image(name = PATH + '/../icons/DNAicon.png').ConvertToBitmap())
		self.hBox27.Add(self.imageCtrl,flag = wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT | wx.TOP , border = 25)
		self.v1Box= wx.BoxSizer(wx.VERTICAL)
		head =  wx.StaticText(self,label = "DNA-CLOUD")
		font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, underline = True)
		head.SetFont(font)
		self.v1Box.Add(head,flag = wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.TOP,border = 25)
		head =  wx.StaticText(self,label = SOFTWARE_DETAILS)
		font = wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.v1Box.Add(head,flag = wx.ALIGN_CENTER_VERTICAL | wx.LEFT , border = 20)
		self.hBox27.Add(self.v1Box)
		self.vBox2.Add(self.hBox27)
		
		self.SetSizer(self.vBox2)
                
                
class Preferences(wx.Dialog):

	def __init__(self,parent,id,title):
		wx.Dialog.__init__(self,parent,id,title)

		self.vBox = wx.BoxSizer(wx.VERTICAL)

		ico = wx.Icon(PATH + '/../icons/DNAicon.ico', wx.BITMAP_TYPE_ICO)
		self.SetIcon(ico)
		head = wx.StaticText(self ,label = "Enter your details",style = wx.CENTER)
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.vBox.Add(head ,flag = wx.EXPAND | wx.TOP | wx.LEFT , border = 5)
		
		line1 = wx.StaticLine(self, size=(300,1) , style = wx.ALIGN_CENTRE)
		self.vBox.Add(line1, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 5)

		self.hBoxa = wx.BoxSizer(wx.HORIZONTAL)
		path = wx.StaticText(self, label = " Name(Full) : \t\t\t\t\t", style = wx.ALIGN_CENTRE)
		self.hBoxa.Add(path, 3, wx.EXPAND)
		self.txta = wx.TextCtrl(self,name = "hBox")
		self.hBoxa.Add(self.txta, 8, flag = wx.EXPAND | wx.RIGHT , border = 10)
		self.vBox.Add(self.hBoxa,flag = wx.TOP | wx.BOTTOM , border = 7)

		self.hBoxc = wx.BoxSizer(wx.HORIZONTAL)
		path = wx.StaticText(self,label = " Number(M) :\t\t\t\t\t", style = wx.ALIGN_CENTRE)
		self.hBoxc.Add(path, 3,flag = wx.EXPAND)
		self.txtc = wx.TextCtrl(self,name = "hBox")
		self.hBoxc.Add(self.txtc, 8,flag = wx.EXPAND | wx.RIGHT , border = 10)
		self.vBox.Add(self.hBoxc , flag = wx.TOP | wx.BOTTOM , border = 7)
	
		self.hBoxd =  wx.BoxSizer(wx.HORIZONTAL)
		path = wx.StaticText(self,label = " Email(Eg Gmail) : \t\t\t", style = wx.ALIGN_CENTRE)
		self.hBoxd.Add(path, 3,flag = wx.EXPAND)
		self.txtd = wx.TextCtrl(self,name = "hBox")
		self.hBoxd.Add(self.txtd, 8,flag = wx.EXPAND | wx.RIGHT , border = 10)
		self.vBox.Add(self.hBoxd, flag = wx.TOP | wx.BOTTOM, border = 7)

		self.hBoxb = wx.BoxSizer(wx.HORIZONTAL)
		path = wx.StaticText(self,label = "File Name(Eg a.mkv) :  ", style = wx.ALIGN_CENTRE)
		self.hBoxb.Add(path,proportion = 2,flag = wx.EXPAND | wx.LEFT,border = 7)
		self.txtb = wx.TextCtrl(self,name = "hBox")
		self.hBoxb.Add(self.txtb,proportion = 6 ,flag = wx.EXPAND , border = 30)
		self.vBox.Add(self.hBoxb , flag = wx.TOP | wx.BOTTOM , border = 7)

		line2 = wx.StaticLine(self, size=(300,1) , style = wx.ALIGN_CENTRE)
		self.vBox.Add(line2, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 15)
		
		img = Image.open(PATH + '/../icons/barcode.png')
		img.thumbnail((BARCODE_WIDTH,BARCODE_HEIGHT),Image.BICUBIC)
		img.save(PATH + '/../.temp/barcode', "PNG")
		img = wx.Image(PATH + '/../.temp/barcode', wx.BITMAP_TYPE_ANY)
		self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY,wx.BitmapFromImage(img))
		self.vBox.Add(self.imageCtrl,flag = wx.LEFT | wx.RIGHT |wx.BOTTOM , border = 10)
		
		head = wx.StaticText(self ,label = PREF_DISCLAIMER,style = wx.ALIGN_CENTER_HORIZONTAL)
		font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		head.Wrap(450)
		self.vBox.Add(head ,flag = wx.EXPAND | wx.LEFT | wx.RIGHT , border = 10)

		line3 = wx.StaticLine(self, size=(300,1) , style = wx.ALIGN_CENTRE)
		self.vBox.Add(line3, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 10)

		self.hBoxe = wx.BoxSizer(wx.HORIZONTAL)
		self.saveBut = wx.Button(self,label="  Save  ")
		self.barcodeBut = wx.Button(self,label="  Generate Barcode  ")
		self.cancelBut = wx.Button(self,label="  Close  ")
		self.hBoxe.Add(self.saveBut, flag = wx.RIGHT , border = 10)
		self.hBoxe.Add(self.barcodeBut, flag = wx.RIGHT | wx.wx.LEFT , border = 10)
		self.hBoxe.Add(self.cancelBut, flag = wx.RIGHT , border = 10)
		self.saveBut.Bind(wx.EVT_BUTTON,self.save)
		self.barcodeBut.Bind(wx.EVT_BUTTON,self.generate)
		self.cancelBut.Bind(wx.EVT_BUTTON,self.cancel)
		self.vBox.Add(self.hBoxe, flag = wx.TOP | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTRE_VERTICAL |wx.BOTTOM, border = 10)

		#self.SetSizer(self.vBox)
		self.SetSizerAndFit(self.vBox)

		con = sqlite3.connect(PATH + '/../database/prefs.db')
		try:
			cur = con.cursor()
			string = (cur.execute('SELECT * FROM prefs where id = 1').fetchone())[1]
			self.txta.WriteText(string)
			string = (cur.execute('SELECT * FROM prefs where id = 2').fetchone())[1]
			self.txtc.WriteText(string)
			string = (cur.execute('SELECT * FROM prefs where id = 3').fetchone())[1]
			self.txtd.WriteText(string)
			
			con.commit()
		except sqlite3.OperationalError:
			DATABASE_ERROR = True
		if con:
			con.close()	
			
		#self.SetSize((500,450))

	def save(self,e):
		con = sqlite3.connect(PATH + '/../database/prefs.db')
		try:
			cur = con.cursor()
			cur.execute('UPDATE prefs SET details = ? WHERE id = ?',(self.txta.GetString(0,self.txta.GetLastPosition()),len("x")))
			cur.execute('UPDATE prefs SET details = ? WHERE id = ?',(self.txtc.GetString(0,self.txtc.GetLastPosition()),len("xy")))
			cur.execute('UPDATE prefs SET details = ? WHERE id = ?',(self.txtd.GetString(0,self.txtd.GetLastPosition()),len("xyz")))
			cur.execute('UPDATE prefs SET details = "true" WHERE id = 4')
			con.commit()
		except sqlite3.OperationalError:
			DATABASE_ERROR = True
		if con:
			con.close()		

		self.Destroy()
		
	def generate(self,e):
		barcodeGenerator.generate(self.txta.GetString(0,self.txta.GetLastPosition()) + "-" + self.txtb.GetString(0,self.txtb.GetLastPosition())+ "-" + self.txtc.GetString(0,self.txtc.GetLastPosition()) + "-" + self.txtd.GetString(0,self.txtd.GetLastPosition()),PATH + "/../icons/")
		
		img = Image.open(PATH + '/../icons/barcode.png')
		img.thumbnail((BARCODE_WIDTH,BARCODE_HEIGHT),Image.BICUBIC)
		img.save(PATH + '/../.temp/barcode', "PNG")
		
		img = wx.Image(PATH + '/../.temp/barcode', wx.BITMAP_TYPE_ANY)
		self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
		self.Refresh()

	def cancel(self,e):
		self.Destroy()
		
		
#dialog used to set or change password
class setPasswordDialog(wx.Dialog):

	def __init__(self,parent,id,title):
		wx.Dialog.__init__(self,parent,id,title)

		self.vBox = wx.BoxSizer(wx.VERTICAL)
		ico = wx.Icon(PATH + '/../icon/DNAicon.ico', wx.BITMAP_TYPE_ICO)
		self.SetIcon(ico)
		head = wx.StaticText(self ,label = "Please Enter your password",style = wx.CENTER)
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.vBox.Add(head ,flag = wx.EXPAND | wx.TOP | wx.LEFT , border = 5)
		
		line1 = wx.StaticLine(self, size=(300,1) , style = wx.ALIGN_CENTRE)
		self.vBox.Add(line1, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 5)

		self.hBoxa = wx.BoxSizer(wx.HORIZONTAL)
		path = wx.StaticText(self, label = " Old Password :\t\t")
		
		con = sqlite3.connect(PATH + '/../database/prefs.db')
		with con:
			cur = con.cursor()
			string = cur.execute('SELECT * FROM prefs WHERE id = 5').fetchone()[1]
			if string == 'false':
				self.txta = wx.TextCtrl(self,name = "hBox",style = wx.TE_READONLY)
			else:
				self.txta = wx.TextCtrl(self,name = "hBox",style = wx.TE_PASSWORD)
				
		self.hBoxa.Add(path,1,wx.EXPAND)
		self.hBoxa.Add(self.txta,3,wx.EXPAND | wx.RIGHT ,border = 10)
		self.vBox.Add(self.hBoxa,flag = wx.TOP | wx.BOTTOM , border = 7)
		
		self.hBoxc = wx.BoxSizer(wx.HORIZONTAL)
		path = wx.StaticText(self,label = " New Password :\t  ")
		self.txtc = wx.TextCtrl(self,name = "hBox",style = wx.TE_PASSWORD)
		self.hBoxc.Add(path, 1, flag = wx.EXPAND)
		self.hBoxc.Add(self.txtc, 3, wx.EXPAND | wx.RIGHT , border = 10)
		self.vBox.Add(self.hBoxc , flag = wx.TOP | wx.BOTTOM , border = 7)
	
		self.hBoxd =  wx.BoxSizer(wx.HORIZONTAL)
		path = wx.StaticText(self,label = " Confirm Password : ")
		self.txtd = wx.TextCtrl(self,name = "hBox1",style = wx.TE_PASSWORD)
		self.hBoxd.Add(path, 1, flag = wx.EXPAND)
		self.hBoxd.Add(self.txtd, 3, flag = wx.EXPAND | wx.RIGHT,border = 10)
		self.vBox.Add(self.hBoxd,flag = wx.TOP | wx.BOTTOM, border = 7)

		line1 = wx.StaticLine(self, size=(300,1) , style = wx.ALIGN_CENTRE)
		self.vBox.Add(line1, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 10)
		
		head = wx.StaticText(self ,label = "It is recommended that you use password to keep your data private")
		font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.vBox.Add(head ,flag = wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT | wx.RIGHT , border = 5)
		
		line3 = wx.StaticLine(self, size=(300,1) , style = wx.ALIGN_CENTRE)
		self.vBox.Add(line3, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 10)
		
		self.hBoxe = wx.BoxSizer(wx.HORIZONTAL)
		self.saveBut = wx.Button(self,label=" Save ")
		self.cancelBut = wx.Button(self,label=" Cancel ")
		self.hBoxe.Add(self.saveBut,flag = wx.RIGHT | wx.BOTTOM, border = 10)
		self.hBoxe.Add(self.cancelBut,flag = wx.LEFT | wx.BOTTOM, border = 10)
		self.vBox.Add(self.hBoxe, flag = wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL)

		self.saveBut.Bind(wx.EVT_BUTTON,self.save)
		self.cancelBut.Bind(wx.EVT_BUTTON,self.cancel)
		
		#self.SetSizer(self.vBox)
		#self.SetSize((570,250))
		self.SetSizerAndFit(self.vBox)

	def save(self,e):
		con = sqlite3.connect(PATH + '/../database/prefs.db')
		try:
			cur = con.cursor()
			string = cur.execute('SELECT * FROM prefs WHERE id = 5').fetchone()[1]
			if string == 'true':
				oldPassword = (cur.execute('SELECT * FROM prefs where id = 6').fetchone())[1]
				if self.txta.GetString(0,self.txta.GetLastPosition()) != oldPassword or self.txtc.GetString(0,self.txtc.GetLastPosition()) != self.txtd.GetString(0,self.txtd.GetLastPosition()):
					wx.MessageBox('Your Passwords donot match or else your old password might be wrong', 'Information!',wx.OK | wx.ICON_INFORMATION)
				else:
					cur.execute('UPDATE prefs SET details = ? WHERE id = ?',(self.txtd.GetString(0,self.txtd.GetLastPosition()),6))
					con.execute('UPDATE prefs SET details = ? WHERE id = ?',("true",5))
					self.Destroy()
					wx.MessageBox('Your Password has been updated!!', 'Information!',wx.OK |wx.ICON_INFORMATION)
			else:
				if self.txtc.GetString(0,self.txtc.GetLastPosition()) != self.txtd.GetString(0,self.txtd.GetLastPosition()):
					wx.MessageBox('Your Passwords donot match', 'Information!',wx.OK | wx.ICON_INFORMATION)
				else:
					cur.execute('UPDATE prefs SET details = ? WHERE id = ?',(self.txtd.GetString(0,self.txtd.GetLastPosition()),6))	
					con.execute('UPDATE prefs SET details = ? WHERE id = ?',("true",5))
					self.Destroy()
					wx.MessageBox('Your Password has been updated!!', 'Information!',wx.OK |wx.ICON_INFORMATION)
			con.commit()
		except sqlite3.OperationalError:
			DATABASE_ERROR = True
			self.Destroy()
		if con:
			con.close()		
		
	def cancel(self,e):
		self.Destroy()
		
		
#dialog used to select encode /decode while the software starts
class chooseDialog(wx.Dialog):
	def __init__(self,parent,id,title):
		wx.Dialog.__init__(self,parent,id,title)
		self.vBox = wx.BoxSizer(wx.VERTICAL)
		
		ico = wx.Icon(PATH + '/../icons/DNAicon.ico', wx.BITMAP_TYPE_ICO)
		self.SetIcon(ico)
		head = wx.StaticText(self ,label = "Please Select your Choice",style = wx.CENTER)
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.vBox.Add(head ,flag = wx.EXPAND | wx.TOP | wx.LEFT |wx.ALIGN_CENTER_HORIZONTAL, border = 5)
		
		line1 = wx.StaticLine(self, size=(300,1) , style = wx.ALIGN_CENTRE)
		self.vBox.Add(line1, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 5)
		
		self.encodeBut = wx.Button(self,label = "File To DNA(Encode)")
		self.decodeBut = wx.Button(self,label = "DNA To File(Decode)")
		self.vBox.Add(self.encodeBut,flag =  wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL ,border = 10,proportion = 1)
		self.vBox.Add(self.decodeBut,flag =  wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL ,border = 10,proportion = 1)
		
		self.SetSizer(self.vBox)
		self.SetSize((300,150))
		
		
class memEstimator(wx.Dialog):
	def __init__(self,parent,id,title):
		wx.Dialog.__init__(self,parent,id,title)
		self.vBox = wx.BoxSizer(wx.VERTICAL)
		
		ico = wx.Icon(PATH + '/../icons/DNAicon.ico', wx.BITMAP_TYPE_ICO)
		self.SetIcon(ico)
		head = wx.StaticText(self ,label = "Estimate the numbers",style = wx.ALIGN_CENTER_HORIZONTAL)
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.vBox.Add(head ,flag = wx.EXPAND | wx.TOP | wx.LEFT , border = 5)
		
		line1 = wx.StaticLine(self, size=(300,1) , style = wx.ALIGN_CENTRE)
		self.vBox.Add(line1, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 15)
		
		self.hBox = wx.BoxSizer(wx.HORIZONTAL)
		self.butChoose = wx.Button(self , label = "Choose File")
		self.hBox.Add(self.butChoose,flag = wx.EXPAND | wx.LEFT | wx.RIGHT , border = 10,proportion = 1)
		path = wx.StaticText(self, label = "Select a File from your File System")
		self.hBox.Add(path,flag = wx.EXPAND,proportion = 2)
		self.vBox.Add(self.hBox)
		
		self.txt = wx.TextCtrl(self,name = "hBox",size = (200,250),style= wx.TE_READONLY | wx.TE_MULTILINE)
		self.vBox.Add(self.txt,flag = wx.EXPAND | wx.ALL , border = 10)
		
		head = wx.StaticText(self ,label = "Disclaimer:This values are just an approximation,the actual\nvalues may vary",style = wx.ALIGN_CENTRE_HORIZONTAL)
		font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		#head.Wrap(440)
		self.vBox.Add(head ,flag = wx.TOP | wx.LEFT, border = 10)
		
		line2 = wx.StaticLine(self, size=(300,1) , style = wx.ALIGN_CENTRE)
		self.vBox.Add(line2, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 15)
		
		self.butOk = wx.Button(self , label = "OK")
		self.vBox.Add(self.butOk,flag = wx.ALIGN_CENTER_HORIZONTAL)
		
		self.SetSizer(self.vBox)
		self.SetSize((370,470))
		
		self.butChoose.Bind(wx.EVT_BUTTON,self.onChoose)
		self.butOk.Bind(wx.EVT_BUTTON,self.ok)

	def onChoose(self,e):
		self.txt.Clear()
		fileSelector = wx.FileDialog(self, message="Choose a file",defaultFile="",style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR )
		if fileSelector.ShowModal() == wx.ID_OK:
			paths = fileSelector.GetPaths()
			path = paths[0]
                        length = os.path.getsize(path)
                        dnaLength = int(5.5 * length)
                        dnaStringMem = 6 * length
        		dnaStringMem = dnaStringMem/CHUNK_SIZE
                	if dnaStringMem == 0:
                        	dnaStringMem = 1
                        dnaListMem = (((dnaLength)/25) - 3) * 117
                        dnaListMem = dnaListMem/CHUNK_SIZE
                        if dnaListMem == 0:
                                dnaListMem = 1
                        errorCorrectionMem = 15 * length
        		line1 = "File Size(bytes) : \t\t" +  `length`
                	line2 = "Size of DNA String : \t" + `dnaLength`
                        line3 = "Free Memory Required : \n" + "To genrate DNA String :\t" +  `dnaStringMem` + "MB\n" + "To generate DNA Chunks :\t" + `dnaListMem` + "MB\n"
        		line4 = "Amount of DNA Required : \t" + `length / (10.0 ** 20)`
                	text = line1 + "\n\n" + line2 + "\n\n" + line3 + "\n\n" + line4 + " gms\n\n" + "File Selected : " + path
                        self.txt.WriteText(text)
		fileSelector.Destroy()
		
		

	def ok(self,e):
		self.Destroy()
		
		
class estimator(wx.Dialog):
	def __init__(self,parent,id,title):
		wx.Dialog.__init__(self,parent,id,title)
		
		self.vBox = wx.BoxSizer(wx.VERTICAL)
		ico = wx.Icon(PATH + '/../icons/DNAicon.ico', wx.BITMAP_TYPE_ICO)
		self.SetIcon(ico)
		head = wx.StaticText(self ,label = "Estimate properties",style = wx.ALIGN_CENTER_HORIZONTAL)
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.vBox.Add(head ,flag = wx.EXPAND | wx.TOP | wx.LEFT , border = 5)
		
		line1 = wx.StaticLine(self, size=(300,1) , style = wx.ALIGN_CENTRE)
		self.vBox.Add(line1, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 10)
		
		self.hBox = wx.BoxSizer(wx.HORIZONTAL)
		self.butChoose = wx.Button(self , label = "Choose File")
		self.hBox.Add(self.butChoose,flag = wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL , border = 10,proportion = 1)
		path = wx.StaticText(self, label = "Select a DNA File from your File System",style = wx.ALIGN_CENTER_VERTICAL)
		self.hBox.Add(path,flag = wx.ALIGN_CENTER_VERTICAL,proportion = 2)
		self.vBox.Add(self.hBox)
		
		self.hBox1 = wx.BoxSizer(wx.HORIZONTAL)
		text1 = wx.StaticText(self, label = "  Enter salt concentration(mM) :",style = wx.ALIGN_CENTER)
		self.saltText = wx.TextCtrl(self,name = "Salt Concentration")
		self.hBox1.Add(text1, 1, wx.EXPAND)
		self.hBox1.Add(self.saltText, 2, wx.EXPAND | wx.LEFT , border = 15)
		self.vBox.Add(self.hBox1,flag = wx.TOP | wx.BOTTOM , border = 5)

		self.hBox2 = wx.BoxSizer(wx.HORIZONTAL)
		text1 = wx.StaticText(self, label = "  Enter cost for a base($) : \t\t",style = wx.ALIGN_CENTER)
		self.priceText = wx.TextCtrl(self,name = "Price")
		self.hBox2.Add(text1, 1, wx.EXPAND)
		self.hBox2.Add(self.priceText, 2, wx.EXPAND | wx.LEFT, border = 15)
		self.vBox.Add(self.hBox2,flag = wx.TOP | wx.BOTTOM , border = 5)
		
		line2 = wx.StaticLine(self, size=(300,1) , style = wx.ALIGN_CENTRE)
		self.vBox.Add(line2, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 15)
		
		self.txt = wx.TextCtrl(self,name = "hBox",size = (200,250),style= wx.TE_READONLY | wx.TE_MULTILINE)
		self.vBox.Add(self.txt,flag = wx.EXPAND | wx.ALL , border = 10)
		
		head = wx.StaticText(self ,label = "Disclaimer:This values are just an approximation and the actual values may vary",style = wx.ALIGN_CENTER_HORIZONTAL)
		font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		head.SetFont(font)
		self.vBox.Add(head ,flag = wx.EXPAND | wx.TOP | wx.LEFT |wx.ALIGN_CENTER_HORIZONTAL, border = 10)
		
		line2 = wx.StaticLine(self, size=(300,1) , style = wx.ALIGN_CENTRE)
		self.vBox.Add(line2, flag = wx.EXPAND | wx.TOP | wx.BOTTOM , border = 15)
		
		self.hBox3 = wx.BoxSizer(wx.HORIZONTAL)
		self.butCalc = wx.Button(self , label = " Calculate ")
		self.butCancel = wx.Button(self, label = " Close ")
		self.butSave = wx.Button(self , label = " Save ")
		self.hBox3.Add(self.butCalc, 1, wx.RIGHT , border = 5)
		self.hBox3.Add(self.butSave, 1, wx.LEFT | wx.RIGHT , border = 5)
		self.hBox3.Add(self.butCancel, 1, wx.LEFT , border = 5)
		self.vBox.Add(self.hBox3,flag = wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.BOTTOM, border = 10)
		
		self.SetSizerAndFit(self.vBox)
		#self.SetSize((500,580))
		
		self.butChoose.Bind(wx.EVT_BUTTON,self.onChoose)
		self.butCancel.Bind(wx.EVT_BUTTON,self.onCancel)
		self.butCalc.Bind(wx.EVT_BUTTON,self.calc)
		self.butSave.Bind(wx.EVT_BUTTON,self.onSave)
		self.butSave.Disable()

	def onChoose(self,e):
		self.butSave.Disable()
		self.txt.Clear()
		self.priceText.Clear()
		self.saltText.Clear()
		
		fileSelector = wx.FileDialog(self, message="Choose a file",defaultFile="",style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR )
		if fileSelector.ShowModal() == wx.ID_OK:
			paths = fileSelector.GetPaths()
			self.path = paths[0]
		fileSelector.Destroy()
	
	def calc(self,e):
		self.txt.Clear()
		if not self.saltText.IsEmpty() and not self.priceText.IsEmpty() and ".dna" in self.path:
			"""
			tempTuple = extraModules.getGCContent(self.path)
			noOfGCPairs = tempTuple[0]; self.minGC = (tempTuple[1] * 100)/OLIGO_SIZE; self.maxGC = (tempTuple[2] * 100)/OLIGO_SIZE
			print tempTuple[0] , tempTuple[1] , tempTuple[2]
			totalPairs = os.path.getsize(PATH + "/../.temp/dnaString.txt")
			self.GCContent = (noOfGCPairs * 100)/totalPairs
			self.totalCost = int(self.priceText.GetString(0,self.priceText.GetLastPosition())) * totalPairs
			naContent = int(self.saltText.GetString(0,self.saltText.GetLastPosition()))
			
			self.minMeltingPoint = (81.5 + 16.6 * math.log10(naContent) + 0.41 * (self.minGC) - 600)/OLIGO_SIZE 
			self.maxMeltingPoint = (81.5 + 16.6 * math.log10(naContent) + 0.41 * (self.maxGC) - 600)/OLIGO_SIZE 
			
			self.details = "#Details for the DNA :\n\n-  GC Content(% in DNA String):\t\t\t" + `self.GCContent` + "\n-  Total Cost($ of DNA String):\t\t\t" + `self.totalCost` + "\n-   Min Melting Point(℃/nucleotide):\t" + str(self.minMeltingPoint) + "\n-   Max Melting Point(℃/nucleotide):\t" + str(self.maxMeltingPoint)
			"""
			naContent = int(self.saltText.GetString(0,self.saltText.GetLastPosition()))
			
			p = multiprocessing.Process(target = extraModules.getGCContent , args = (self.path,float(self.priceText.GetString(0,self.priceText.GetLastPosition())),naContent,) , name = "Checking Details Process")
			p.start()
			temp = wx.ProgressDialog('Please wait...','Analysing the String....This may take a while....' ,parent = self,style = wx.PD_APP_MODAL | wx.PD_CAN_ABORT)
			temp.SetSize((400,180))
			while len(multiprocessing.active_children()) != 0:
				time.sleep(0.5)
				if not temp.UpdatePulse("Analysing the File....This may take several minutes...\n\tso sit back and relax.....")[0]:
					p.terminate()
					break
			p.join()
			temp.Destroy()
			p.terminate()
			
			tempFile = open(PATH + "/../.temp/details.txt","r")
			self.details = tempFile.read()
			self.txt.WriteText(self.details)
			tempFile.close()
			self.butSave.Enable()
		else:
			wx.MessageDialog(self,'Make sure you filled the required details and .dna file is selected', 'Error',wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP).ShowModal() 
		
		
	def onSave(self,e):
		locationSelector = wx.FileDialog(self,"Please select location to save your details",style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
		if locationSelector.ShowModal() == wx.ID_OK:
			paths = locationSelector.GetPath()
			self.savePath = paths
			
			propFile = file(self.savePath + ".txt","w")
			propFile.write("\n" + self.details)
			propFile.write("\n\n\n © 2013 - GUPTA RESEARCH LABS - Generated by DNA-CLOUD")		
			
			wx.MessageDialog(self,'Details written to file', 'Info',wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP).ShowModal() 
		else:
			locationSelector.Destroy()
			del locationSelector
		
	def onCancel(self,e):
		self.Destroy()
