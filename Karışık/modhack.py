#######################################################
# Metin2 | Farm | Level | Buff | Bot | (c) 2017 iPUSH #
#######################################################

import app,item,chr,net,player,time,ui,os,textTail,math

### Modules substitute ###
""" Function list """
class MyFunc:
	
	### AutoTP ###
	@staticmethod
	def autoTP(threshold):
		if (float(player.GetStatus(player.HP)) / (float(player.GetStatus(player.MAX_HP))) * 100) < int(threshold):
			if not MyFunc.useItem(27001):
				if not MyFunc.useItem(27002):
					MyFunc.useItem(27003)
	
	### AutoMP ###
	@staticmethod
	def autoMP(threshold):
		if (float(player.GetStatus(player.SP)) / (float(player.GetStatus(player.MAX_SP))) * 100) < int(threshold):
			if not MyFunc.useItem(27004):
				if not MyFunc.useItem(27005):
					MyFunc.useItem(27006)
	
	### AutoAttack ###
	@staticmethod
	def autoAttack(type):
		nearestEnemey = MyFunc.walkToEnemy(type)
		isAlive = MyFunc.isAlive(nearestEnemey)
		isInRange = player.GetCharacterDistance(nearestEnemey) < 300
		tp = (float(player.GetStatus(player.HP)) / (float(player.GetStatus(player.MAX_HP))) * 100)
		if (isAlive and isInRange) or tp < 90:
			MyFunc.setCharDirection(nearestEnemey)
			chr.SetRotation(MyFunc.getDegree(nearestEnemey))
			player.SetAttackKeyState(TRUE)
		else:
			player.SetAttackKeyState(FALSE)
	
	### Follow target ###
	targetVID = 0
	@staticmethod
	def followTar():
		if MyFunc.targetVID == 0:
			MyFunc.targetVID = player.GetTargetVID()
		player.SetTarget(MyFunc.targetVID) 
		if player.GetCharacterDistance(MyFunc.targetVID) >= 1000:
			MyFunc.charMoveToPos(MyFunc.targetVID)
			
	### Horse ###
	horseCount = 0
	@staticmethod
	def useHorse(autoAttack):
		tp = (float(player.GetStatus(player.HP)) / (float(player.GetStatus(player.MAX_HP))) * 100)
		if player.IsMountingHorse() == TRUE:
			MyFunc.horseCount = 0
			if tp > 0 and tp < 30:
				autoAttack.pauseEvent(2)
				chr.SetDirection(app.GetRandom(0,7))
				player.SetTarget(player.GetMainCharacterIndex())
				player.ClickSkillSlot(9)
		else:
			if tp > 0:
				net.SendChatPacket("/ride")
			MyFunc.horseCount += 1
		if MyFunc.horseCount > 2:
			net.SendItemUsePacket(0)
			MyFunc.horseCount = 0
	
	### BuffBot ###
	@staticmethod
	def loadBuffBot(board, horse):
		btn = []
		editline = []
		for i in xrange(1, 7, 1):
			editline.append(Gui.addEditLine(board, 50, (i * 20) + 1, 25, 16, "5", 3))
			btn.append(Gui.addToggleButton(board, str(i), 5, i * 20, "small", MyFunc.buffBot, None, 5))
			btn[i-1].setEventDownArgs(btn[i-1], editline[i-1], i, horse)
		return btn, editline
	
	@staticmethod
	def buffBot(buffBtn, buffDelay, skill, horseBtn):
		horse = False
		tp = (float(player.GetStatus(player.HP)) / (float(player.GetStatus(player.MAX_HP))) * 100)
		if player.IsSkillCoolTime(skill) == 0 and tp > 30:
			if player.IsMountingHorse() == TRUE:
				horse = True
				horseBtn.pauseEvent(2)
				net.SendChatPacket("/ride")
			MyFunc.callFnc(1, player.ClickSkillSlot, skill)
			if horse:
				MyFunc.callFnc(2, net.SendChatPacket, "/ride")
		buffBtn.setEventDelay(int(buffDelay[1].GetText()))
	
	### UseItem ###
	@staticmethod
	def showUseItem(board, btn):
		board.SetSize(130, (len(btn) + 2) * 25)
		board.Show()
	
	@staticmethod
	def addUseItem(board, btn, time):
		item.SelectItem(player.GetItemIndex(0))
		itemName = str(item.GetItemName())
		itemTime = int(time[1].GetText())
		itemID = int(player.GetItemIndex(0))
		MyFunc.writeFile("Bot-Settings.txt", itemName, itemID, itemTime)
		btn.append(Gui.addToggleButton(board, itemName, 20, (len(btn) + 2) * 25, "large", MyFunc.useItem, None, itemTime))
		btn[-1].setEventDownArgs(itemID)
		MyFunc.showUseItem(board, btn)
	
	@staticmethod
	def removeUseItem(board, btn):
		MyFunc.removeLastLines()
		btn[-1].close()
		del btn[-1]
		MyFunc.showUseItem(board, btn)
	
	@staticmethod
	def loadUseItem(board):
		settings = MyFunc.readFile("Bot-Settings.txt")
		btn = []
		count = 0
		if settings != None:
			for i in range(0,len(settings),4):
				itemName = str(settings[i].split('=')[1])
				itemID = int(settings[i+1].split('=')[1])
				itemTime = int(settings[i+2].split('=')[1])
				btn.append(Gui.addToggleButton(board, itemName, 20, (count + 2) * 25, "large", MyFunc.useItem, None, itemTime))
				btn[count].setEventDownArgs(itemID)
				count += 1
		return btn
			
	### PickUp ###
	@staticmethod
	def pickUpBot():
		try:
			for vid in MyFunc.getItemsVID():
				net.SendItemPickUpPacket(vid)
		except:
			player.PickCloseItem()
	
	### RestartHere ###
	@staticmethod
	def restartHere(autoAttack, useItemList, horse):
		if player.GetStatus(player.HP) <= 0:
			if autoAttack.getState():
				player.SetAttackKeyState(FALSE)
				autoAttack.pauseEvent(10)
			for item in useItemList:
				if item.getEventDownArgs()[0] == 70038 and item.getState():
					item.pauseEvent(10)
			net.SendChatPacket("/restart_here")
			for i in xrange(5):
				MyFunc.callFnc(1+i*0.1, net.SendItemUsePacket, i)
			if horse.getState() and player.GetStatus(player.HP) > 0:
				MyFunc.callFnc(2, net.SendChatPacket, "/ride")
				MyFunc.callFnc(4, player.ClickSkillSlot, 9)
	
	''''''''''''''''''''''''''' Misc functions '''''''''''''''''''''''''''
	
	### Call function with delay and args ###
	callFncList = []
	@staticmethod
	def callFnc(delay, fnc, *args):
		MyFunc.callFncList = [x for x in MyFunc.callFncList if not x.state]
		MyFunc.callFncList.append(CallFnc(delay, fnc, *args))
		
	### Read & write file ###
	@staticmethod
	def readFile(path):
		if(os.path.isfile(path) and os.path.getsize(path) > 0):
			f = open(path, 'r')
			return f.readlines()
		else:
			return None
	
	@staticmethod
	def writeFile(path, name, id, time):
		f = open(path, 'a')
		f.write("Name=%s\n"%(name))
		f.write("ID=%i\n"%(id))
		f.write("Time=%i\n\n"%(time))
		f.close()
	
	@staticmethod
	def removeLastLines():
		settings = MyFunc.readFile("Bot-Settings.txt")
		f = open("Bot-Settings.txt", "w")
		f.writelines(settings[:-4])
		f.close()
	
	### Use item from inventory ###
	@staticmethod	
	def useItem(itemID):
		for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				if player.GetItemIndex(i) == itemID:
					net.SendItemUsePacket(i)
					return True
	
	### Get VID of near items ###
	@staticmethod
	def getItemsVID():
		itemList = []
		for y in xrange(125,600,9):
			for x in xrange(300,825,25):
					iVID = textTail.Pick(x, y)
					if iVID != -1 and iVID not in itemList:
						itemList.append(iVID)
		return itemList
	
	### Check if target is alive ###
	@staticmethod
	def isAlive(vid):
		player.SetTarget(vid)
		if player.GetTargetVID() != 0:
			return True
	
	### Get degree in between char and target ###
	@staticmethod
	def getDegree(vid):
		mobX, mobY = chr.GetPixelPosition(vid)[:2]
		playerX, playerY = player.GetMainCharacterPosition()[:2]
		try:
			rada = 180 * (math.acos((mobY-playerY)/math.sqrt((mobX - playerX)**2 + (mobY - playerY)**2))) / math.pi + 180
			if playerX >= mobX:
				rada = 360 - rada
		except:
			rada = 0
		return rada
	
	### Char move to position and check if get stucked ###
	charIsMoving = [False]
	getStuckedCounter = 0
	@staticmethod
	def charMoveToPos(vid):
		if player.GetCharacterDistance(vid) > 500:
			MyFunc.getStuckedCounter += 1
		
		if not MyFunc.charIsMoving[0] and MyFunc.getStuckedCounter > 5:
			MyFunc.charIsMoving[0] = True
			MyFunc.getStuckedCounter = 0
			MyFunc.charMoveRandom()
			MyFunc.callFnc(2, lambda : MyFunc.charIsMoving.__setitem__(0,False))
		else:
			x, y = chr.GetPixelPosition(vid)[:2]
			myX, myY = player.GetMainCharacterPosition()[:2]
			
			if myX < x:
				x -= 135
			else:
				x += 135
			if myY < y:
				y -= 135
			else:
				y += 135
		
			chr.MoveToDestPosition(player.GetMainCharacterIndex(), x, y)
		
	### Char move random direction ###
	@staticmethod
	def charMoveRandom():
		x, y = (0, 0)
		myX, myY = player.GetMainCharacterPosition()[:2]
		
		direction = app.GetRandom(1,4)
		if direction == 1:
			x = myX
			y = myY - 1000
		elif direction == 2:
			x = myX + 1000
			y = myY
		elif direction == 3:
			x = myX
			y = myY + 1000
		elif direction == 4:
			x = myX - 1000
			y = myY
		
		chr.MoveToDestPosition(player.GetMainCharacterIndex(), x, y)
	
	### Find the vid range with the most enemys ###
	@staticmethod
	def setVidRange(type):
		start = 0
		end = 1000
		limit = 1000
		range = 50000
		minVid = 0
		maxVid = 0
		vidList = []
		
		for i in xrange(limit):
			for j in xrange(start, end):
				if chr.GetInstanceType(j) == type:
					vidList.append(j)
			start = end
			end += 1000
			if not vidList and limit < 10000:
				limit += 1000
		
		if vidList:
			common = 0
			rangeDigitNum = len(str(range))
			
			for i in xrange(1, rangeDigitNum):
				tmp = [x / (10 ** i) for x in vidList]
				common = max(set(tmp), key=tmp.count)
			
			minVid = (common * (10 ** (rangeDigitNum - 1))) - range
			maxVid = (common * (10 ** (rangeDigitNum - 1))) + range
			
			if minVid < range:
				minVid = 0
				maxVid = range * 2
		
		return minVid, maxVid
	
	### Walk to nearest enemey ###
	vidStart = 0
	vidEnd = 0
	scanRangeCounter = 0
	@staticmethod
	def walkToEnemy(type):
		enemyList = []
		nearestEnemey = 0
		
		if MyFunc.vidEnd == 0 or MyFunc.scanRangeCounter > 3:
			MyFunc.scanRangeCounter = 0
			MyFunc.vidStart, MyFunc.vidEnd = MyFunc.setVidRange(type)
		
		for i in xrange(MyFunc.vidStart, MyFunc.vidEnd):
			if chr.GetInstanceType(i) == type:
				enemyList.append(i)
		
		if enemyList:
			counter = 0
			enemyDistanceList = [player.GetCharacterDistance(enemy) for enemy in enemyList]
			while counter < len(enemyList) and not MyFunc.isAlive(nearestEnemey):
				nearestEnemey = enemyList[enemyDistanceList.index(sorted(enemyDistanceList)[counter])]
				counter += 1
			if player.GetCharacterDistance(nearestEnemey) > 200:
				MyFunc.charMoveToPos(nearestEnemey)
		else:
			app.RotateCamera(1)
			MyFunc.callFnc(4, app.RotateCamera, 0)
			MyFunc.charMoveRandom()
			MyFunc.scanRangeCounter += 1
			
		return nearestEnemey
	
	### Press an arrow key ###
	@staticmethod
	def pressArrowKey(key):
		if key == "UP":
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			MyFunc.callFnc(0.5, player.SetSingleDIKKeyState, app.DIK_UP, FALSE)
		elif key == "DOWN":
			player.SetSingleDIKKeyState(app.DIK_DOWN, TRUE)
			MyFunc.callFnc(0.5, player.SetSingleDIKKeyState, app.DIK_DOWN, FALSE)
		elif key == "RIGHT":
			player.SetSingleDIKKeyState(app.DIK_RIGHT, TRUE)
			MyFunc.callFnc(0.5, player.SetSingleDIKKeyState, app.DIK_RIGHT, FALSE)
		elif key == "LEFT":
			player.SetSingleDIKKeyState(app.DIK_LEFT, TRUE)
			MyFunc.callFnc(0.5, player.SetSingleDIKKeyState, app.DIK_LEFT, FALSE)
	
	### Set char direction ###
	@staticmethod
	def setCharDirection(vid):
		x, y = chr.GetPixelPosition(vid)[:2]
		myX, myY = player.GetMainCharacterPosition()[:2]
		rotation = app.GetCameraRotation()
		direction = ""
		
		if abs(x - myX) > abs(y - myY):
			if myX < x:
				if rotation > -45 and rotation < 45:
					direction = "RIGHT"
				elif rotation > 45 and rotation < 135:
					direction = "UP"
				elif rotation > 135 and rotation < 180 or rotation < -145 and rotation > -180:
					direction = "LEFT"
				elif rotation > -145 and rotation < -45:
					direction = "DOWN"
			else:
				if rotation > -45 and rotation < 45:
					direction = "LEFT"
				elif rotation > 45 and rotation < 135:
					direction = "DOWN"
				elif rotation > 135 and rotation < 180 or rotation < -145 and rotation > -180:
					direction = "RIGHT"
				elif rotation > -145 and rotation < -45:
					direction = "UP"
		else:
			if myY < y:
				if rotation > -45 and rotation < 45:
					direction = "DOWN"
				elif rotation > 45 and rotation < 135:
					direction = "RIGHT"
				elif rotation > 135 and rotation < 180 or rotation < -145 and rotation > -180:
					direction = "UP"
				elif rotation > -145 and rotation < -45:
					direction = "LEFT"
			else:
				if rotation > -45 and rotation < 45:
					direction = "UP"
				elif rotation > 45 and rotation < 135:
					direction = "LEFT"
				elif rotation > 135 and rotation < 180 or rotation < -145 and rotation > -180:
					direction = "DOWN"
				elif rotation > -145 and rotation < -45:
					direction = "RIGHT"
		
		MyFunc.pressArrowKey(direction)

