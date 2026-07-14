import ui,app,chat,chr,net,player,item,skill,time,game,shop,chrmgr,os
import background,constInfo,wndMgr,math,uiCommon,grp

class InfoDialog(ui.ScriptWindow): 				
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadGui()
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
	
	def LoadGui(self):
		
		self.m2kInfoBoard = ui.ThinBoard() 
		self.m2kInfoBoard.SetPosition(52,40)
		self.m2kInfoBoard.SetSize(190, 430)
	#	self.m2kInfoBoard.AddFlag("movable") 
		self.m2kInfoBoard.Show()
		
		self.comp = Component()
		self.Logo = self.comp.ExpandedImage(self.m2kInfoBoard, 34, 15, ("m2kmod/Images/logo.tga"))
		self.CloseButton = self.comp.Button(self.m2kInfoBoard, '', 'Close', 170, 8, self.Close, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
		self.txt159 = self.comp.TextLine(self.m2kInfoBoard, 'Credits:', 80, 55, self.comp.RGB(255, 255, 0))
		self.txt344 = self.comp.TextLine(self.m2kInfoBoard, 'DaRealFreak:', 8, 79, self.comp.RGB(255, 0, 0))
		self.txt345 = self.comp.TextLine(self.m2kInfoBoard, 'KaMeR1337:', 8, 99, self.comp.RGB(255, 0, 0))
		self.txt346 = self.comp.TextLine(self.m2kInfoBoard, '!Beni!:', 8, 119, self.comp.RGB(255, 0, 0))
		self.txt347 = self.comp.TextLine(self.m2kInfoBoard, 'Kamarun:', 8, 139, self.comp.RGB(255, 0, 0))
		self.txt348 = self.comp.TextLine(self.m2kInfoBoard, 'romeo79:', 8, 159, self.comp.RGB(255, 0, 0))
		self.txt314 = self.comp.TextLine(self.m2kInfoBoard, 'Many scripts are his work', 73, 79, self.comp.RGB(255, 255, 255))
		self.txt114 = self.comp.TextLine(self.m2kInfoBoard, 'Mobber-Module,GuiEditor', 73, 99, self.comp.RGB(255, 255, 255))
		self.txt214 = self.comp.TextLine(self.m2kInfoBoard, 'MobScanner,Itemstealer', 73, 119, self.comp.RGB(255, 255, 255))
		self.txt215 = self.comp.TextLine(self.m2kInfoBoard, 'Helped sometimes', 73, 139, self.comp.RGB(255, 255, 255))
		self.txt235 = self.comp.TextLine(self.m2kInfoBoard, 'Shop-Creator base', 73, 159, self.comp.RGB(255, 255, 255))
		self.txt115 = self.comp.TextLine(self.m2kInfoBoard, 'This Mod includes many scripts from ', 10, 189, self.comp.RGB(255, 255, 255))
		self.txt116 = self.comp.TextLine(self.m2kInfoBoard, 'others. I modified them and put them ', 10, 199, self.comp.RGB(255, 255, 255))
		self.txt117 = self.comp.TextLine(self.m2kInfoBoard, 'all in one mod. Please do not upload', 10, 209, self.comp.RGB(255, 255, 255))
		self.txt118 = self.comp.TextLine(self.m2kInfoBoard, 'the mod somewhere else. Anyway you  ', 10, 219, self.comp.RGB(255, 255, 255))
		self.txt119 = self.comp.TextLine(self.m2kInfoBoard, 'will have to download it every sunday ', 10, 229, self.comp.RGB(255, 255, 255))
		self.txt120 = self.comp.TextLine(self.m2kInfoBoard, 'because I want to finance the project.', 10, 239, self.comp.RGB(255, 255, 255))
		self.txt129 = self.comp.TextLine(self.m2kInfoBoard, 'Have fun with it! :)', 10, 249, self.comp.RGB(255, 255, 255))
		self.txt121 = self.comp.TextLine(self.m2kInfoBoard, 'your 123klo', 70, 262, self.comp.RGB(255, 255, 0))
	#	self.youtube = self.comp.ExpandedImage(self.m2kInfoBoard, 14, 303, ("m2kmod/Images/yt.tga"))
	#	self.elitepvpers = self.comp.ExpandedImage(self.m2kInfoBoard, 100, 300, ("m2kmod/Images/epvp.tga"))
		self.youtubebutton = self.comp.Button(self.m2kInfoBoard, 'Homepage', '', 27, 300, self.RunYT, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub','d:/ymir work/ui/public/middle_button_03.sub')
		self.epvpbutton = self.comp.Button(self.m2kInfoBoard, 'Elitepvpers', '', 100, 300, self.RunEpvp, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub','d:/ymir work/ui/public/middle_button_03.sub')
		self.faqbuttont = self.comp.Button(self.m2kInfoBoard, 'YouTube', '', 27, 340, self.FAQ, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub','d:/ymir work/ui/public/middle_button_03.sub')
		self.faqbuttont1 = self.comp.Button(self.m2kInfoBoard, 'FAQ', '', 100, 340, self.FAQ, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub','d:/ymir work/ui/public/middle_button_03.sub')
		self.CopyrightLabel = self.comp.TextLine(self.m2kInfoBoard, '(c)123klo                                      v2.3', 6, 410, self.comp.RGB(255, 255, 0))
	
	def Close(self):
		self.m2kInfoBoard.Hide()


	def RunYT(self):
		os.system("start http://www.youtube.com/user/123kloEpvp")
	def RunEpvp(self):
		os.system("start http://www.elitepvpers.com/forum/metin2-hacks-bots-cheats-exploits-macros/2313515-release-m2k-mod.html")
	def FAQ(self):
		os.system("start http://i.epvpimg.com/tBuFb.png")
class Component:
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button
	def TextLine(self, parent, textlineText, x, y, color):
		textline = ui.TextLine()
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0], color[1], color[2])
		textline.SetText(textlineText)
		textline.SetOutline()
		textline.Show()
		return textline
	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)
	def ExpandedImage(self, parent, x, y, img):
		image = ui.ExpandedImageBox()
		if parent != None:
			image.SetParent(parent)
		image.SetPosition(x, y)
		image.LoadImage(img)
		image.Show()
		return image	
	def SliderBar(self, parent, sliderPos, func, x, y):
		Slider = ui.SliderBar()
		if parent != None:
			Slider.SetParent(parent)
		Slider.SetPosition(x, y)
		Slider.SetSliderPos(sliderPos)
		Slider.Show()
		Slider.SetEvent(func)
		return Slider		
	def EditLine(self, parent, width, heigh, x, y, editlineText, max):
		Value = ui.EditLine()
		if parent != None:
			Value.SetParent(parent)
		Value.SetSize(width, heigh)
		Value.SetPosition(x, y)
		Value.SetMax(max)
		Value.SetText(editlineText)
		Value.SetNumberMode()
		Value.Show()
		return Value
	def SlotBarEditLine(self, parent, editlineText, x, y, width, heigh, max):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		Value = ui.EditLine()
		Value.SetParent(SlotBar)
		Value.SetSize(width, heigh)
		Value.SetPosition(6, 0)
		Value.SetMax(max)
		Value.SetLimitWidth(width)
		Value.SetMultiLine()
		Value.SetText(editlineText)
		Value.SetNumberMode()
		Value.Show()
		return SlotBar, Value
		
#InfoDialog().Show()
		
