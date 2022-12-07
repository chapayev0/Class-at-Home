# -*- coding: utf-8 -*-

import sys
import cpuinfo
import platform
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import os
import sqlite3
from PySide2.QtMultimedia import *
from PySide2.QtMultimediaWidgets import *
from PySide2.QtWebEngineWidgets import QWebEngineView
import vlc
import threading
import time
from pyrebase import *
import base64
from Crypto import Random
from Crypto.Cipher import AES
from hashlib import sha256
import qrcode
import pyperclip
import shutil



from ui.ui_cal import *
from ui.ui_splash import *
from ui.ui_login import *


global_state = 0
ful_scrn_status = 0
splash_counter = 0
chap_id = ""
play_list_show = 0
selected_video = ""
selected_video_title = ""
video_count = 0
win_id = 0
home_image_count = 0
slide_thred_stop = 0
ful_scr = False
player_show = False
current_vol = 20
video_row_count = 0
chapter_main_vid_count = 0
main_lesson_place = 0
ps = ""
spec = ""

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s : s[0:-ord(s[-1:])]

#THIS_DIR = os.path.dirname(__file__)
#CODE_DIR = os.path.abspath(os.path.join(THIS_DIR, '..', 'ui'))
#sys.path.append(CODE_DIR)
import ui.resource_rc


firebase_cinfig = {

    "apiKey": "AIzaSyAcZB0jg_xewgeTnKDYl6sT3dLi4-Xdl18",
    "authDomain": "work-at-home-86c88.firebaseapp.com",
    "projectId": "work-at-home-86c88",
    "databaseURL": "https://work-at-home-86c88-default-rtdb.firebaseio.com/",
    "storageBucket": "work-at-home-86c88.appspot.com",
    "messagingSenderId": "1063493514846",
    "appId": "1:1063493514846:web:5add5cf06930ce300566cf",
    "measurementId": "G-NC594PL4R5"


}
class AESCipher:

    def __init__( self, key ):
        self.key = bytes(key, 'utf-8')

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] )).decode('utf8')

class Login_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.login_ui = Ui_login()
        self.login_ui.setupUi(self)


        def move_window(event):

            if event.buttons() == Qt.LeftButton:

                self.move(self.pos() + event.globalPos() - self.dragpos)
                self.dragpos = event.globalPos()
                event.accept()

        self.login_ui.frame_12.mouseMoveEvent = move_window

        #auto run

        self.login_ui.stackedWidget.setCurrentWidget(self.login_ui.welcome_page)



        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.login_ui.close_btn.clicked.connect(self.close_fun)
        self.login_ui.key_generate_btn.clicked.connect(self.gen_key_fun)
        self.login_ui.cd_key_copy_btn.clicked.connect(self.copy_clip)
        self.login_ui.qr_save_btn.clicked.connect(self.copy_to_desk)

        #self.show()

    def copy_to_desk(self):

        #os.system("copy data/qr.png %DESKTOP%/qr.png")
        source = "data\\cd_key_qr.png"

        destination = "C:" + os.environ["HOMEPATH"] + "\Desktop\cd_key_qr.png"

        print(destination)



        try:
            shutil.copy(source, destination)
            print("File copied successfully.")

        except shutil.SameFileError:
            print("Source and destination represents the same file.")


        except PermissionError:
            print("Permission denied.")

        except:
            print("Error occurred while copying file.")
    def copy_clip(self):
        pyperclip.copy(self.login_ui.cd_key_edit.text())

    def gen_key_fun(self):
        self.login_ui.stackedWidget.setCurrentWidget(self.login_ui.generate_cd_key_page)

        MainWindow.act(self)
        cipher = AESCipher(ps)
        encrypted = str(cipher.encrypt(spec)).replace("==", "")
        rep_j = encrypted.replace("j", "@")
        rep_x = rep_j.replace("x", "j")
        rep_comma = rep_x.replace("'", "")
        self.login_ui.cd_key_edit.setText(rep_comma)
        self.qr_gen(rep_comma)

    def close_fun(self):

        self.close()
        MainWindow().close()


    def mousePressEvent(self, event):

        self.dragpos = event.globalPos()

    def qr_gen(self, data):

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=4,
            border=4,
        )

        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()

        img.save('data/cd_key_qr.png')

        self.image = QImage("data/cd_key_qr.png")
        self.pixe_image1 = QPixmap.fromImage(self.image)
        self.login_ui.qr_lbl.setPixmap(self.pixe_image1)
        self.login_ui.qr_lbl.setScaledContents(True)