""" Gui wrapper """
class Gui:

	@staticmethod
	def addThinBoard(parent, x, y, width, heigh):
		board = ui.ThinBoard()
		if parent != None:
			board.SetParent(parent)
		board.AddFlag('movable')
		board.AddFlag('float')
		board.SetSize(width, heigh)
		board.SetPosition(x, y)
		board.Hide()
		return board
	
	@staticmethod
	def addTextLine(parent, textlineText, x, y, color):
		textline = ui.TextLine()
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0]*255, color[1]*255, color[2]*255)
		textline.SetText(textlineText)
		textline.SetOutline()
		textline.Show()
		return textline
	
	@staticmethod
	def addEditLine(parent, x, y, width, heigh, editlineText, max):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		EditLine = ui.EditLine()
		EditLine.SetParent(SlotBar)
		EditLine.SetSize(width, heigh)
		EditLine.SetPosition(6, 2)
		EditLine.SetMax(max)
		EditLine.SetNumberMode()
		EditLine.SetText(editlineText)
		EditLine.Show()
		return SlotBar, EditLine
	
	@staticmethod
	def addButton(parent, label, x, y, size, func, *args):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual('d:/ymir work/ui/public/' + size + '_button_01.sub')
		button.SetOverVisual('d:/ymir work/ui/public/' + size + '_button_02.sub')
		button.SetDownVisual('d:/ymir work/ui/public/' + size + '_button_03.sub')
		button.SetText(label)
		button.SetEvent(func, *args)
		button.Show()
		return button

	@staticmethod
	def addToggleButton(parent, label, x, y, size, eventDown, eventUp, time):
		button = ToggleButton()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual('d:/ymir work/ui/public/' + size + '_button_01.sub')
		button.SetOverVisual('d:/ymir work/ui/public/' + size + '_button_02.sub')
		button.SetDownVisual('d:/ymir work/ui/public/' + size + '_button_03.sub')
		button.SetText(label)
		button.setEventDown(eventDown)
		button.setEventUp(eventUp)
		button.setEventDelay(time)
		button.SetToggleDownEvent(button.startEvent)
		button.SetToggleUpEvent(button.stopEvent)
		button.Show()
		return button

