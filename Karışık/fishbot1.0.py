# Metin2Bot [Dreamfancy]
import grp
import chr
import player
import net
import app
import chat
import time
import chrmgr
import item
import ui
MIDDLE_BUTTON = {'default_image': 'd:/ymir work/ui/public/middle_button_01.sub',
 'over_image': 'd:/ymir work/ui/public/middle_button_02.sub',
 'down_image': 'd:/ymir work/ui/public/middle_button_03.sub'}
LARGE_BUTTON = {'default_image': 'd:/ymir work/ui/public/large_button_01.sub',
 'over_image': 'd:/ymir work/ui/public/large_button_02.sub',
 'down_image': 'd:/ymir work/ui/public/large_button_03.sub'}
if app.GetLocalePath() == 'locale/pl':
	LOCALE_KILL_FISHES = 'Zabijaj ryby'
	LOCALE_OPEN_CLAMS = 'Otwieraj ma\xb3\xbfe'
	LOCALE_DROP_DYE = 'Wyrzucaj farby'
	LOCALE_DROP_DEAD = 'Wyrz. martwe ryby'
	LOCALE_SELL_FISH = 'Sell martwe'
	LOCALE_TOOLTIP_SELL_FISH = 'Wymagany otwarty sklep'
	LOCALE_TEXT_GM = 'je\x9cli GM szepnie:'
	LOCALE_QUIT_BTN = 'Wyjd\x9f'
	LOCALE_LOGOUT_BTN = 'Wyloguj'
	LOCALE_STOPFISH_BTN = 'przesta\xf1 \xb3owi\xe6'
else:
	LOCALE_KILL_FISHES = 'Baliklari oldur'
	LOCALE_OPEN_CLAMS = 'Istiridyeleri ac'
	LOCALE_DROP_DYE = 'Sac boyalarini at'
	LOCALE_DROP_DEAD = 'Olu baliklari at'
	LOCALE_SELL_FISH = 'Olu baliklari sat'
	LOCALE_TOOLTIP_SELL_FISH = 'Marketten al'
	LOCALE_TEXT_GM = 'GM Mesaj atarsa:'
	LOCALE_QUIT_BTN = 'Sonlandir'
	LOCALE_LOGOUT_BTN = 'Cikis'
	LOCALE_STOPFISH_BTN = 'Tutmayi durdur'
HOOK_INSTALLED = 0
oldOnRecvWhisper = 0
quit_gm_whisper = 0
logout_gm_whisper = 0
MODE = 0
NAME = ''

def NewOnRecvWhisper(self, mode, name, line):
	global quit_gm_whisper
	global NAME
	global oldOnRecvWhisper
	global logout_gm_whisper
	global MODE
	oldOnRecvWhisper(self, mode, name, line)
	if name.startswith('[') or mode == chat.WHISPER_TYPE_GM:
		if quit_gm_whisper == 1:
			app.Exit()
		if logout_gm_whisper == 1:
			net.SendChatPacket('/logout')
	MODE = mode
	NAME = name


def InstallHook():
	global HOOK_INSTALLED
	global oldOnRecvWhisper
	import game
	oldOnRecvWhisper = game.GameWindow.OnRecvWhisper
	game.GameWindow.OnRecvWhisper = NewOnRecvWhisper
	HOOK_INSTALLED = 1


def UninstallHook():
	global HOOK_INSTALLED
	import game
	game.GameWindow.OnRecvWhisper = oldOnRecvWhisper
	HOOK_INSTALLED = 0


