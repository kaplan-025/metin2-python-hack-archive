import chatm2g as chat, playerm2g2 as player, m2netm2g as m2net
import ui,app,chr,background
from time import sleep,clock
from CY_FIX import *

class Teleport(object):
	def __init__(self,x=None,y=None,vid=None,loadnear=1):
		self.rdyY = 0
		self.rdyX = 0
		self.VidMode=0
		self.counter=0
		self.start=self.Start
		self.TarX,self.TarY,self.TarZ,self.vid,self.ln=0,0,0,0,0
		if x is None and y is None and vid is None and loadnear==1:
			pass
		else:
			self.SetMode(x,y,vid,loadnear)
		self.SendPosi = lambda bla=player.SetSingleDIKKeyState,key=app.DIK_LEFT, blax=chr.SetLoopMotion,val1=chr.MOTION_WAIT: bla(key, TRUE) == bla(key, FALSE) == blax(val1)
	def Start(self,owner=None):
		self.owner=owner
		self.isFinish = 0
		self.maxRange=1249#1649
		try:
			self.Mem.Hide()
		except:
			pass
		self.Set()
		#thread.start_new_thread(self.Set,())
	def SendPos(self):
		chr.SetLoopMotion(chr.MOTION_WAIT)
		player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
		player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
		chr.SetLoopMotion(chr.MOTION_WAIT)
		#if not self.VidMode:
		#	self.nomove.Deactiv()
	def LoadNear(self):
		chr.SetPixelPosition(self.TarX, self.TarY)
		chr.SetPixelPosition(self.TarX, self.TarY)
		player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
		time=clock()#3
		while time+5>=clock():
			self.Upda()
		player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
		chr.SetPixelPosition(int(self.TarX), int(self.TarY))
	def End(self):
		chr.SetPixelPosition(int(self.TarX), int(self.TarY))
		if self.ln!=0:
			self.LoadNear()
		else:
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
	def Set(self):
		MAP = background.GetCurrentMapName()
		px,py = player.GetMainCharacterPosition()[:2]
		px,py = int(px),int(py)
		setPosition = chr.SetPixelPosition
		chr.SelectInstance(player.GetMainCharacterIndex())
		SendPosi = self.SendPosi
		TarY = int(self.TarY)
		TarX = int(self.TarX)
		maxRange=1765
		rdyX,rdyY=0,0
		while rdyX==0 or rdyY==0:
			if not rdyY:
				if not TarY-(maxRange+1) < py < TarY+(maxRange+1):
					if py < TarY:
						py+=(maxRange)
					elif py > TarY:
						py-=(maxRange)
				else:
					maxRange=2500
					rdyY=1
			if not rdyX:
				if not TarX-(maxRange+1) < px < TarX+(maxRange+1):
					if px < TarX:
						px+=(maxRange)
					elif px > TarX:
						px-=(maxRange)
				else:
					maxRange=2500
					rdyX=1
			# SetPosition Clientside
			setPosition(px, py)
			SendPosi() # SendPositionPacket
		setPosition(TarX, TarY)
		SendPosi()
		if self.owner: self.owner.TeleportState=1
	def SetMode(self,x=None,y=None,vid=None,loadnear=1):
		# ueberladenes begin
		if chr.HasInstance(x) and vid==None:
			vid=x
			x=None
		if vid and 0<=y<=1:
			loadnear=y
			y=None
		# ueberladenes end
		self.ln=loadnear
		if vid != None:
			self.vid = vid
			self.TarX,self.TarY,self.TarZ = [int(i) for i in chr.GetPixelPosition(vid)]
			return self.TarX,self.TarY,self.TarZ
		elif x != None and y != None:
			self.vid = None
			self.TarX,self.TarY = int(x),int(y)
			return self.TarX,self.TarY,1
	def tp2dest(self,vid):
		self.ln=0
		self.vid = vid
		self.VidMode=1
		try:
			if isinstance(vid,int):
				self.TarX,self.TarY,self.TarZ = [int(i) for i in chr.GetPixelPosition(vid)]
			elif isinstance(vid,tuple):
				self.TarX,self.TarY=vid
		except:
			return
		self.TarX+=50
		self.start()