""" Extended ToggleButton """
class ToggleButton(ui.ToggleButton):
	
	def __init__(self):
		ui.ToggleButton.__init__(self)
		self.timer = WaitingDialog()
		self.delay = None
		self.event_down = None
		self.event_up = None
		self.eventDownArgs = None
		self.eventUpArgs = None
		self.eventDownReturnValue = None
		self.eventUpReturnValue = None
		self.state = False
		self.pause = False
		self.pauseTimer = None
		
	def __del__(self):
		ui.ToggleButton.__del__(self)
	
	def close(self):
		self.timer.Close()
		self.eventDownReturnValue = None
		self.eventUpReturnValue = None
		self.Hide()
	
	def setEventDown(self, event):
		self.event_down = event
		
	def setEventUp(self, event):
		self.event_up = event
		
	def setEventDelay(self, time):
		self.delay = time
		
	def setEventDownArgs(self, *args):
		self.eventDownArgs = args
		
	def setEventUpArgs(self, *args):
		self.eventUpArgs = args
	
	def getState(self):
		return self.state
	
	def getEventDownArgs(self):
		return self.eventDownArgs
		
	def getEventUpArgs(self):
		return self.eventUpArgs
		
	def getEventDownReturnValue(self):
		return self.eventDownReturnValue
		
	def getEventUpReturnValue(self):
		return self.eventUpReturnValue
	
	def isPause(self):
		return self.pause
	
	def pauseEvent(self, time):
		self.pause = True
		self.pauseTimer = WaitingDialog()
		self.pauseTimer.Open(time)
		self.pauseTimer.SAFE_SetTimeOverEvent(self.resumeEvent)
		
	def resumeEvent(self):
		self.pause = False
		
	def startEvent(self):
		self.state = True
		if self.event_down != None and not self.pause:
			if self.eventDownArgs != None:
				self.eventDownReturnValue = self.event_down(*self.eventDownArgs)
			else:
				self.eventDownReturnValue = self.event_down()
		if self.delay != None:
			self.timer.Open(self.delay)
			self.timer.SAFE_SetTimeOverEvent(self.startEvent)

	def stopEvent(self):
		self.state = False
		if self.event_up != None:
			if self.eventUpArgs != None:
				self.eventUpReturnValue = self.event_up(*self.eventUpArgs)
			else:
				self.eventUpReturnValue = self.event_up()
		self.timer.Close()

