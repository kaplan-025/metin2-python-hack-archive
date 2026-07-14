# Metin2Bot [Dreamfancy]
import time
import net
import ui
import sys
import dbg
import player
import chat
import chr
import chrmgr

class bot(ui.BoardWithTitleBar):

    def __init__(self):
        ui.BoardWithTitleBar.__init__(self)
        self.BuildWindow()
        chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFF00FF00|H|h Metin2Bot - Multihack 1.0 hilesine hosgeldiniz.')

    def BuildWindow(self):
        global spambot_delay
        global exp
        global gold
        global autopott_b
        global gold_last
        global standup
        global spambot_art
        global relifed
        global spambot
        global tapfi_delay
        global autopott_r
        global exp_last
        global tapfi
        global stay_n_attack
        global autopickup
        global stay_n_attack_y
        global stay_n_attack_x
        global stay_n_attack_z
        self.SetSize(300, 400)
        self.SetCenterPosition()
        self.AddFlag('movable')
        self.AddFlag('float')
        self.SetTitleName('Multihack')
        self.SetCloseEvent(self.Hide)
        gold = 0
        gold_last = player.GetMoney()
        autopott_r = 0
        autopott_b = 0
        exp = 0
        exp_last = player.GetStatus(3)
        autopickup = 0
        standup = 0
        relifed = 0
        stay_n_attack = 0
        tapfi = 0
        tapfi_delay = 0
        stay_n_attack_x, stay_n_attack_y, stay_n_attack_z = player.GetMainCharacterPosition()
        spambot = 0
        spambot_art = 1
        spambot_delay = 15
        self.build_standup()
        self.build_warpbot()
        self.build_speedhack()
        self.build_atk_speedhack()
        self.build_charinfo()
        self.build_autopott_rot()
        self.build_autopott_blau()
        self.build_autopickup()
        self.build_stay_n_attack()
        self.build_capes()
        self.build_spambot()
        self.build_copyright()

    def build_copyright(self):
        copyright_x = 12
        copyright_y = 375
        self.copyright_text = ui.TextLine()
        self.copyright_text.SetParent(self)
        self.copyright_text.SetDefaultFontName()
        self.copyright_text.SetPosition(copyright_x, copyright_y)
        self.copyright_text.SetFeather()
        self.copyright_text.SetText('Metin2Bot (C)by Dreamfancy')
        self.copyright_text.SetFontColor(1, 0.2, 0)
        self.copyright_text.SetOutline()
        self.copyright_text.Show()

    def build_spambot(self):
        spambot_x = 10
        spambot_y = 330
        self.spambot_art_button = ui.Button()
        self.spambot_art_button.SetParent(self)
        self.spambot_art_button.SetPosition(spambot_x, spambot_y + 20)
        self.spambot_art_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
        self.spambot_art_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
        self.spambot_art_button.SetDownVisual('d:/ymir work/ui/public/large_Button_03.sub')
        self.spambot_art_button.SetEvent(self.chat_mode)
        self.spambot_art_button.SetText('Normal')
        self.spambot_art_button.Show()
        self.spambot_delay_button = ui.Button()
        self.spambot_delay_button.SetParent(self)
        self.spambot_delay_button.SetPosition(spambot_x + 90, spambot_y + 20)
        self.spambot_delay_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
        self.spambot_delay_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
        self.spambot_delay_button.SetDownVisual('d:/ymir work/ui/public/large_Button_03.sub')
        self.spambot_delay_button.SetEvent(self.delay)
        self.spambot_delay_button.SetText('Sure \xe4ndern')
        self.spambot_delay_button.Show()
        self.spambot_button = ui.Button()
        self.spambot_button.SetParent(self)
        self.spambot_button.SetPosition(spambot_x + 180, spambot_y + 20)
        self.spambot_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
        self.spambot_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
        self.spambot_button.SetDownVisual('d:/ymir work/ui/public/large_Button_03.sub')
        self.spambot_button.SetEvent(self.spamming)
        self.spambot_button.SetText('Mesaj yaz')
        self.spambot_button.Show()
        self.spambot_text_slote = ui.SlotBar()
        self.spambot_text_slote.SetParent(self)
        self.spambot_text_slote.SetSize(266, 14)
        self.spambot_text_slote.SetPosition(spambot_x + 1, spambot_y)
        self.spambot_text_slote.Show()
        self.spambot_text = ui.EditLine()
        self.spambot_text.SetParent(self.spambot_text_slote)
        self.spambot_text.SetSize(265, 18)
        self.spambot_text.SetPosition(4, 1)
        self.spambot_text.SetMax(55)
        self.spambot_text.Show()

    def spamming(self):
        global spambot
        global spambot_text
        if spambot == 0:
            if len(self.spambot_text.GetText()) < 5:
                chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFF0000|H|h Yazilacak l\xe4ngere mesaji girin.')
                return
            spambot = 1
            spambot_text = self.spambot_text.GetText()
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Metin2Bot - Spambot basariyla aktif edildi.')
            self.spambot_button.SetOverVisual('d:/ymir work/ui/public/large_Button_03.sub')
            self.spambot_button.SetUpVisual('d:/ymir work/ui/public/large_Button_03.sub')
        else:
            spambot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Metin2Bot - Spambot basariyla kapatildi.')
            self.spambot_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
            self.spambot_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')

    def delay(self):
        global spambot_delay
        if spambot_delay < 120:
            spambot_delay = spambot_delay + 5
        else:
            spambot_delay = 5
        chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFF0000|H|h Mesajlar ' + str(spambot_delay) + ' saniyede bir yazilsin.')

    def chat_mode(self):
        global spambot_art
        if spambot_art == 1:
            spambot_art = 2
            self.spambot_art_button.SetText('Lonca')
        elif spambot_art == 2:
            spambot_art = 3
            self.spambot_art_button.SetText('Grup')
        elif spambot_art == 3:
            spambot_art = 4
            self.spambot_art_button.SetText('Bagirma')
        elif spambot_art == 4:
            spambot_art = 1
            self.spambot_art_button.SetText('Normal')

    def build_capes(self):
        capes_y = 240
        capes_x = 10
        self.capes_button = ui.Button()
        self.capes_button.SetParent(self)
        self.capes_button.SetPosition(capes_x + 180, capes_y)
        self.capes_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
        self.capes_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
        self.capes_button.SetDownVisual('d:/ymir work/ui/public/large_Button_03.sub')
        self.capes_button.SetEvent(self.capes)
        self.capes_button.SetText('Mobber')
        self.capes_button.Show()
        self.capestext = ui.TextLine()
        self.capestext.SetParent(self)
        self.capestext.SetDefaultFontName()
        self.capestext.SetPosition(capes_x + 2, capes_y)
        self.capestext.SetFeather()
        self.capestext.SetText('Suresi:')
        self.capestext.SetFontColor(0.7, 0.7, 0.7)
        self.capestext.SetOutline()
        self.capestext.Show()
        self.capes_value_slote = ui.SlotBar()
        self.capes_value_slote.SetParent(self)
        self.capes_value_slote.SetSize(29, 14)
        self.capes_value_slote.SetPosition(capes_x + 65, capes_y)
        self.capes_value_slote.Show()
        self.capes_value = ui.EditLine()
        self.capes_value.SetParent(self.capes_value_slote)
        self.capes_value.SetSize(29, 18)
        self.capes_value.SetPosition(4, 1)
        self.capes_value.SetMax(3)
        self.capes_value.SetNumberMode()
        self.capes_value.SetText('15')
        self.capes_value.Show()

    def build_stay_n_attack(self):
        stay_n_attack_x = 10
        stay_n_attack_y = 206
        self.stay_and_attack_button = ui.Button()
        self.stay_and_attack_button.SetParent(self)
        self.stay_and_attack_button.SetPosition(stay_n_attack_x, stay_n_attack_y)
        self.stay_and_attack_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
        self.stay_and_attack_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
        self.stay_and_attack_button.SetDownVisual('d:/ymir work/ui/public/large_Button_03.sub')
        self.stay_and_attack_button.SetEvent(self.stay_and_attack)
        self.stay_and_attack_button.SetText('Otomatik Saldiri')
        self.stay_and_attack_button.Show()

    def stay_and_attack(self):
        global stay_n_attack_y
        global stay_n_attack_x
        global stay_n_attack
        global stay_n_attack_z
        if stay_n_attack == 0:
            stay_n_attack = 1
            stay_n_attack_x, stay_n_attack_y, stay_n_attack_z = player.GetMainCharacterPosition()
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Metin2Bot - Otomatik saldiri aktiflestirildi.')
            self.stay_and_attack_button.SetOverVisual('d:/ymir work/ui/public/large_Button_03.sub')
            self.stay_and_attack_button.SetUpVisual('d:/ymir work/ui/public/large_Button_03.sub')
            player.SetAttackKeyState(TRUE)
        else:
            stay_n_attack = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Metin2Bot - Otomatik saldiri kapatildi.')
            self.stay_and_attack_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
            self.stay_and_attack_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
            player.SetAttackKeyState(FALSE)

    def OnUpdate(self):
        global exp
        global gold
        global exp_last
        global gold_last
        global tapfi
        global stay_n_attack
        global relifed
        global spambot
        global tapfi_delay
        if spambot == 1:
            self.spam_delay()
            spambot = 2
        if stay_n_attack == 1:
            self.stay_delay()
            stay_n_attack = 2
        if autopickup == 1:
            player.PickCloseItem()
        if player.GetStatus(3) > exp_last:
            exp = exp + (player.GetStatus(3) - exp_last)
            self.exp_statistik.SetText('Bagislanacak EXP: ' + str(exp))
            exp_last = player.GetStatus(3)
        elif player.GetStatus(3) == exp_last:
            self.exp_statistik.SetText('Bagislanacak EXP: ' + str(exp))
        else:
            exp_last = 0
        if autopott_r == 1:
            self.use_red()
        if autopott_b == 1:
            self.use_blue()
        if int(player.GetStatus(player.HP)) <= 0 and standup == 1 and relifed == 0:
            self.restart_delay()
            relifed = 1
        if tapfi == 1:
            tapfi = 2
            tapfi_delay = self.capes_value.GetText()
            self.tapfi_delay()
        if player.GetMoney() > gold_last:
            gold = gold + (player.GetMoney() - gold_last)
            self.gold_statistik.SetText('Bagislanacak Yang: ' + str(gold))
            gold_last = player.GetMoney()
        elif player.GetMoney() == gold_last:
            self.gold_statistik.SetText('Bagislanacak Yang: ' + str(gold))
        else:
            gold_last = player.GetMoney()
        self.hp_statistik.SetText('Adlar: ' + str(player.GetStatus(5)) + '/' + str(player.GetStatus(6)) + ' (' + str(float(player.GetStatus(5)) / player.GetStatus(6) * 100)[:5] + '%)')

    def tapfi_delay(self):
        self.tapfi_WaitingDialog = WaitingDialog()
        self.tapfi_WaitingDialog.Open(float(tapfi_delay))
        self.tapfi_WaitingDialog.SAFE_SetTimeOverEvent(self.use_tapfi)

    def spam_delay(self):
        self.spam_WaitingDialog = WaitingDialog()
        self.spam_WaitingDialog.Open(float(spambot_delay))
        self.spam_WaitingDialog.SAFE_SetTimeOverEvent(self.send_spam)

    def send_spam(self):
        global spambot
        if spambot == 2:
            spambot = 1
            if spambot_art == 1:
                net.SendChatPacket(spambot_text)
            elif spambot_art == 2:
                net.SendChatPacket(spambot_text, chat.CHAT_TYPE_GUILD)
            elif spambot_art == 3:
                net.SendChatPacket(spambot_text, chat.CHAT_TYPE_PARTY)
            elif spambot_art == 4:
                net.SendChatPacket(spambot_text, chat.CHAT_TYPE_SHOUT)

    def use_tapfi(self):
        global tapfi
        if tapfi == 0:
            return
        tapfi = 1
        for a in range(90):
            if player.GetItemIndex(a) == 70038:
                net.SendItemUsePacket(a)
                return

        tapfi = 0
        chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Metin2Bot - Auto puller nedeniyle devre disi birakildi.')

    def stay_delay(self):
        self.stay_WaitingDialog = WaitingDialog()
        self.stay_WaitingDialog.Open(2.0)
        self.stay_WaitingDialog.SAFE_SetTimeOverEvent(self.wart_to_stay)

    def wart_to_stay(self):
        global stay_n_attack
        telestep = 1
        x_coordinate = stay_n_attack_x
        y_coordinate = stay_n_attack_y
        z_coordinate = stay_n_attack_z
        ax, ay, az = player.GetMainCharacterPosition()
        if int(x_coordinate) < int(ax):
            while int(x_coordinate) < int(ax):
                if telestep > 10:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Metin2Bot - Teleport islemi basariyla gerceklesti.')
                    return
                chr.SetPixelPosition(int(ax) - 2000, int(ay))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(x_coordinate), int(ay))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(x_coordinate) > int(ax):
            while int(x_coordinate) > int(ax):
                if telestep > 10:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Metin2Bot - Teleport islemi basariyla gerceklesti.')
                    return
                chr.SetPixelPosition(int(ax) + 2000, int(ay))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(x_coordinate), int(ay))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(y_coordinate) < int(ay):
            while int(y_coordinate) < int(ay):
                if telestep > 10:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Metin2Bot - Teleport islemi basariyla gerceklesti.')
                    return
                chr.SetPixelPosition(int(ax), int(ay) - 2000)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(ax), int(y_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(y_coordinate) > int(ay):
            while int(y_coordinate) > int(ay):
                if telestep > 10:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Metin2Bot - Teleport islemi basariyla gerceklesti.')
                    return
                chr.SetPixelPosition(int(ax), int(ay) + 2000)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(ax), int(y_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(z_coordinate) < int(az) and int(z_coordinate) != 0:
            while int(z_coordinate) < int(az):
                if telestep > 7:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Metin2Bot - Teleport islemi basariyla gerceklesti.')
                    return
                chr.SetPixelPosition(int(ax), int(ay), int(az) - 2000)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(z_coordinate) > int(az) and int(z_coordinate) != 0:
            while int(z_coordinate) > int(az):
                if telestep > 7:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Metin2Bot - Teleport islemi basariyla gerceklesti.')
                    return
                chr.SetPixelPosition(int(ax), int(ay), int(az) + 2000)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if stay_n_attack == 2:
            stay_n_attack = 1

    def restart_delay(self):
        self.restart_WaitingDialog = WaitingDialog()
        self.restart_WaitingDialog.Open(10.0)
        self.restart_WaitingDialog.SAFE_SetTimeOverEvent(self.restart)

    def restart(self):
        global relifed
        net.SendChatPacket('/restart_here')
        relifed = 0

    def build_autopickup(self):
        pickup_x = 190
        pickup_y = 206
        self.autopickup_button = ui.Button()
        self.autopickup_button.SetParent(self)
        self.autopickup_button.SetPosition(pickup_x, pickup_y)
        self.autopickup_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
        self.autopickup_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
        self.autopickup_button.SetDownVisual('d:/ymir work/ui/public/large_Button_03.sub')
        self.autopickup_button.SetEvent(self.autopickup)
        self.autopickup_button.SetText('Autopickup')
        self.autopickup_button.Show()

    def capes(self):
        global tapfi
        if tapfi == 0:
            tapfi = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Metin2Bot - Sectiginiz hile aktiflestirildi.')
            self.capes_button.SetOverVisual('d:/ymir work/ui/public/large_Button_03.sub')
            self.capes_button.SetUpVisual('d:/ymir work/ui/public/large_Button_03.sub')
        else:
            tapfi = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Metin2Bot - Sectiginiz hile kapatildi.')
            self.capes_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
            self.capes_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')

    def autopickup(self):
        global autopickup
        if autopickup == 0:
            autopickup = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Metin2Bot - Toplama hilesi aktiflestirildi.')
            self.autopickup_button.SetOverVisual('d:/ymir work/ui/public/large_Button_03.sub')
            self.autopickup_button.SetUpVisual('d:/ymir work/ui/public/large_Button_03.sub')
        else:
            autopickup = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Der Metin2Bot - Toplama hilesi kapatildi.')
            self.autopickup_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
            self.autopickup_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')

    def standup(self):
        global standup
        if standup == 0:
            standup = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Metin2Bot -  Otomatik kurtarma aktiflestirildi.')
            self.standup_button.SetOverVisual('d:/ymir work/ui/public/large_Button_03.sub')
            self.standup_button.SetUpVisual('d:/ymir work/ui/public/large_Button_03.sub')
        else:
            standup = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Metin2Bot -  Otomatik kurtarma kapatildi.')
            self.standup_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
            self.standup_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')

    def build_standup(self):
        pickup_x = 100
        pickup_y = 206
        self.standup_button = ui.Button()
        self.standup_button.SetParent(self)
        self.standup_button.SetPosition(pickup_x, pickup_y)
        self.standup_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
        self.standup_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
        self.standup_button.SetDownVisual('d:/ymir work/ui/public/large_Button_03.sub')
        self.standup_button.SetEvent(self.standup)
        self.standup_button.SetText('Tekrar')
        self.standup_button.Show()

    def build_autopott_blau(self):
        autopott_y = 300
        autopott_x = 10
        self.autopott_b_button = ui.Button()
        self.autopott_b_button.SetParent(self)
        self.autopott_b_button.SetPosition(autopott_x + 180, autopott_y)
        self.autopott_b_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
        self.autopott_b_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
        self.autopott_b_button.SetDownVisual('d:/ymir work/ui/public/large_Button_03.sub')
        self.autopott_b_button.SetEvent(self.blauer_autopott)
        self.autopott_b_button.SetText('Mavi Iksir')
        self.autopott_b_button.Show()
        self.autopot_b_text = ui.TextLine()
        self.autopot_b_text.SetParent(self)
        self.autopot_b_text.SetDefaultFontName()
        self.autopot_b_text.SetPosition(autopott_x + 2, autopott_y)
        self.autopot_b_text.SetFeather()
        self.autopot_b_text.SetText('Potten ab:                %')
        self.autopot_b_text.SetFontColor(0, 0, 1)
        self.autopot_b_text.SetOutline()
        self.autopot_b_text.Show()
        self.autopott_b_value_slote = ui.SlotBar()
        self.autopott_b_value_slote.SetParent(self)
        self.autopott_b_value_slote.SetSize(29, 14)
        self.autopott_b_value_slote.SetPosition(autopott_x + 65, autopott_y)
        self.autopott_b_value_slote.Show()
        self.autopott_b_value = ui.EditLine()
        self.autopott_b_value.SetParent(self.autopott_b_value_slote)
        self.autopott_b_value.SetSize(29, 18)
        self.autopott_b_value.SetPosition(4, 1)
        self.autopott_b_value.SetMax(2)
        self.autopott_b_value.SetNumberMode()
        self.autopott_b_value.SetText('50')
        self.autopott_b_value.Show()

    def build_autopott_rot(self):
        autopott_y = 270
        autopott_x = 10
        self.autopott_r_button = ui.Button()
        self.autopott_r_button.SetParent(self)
        self.autopott_r_button.SetPosition(autopott_x + 180, autopott_y)
        self.autopott_r_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
        self.autopott_r_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
        self.autopott_r_button.SetDownVisual('d:/ymir work/ui/public/large_Button_03.sub')
        self.autopott_r_button.SetEvent(self.roter_autopott)
        self.autopott_r_button.SetText('Kirmizi Iksir')
        self.autopott_r_button.Show()
        self.autopot_r_text = ui.TextLine()
        self.autopot_r_text.SetParent(self)
        self.autopot_r_text.SetDefaultFontName()
        self.autopot_r_text.SetPosition(autopott_x + 2, autopott_y)
        self.autopot_r_text.SetFeather()
        self.autopot_r_text.SetText('Potten ab:                %')
        self.autopot_r_text.SetFontColor(1, 0, 0)
        self.autopot_r_text.SetOutline()
        self.autopot_r_text.Show()
        self.autopott_r_value_slote = ui.SlotBar()
        self.autopott_r_value_slote.SetParent(self)
        self.autopott_r_value_slote.SetSize(29, 14)
        self.autopott_r_value_slote.SetPosition(autopott_x + 65, autopott_y)
        self.autopott_r_value_slote.Show()
        self.autopott_r_value = ui.EditLine()
        self.autopott_r_value.SetParent(self.autopott_r_value_slote)
        self.autopott_r_value.SetSize(29, 18)
        self.autopott_r_value.SetPosition(4, 1)
        self.autopott_r_value.SetMax(2)
        self.autopott_r_value.SetNumberMode()
        self.autopott_r_value.SetText('50')
        self.autopott_r_value.Show()

    def blauer_autopott(self):
        global autopott_b
        if autopott_b == 0:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Metin2Bot - Otomatik iksir basariyla aktiflestirildi.')
            self.autopott_b_button.SetUpVisual('d:/ymir work/ui/public/large_Button_03.sub')
            self.autopott_b_button.SetOverVisual('d:/ymir work/ui/public/large_Button_03.sub')
            autopott_b = 1
        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Metin2Bot - Otomatik iksir basariyla kapatildi.')
            self.autopott_b_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
            self.autopott_b_button.SetUPVisual('d:/ymir work/ui/public/large_Button_01.sub')
            autopott_b = 0

    def roter_autopott(self):
        global autopott_r
        if autopott_r == 0:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Metin2Bot - Otomatik iksir basariyla aktiflestirildi.')
            self.autopott_r_button.SetUpVisual('d:/ymir work/ui/public/large_Button_03.sub')
            self.autopott_r_button.SetOverVisual('d:/ymir work/ui/public/large_Button_03.sub')
            autopott_r = 1
        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFFFF00|H|h Metin2Bot - Otomatik iksir basariyla kapatildi.')
            self.autopott_r_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
            self.autopott_r_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
            autopott_r = 0

    def use_red(self):
        if float(player.GetStatus(5) / float(player.GetStatus(6) * 100)) > int(self.autopott_r_value.GetText()):
            for item in range(90):
                if player.GetItemIndex(item) == 27001 or player.GetItemIndex(item) == 27002 or player.GetItemIndex(item) == 27003:
                    net.SendItemUsePacket(item)

    def use_blue(self):
        if float(player.GetStatus(7) / float(player.GetStatus(8) * 100)) > int(self.autopott_b_value.GetText()):
            for item in range(90):
                if player.GetItemIndex(item) == 27004 or player.GetItemIndex(item) == 27005 or player.GetItemIndex(item) == 27006:
                    net.SendItemUsePacket(item)

    def build_charinfo(self):
        charinfo_y = 35
        charinfo_x = 10
        self.charinfo_text = ui.TextLine()
        self.charinfo_text.SetParent(self)
        self.charinfo_text.SetDefaultFontName()
        self.charinfo_text.SetPosition(charinfo_x + 2, charinfo_y)
        self.charinfo_text.SetFeather()
        self.charinfo_text.SetText('Bilgi \xfcber ' + player.GetName())
        self.charinfo_text.SetFontColor(1, 0, 0)
        self.charinfo_text.SetOutline()
        self.charinfo_text.Show()
        self.hp_statistik = ui.TextLine()
        self.hp_statistik.SetParent(self)
        self.hp_statistik.SetDefaultFontName()
        self.hp_statistik.SetPosition(charinfo_x + 2, charinfo_y + 45)
        self.hp_statistik.SetFeather()
        self.hp_statistik.SetText('Adlar: ' + str(player.GetStatus(5)) + '/' + str(player.GetStatus(6)) + ' (' + str(float(player.GetStatus(5)) / player.GetStatus(6) * 100)[:5] + '%)')
        self.hp_statistik.SetFontColor(0.9, 0.9, 0.9)
        self.hp_statistik.SetOutline()
        self.hp_statistik.Show()
        self.gold_statistik = ui.TextLine()
        self.gold_statistik.SetParent(self)
        self.gold_statistik.SetDefaultFontName()
        self.gold_statistik.SetPosition(charinfo_x + 2, charinfo_y + 15)
        self.gold_statistik.SetFeather()
        self.gold_statistik.SetText('Bagilanan Yang: ' + str(gold))
        self.gold_statistik.SetFontColor(1, 1, 1)
        self.gold_statistik.SetOutline()
        self.gold_statistik.Show()
        self.exp_statistik = ui.TextLine()
        self.exp_statistik.SetParent(self)
        self.exp_statistik.SetDefaultFontName()
        self.exp_statistik.SetPosition(charinfo_x + 2, charinfo_y + 30)
        self.exp_statistik.SetFeather()
        self.exp_statistik.SetText('Bagislanan EXP: ' + str(exp))
        self.exp_statistik.SetFontColor(1, 1, 1)
        self.exp_statistik.SetOutline()
        self.exp_statistik.Show()

    def build_atk_speedhack(self):
        speed_y = 150
        speed_x = 10
        self.atk_speedhack_text = ui.TextLine()
        self.atk_speedhack_text.SetParent(self)
        self.atk_speedhack_text.SetDefaultFontName()
        self.atk_speedhack_text.SetPosition(speed_x + 2, speed_y)
        self.atk_speedhack_text.SetFeather()
        self.atk_speedhack_text.SetText('Hizli vurma')
        self.atk_speedhack_text.SetFontColor(0.7, 0.7, 0.7)
        self.atk_speedhack_text.SetOutline()
        self.atk_speedhack_text.Show()
        self.atk_speed_value_slote = ui.SlotBar()
        self.atk_speed_value_slote.SetParent(self)
        self.atk_speed_value_slote.SetSize(29, 14)
        self.atk_speed_value_slote.SetPosition(speed_x + 65, speed_y)
        self.atk_speed_value_slote.Show()
        self.atk_speed_value = ui.EditLine()
        self.atk_speed_value.SetParent(self.atk_speed_value_slote)
        self.atk_speed_value.SetSize(29, 18)
        self.atk_speed_value.SetPosition(4, 1)
        self.atk_speed_value.SetMax(4)
        self.atk_speed_value.SetNumberMode()
        self.atk_speed_value.SetText(str(player.GetStatus(17)))
        self.atk_speed_value.Show()
        self.atk_speedhack_button = ui.Button()
        self.atk_speedhack_button.SetParent(self)
        self.atk_speedhack_button.SetPosition(speed_x + 180, speed_y - 3)
        self.atk_speedhack_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
        self.atk_speedhack_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
        self.atk_speedhack_button.SetDownVisual('d:/ymir work/ui/public/large_Button_03.sub')
        self.atk_speedhack_button.SetEvent(self.set_atkspd)
        self.atk_speedhack_button.SetText('Uygula')
        self.atk_speedhack_button.Show()

    def build_speedhack(self):
        speed_y = 120
        speed_x = 10
        self.speedhack_text = ui.TextLine()
        self.speedhack_text.SetParent(self)
        self.speedhack_text.SetDefaultFontName()
        self.speedhack_text.SetPosition(speed_x + 2, speed_y)
        self.speedhack_text.SetFeather()
        self.speedhack_text.SetText('Hizli kosma')
        self.speedhack_text.SetFontColor(0.7, 0.7, 0.7)
        self.speedhack_text.SetOutline()
        self.speedhack_text.Show()
        self.speed_value_slote = ui.SlotBar()
        self.speed_value_slote.SetParent(self)
        self.speed_value_slote.SetSize(29, 14)
        self.speed_value_slote.SetPosition(speed_x + 65, speed_y)
        self.speed_value_slote.Show()
        self.speed_value = ui.EditLine()
        self.speed_value.SetParent(self.speed_value_slote)
        self.speed_value.SetSize(29, 18)
        self.speed_value.SetPosition(4, 1)
        self.speed_value.SetMax(4)
        self.speed_value.SetNumberMode()
        self.speed_value.SetText(str(player.GetStatus(19)))
        self.speed_value.Show()
        self.speedhack_button = ui.Button()
        self.speedhack_button.SetParent(self)
        self.speedhack_button.SetPosition(speed_x + 180, speed_y - 3)
        self.speedhack_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
        self.speedhack_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
        self.speedhack_button.SetDownVisual('d:/ymir work/ui/public/large_Button_03.sub')
        self.speedhack_button.SetEvent(self.set_bewspd)
        self.speedhack_button.SetText('Uygula')
        self.speedhack_button.Show()

    def set_atkspd(self):
        if int(self.atk_speed_value.GetText()) > 1000:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFF0000|H|h Metin2Bot - Maksimum hizi 1000 olmalidir. \xfcberschreiten')
            return
        chr.SetAttackSpeed(int(self.atk_speed_value.GetText()))

    def set_bewspd(self):
        if int(self.speed_value.GetText()) > 1000:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '|cFFFF0000|H|h Metin2Bot - Maksimum hizi 1000 olmalidir. \xfcberschreiten')
            return
        chrmgr.SetMovingSpeed(int(self.speed_value.GetText()))

    def build_warpbot(self):
        warp_y = 180
        warp_x = 10
        player_x, player_y, player_z = player.GetMainCharacterPosition()
        self.warpbot_text = ui.TextLine()
        self.warpbot_text.SetParent(self)
        self.warpbot_text.SetDefaultFontName()
        self.warpbot_text.SetPosition(warp_x + 2, warp_y)
        self.warpbot_text.SetFeather()
        self.warpbot_text.SetText('Isinlan')
        self.warpbot_text.SetFontColor(0.7, 0.7, 0.7)
        self.warpbot_text.SetOutline()
        self.warpbot_text.Show()
        self.x_warp_slote = ui.SlotBar()
        self.x_warp_slote.SetParent(self)
        self.x_warp_slote.SetSize(29, 14)
        self.x_warp_slote.SetPosition(warp_x + 65, warp_y)
        self.x_warp_slote.Show()
        self.x_warp = ui.EditLine()
        self.x_warp.SetParent(self.x_warp_slote)
        self.x_warp.SetSize(29, 18)
        self.x_warp.SetPosition(4, 1)
        self.x_warp.SetMax(4)
        self.x_warp.SetNumberMode()
        self.x_warp.SetText(str(int(player_x) / 100))
        self.x_warp.Show()
        self.y_warp_slote = ui.SlotBar()
        self.y_warp_slote.SetParent(self)
        self.y_warp_slote.SetSize(29, 14)
        self.y_warp_slote.SetPosition(warp_x + 105, warp_y)
        self.y_warp_slote.Show()
        self.y_warp = ui.EditLine()
        self.y_warp.SetParent(self.y_warp_slote)
        self.y_warp.SetSize(29, 18)
        self.y_warp.SetPosition(4, 1)
        self.y_warp.SetMax(4)
        self.y_warp.SetNumberMode()
        self.y_warp.SetText(str(int(player_y) / 100))
        self.y_warp.Show()
        self.z_warp_slote = ui.SlotBar()
        self.z_warp_slote.SetParent(self)
        self.z_warp_slote.SetSize(29, 14)
        self.z_warp_slote.SetPosition(warp_x + 145, warp_y)
        self.z_warp_slote.Show()
        self.z_warp = ui.EditLine()
        self.z_warp.SetParent(self.z_warp_slote)
        self.z_warp.SetSize(29, 18)
        self.z_warp.SetPosition(4, 1)
        self.z_warp.SetMax(4)
        self.z_warp.SetNumberMode()
        self.z_warp.SetText(str(int(player_z) / 100))
        self.z_warp.Show()
        self.Warpen_button = ui.Button()
        self.Warpen_button.SetParent(self)
        self.Warpen_button.SetPosition(warp_x + 180, warp_y - 3)
        self.Warpen_button.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
        self.Warpen_button.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
        self.Warpen_button.SetDownVisual('d:/ymir work/ui/public/large_Button_03.sub')
        self.Warpen_button.SetEvent(self.warp_player_to)
        self.Warpen_button.SetText('Isinlan')
        self.Warpen_button.Show()

    def warp_player_to(self):
        telestep = 1
        x_coordinate = self.x_warp.GetText()
        y_coordinate = self.y_warp.GetText()
        z_coordinate = self.z_warp.GetText()
        x_coordinate = int(x_coordinate) * 100
        y_coordinate = int(y_coordinate) * 100
        z_coordinate = int(z_coordinate) * 100
        ax, ay, az = player.GetMainCharacterPosition()
        if int(x_coordinate) < int(ax):
            while int(x_coordinate) < int(ax):
                if telestep > 10:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Metin2Bot - Teleport islemi basariyla gerceklesti.')
                    return
                chr.SetPixelPosition(int(ax) - 2000, int(ay))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(x_coordinate), int(ay))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(x_coordinate) > int(ax):
            while int(x_coordinate) > int(ax):
                if telestep > 10:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Metin2Bot - Teleport islemi basariyla gerceklesti.')
                    return
                chr.SetPixelPosition(int(ax) + 2000, int(ay))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(x_coordinate), int(ay))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(y_coordinate) < int(ay):
            while int(y_coordinate) < int(ay):
                if telestep > 10:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Metin2Bot - Teleport islemi basariyla gerceklesti.')
                    return
                chr.SetPixelPosition(int(ax), int(ay) - 2000)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(ax), int(y_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(y_coordinate) > int(ay):
            while int(y_coordinate) > int(ay):
                if telestep > 10:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Metin2Bot - Teleport islemi basariyla gerceklesti.')
                    return
                chr.SetPixelPosition(int(ax), int(ay) + 2000)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(ax), int(y_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(z_coordinate) < int(az) and int(z_coordinate) != 0:
            while int(z_coordinate) < int(az):
                if telestep > 7:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Metin2Bot - Teleport islemi basariyla gerceklesti.')
                    return
                chr.SetPixelPosition(int(ax), int(ay), int(az) - 2000)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(z_coordinate) > int(az) and int(z_coordinate) != 0:
            while int(z_coordinate) > int(az):
                if telestep > 7:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Metin2Bot - Teleport islemi basariyla gerceklesti.')
                    return
                chr.SetPixelPosition(int(ax), int(ay), int(az) + 2000)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)


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

    def OnPressExitKey(self):
        self.Close()
        return TRUE


bot().Show()