class Splash_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.splash = Ui_splash_window()
        self.splash.setupUi(self)

        self.login_ui = Login_window()

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)




        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.splash.splash_back.setGraphicsEffect(self.shadow)


        self.splash_timer = QtCore.QTimer()
        self.splash_timer.timeout.connect(self.progress_fun)
        self.splash_timer.start(35)


        QtCore.QTimer.singleShot(1000, lambda: self.splash.prog_lbl.setText("<strong>Loading </strong>Database"))
        QtCore.QTimer.singleShot(2000, lambda: self.splash.prog_lbl.setText("<strong>Loading </strong>Settings"))
        QtCore.QTimer.singleShot(3000, lambda: self.splash.prog_lbl.setText("<strong>Connecting  </strong>to server"))
        QtCore.QTimer.singleShot(4000, lambda: self.splash.prog_lbl.setText("<strong>Loading </strong>User Interface"))
        QtCore.QTimer.singleShot(5000, lambda: self.splash.prog_lbl.setText("<strong>Finalizing.</strong>"))
        QtCore.QTimer.singleShot(5500, lambda: self.splash.prog_lbl.setText("<strong>Finalizing..</strong>"))
        QtCore.QTimer.singleShot(6000, lambda: self.splash.prog_lbl.setText("<strong>Finalizing...</strong>"))
        QtCore.QTimer.singleShot(5000, lambda: self.splash.prog_lbl.setText("<strong>Ready to go!</strong>"))

        #self.show()

    def progress_fun(self):
        global splash_counter

        self.splash.progressBar.setValue(splash_counter)

        if splash_counter > 100:


            self.splash_timer.stop()


           # self.main_window =

            self.login_ui.show()

            #MainWindow().show()
            self.close()

        splash_counter += 1

class MainWindow(QDialog):

    fullScreenChanged = Signal(bool)

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_main_ui()
        self.ui.setupUi(self)

       # self.media_player = MediaPlayer()

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_NativeWindow)

        #window move

        def move_window(event):

            if event.buttons() == Qt.LeftButton:

                if self.return_status_max() == 1:

                    self.maxmize_fun()

                elif self.return_status_ful() ==1:

                    self.ful_scrn_fun()

                self.move(self.pos() + event.globalPos() - self.dragpos)
                self.dragpos = event.globalPos()
                event.accept()

        self.ui.top_title_bar.mouseMoveEvent = move_window

        # shadow Effects

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
#        self.ui.main_ui.setGraphicsEffect(self.shadow)

        self.shadow1 = QGraphicsDropShadowEffect(self)
        self.shadow1.setBlurRadius(10)
        self.shadow1.setXOffset(0)
        self.shadow1.setYOffset(0)
        self.shadow1.setColor(QColor(0, 0, 0, 50))

        self.shadow2 = QGraphicsDropShadowEffect(self)
        self.shadow2.setBlurRadius(10)
        self.shadow2.setXOffset(0)
        self.shadow2.setYOffset(0)
        self.shadow2.setColor(QColor(0, 0, 0, 50))

        self.shadow3 = QGraphicsDropShadowEffect(self)
        self.shadow3.setBlurRadius(10)
        self.shadow3.setXOffset(0)
        self.shadow3.setYOffset(0)
        self.shadow3.setColor(QColor(0, 0, 0, 50))

        self.shadow4 = QGraphicsDropShadowEffect(self)
        self.shadow4.setBlurRadius(10)
        self.shadow4.setXOffset(0)
        self.shadow4.setYOffset(0)
        self.shadow4.setColor(QColor(0, 0, 0, 50))

        self.shadow5 = QGraphicsDropShadowEffect(self)
        self.shadow5.setBlurRadius(10)
        self.shadow5.setXOffset(0)
        self.shadow5.setYOffset(0)
        self.shadow5.setColor(QColor(0, 0, 0, 50))

        self.shadow6 = QGraphicsDropShadowEffect(self)
        self.shadow6.setBlurRadius(10)
        self.shadow6.setXOffset(0)
        self.shadow6.setYOffset(0)
        self.shadow6.setColor(QColor(0, 0, 0, 50))

        self.shadow7 = QGraphicsDropShadowEffect(self)
        self.shadow7.setBlurRadius(10)
        self.shadow7.setXOffset(0)
        self.shadow7.setYOffset(2)
        self.shadow7.setColor(QColor(0, 0, 0, 50))
        self.ui.chapto_owerview.setGraphicsEffect(self.shadow7)

        self.shadow8 = QGraphicsDropShadowEffect(self)
        self.shadow8.setBlurRadius(10)
        self.shadow8.setXOffset(2)
        self.shadow8.setYOffset(0)
        self.shadow8.setColor(QColor(0, 0, 0, 50))

        self.shadow9 = QGraphicsDropShadowEffect(self)
        self.shadow9.setBlurRadius(10)
        self.shadow9.setXOffset(2)
        self.shadow9.setYOffset(0)
        self.shadow9.setColor(QColor(0, 0, 0, 50))

        self.shadow10 = QGraphicsDropShadowEffect(self)
        self.shadow10.setBlurRadius(10)
        self.shadow10.setXOffset(2)
        self.shadow10.setYOffset(0)
        self.shadow10.setColor(QColor(0, 0, 0, 50))

        self.shadow11 = QGraphicsDropShadowEffect(self)
        self.shadow11.setBlurRadius(10)
        self.shadow11.setXOffset(2)
        self.shadow11.setYOffset(0)
        self.shadow11.setColor(QColor(0, 0, 0, 50))


        self.ui.cf1.setGraphicsEffect(self.shadow1)
        self.ui.cf2.setGraphicsEffect(self.shadow2)
        self.ui.cf3.setGraphicsEffect(self.shadow3)
        self.ui.cf4.setGraphicsEffect(self.shadow4)
        self.ui.cf5.setGraphicsEffect(self.shadow5)
        self.ui.cf6.setGraphicsEffect(self.shadow6)

        self.ui.about_top_frm.setGraphicsEffect(self.shadow9)
        self.ui.about_bottom_frm.setGraphicsEffect(self.shadow10)
        self.ui.about_social_frm.setGraphicsEffect(self.shadow11)

        self.ui.top_title_bar.setGraphicsEffect(self.shadow7)
        self.ui.btn_container.setGraphicsEffect(self.shadow8)

        #*********Media Player*******************

        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.player.setVideoOutput(self.ui.widget)
        self.vol = 20
        self.player.setVolume(self.vol)
        self.ui.vol_slider.setValue(self.vol)
        self.ui.vol_slider.setRange(0, 100)
        self.ui.vol_slider.setFocusPolicy(Qt.NoFocus)

        # ************ new created objects**********

        self.thred1 = threading.Thread(target=self.home_slide_show )
        #self.thred1.start()
        #threading.L


        self.image = QImage(":/home_content/style/home_1.jpg")
        self.pix_image = QPixmap.fromImage(self.image)
        self.ui.home_conten_lbl.setPixmap(self.pix_image)
        self.ui.home_conten_lbl.setScaledContents(True)

        # ******** Application load time functions ********

        self.ui.pages.setCurrentWidget(self.ui.home_page)
        self.ui.play_lst_btn.hide()
        self.ui.play_list.hide()

        self.duration = 0

        #self.about_style_load()


        # web