class MultihackDialog(ui.ScriptWindow):
	state = 'stop'
	FishingRodTime = 0.0
	fishAgTime = 0.0
	kill_fishes = 0
	open_clams = 0
	drop_dead_fish = 0
	drop_hair_dye = 0
	sell_dead_fish = 0
	stop_gm_whisper = 0

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadGUI()
		self.LoadButtons()
		self.SetCenterPosition()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadGUI(self):
		self.WIDTH = 130
		self.HEIGH = 240
		self.TBoard = ui.BoardWithTitleBar()
		self.TBoard.SetSize(self.WIDTH, self.HEIGH)
		self.TBoard.SetCenterPosition()
		self.TBoard.AddFlag('movable')
		self.TBoard.AddFlag('float')
		self.TBoard.SetTitleName('Balik Botu')
		self.TBoard.SetCloseEvent(self.Close)
		self.TBoard.Show()

	def LoadButtons(self):
		boxList = [{'NAME': 'box1',
			'PARENT': self.TBoard,
			'X': 17,
			'Y': 75,
			'SIZE_X': 92,
			'SIZE_Y': 130,
			'COLOR': grp.GenerateColor(0.0, 0.0, 0.5, 0.3)}]
		self.boxDict = {}
		for boxData in boxList:
			box = ui.Box()
			box.SetParent(boxData['PARENT'])
			box.SetPosition(boxData['X'], boxData['Y'])
			box.SetSize(boxData['SIZE_X'], boxData['SIZE_Y'])
			box.SetColor(boxData['COLOR'])
			box.AddFlag('movable')
			box.AddFlag('float')
			box.Show()
			self.boxDict[boxData['NAME']] = box

		ToggleButtonList = [{'NAME': 'FishingBot',
			'BUTTON_NAME': 'Baslat',
			'TOOLTIP_TEXT': '',
			'PARENT': self.TBoard,
			'X': 45,
			'Y': 207,
			'EVENT_UP': self.StopFishBot,
			'EVENT_DOWN': self.StartFishBot,
			'default_image': MIDDLE_BUTTON['default_image'],
			'over_image': MIDDLE_BUTTON['over_image'],
			'down_image': MIDDLE_BUTTON['down_image']},
			{'NAME': 'kill_fishes',
			'BUTTON_NAME': LOCALE_KILL_FISHES,
			'TOOLTIP_TEXT': '',
			'PARENT': self.boxDict['box1'],
			'X': 2,
			'Y': 5,
			'EVENT_UP': self.killFishes_off,
			'EVENT_DOWN': self.killFishes_on,
			'default_image': LARGE_BUTTON['default_image'],
			'over_image': LARGE_BUTTON['over_image'],
			'down_image': LARGE_BUTTON['down_image']},
			{'NAME': 'open_clams',
			'BUTTON_NAME': LOCALE_OPEN_CLAMS,
			'TOOLTIP_TEXT': '',
			'PARENT': self.boxDict['box1'],
			'X': 2,
			'Y': 30,
			'EVENT_UP': self.openClam_off,
			'EVENT_DOWN': self.openClam_on,
			'default_image': LARGE_BUTTON['default_image'],
			'over_image': LARGE_BUTTON['over_image'],
			'down_image': LARGE_BUTTON['down_image']},
			{'NAME': 'drop_dead',
			'BUTTON_NAME': LOCALE_DROP_DEAD,
			'TOOLTIP_TEXT': '',
			'PARENT': self.boxDict['box1'],
			'X': 2,
			'Y': 55,
			'EVENT_UP': self.dropDeadFishes_off,
			'EVENT_DOWN': self.dropDeadFishes_on,
			'default_image': LARGE_BUTTON['default_image'],
			'over_image': LARGE_BUTTON['over_image'],
			'down_image': LARGE_BUTTON['down_image']},
			{'NAME': 'drop_hair_dye',
			'BUTTON_NAME': LOCALE_DROP_DYE,
			'TOOLTIP_TEXT': '',
			'PARENT': self.boxDict['box1'],
			'X': 2,
			'Y': 80,
			'EVENT_UP': self.dropHairDye_off,
			'EVENT_DOWN': self.dropHairDye_on,
			'default_image': LARGE_BUTTON['default_image'],
			'over_image': LARGE_BUTTON['over_image'],
			'down_image': LARGE_BUTTON['down_image']},
			{'NAME': 'sell_dead_fish',
			'BUTTON_NAME': LOCALE_SELL_FISH,
			'TOOLTIP_TEXT': LOCALE_TOOLTIP_SELL_FISH,
			'PARENT': self.boxDict['box1'],
			'X': 2,
			'Y': 105,
			'EVENT_UP': self.sellDeadFish_off,
			'EVENT_DOWN': self.sellDeadFish_on,
			'default_image': LARGE_BUTTON['default_image'],
				'over_image': LARGE_BUTTON['over_image'],
			'down_image': LARGE_BUTTON['down_image']}]
		TextLineList = [{'NAME': 'delay_text',
			'BUTTON_NAME': 'Gecikme:',
			'PARENT': self.TBoard,
			'X': 20,
			'Y': 50}]
		EditLineList = [{'NAME': 'delay_textbox',
			'EDIT_TEXT': '2.600',
			'PARENT': self.TBoard,
			'X': 67,
			'Y': 50,
			'SIZE_X': 35,
			'SIZE_Y': 15,
			'MAX': 5}]
		self.editlineDict = {}
		self.slotbarDict = {}
		for EditLineData in EditLineList:
			self.SlotBar = ui.SlotBar()
			self.SlotBar.SetParent(self.TBoard)
			self.SlotBar.SetSize(EditLineData['SIZE_X'], EditLineData['SIZE_Y'])
			self.SlotBar.SetPosition(EditLineData['X'], EditLineData['Y'])
			self.SlotBar.Show()
			self.Value = ui.EditLine()
			self.Value.SetParent(self.SlotBar)
			self.Value.SetSize(EditLineData['SIZE_X'], EditLineData['SIZE_Y'])
			self.Value.SetPosition(5, 1)
			self.Value.SetMax(EditLineData['MAX'])
			self.Value.SetText(EditLineData['EDIT_TEXT'])
			self.Value.Show()
			self.editlineDict[EditLineData['NAME']] = self.Value
			self.slotbarDict[EditLineData['NAME']] = self.SlotBar

		self.textDict = {}
		for TextLineData in TextLineList:
			textline = ui.TextLine()
			textline.SetParent(TextLineData['PARENT'])
			textline.SetDefaultFontName()
			textline.SetPosition(TextLineData['X'], TextLineData['Y'])
			textline.SetFeather()
			textline.SetText(TextLineData['BUTTON_NAME'])
			textline.SetOutline()
			textline.Show()
			self.textDict[TextLineData['NAME']] = textline

		self.togglebuttonDict = {}
		for ToggleBtnData in ToggleButtonList:
			tbutton = ui.ToggleButton()
			tbutton.SetParent(ToggleBtnData['PARENT'])
			tbutton.SetPosition(ToggleBtnData['X'], ToggleBtnData['Y'])
			tbutton.SetUpVisual(ToggleBtnData['default_image'])
			tbutton.SetOverVisual(ToggleBtnData['over_image'])
			tbutton.SetDownVisual(ToggleBtnData['down_image'])
			tbutton.SetText(ToggleBtnData['BUTTON_NAME'])
			tbutton.SetToolTipText(ToggleBtnData['TOOLTIP_TEXT'])
			tbutton.Show()
			self.togglebuttonDict[ToggleBtnData['NAME']] = tbutton
			tbutton.SetToggleUpEvent(ToggleBtnData['EVENT_UP'])
			tbutton.SetToggleDownEvent(ToggleBtnData['EVENT_DOWN'])

	def logout_gm(self, arg):
		global logout_gm_whisper
		if arg == 'on':
			logout_gm_whisper = 1
		elif arg == 'off':
			logout_gm_whisper = 0

	def quit_gm(self, arg):
		global quit_gm_whisper
		if arg == 'on':
			quit_gm_whisper = 1
		elif arg == 'off':
			quit_gm_whisper = 0

	def stop_gm(self, arg):
		if arg == 'on':
			self.stop_gm_whisper = 1
		elif arg == 'off':
			self.stop_gm_whisper = 0

	def StartFishBot(self):
		global MODE
		global NAME
		self.togglebuttonDict['FishingBot'].SetText('Durdur')
		self.time = float(self.editlineDict['delay_textbox'].GetText())
		if self.AddBait():
			MODE = 0
			NAME = ''
			player.SetAttackKeyState(TRUE)
			player.SetAttackKeyState(FALSE)
			self.ProcessTimeStamp = app.GetTime()
			self.state = 'waiting'

	def StopFishBot(self):
		self.togglebuttonDict['FishingBot'].SetText('Baslat')
		self.state = 'stop'
		player.SetAttackKeyState(TRUE)
		player.SetAttackKeyState(FALSE)

	def killFishes_on(self):
		self.kill_fishes = 1

	def killFishes_off(self):
		self.kill_fishes = 0

	def killFishes(self):
		for Slot in xrange(player.INVENTORY_PAGE_SIZE * 2):
			if player.GetItemIndex(Slot) in (27803, 27804, 27805, 27806, 27807, 27808, 27809, 27811, 27812, 27813, 27814, 27815, 27816, 27817, 27818, 27819, 27820, 27821, 27822, 27823, 30112):
				net.SendItemUsePacket(Slot)

	def openClam_on(self):
		self.open_clams = 1

	def openClam_off(self):
		self.open_clams = 0

	def openClams(self):
		for Slot in xrange(player.INVENTORY_PAGE_SIZE * 2):
			if player.GetItemIndex(Slot) == 27987:
				net.SendItemUsePacket(Slot)

	def dropDeadFishes_on(self):
		self.drop_dead_fish = 1

	def dropDeadFishes_off(self):
		self.drop_dead_fish = 0

	def dropDeadFishes(self):
		for Slot in xrange(player.INVENTORY_PAGE_SIZE * 2):
			if player.GetItemIndex(Slot) in (27833, 27834, 27835, 27836, 27837, 27838, 27839, 27840, 27841, 27842, 27843, 27844, 27845, 27846, 27847, 27848, 27849, 27850, 27851, 27852, 27853, 27802):
				net.SendItemDropPacket(Slot)

	def dropHairDye_on(self):
		self.drop_hair_dye = 1

	def dropHairDye_off(self):
		self.drop_hair_dye = 0

	def dropHairDye(self):
		for Slot in xrange(player.INVENTORY_PAGE_SIZE * 2):
			if player.GetItemIndex(Slot) >= 70201 and player.GetItemIndex(Slot) <= 70208:
				net.SendItemDropPacket(Slot)

	def sellDeadFish_on(self):
		self.sell_dead_fish = 1

	def sellDeadFish_off(self):
		self.sell_dead_fish = 0

	def sellDeadFish(self):
		for Slot in xrange(player.INVENTORY_PAGE_SIZE * 2):
			getItemCount = player.GetItemCount(Slot)
			if player.GetItemIndex(Slot) >= 27833 and player.GetItemIndex(Slot) <= 27853 or player.GetItemIndex(Slot) == 27802:
				net.SendShopSellPacket(Slot, getItemCount)

	def UseBait(self):
		for Slot in xrange(player.INVENTORY_PAGE_SIZE * 2):
			if player.GetItemIndex(Slot) in (27800, 27801, 27802):
				net.SendItemUsePacket(Slot)
				break

	def AddBait(self):
		Bait = player.GetItemCountByVnum
		if Bait(27800) == 0 and Bait(27801) == 0 and Bait(27802) == 0:
			self.state = 'stop'
			self.togglebuttonDict['FishingBot'].SetUp()
			self.togglebuttonDict['FishingBot'].SetText('Start')
			return 0
		self.UseBait()
		return 1

	def BubbleAppear(self):
		if chrmgr.IsPossibleEmoticon(-1) == 1:
			return 0
		else:
			return 1

	def OnUpdate(self):
		if self.state == 'start':
			if self.ProcessTimeStamp + 5.0 < app.GetTime():
				if self.AddBait():
					if self.kill_fishes == 1:
						self.killFishes()
					if self.open_clams == 1:
						self.openClams()
					if self.drop_dead_fish == 1:
						self.dropDeadFishes()
					if self.drop_hair_dye == 1:
						self.dropHairDye()
					if self.sell_dead_fish == 1:
						self.sellDeadFish()
					player.SetAttackKeyState(TRUE)
					player.SetAttackKeyState(FALSE)
					self.ProcessTimeStamp = app.GetTime()
					self.state = 'waiting'
		if self.state == 'action':
			if self.ProcessTimeStamp + self.time < app.GetTime():
				player.SetAttackKeyState(TRUE)
				player.SetAttackKeyState(FALSE)
				self.ProcessTimeStamp = app.GetTime()
				self.state = 'start'
		if self.state == 'waiting':
			if not chrmgr.IsPossibleEmoticon(-1):
				self.ProcessTimeStamp = app.GetTime() + float(app.GetRandom(0, int(0.5)))
				self.state = 'action'
			if self.ProcessTimeStamp + 40.0 < app.GetTime():
				self.ProcessTimeStamp = app.GetTime()
				self.state = 'start'
		if self.stop_gm_whisper == 1:
			if NAME.startswith('[') or MODE == chat.WHISPER_TYPE_GM:
				self.state = 'stop'

	def Close(self):
		self.kill_fishes = 0
		self.open_clams = 0
		self.drop_dead_fish = 0
		self.drop_hair_dye = 0
		self.sell_dead_fish = 0
		self.state = 'stop'
		stop_gm_whisper = 0
		if HOOK_INSTALLED == 1:
			chat.AppendChat(1, 'Hook Uninstalled')
			UninstallHook()
		else:
			chat.AppendChat(1, 'Hook Already Uninstalled')
		self.TBoard.Hide()


ItemBoard = MultihackDialog()
ItemBoard.Show()