""" Call function with agrs and delay """
class CallFnc:

	def __init__(self, time, fnc, *args):
		self.event = fnc
		self.eventArgs = args
		self.state = False
		self.timer = WaitingDialog()
		self.timer.Open(time)
		self.timer.SAFE_SetTimeOverEvent(self.startEvent)
	
	def close(self):
		self.state = True
		self.timer.Close()
		
	def startEvent(self):
		if self.event != None:
			if self.eventArgs != None:
				self.event(*self.eventArgs)
			else:
				self.event()
		self.close()

""" Call function with delay """
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

	def Destroy(self):
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

### Main Modul ###
pos = 10

### Main ###
mainBoard = Gui.addThinBoard(None, 15, 100, 100, 220)
mainBtn = Gui.addToggleButton(None, "iPUSH", 20, 75, "large", mainBoard.Show, mainBoard.Hide, None)
# mainLabel = Gui.addTextLine(mainBoard, "iPUSH", 35, 5, (248, 24, 58))
### AutoTP ###
autoTPEditLine = Gui.addEditLine(mainBoard, 70, pos+1, 20, 16, "90", 2)
autoTPBtn = Gui.addToggleButton(mainBoard, "AutoTP", 5, pos, "middle", lambda : MyFunc.autoTP(autoTPEditLine[1].GetText()), None, 1); pos += 20
### AutoMP ###
autoMPEditLine = Gui.addEditLine(mainBoard, 70, pos+1, 20, 16, "90", 2)
autoMPBtn = Gui.addToggleButton(mainBoard, "AutoMP", 5, pos, "middle", lambda : MyFunc.autoMP(autoMPEditLine[1].GetText()), None, 1); pos += 20
### AutoAttack ###
autoAttackEditLine = Gui.addEditLine(mainBoard, 70, pos+1, 20, 16, "0", 2)	# 0 = Mobs | 2 = Metins | 6 = Players
autoAttackBtn = Gui.addToggleButton(mainBoard, "AutoAttack", 5, pos, "middle", lambda : MyFunc.autoAttack(int(autoAttackEditLine[1].GetText())), lambda : player.SetAttackKeyState(FALSE), 1); pos += 20
### Follow target ###
followTarBtn = Gui.addToggleButton(mainBoard, "Follow", 5, pos, "large", MyFunc.followTar, None, 1); pos += 20
### Horse ###
useHorseBtn = Gui.addToggleButton(mainBoard, "Horse", 5, pos, "large", lambda : MyFunc.useHorse(autoAttackBtn), None, 1); pos += 20
### BuffBot ###
buffBotBoard = Gui.addThinBoard(None, 115, 100, 85, 160)
buffBotMainBtn = Gui.addToggleButton(mainBoard, "BuffBot", 5, pos, "large", buffBotBoard.Show, buffBotBoard.Hide, None); pos += 20
buffBotBtnList, buffBotEditLineList = MyFunc.loadBuffBot(buffBotBoard, useHorseBtn)
### UseItem ###
useItemBoard = Gui.addThinBoard(None, 115, 100, 100, 200)
useItemBtnList = MyFunc.loadUseItem(useItemBoard)
useItemBtn = Gui.addToggleButton(mainBoard, "UseItem", 5, pos, "large", lambda : MyFunc.showUseItem(useItemBoard, useItemBtnList), useItemBoard.Hide, None); pos += 20
useItemEditLine = Gui.addEditLine(useItemBoard, 95, 11, 25, 16, "5", 3)
addUseItemBtn = Gui.addButton(useItemBoard, "+", 5, 10, "small", lambda : MyFunc.addUseItem(useItemBoard, useItemBtnList, useItemEditLine))
delUseItemBtn = Gui.addButton(useItemBoard, "-", 50, 10, "small", lambda : MyFunc.removeUseItem(useItemBoard, useItemBtnList))
### PickUp ###
pickUpBtn = Gui.addToggleButton(mainBoard, "PickUp", 5, pos, "large", MyFunc.pickUpBot, None, 1); pos += 20
### Restart here###
restartBtn = Gui.addToggleButton(mainBoard, "Restart", 5, pos, "large", lambda : MyFunc.restartHere(autoAttackBtn, useItemBtnList, useHorseBtn), None, 5); pos += 20
### Ghost ###
ghostBtn = Gui.addButton(mainBoard, "Ghost", 5, pos, "large", chr.Revive); pos += 20
# repeatFncs = {"TP":autoTPBtn, "MP":autoMPBtn, "Horse":useHorseBtn, "Buff":buffBotBtnList, "Items":useItemBtnList, "Attack":autoAttackBtn, "Pickup":pickUpBtn, "Follow":followTarBtn, "Restart":restartBtn}
