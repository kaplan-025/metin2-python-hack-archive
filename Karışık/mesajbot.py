import ui,app,chat,chr,net,player,item,skill,time,game,shop,chrmgr,event
import background,constInfo,miniMap,uiminimap,wndMgr,math,uiCommon,grp
import m2kmod.Modules.Mobscanner

class WhisperSpammerDialog(ui.ScriptWindow): 				
	
	State = "Stop"	
	TimeStamp = 0
	Time = 30
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadGui()
		self.MobScanner = m2kmod.Modules.Mobscanner.MobScannerDialog()
		self.MobScanner.Start()
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Close(self):
		self.Board.Hide()
		
	def LoadGui(self):
	
		self.Board = ui.ThinBoard() 
		self.Board.SetCenterPosition()
		self.Board.SetSize(190, 180) 
		self.Board.AddFlag("float") 
		self.Board.AddFlag("movable")
		self.Board.Show()
		
		self.comp = Component()
		self.CloseButton = self.comp.Button(self.Board, '', 'Close', 170, 8, self.Close, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
		self.HeaderLabel = self.comp.TextLine(self.Board, 'Whisper-Spammer', 50, 8, self.comp.RGB(255, 255, 0))
		self.DelayLabel = self.comp.TextLine(self.Board, 'Delay: 30 Seconds', 20, 104, self.comp.RGB(255, 255, 255))
		
		self.StartButton = self.comp.Button(self.Board, 'Start', '', 30, 165, self.StateStart, 'd:/ymir work/ui/public/Middle_Button_01.sub', 'd:/ymir work/ui/public/Middle_Button_02.sub', 'd:/ymir work/ui/public/Middle_Button_03.sub')
		self.StopButton = self.comp.Button(self.Board, 'Stop', '', 100, 165, self.StateStop, 'd:/ymir work/ui/public/Middle_Button_01.sub', 'd:/ymir work/ui/public/Middle_Button_02.sub', 'd:/ymir work/ui/public/Middle_Button_03.sub')
		self.Slotbar, self.Edidline = self.comp.SlotBarEditLine(self.Board, 'Hey, brauche schnelles Geld, Interesse an Aura FB für 1kk?', 20, 40, 150, 55, 100)
		self.DelaySlideBar = self.comp.SliderBar(self.Board, 0.3, self.Slide, 7, 125)
		
	def Slide(self):
		self.Time = int(self.DelaySlideBar.GetSliderPos()*100)
		self.DelayLabel.SetText("Delay: "+str(self.Time)+ ' Seconds')
	def StateStart(self):
		if not self.MobScanner.runned:
			chat.AppendChat(1, "You have to wait some seconds for scannning :)")
			return
		else:
			self.MobScanner.SpamAll(self.Edidline.GetText())
			
		self.Update = WaitingDialog()			
		self.Update.Open(int(self.Time))
		self.Update.SAFE_SetTimeOverEvent(self.StateStart)
	
	def StateStop(self):
		self.Update = WaitingDialog()
		self.Update.Close()	
	
	
		
	
	
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
	def CheckButton(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
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
		#Value.SetNumberMode()
		Value.Show()
		return SlotBar, Value		

class WaitingDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self, waitTime):
		curTime = time.clock()
		self.endTime = curTime + waitTime
		self.Show()		

	def Close(self):
		self.Hide()

	def SAFE_SetTimeOverEvent(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = ui.__mem_func__(event)
		
	def OnUpdate(self):
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()
		else:
			return
		
	def OnPressExitKey(self):
		self.Close()
		return TRUE
try:
	app.Shop.Close()
except:
	pass
app.Shop = WhisperSpammerDialog()