#        self.web = self.ui.browser


        # ********* Button Commands **********

        self.ui.maxmize_btn.clicked.connect(self.maxmize_fun)
        self.ui.close_btn.clicked.connect(self.terminate_fun)
        self.ui.minimize_btn.clicked.connect(self.minimize_fun)
        self.ui.ful_scrn_btn.clicked.connect(self.ful_scrn_fun)
        self.ui.home_btn.clicked.connect(self.home_page_action)
        self.ui.chap_btn.clicked.connect(self.category_page)
        self.ui.assest_btn.clicked.connect(self.product_page)
        self.ui.about_btn.clicked.connect(self.about_page)
        self.ui.tool_btn.clicked.connect(self.setting_page)
#        self.ui.profile_btn.clicked.connect(self.user_page)
        self.ui.c_btn1.clicked.connect(self.c_btn1_action)
        self.ui.c_btn2.clicked.connect(self.c_btn2_action)
        self.ui.c_btn3.clicked.connect(self.c_btn3_action)
        self.ui.c_btn4.clicked.connect(self.c_btn4_action)
        self.ui.c_btn5.clicked.connect(self.c_btn5_action)
        self.ui.c_btn6.clicked.connect(self.c_btn6_action)

        self.ui.chapter_content_lst.itemClicked.connect(self.owerview_lst_action)
        self.ui.chap_start_btn.clicked.connect(self.chap_start_btn_action)
        self.ui.ext_btn.clicked.connect(self.terminate)
        self.ui.play_lst_btn.clicked.connect(self.play_list_btn_action)

       # self.player.positionChanged.connect(self.positionChanged)
       # self.player.durationChanged.connect(self.media_duration)

        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)
        self.player.mediaStatusChanged.connect(self.statusChanged)
        self.player.bufferStatusChanged.connect(self.bufferingProgress)
        self.ui.player_slider.sliderMoved.connect(self.seek)
