import ui,app,chat,chr,net,player,item,skill,time,game,shop,chrmgr
import background,constInfo,miniMap,uiminimap,wndMgr,math,uiCommon,grp


from m2kmod.Modules import m2k_lib, m2k_hook, Settings, Levelbot, Buffbot, Spambot, swich, Bookreader, Soulstonereader, Shopcreator, Itemstealer, Telehack, Inventorymanager, Info, Itemcreator, EQChanger, Taubuyer
#import m2kmod_script

class M2kHackbarDialog(ui.ScriptWindow): 				
	
	Hackbar = 0
	Teleport = 0
	ShortCuts = 0
	
	comp = m2k_lib.Component()
	gnrl = Settings.SettingsDialog()
	levl = Levelbot.LevelbotDialog()
	buff = Buffbot.BuffDialog()
	spam = Spambot.SpamDialog()
	
	book = Bookreader.BookReaderDialog()
	soul = Soulstonereader.SoulStoneBotDialog()
	shop = Shopcreator.ShopDialog()
	steal = Itemstealer.ItemStealerDialog()
	tele = Telehack.TeleportHackDialog()
	inve = Inventorymanager.InventoryDialog()
	swch = swich.Bot()
	
	def __init__(self):
		self.m2kBoard = ui.ThinBoard() 
		self.m2kBoard.SetPosition(0, 40)
		self.m2kBoard.SetSize(51, 560) 
		self.m2kBoard.AddFlag("float") 
		self.m2kBoard.AddFlag("movable")
		self.m2kBoard.Hide()
		
		self.ShowHackbarButton = self.comp.Button(None, '', 'Show Hackbar', wndMgr.GetScreenWidth()-99, 260, self.OpenHackbar, 'm2kmod/Images/Shortcuts/show_0.tga', 'm2kmod/Images/Shortcuts/show_1.tga', 'm2kmod/Images/Shortcuts/show_0.tga')
		self.HideHackbarButton = self.comp.HideButton(None, '', 'Hide Hackbar', wndMgr.GetScreenWidth()-99, 260, self.OpenHackbar, 'm2kmod/Images/Shortcuts/hide_0.tga', 'm2kmod/Images/Shortcuts/hide_1.tga', 'm2kmod/Images/Shortcuts/hide_0.tga')
		self.ShortCutButton = self.comp.Button(None, '', 'ShortCuts', wndMgr.GetScreenWidth()-62, 260, self.OpenShortCuts, 'm2kmod/Images/Shortcuts/shortcut_0.tga', 'm2kmod/Images/Shortcuts/shortcut_1.tga', 'm2kmod/Images/Shortcuts/shortcut_0.tga')
		
		self.GhostButton = self.comp.HideButton(None, '', 'Ghostmod', wndMgr.GetScreenWidth()-115, 310, self.GhostMod, 'm2kmod/Images/Shortcuts/ghost_0.tga', 'm2kmod/Images/Shortcuts/ghost_1.tga', 'm2kmod/Images/Shortcuts/ghost_0.tga')
		self.TeleportButton = self.comp.HideButton(None, '', 'Teleporthack', wndMgr.GetScreenWidth()-80, 310, self.OpenTeleport, 'm2kmod/Images/Shortcuts/tele_0.tga', 'm2kmod/Images/Shortcuts/tele_1.tga', 'm2kmod/Images/Shortcuts/tele_0.tga')
		self.CrashButton = self.comp.HideButton(None, '', 'Exit', wndMgr.GetScreenWidth()-45, 310, self.CloseRequest, 'm2kmod/Images/Shortcuts/close_0.tga', 'm2kmod/Images/Shortcuts/close_1.tga', 'm2kmod/Images/Shortcuts/close_0.tga')
		self.ZoomButton = self.comp.HideButton(None, '', 'Zoom-Hack', wndMgr.GetScreenWidth()-115, 350, self.Zoom, 'm2kmod/Images/Shortcuts/zoom_0.tga', 'm2kmod/Images/Shortcuts/zoom_1.tga', 'm2kmod/Images/Shortcuts/zoom_0.tga')
		self.NoFogButton = self.comp.HideButton(None, '', 'No-Fog', wndMgr.GetScreenWidth()-80, 350, self.NoFog, 'm2kmod/Images/General/nofog_0.tga', 'm2kmod/Images/General/nofog_1.tga', 'm2kmod/Images/General/nofog_0.tga')
		self.RunPythonButton = self.comp.HideButton(None, '', 'Run-Python', wndMgr.GetScreenWidth()-45, 350, self.RunPython, 'm2kmod/Images/Shortcuts/loadpy_0.tga', 'm2kmod/Images/Shortcuts/loadpy_1.tga', 'm2kmod/Images/Shortcuts/loadpy_0.tga')
		
		
		
		self.SpamtextCombo = self.comp.ComboBox(None, 'Text 1', wndMgr.GetScreenWidth()-70, 490, 55)
		SpamList = ("Text 1", "Text 2", "Text 3", "Text 4", "Text 5", "Text 6", "Text 7", "Text 8")
		for text in SpamList:
			self.SpamtextCombo.InsertItem(0, text)
		self.SpamtextCombo.Hide()
		self.SpamTextButton = self.comp.HideButton(None, '', 'Spam-Text', wndMgr.GetScreenWidth()-115, 480, lambda : self.SpamText(), 'm2kmod/Images/Hackbar/spam_0.tga', 'm2kmod/Images/Hackbar/spam_1.tga', 'm2kmod/Images/Hackbar/spam_0.tga')
		
		self.GoForward = self.comp.HideButton(None, '', '', wndMgr.GetScreenWidth()-230, -2, lambda : self.TeleportInDirection(1), 'm2kmod/Images/Shortcuts/Arrow/tele_up_0.tga', 'm2kmod/Images/Shortcuts/Arrow/tele_up_1.tga', 'm2kmod/Images/Shortcuts/Arrow/tele_up_0.tga')
		self.GoBack = self.comp.HideButton(None, '', '', wndMgr.GetScreenWidth()-229, 92, lambda : self.TeleportInDirection(2), 'm2kmod/Images/Shortcuts/Arrow/tele_down_0.tga', 'm2kmod/Images/Shortcuts/Arrow/tele_down_1.tga', 'm2kmod/Images/Shortcuts/Arrow/tele_down_0.tga')
		self.GoRight = self.comp.HideButton(None, '', '', wndMgr.GetScreenWidth()-196, 58, lambda : self.TeleportInDirection(3), 'm2kmod/Images/Shortcuts/Arrow/tele_right_0.tga', 'm2kmod/Images/Shortcuts/Arrow/tele_right_1.tga', 'm2kmod/Images/Shortcuts/Arrow/tele_right_0.tga')
		self.GoLeft = self.comp.HideButton(None, '', '', wndMgr.GetScreenWidth()-290, 59, lambda : self.TeleportInDirection(4), 'm2kmod/Images/Shortcuts/Arrow/tele_left_0.tga', 'm2kmod/Images/Shortcuts/Arrow/tele_left_1.tga', 'm2kmod/Images/Shortcuts/Arrow/tele_left_0.tga')
		
		self.SettingsButton = self.comp.Button(self.m2kBoard, '', 'Settings', 9, 10, self.Generel, 'm2kmod/Images/Hackbar/sett_0.tga', 'm2kmod/Images/Hackbar/sett_1.tga', 'm2kmod/Images/Hackbar/sett_2.tga')
		self.LevelbotButton = self.comp.Button(self.m2kBoard, '', 'Levelbot', 8, 43, self.Levelbot, 'm2kmod/Images/Hackbar/sword_0.tga', 'm2kmod/Images/Hackbar/sword_1.tga', 'm2kmod/Images/Hackbar/sword_0.tga')
		self.BuffbotButton = self.comp.Button(self.m2kBoard, '', 'Buffbot', 8, 78, self.BuffBot, 'm2kmod/Images/Hackbar/buff_0.tga', 'm2kmod/Images/Hackbar/buff_1.tga', 'm2kmod/Images/Hackbar/buff_0.tga')
		self.SpambotButton = self.comp.Button(self.m2kBoard, '', 'Spambot', 8, 113, self.Spambot, 'm2kmod/Images/Hackbar/spam_0.tga', 'm2kmod/Images/Hackbar/spam_1.tga', 'm2kmod/Images/Hackbar/spam_0.tga')
		self.SwichbotButton = self.comp.Button(self.m2kBoard, '', 'Swichbot', 8, 148, self.Swichbot, 'm2kmod/Images/Hackbar/swich_0.tga', 'm2kmod/Images/Hackbar/swich_1.tga', 'm2kmod/Images/Hackbar/swich_0.tga')
		self.FBButton = self.comp.Button(self.m2kBoard, '', 'BookReader', 8, 183, self.BookReader, 'm2kmod/Images/Hackbar/fb_0.tga', 'm2kmod/Images/Hackbar/fb_1.tga', 'm2kmod/Images/Hackbar/fb_0.tga')
		self.SeliButton = self.comp.Button(self.m2kBoard, '', 'SoulReader', 8, 218, self.SoulstoneReader, 'm2kmod/Images/Hackbar/seli_0.tga', 'm2kmod/Images/Hackbar/seli_1.tga', 'm2kmod/Images/Hackbar/seli_0.tga')
		self.BuyTauButton = self.comp.Button(self.m2kBoard, '', 'Tau-Buyer', 8, 253, self.BuyTau, 'm2kmod/Images/Hackbar/tau_0.tga', 'm2kmod/Images/Hackbar/tau_1.tga', 'm2kmod/Images/Hackbar/tau_0.tga')
		self.ShopCreator = self.comp.Button(self.m2kBoard, '', 'Shopbot', 8, 288, self.ShopCreator, 'm2kmod/Images/Hackbar/shop_0.tga', 'm2kmod/Images/Hackbar/shop_1.tga', 'm2kmod/Images/Hackbar/shop_0.tga')
		self.ItemstealerCreator = self.comp.Button(self.m2kBoard, '', 'Itemstealer', 10, 325, self.Itemstealer, 'm2kmod/Images/Hackbar/pickup_0.tga', 'm2kmod/Images/Hackbar/pickup_1.tga', 'm2kmod/Images/Hackbar/pickup_0.tga')
		self.TeleButton = self.comp.Button(self.m2kBoard, '', 'Teleport', 10, 360, self.TeleportHack, 'm2kmod/Images/Hackbar/teleport_0.tga', 'm2kmod/Images/Hackbar/teleport_1.tga', 'm2kmod/Images/Hackbar/teleport_0.tga')
		self.InventoryButton = self.comp.Button(self.m2kBoard, '', 'Manager', 10, 395, self.InventoryManager, 'm2kmod/Images/Hackbar/inventory_0.tga', 'm2kmod/Images/Hackbar/inventory_1.tga', 'm2kmod/Images/Hackbar/inventory_0.tga')
		self.ItemCreatorButton = self.comp.Button(self.m2kBoard, '', 'ItemCreator', 8, 428, self.ItemCreator, 'm2kmod/Images/Hackbar/itemc_0.tga', 'm2kmod/Images/Hackbar/itemc_1.tga', 'm2kmod/Images/Hackbar/itemc_0.tga')
		self.EQChangerButton = self.comp.Button(self.m2kBoard, '', 'EQ-Changer', 8, 463, self.EQChanger, 'm2kmod/Images/Hackbar/eqchanger_0.tga', 'm2kmod/Images/Hackbar/eqchanger_1.tga', 'm2kmod/Images/Hackbar/eqchanger_0.tga')
	#	self.AlchemistBotButton = self.comp.Button(self.m2kBoard, '', 'Alchemist', 10, 500, self.Alchemist, 'm2kmod/Images/Hackbar/energy_0.tga', 'm2kmod/Images/Hackbar/energy_1.tga', 'm2kmod/Images/Hackbar/energy_0.tga')
		self.InfoButton = self.comp.Button(self.m2kBoard, '', 'Info', 10, 500, self.Info, 'm2kmod/Images/Hackbar/info_0.tga', 'm2kmod/Images/Hackbar/info_1.tga', 'm2kmod/Images/Hackbar/info_0.tga')
		self.CopyrightLabel = self.comp.TextLine(self.m2kBoard, '(c)123klo', 7, 540, self.comp.RGB(255, 255, 0))
	
	def OpenHackbar(self):
		if player.GetName() == "":
			#return
			pass
		self.item = Itemcreator.CreateItemDialog()
		self.equi = EQChanger.EquipmentDialog()
		self.buyer = Taubuyer.TauAutobuyDialog()
		if self.Hackbar:
			self.Hackbar = 0
			self.ShowHackbarButton.Show()
			self.HideHackbarButton.Hide()
			self.m2kBoard.Hide()
		else:	
			self.Hackbar = 1
			self.ShowHackbarButton.Hide()
			self.HideHackbarButton.Show()
			self.m2kBoard.Show()
			
	def OpenTeleport(self):
		if self.Teleport:
			self.Teleport = 0
			self.GoForward.Hide()
			self.GoBack.Hide()
			self.GoRight.Hide()
			self.GoLeft.Hide()
		else:	
			self.Teleport = 1
			self.GoForward.Show()
			self.GoBack.Show()
			self.GoRight.Show()
			self.GoLeft.Show()
			
			
	def OpenShortCuts(self):
		if player.GetName() == "":
			#return
			pass
		if self.ShortCuts:
			self.ShortCuts = 0
			self.GhostButton.Hide()
			self.CrashButton.Hide()
			self.TeleportButton.Hide()
			self.ZoomButton.Hide()
			self.NoFogButton.Hide()
			self.RunPythonButton.Hide()
			self.SpamTextButton.Hide()
			self.SpamtextCombo.Hide()
		else:	
			self.ShortCuts = 1	
			self.GhostButton.Show()
			self.CrashButton.Show()
			self.TeleportButton.Show()
			self.ZoomButton.Show()
			self.NoFogButton.Show()
			self.RunPythonButton.Show()
			self.SpamTextButton.Show()
			self.SpamtextCombo.Show()
		
	def Generel(self):
		self.gnrl.switch_state()
	def Levelbot(self):
		self.levl.switch_state()
	def BuffBot(self):
		self.buff.switch_state()
	def Spambot(self):	
		self.spam.switch_state()
	def Swichbot(self):
		self.swch.switch_state()
	def BookReader(self):
		self.book.switch_state()
	def SoulstoneReader(self):
		self.soul.switch_state()
	def BuyTau(self): 
		self.buyer.switch_state()
	def ShopCreator(self):
		self.shop.switch_state()
	def Itemstealer(self):
		self.steal.switch_state()
	def TeleportHack(self):
		self.tele.switch_state()
	def InventoryManager(self):
		self.inve.switch_state()
	def	ItemCreator(self):
		self.item.switch_state()
	def EQChanger(self): 
		self.equi.switch_state()
	def Info(self): 
		self.Inf = Info.InfoDialog()
		self.Inf.Show()
		
	
	def GhostMod(self):
		if player.GetStatus(player.HP) < 1:
			chr.Revive()
		else:
			chat.AppendChat(7,"[m2k-Mod] You have to die and than you can restart in the Ghost-Mod!")
	
	def CloseRequest(self):
		self.QuestionDialog = uiCommon.QuestionDialog()
		self.QuestionDialog.SetText("Do You want to quit Metin2 immediately?")
		self.QuestionDialog.SetAcceptEvent(ui.__mem_func__(self.Close))
		self.QuestionDialog.SetCancelEvent(ui.__mem_func__(self.CancelQuestionDialog))
		self.QuestionDialog.Open()
	def Close(self):
		app.Abort()
	def CancelQuestionDialog(self):
		self.QuestionDialog.Close()
		self.QuestionDialog = None 
	
	def Zoom(self):
		app.SetCameraMaxDistance(12000)	
		
	def NoFog(self): 
		app.SetMinFog(12000) 	
		
	def RunPython(self): 
		m2k_lib.imp_or_reload("m2kmod_script").RunPythonCode()

	
		
	
	
	
		
	def SpamText(self):
		self.AttackSpeed = int(m2k_lib.ReadConfig("AttackSpeed"))
		Type = m2k_lib.ReadConfig("Type")
		SpamText = m2k_lib.ReadConfig("Text"+str(self.SpamtextCombo.GetSelectedIndex()+1))
		
		if Type == "Normal":
			net.SendChatPacket(str(SpamText), chat.CHAT_TYPE_TALKING)
		else: 
			net.SendChatPacket(str(SpamText), chat.CHAT_TYPE_SHOUT)
		
	def TeleportInDirection(self, direction):
		(x, y, z) = player.GetMainCharacterPosition()
		if direction == 1:
			trueX = x
			trueY = y - 2000
		elif direction == 2:
			trueX = x + 2000
			trueY = y
		elif direction == 3:
			trueX = x
			trueY = y + 2000
		elif direction == 4:
			trueX = x - 2000
			trueY = y
		chr.SetPixelPosition(int(trueX), int(trueY), int(z))
		player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
		player.SetSingleDIKKeyState(app.DIK_UP, FALSE)		
try:
	app.Shop.Close()
except:
	pass
app.Shop = M2kHackbarDialog()
