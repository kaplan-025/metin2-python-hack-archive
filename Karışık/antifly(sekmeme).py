# AntiFly - Fake - Mode
import player,chr,chrmgr,thread,time,chat,app

class AntiFly(object):
	def __init__(self):
		self.end = 0
		#self.count = 1
	def Start(self):
		#chr.BlendLoopMotion(chr.MOTION_RUN)
		#player.SetAttackKeyState(TRUE)
		self.AttackRuns = time.clock()
		while self.end == 0:
			while app.IsPressed(app.DIK_SPACE) == 0:
				time.sleep(0.03)
			while app.IsPressed(app.DIK_SPACE) == 1:
				self.BlockFly()
			player.SetAttackKeyState(FALSE)
	def BlockFly(self):
#		chr.SetMotionMode(chr.MOTION_MODE_ONEHAND_SWORD)
		YetClock = time.clock()
		if (YetClock-self.AttackRuns) >= 0.6:
#			chr.testSetComboType(2)
			chr.SetLoopMotion(chr.MOTION_WAIT)
			self.AttackRuns = time.clock()
			player.SetAttackKeyState(TRUE)
			
def Run():
	AntiFly().Start()
thread.start_new_thread(Run,())