#        self.player.videoAvailableChanged.connect(self.videoAvailableChanged)
#        self.ui.play_btn_3.cl
        self.ui.player_ful_scrn_btn.clicked.connect(self.ful_screen)
        self.ui.widget.keyPressEvent = self.keyPressEvent
        self.ui.widget.mouseDoubleClickEvent = self.mouseDoubleClickEven
        self.ui.vol_btn.clicked.connect(self.mute)
        self.ui.vol_slider.valueChanged.connect(self.volume_seek)
        print(self.player.volume())

        self.ui.prev_btn.clicked.connect(self.backward_video)
        self.ui.next_btn.clicked.connect(self.forward_video)
        self.ui.play_btn.clicked.connect(self.PlayPause)
        self.ui.stop_btn.clicked.connect(self.player_stop)
        #ful_scr = True
        self.act()
        self.gen_ps()

    def gen_ps(self):

        global ps

        ful = ""

        ls = [9,1,8,5,1,9,8,1]
        nam = "shashika dilhara hiruni @"

        for i in ls:

            ful = ful + str(i)

        sp = nam.split()

        ful = ful + sp[3] + sp[1]

        ps = ful


    def ret_ps(self):

        firebase = pyrebase.initialize_app(firebase_cinfig)





    def act(self):
        global ps, spec
        os_detail = str(platform.platform())
        p_node = str(platform.node())

        command_1 = "wmic csproduct get uuid"
        uuid = os.popen(command_1).read().replace("\n", "").replace("	", "").replace(" ", "").replace("UUID", "")

        command_2 = "wmic cpu get name"
        pname = os.popen(command_2).read().replace("\n", "").replace("	", "").replace(" ", "").replace("Name", "")

        command_3 = "wmic diskdrive get SerialNumber"
        hdd_serial = os.popen(command_3).read().replace("\n", "").replace("	", "").replace(" ", "").replace("SerialNumber",
                                                                                                  "").split("-")[0]

        command_4 = "wmic bios get SMBIOSBIOSVersion"
        smd_ver = os.popen(command_4).read().replace("\n", "").replace("	", "").replace(" ", "").replace(
            "SMBIOSBIOSVersion", "")

        command_5 = "wmic baseboard get serialnumber"
        mb_serial = os.popen(command_5).read().replace("\n", "").replace("	", "").replace(" ", "").replace(
            "SerialNumber", "")

        text = os_detail + "|" + "pnd:" + p_node + "|" + "mbs:" + mb_serial + "|" + "uuid:" + uuid + "|" + "pn:" + pname + "|bo:" + smd_ver + "|hd:" +hdd_serial

        rp = text.replace("Windows", "wn")
        rp1 = rp.replace("Intel", "it")
        rp2 = rp1.replace("Core", "cr")
        r3 = rp2.replace("DESKTOP", "dk")

        spec = r3


        print(r3)

    def about_style_load(self):

        path = ":/thumbnals/style/chp1.jpg"
        path1 = ":/thumbnals/style/comp.png"

        self.image = QImage(path)
        self.pix_image = QPixmap.fromImage(self.image)
        self.ui.instruct_lbl.setPixmap(self.pix_image)

        self.image1 = QImage(path1)
        self.piximage1 = QPixmap.fromImage(self.image1)
        self.ui.company_lbl.setPixmap(self.piximage1)




    def player_window_show(self):

        self.media_player.show()


    def home_slide_show_thred(self):

        global home_image_count, slide_thred_stop

        home_image_count += 1

        if home_image_count > 5:

            home_image_count = 0

        elif slide_thred_stop == 1:

            print("slidthred stopped")

        else:

            path = ":/home_content/style/home_" + str(home_image_count) + ".jpg"

            self.image = QImage(path)
            self.pix_image = QPixmap.fromImage(self.image)
            self.ui.home_conten_lbl.setPixmap(self.pix_image)
            time.sleep(5)

    def home_slide_show(self):

        global home_image_count, slide_thred_stop

        while True:
            home_image_count += 1

            if slide_thred_stop == 1:

                print("slide thred stopped")

            elif slide_thred_stop == 0:

                if home_image_count > 5:

                    home_image_count = 0
                else:

                    path = ":/home_content/style/home_" + str(home_image_count) + ".jpg"

                    self.image = QImage(path)
                    self.pix_image = QPixmap.fromImage(self.image)
                    self.ui.home_conten_lbl.setPixmap(self.pix_image)
                    time.sleep(5)
            else:

                print("thread has been breacked")
                break






    def play_list_btn_action(self):

        global chap_id, play_list_show

        if play_list_show == 0:

            play_list_show = 1

        else:

            play_list_show = 0

        if play_list_show == 1 :

            self.progress(0)
            self.ui.play_list_wid.clear()

            db = sqlite3.connect("data/chpt_dat.ire")
            db.text_factory

            sql_data = db.execute("""SELECT t_name FROM '%s'""" % (chap_id))

            for lines in sql_data:
                self.ui.play_list_wid.addItem(lines[0])

            self.ui.play_list.show()


        else:

            self.ui.play_list.hide()



    def terminate(self):

        global slide_thred_stop

        slide_thred_stop = 2

        self.close()



    def progress(self, value):

        progress = (100 - value)/ 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        stylesheet = """


                QFrame{

            border-radius:90px;
        		background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:'%s' rgba(255, 0, 157, 0), stop:"%s" rgba(32, 166, 255, 255));
        }
                """ %(stop_1, stop_2)


        self.ui.circular_progress.setStyleSheet(stylesheet)

       # self.ui.circular_progress.setAttribute(QtCore.Qt.WA_StyledBackground)

    def owerview_lst_action(self):
        global chap_id, selected_video, selected_video_title, main_lesson_place

        title = self.ui.chapter_content_lst.currentItem().text()


        db = sqlite3.connect("data/chpt_dat.ire")
        db.text_factory

        sql_data = db.execute("""SELECT * FROM '%s' WHERE t_name = '%s'""" % (chap_id, title))

        for lines in sql_data:

            image_id = lines[3]
            main_lesson_place = lines[1]
            print("main lesson", main_lesson_place)

            self.ui.chap_discription_lbl.setPlainText(lines[4])
            self.ui.tot_vid_lbl.setText(lines[5])
            self.ui.tot_due_lbl.setText(lines[6] + " min")

        stylesheet = """

                QFrame{

                    background-position: center;
                    background-repeat: no-repeat;
               		background-image:url(:/thumbnals/style/%s);
                  }""" % (image_id)

        # forward data to player

        selected_video_title = title
        print(image_id)
        print("main l place", main_lesson_place)
        selected_video = image_id


        self.ui.chap_img.setStyleSheet(stylesheet)


    def chap_start_btn_action(self):
        global play_list_show, selected_video, selected_video_title
        global chap_id , player_show, chapter_main_vid_count, main_lesson_place

        player_show = True
        self.ui.widget.setFocus()


        self.ui.pages.setCurrentWidget(self.ui.player)

        db = sqlite3.connect("data/chpt_dat.ire")
        db.text_factory

        sql_data = db.execute("""SELECT COUNT (*) FROM '%s'""" % (chap_id))

        for lines in sql_data:

            chapter_main_vid_count = int(lines[0])
            print(chapter_main_vid_count)

        if selected_video == "":


            sql_data = db.execute("""SELECT * FROM '%s' LIMIT 1""" % (chap_id))

            for lines in sql_data:
                selected_video = lines[3]
                selected_video_title = lines[2]
                main_lesson_place = lines[1]




        self.ui.title_lbl.setText((selected_video_title))

        self.ui.play_lst_btn.show()

        self.OpenFile()


    def forward_video(self):

        global play_list_show, selected_video, selected_video_title
        global video_count, video_row_count, main_lesson_place

        video_count += 1

        db = sqlite3.connect("data/chpt_dat.ire")
        db.text_factory

        if not video_count > video_row_count:


            sql_data1 = db.execute(
                """SELECT l_video FROM '%s' WHERE l_place = '%d'LIMIT 1""" % (selected_video, video_count))

            for lines1 in sql_data1:
                v_id = lines1[0]

            filename = "visual_content/" + v_id + ".ire"

            self.player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(filename)))

            self.PlayPause()
            print(video_count)

        else:
            video_count = 0

            main_lesson_place += 1
            print(" main lesson", main_lesson_place)

            if not main_lesson_place > chapter_main_vid_count:

                sql_data2 = db.execute(
                    """SELECT * FROM '%s' WHERE place = '%d'""" % (chap_id, main_lesson_place))

                for lines in sql_data2:
                    selected_video = lines[3]
                    selected_video_title = lines[2]
                    self.OpenFile()

            else:

                print("chapter end")
            print(video_count)


    def backward_video(self):

        global play_list_show, selected_video, selected_video_title
        global video_count, video_row_count, main_lesson_place

        video_count -= 1

        db = sqlite3.connect("data/chpt_dat.ire")
        db.text_factory

        if not video_count < 1:


            sql_data1 = db.execute(
                """SELECT l_video FROM '%s' WHERE l_place = '%d'LIMIT 1""" % (selected_video, video_count))

            for lines1 in sql_data1:
                v_id = lines1[0]

            filename = "visual_content/" + v_id + ".ire"

            self.player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(filename)))

            self.PlayPause()
            print(video_count)

        else:
            video_count = 0

            main_lesson_place -= 1

            if not main_lesson_place < 1:

                sql_data2 = db.execute(
                    """SELECT * FROM '%s' WHERE place = '%d'""" % (chap_id, main_lesson_place))

                for lines in sql_data2:
                    selected_video = lines[3]
                    selected_video_title = lines[2]
                    self.OpenFile()
            else:

                print("chapter end")


            print(video_count)


    def auto_load(self):
        global play_list_show, selected_video, selected_video_title
        global video_count, video_row_count, chap_id, main_lesson_place

        video_count += 1

        db = sqlite3.connect("data/chpt_dat.ire")
        db.text_factory


        if not video_count > video_row_count:

            sql_data1 = db.execute(
                """SELECT l_video FROM '%s' WHERE l_place = '%d'LIMIT 1""" % (selected_video, video_count))

            for lines1 in sql_data1:
                v_id = lines1[0]

            filename = "visual_content/" + v_id + ".ire"

            self.player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(filename)))

            self.PlayPause()

        else:
            video_count = 0

            main_lesson_place += 1
            print(" main lesson", main_lesson_place)

            if not main_lesson_place > chapter_main_vid_count:

                sql_data2 = db.execute(
                    """SELECT * FROM '%s' WHERE place = '%d'""" % (chap_id, main_lesson_place))

                for lines in sql_data2:
                    selected_video = lines[3]
                    selected_video_title = lines[2]
                    self.OpenFile()
            else:


                print("chapter end")

        print(video_count)





    def OpenFile(self):
        """Open a media file in a MediaPlayer
          """
        global play_list_show, selected_video, selected_video_title
        global video_count, video_row_count

        row_count = 0
        video_count  += 1

        self.ui.title_lbl.setText((selected_video_title))

        db = sqlite3.connect("data/chpt_dat.ire")
        db.text_factory

        print(selected_video)

        sql_data = db.execute("""SELECT COUNT (*) FROM '%s'""" % (selected_video))

        for lines in sql_data:

            video_row_count = int(lines[0])
            print("row" ,video_row_count)


        sql_data1 = db.execute("""SELECT l_video FROM '%s' WHERE l_place = '%d'LIMIT 1""" % (selected_video, video_count))

        for lines1 in sql_data1:

            v_id = lines1[0]
            print(v_id)

        filename = "visual_content/" + v_id + ".ire"

        print(filename)

        self.player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(filename)))

        self.PlayPause()
        print(video_count)



    def PlayPause(self):
        """Toggle play/pause status
        """

        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()

        else:

            self.player.play()

    def player_stop(self):

        self.player.stop()



    def media_duration(self):

        self.ui.total_lenth_lbl.clear()
        mtime = QTime(0, 0, 0, 0)
        mtime = mtime.addMSecs(self.player.duration())
      #  self.ui.player_slider.setRange(0, self.player.duration())

        self.ui.total_lenth_lbl.setText(mtime.toString())



    def media_lenth_current(self):


        self.ui.changed_lenth_lbl.clear()
        mtime = QTime(0, 0, 0, 0)
        self.time = mtime.addMSecs(self.player.position())
        #self.ui.player_slider.setValue(self.player.position())
        self.ui.changed_lenth_lbl.setText(self.time.toString())


    def positionChanged(self, progress):
        progress /= 1000

        if not self.ui.player_slider.isSliderDown():
            self.ui.player_slider.setValue(progress)

        self.updateDurationInfo(progress)

    def durationChanged(self, duration):
        duration /= 1000

        self.duration = duration
        self.ui.player_slider.setMaximum(duration)

    def updateDurationInfo(self, currentInfo):
        duration = self.duration
        curnt_time = "00.00"
        if currentInfo or duration:
            currentTime = QTime((currentInfo/3600)%60, (currentInfo/60)%60,
                    currentInfo%60, (currentInfo*1000)%1000)
            totalTime = QTime((duration/3600)%60, (duration/60)%60,
                    duration%60, (duration*1000)%1000);

            format = 'hh:mm:ss' if duration > 3600 else 'mm:ss'

            curnt_time = currentTime.toString(format)
            tStr = totalTime.toString(format)
        else:
            tStr = ""

        self.ui.total_lenth_lbl.setText(tStr)
        self.ui.changed_lenth_lbl.setText(curnt_time)


    def statusChanged(self, status):
        self.handleCursor(status)

        if status == QMediaPlayer.LoadingMedia:
            self.ui.player_status_lbl.setText("Loading...")
        elif status == QMediaPlayer.StalledMedia:
            self.ui.player_status_lbl.setText("Media Stalled")
        elif status == QMediaPlayer.EndOfMedia:
            self.auto_load()
            #QApplication.alert(self)
        else:
            self.ui.player_status_lbl.setText("")

    def handleCursor(self, status):
        if status in (QMediaPlayer.LoadingMedia, QMediaPlayer.BufferingMedia, QMediaPlayer.StalledMedia):
            self.setCursor(Qt.BusyCursor)
        else:
            self.unsetCursor()
    def bufferingProgress(self, progress):
        self.ui.player_status_lbl.setText("Buffering %d%" % progress)

    def seek(self, seconds):
        self.player.setPosition(seconds * 1000)


    def ful_screen_btn_action(self):

        global ful_scr
        ful_scr = True
        self.ful_screen()


    def ful_screen(self):


        global ful_scr

        if ful_scr == True:

            ful_scr = False

        else:

            ful_scr = True

        if ful_scr == True:

            self.ui.widget.setFullScreen(True)

        else:

            self.ui.widget.setFullScreen(False)


    def mouseDoubleClickEven(self, event):

        global ful_scr

        if ful_scr == True:

            ful_scr = False

        else:

            ful_scr = True

        if ful_scr == True:

            self.ui.widget.setFullScreen(True)

        else:

            self.ui.widget.setFullScreen(False)


    def keyPressEvent(self, event):
        global ful_scr

        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter and player_show == True:

            if ful_scr == True:

                ful_scr = False

            else:

                ful_scr = True

            if ful_scr == True:

                self.ui.widget.setFullScreen(True)

            else:

                self.ui.widget.setFullScreen(False)

        if event.key() == Qt.Key_Right and player_show == True:
            print("right")
            self.player.setPosition(self.player.position() + 10 * 100)
            #self.ui.player_slider.setValue(self.player.position())

        if event.key() == Qt.Key_Left and player_show == True:
            print("left")
            self.player.setPosition(self.player.position() - 9 * 100)

          #  self.positionChanged()

        if event.key() == Qt.Key_Space and player_show == True:
            print("space")
            if self.player.state() == QMediaPlayer.PlayingState:
                self.player.pause()
            elif self.player.state() == QMediaPlayer.PausedState:
                self.player.play()

        if event.key() == Qt.Key_Up and player_show == True:
            print("key up")

            if int(self.volume()) <= 95:
                self.vol += 5
                self.player.setVolume(self.vol)
            self.ui.vol_slider.setValue(self.vol)

        if event.key() == Qt.Key_Down:
            print("key down")

            if self.volume() >= 5:
                self.vol -= 5

                self.player.setVolume(self.vol)
            self.ui.vol_slider.setValue(self.vol)

    def mute(self):

        if self.player.isMuted():

            stylesheet = """

                    QPushButton{

	                    background-image: url(:/image/style/spkr.png);
                        background-position: center;
                        background-repeat: no-repeat;
	                    border:0px solid;
	                    background-color: rgb(255, 255, 255);
                      }"""

            self.player.setMuted(False)
            self.ui.vol_btn.setStyleSheet(stylesheet)

        else:

            stylesheet1 = """

                    QPushButton{
                    
                    	background-image: url(:/image/style/spkr_mute.png);
                        background-position: center;
                        background-repeat: no-repeat;
	                    border:0px solid;
	                    background-color: rgb(255, 255, 255);


                      }"""
            self.player.setMuted(True)
            self.ui.vol_btn.setStyleSheet(stylesheet1)


   # def volume(self):

    #    self.ui.vol_slider.setValue(self.player.volume())
    #    print(self.player.volume())

    def volume_seek(self):

        self.player.setVolume(self.ui.vol_slider.value())

        #self.ui.vol_slider.


       # self.vol += 5
       # self.player.setVolume(self.vol)
       # print(self.player.volume())




    def volume(self):
        return self.ui.vol_slider.value()

    def setVolume(self, volume):
        self.ui.vol_slider.setValue(volume)





# ************* player code end***************

    def c_btn1_action(self):
        play_list_show = 0
        self.ui.play_lst_btn.hide()
        self.ui.play_list.hide()
        self.ui.title_lbl.setText("mßÉfþo wka;¾.;h")

        chap_ID = "1"

        self.chapter_owerview_page(chap_ID)

    def c_btn2_action(self):
        play_list_show = 0
        self.ui.play_lst_btn.hide()
        self.ui.play_list.hide()
        self.ui.title_lbl.setText("mßÉfþo wka;¾.;h")

        chap_ID = "2"

        self.chapter_owerview_page(chap_ID)

    def c_btn3_action(self):
        play_list_show = 0
        self.ui.play_lst_btn.hide()
        self.ui.play_list.hide()
        self.ui.title_lbl.setText("mßÉfþo wka;¾.;h")

        chap_ID = "3"

        self.chapter_owerview_page(chap_ID)

    def c_btn4_action(self):
        play_list_show = 0
        self.ui.play_lst_btn.hide()
        self.ui.play_list.hide()
        self.ui.title_lbl.setText("mßÉfþo wka;¾.;h")

        chap_ID = "4"

        self.chapter_owerview_page(chap_ID)

    def c_btn5_action(self):
        play_list_show = 0
        self.ui.play_lst_btn.hide()
        self.ui.play_list.hide()
        self.ui.title_lbl.setText("mßÉfþo wka;¾.;h")

        chap_ID = "5"

        self.chapter_owerview_page(chap_ID)

    def c_btn6_action(self):
        play_list_show = 0
        self.ui.play_lst_btn.hide()
        self.ui.play_list.hide()
        self.ui.title_lbl.setText("mßÉfþo wka;¾.;h")

        chap_ID = "6"

        self.chapter_owerview_page(chap_ID)



    def chapter_owerview_page(self, chap_ID):

        global chap_id

        self.progress(0)
        self.ui.chapter_content_lst.clear()

        chap_id = chap_ID

        image_id = "chp" + chap_ID + ".jpg"

        db = sqlite3.connect("data/chpt_dat.ire")
        db.text_factory

        sql_data = db.execute("""SELECT t_name FROM '%s'""" % (chap_ID))

        for lines in sql_data:

            self.ui.chapter_content_lst.addItem(lines[0])

        self.ui.pages.setCurrentWidget(self.ui.chapto_owerview)

        stylesheet = """

                QFrame{

                    background-position: center;
                    background-repeat: no-repeat;
               		background-image:url(:/thumbnals/style/%s);
                  }""" % (image_id)

        self.ui.chap_img.setStyleSheet(stylesheet)

        sql_data = db.execute("""SELECT * FROM chapter WHERE chap_id = '%s'""" % (chap_ID))

        for lines1 in sql_data:

            self.ui.chap_discription_lbl.setPlainText(lines1[4])
            self.ui.tot_vid_lbl.setText(lines1[2])
            self.ui.tot_due_lbl.setText(lines1[5] + " h")

    def category_page(self):
        global slide_thred_stop

        slide_thred_stop = 1

        print(threading.enumerate())

        self.ui.pages.setCurrentWidget(self.ui.category_page)
        self.ui.title_lbl.setText("Chapters")

    def home_page_action(self):

        global slide_thred_stop

        slide_thred_stop = 0


        self.ui.pages.setCurrentWidget(self.ui.home_page)
        self.ui.title_lbl.setText("Home")

    def product_page(self):
        global slide_thred_stop

        slide_thred_stop = 0

        self.ui.pages.setCurrentWidget(self.ui.product_page)
        self.ui.title_lbl.setText("Our Products")

        url = "https://www.trsoftway.com/product.html"
        self.ui.widget_2.setUrl(QUrl(url))



    def about_page(self):
        global slide_thred_stop

        slide_thred_stop = 1

        self.ui.pages.setCurrentWidget(self.ui.about_page)
        self.ui.title_lbl.setText("About Us")



    def setting_page(self):
        global slide_thred_stop

        slide_thred_stop = 1

        self.ui.pages.setCurrentWidget(self.ui.settings_page)
        self.ui.title_lbl.setText("Settings")


    def mousePressEvent(self, event):

        self.dragpos = event.globalPos()

    def maxmize_fun(self):

        global global_state

        status = global_state

        if status == 0:

            self.showMaximized()
            global_state = 1


            self.ui.root_frm.setObjectName("root_frm_max")
            self.ui.root_frm.setStyleSheet(open(css_pack, "r").read())
            self.ui.maxmize_btn.setToolTip("Restore")
            self.showMaximized()

        else:

            global_state = 0
            self.showNormal()
            self.ui.root_frm.setObjectName("root_frm")

            self.ui.root_frm.setStyleSheet(open(css_pack, "r").read())
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.maxmize_btn.setToolTip("Maximize")
            self.ui.main_ui_layout.setContentsMargins(10, 10, 10, 10)
            self.showNormal()

    def terminate_fun(self):

        global slide_thred_stop

        slide_thred_stop = 2

        self.close()

    def minimize_fun(self):

        global global_state
        self.showMinimized()

    def ful_scrn_fun(self):

        global ful_scrn_status

        status = ful_scrn_status

        if status == 0:

            self.showFullScreen()
            ful_scrn_status = 1

            self.ui.main_ui_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.root_frm.setObjectName("root_frm_max")
            self.ui.root_frm.setStyleSheet(open(css_pack, "r").read())
            self.ui.maxmize_btn.setToolTip("Restore")

        else:

            ful_scrn_status = 0
            self.showNormal()
            self.ui.root_frm.setObjectName("root_frm")
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.root_frm.setStyleSheet(open(css_pack, "r").read())
            self.ui.maxmize_btn.setToolTip("Maximize")
            self.ui.main_ui_layout.setContentsMargins(10, 10, 10, 10)

    def return_status_max(self):

        global global_state

        return global_state

    def return_status_ful(self):

        global ful_scrn_status

        return ful_scrn_status



if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Login_window()
    window.show()
    twindow = MainWindow()
    twindow.thred1.start()
    #url = "https://web.whatsapp.com/"
    url = "https://www.trsoftway.com/product.html"
    twindow.ui.widget_2.setUrl(QUrl(url))
    sys.exit(app.exec_())