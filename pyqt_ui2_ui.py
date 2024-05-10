# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyqt_ui2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)
import resurce_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 338)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(30, 20, 501, 301))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(360, 80, 121, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(350, 10, 16, 191))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(360, 10, 121, 71))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 0, 0)
        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.radio_AI = QRadioButton(self.verticalLayoutWidget)
        self.radio_AI.setObjectName(u"radio_AI")
        self.radio_AI.setChecked(True)

        self.verticalLayout.addWidget(self.radio_AI)

        self.radio_AO = QRadioButton(self.verticalLayoutWidget)
        self.radio_AO.setObjectName(u"radio_AO")

        self.verticalLayout.addWidget(self.radio_AO)

        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 10, 331, 198))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.vedio_time = QDateTimeEdit(self.gridLayoutWidget)
        self.vedio_time.setObjectName(u"vedio_time")
        self.vedio_time.setDate(QDate(2023, 10, 14))
        self.vedio_time.setTime(QTime(18, 0, 0))
        self.vedio_time.setMaximumDate(QDate(2035, 12, 31))
        self.vedio_time.setMinimumDate(QDate(2023, 9, 14))
        self.vedio_time.setCurrentSection(QDateTimeEdit.YearSection)

        self.gridLayout.addWidget(self.vedio_time, 6, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.file_line = QLineEdit(self.gridLayoutWidget)
        self.file_line.setObjectName(u"file_line")

        self.gridLayout.addWidget(self.file_line, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.path_line = QLineEdit(self.gridLayoutWidget)
        self.path_line.setObjectName(u"path_line")

        self.gridLayout.addWidget(self.path_line, 2, 1, 1, 1)

        self.select_file = QPushButton(self.gridLayoutWidget)
        self.select_file.setObjectName(u"select_file")

        self.gridLayout.addWidget(self.select_file, 1, 2, 1, 1)

        self.select_pipe_type = QComboBox(self.gridLayoutWidget)
        self.select_pipe_type.addItem("")
        self.select_pipe_type.addItem("")
        self.select_pipe_type.addItem("")
        self.select_pipe_type.setObjectName(u"select_pipe_type")

        self.gridLayout.addWidget(self.select_pipe_type, 4, 1, 1, 1)

        self.select_dir = QPushButton(self.gridLayoutWidget)
        self.select_dir.setObjectName(u"select_dir")

        self.gridLayout.addWidget(self.select_dir, 2, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.select_gov = QComboBox(self.gridLayoutWidget)
        self.select_gov.addItem("")
        self.select_gov.addItem("")
        self.select_gov.addItem("")
        self.select_gov.addItem("")
        self.select_gov.setObjectName(u"select_gov")

        self.gridLayout.addWidget(self.select_gov, 5, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)

        self.csv_line = QLineEdit(self.gridLayoutWidget)
        self.csv_line.setObjectName(u"csv_line")

        self.gridLayout.addWidget(self.csv_line, 3, 1, 1, 1)

        self.select_csv = QPushButton(self.gridLayoutWidget)
        self.select_csv.setObjectName(u"select_csv")

        self.gridLayout.addWidget(self.select_csv, 3, 2, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.tab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(360, 90, 127, 122))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label_7 = QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)

        self.check_mel = QCheckBox(self.gridLayoutWidget_3)
        self.check_mel.setObjectName(u"check_mel")
        self.check_mel.setChecked(True)

        self.gridLayout_3.addWidget(self.check_mel, 7, 0, 1, 1)

        self.check_json = QCheckBox(self.gridLayoutWidget_3)
        self.check_json.setObjectName(u"check_json")
        self.check_json.setChecked(True)

        self.gridLayout_3.addWidget(self.check_json, 5, 0, 1, 1)

        self.check_wav = QCheckBox(self.gridLayoutWidget_3)
        self.check_wav.setObjectName(u"check_wav")
        self.check_wav.setChecked(True)

        self.gridLayout_3.addWidget(self.check_wav, 4, 0, 1, 1)

        self.check_stft = QCheckBox(self.gridLayoutWidget_3)
        self.check_stft.setObjectName(u"check_stft")
        self.check_stft.setChecked(True)

        self.gridLayout_3.addWidget(self.check_stft, 6, 0, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.tab)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(20, 210, 461, 41))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.push = QPushButton(self.gridLayoutWidget_4)
        self.push.setObjectName(u"push")

        self.gridLayout_4.addWidget(self.push, 1, 0, 1, 1)

        self.line_3 = QFrame(self.gridLayoutWidget_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 381, 114))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.select_excel_dir = QPushButton(self.gridLayoutWidget_2)
        self.select_excel_dir.setObjectName(u"select_excel_dir")

        self.gridLayout_2.addWidget(self.select_excel_dir, 1, 2, 1, 1)

        self.wav_path_line = QLineEdit(self.gridLayoutWidget_2)
        self.wav_path_line.setObjectName(u"wav_path_line")

        self.gridLayout_2.addWidget(self.wav_path_line, 0, 1, 1, 1)

        self.select_wav_dir = QPushButton(self.gridLayoutWidget_2)
        self.select_wav_dir.setObjectName(u"select_wav_dir")

        self.gridLayout_2.addWidget(self.select_wav_dir, 0, 2, 1, 1)

        self.excel_path_line = QLineEdit(self.gridLayoutWidget_2)
        self.excel_path_line.setObjectName(u"excel_path_line")

        self.gridLayout_2.addWidget(self.excel_path_line, 1, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.save_file_name = QLineEdit(self.gridLayoutWidget_2)
        self.save_file_name.setObjectName(u"save_file_name")

        self.gridLayout_2.addWidget(self.save_file_name, 2, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)

        self.verticalLayoutWidget_2 = QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 130, 381, 31))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.push_2 = QPushButton(self.verticalLayoutWidget_2)
        self.push_2.setObjectName(u"push_2")

        self.verticalLayout_2.addWidget(self.push_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_5 = QWidget(self.tab_3)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 10, 381, 141))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.gridLayoutWidget_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_14, 1, 0, 1, 1)

        self.select_save_dir = QPushButton(self.gridLayoutWidget_5)
        self.select_save_dir.setObjectName(u"select_save_dir")

        self.gridLayout_5.addWidget(self.select_save_dir, 3, 2, 1, 1)

        self.ao_path_line = QLineEdit(self.gridLayoutWidget_5)
        self.ao_path_line.setObjectName(u"ao_path_line")

        self.gridLayout_5.addWidget(self.ao_path_line, 1, 1, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_17, 2, 0, 1, 1)

        self.select_ai_dir = QPushButton(self.gridLayoutWidget_5)
        self.select_ai_dir.setObjectName(u"select_ai_dir")

        self.gridLayout_5.addWidget(self.select_ai_dir, 2, 2, 1, 1)

        self.img_json_path_line = QLineEdit(self.gridLayoutWidget_5)
        self.img_json_path_line.setObjectName(u"img_json_path_line")

        self.gridLayout_5.addWidget(self.img_json_path_line, 0, 1, 1, 1)

        self.out_path_line = QLineEdit(self.gridLayoutWidget_5)
        self.out_path_line.setObjectName(u"out_path_line")

        self.gridLayout_5.addWidget(self.out_path_line, 3, 1, 1, 1)

        self.select_ao_dir = QPushButton(self.gridLayoutWidget_5)
        self.select_ao_dir.setObjectName(u"select_ao_dir")

        self.gridLayout_5.addWidget(self.select_ao_dir, 1, 2, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_18, 3, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setLayoutDirection(Qt.LeftToRight)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_16, 0, 0, 1, 1)

        self.select_img_json_dir = QPushButton(self.gridLayoutWidget_5)
        self.select_img_json_dir.setObjectName(u"select_img_json_dir")

        self.gridLayout_5.addWidget(self.select_img_json_dir, 0, 2, 1, 1)

        self.ai_path_line = QLineEdit(self.gridLayoutWidget_5)
        self.ai_path_line.setObjectName(u"ai_path_line")

        self.gridLayout_5.addWidget(self.ai_path_line, 2, 1, 1, 1)

        self.verticalLayoutWidget_3 = QWidget(self.tab_3)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 150, 381, 31))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.push_3 = QPushButton(self.verticalLayoutWidget_3)
        self.push_3.setObjectName(u"push_3")

        self.verticalLayout_3.addWidget(self.push_3)

        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MopingI S/W", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uc74c\ud5a5 \ud0c0\uc785", None))
        self.radio_AI.setText(QCoreApplication.translate("MainWindow", u"\ub0b4\ubd80 \uc74c\ud5a5", None))
        self.radio_AO.setText(QCoreApplication.translate("MainWindow", u"\uc678\ubd80 \uc74c\ud5a5", None))
        self.vedio_time.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd hh:mm:ss", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uad00 \uc885\ub958", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5 \ud3f4\ub354", None))
        self.select_file.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\uc120\ud0dd", None))
        self.select_pipe_type.setItemText(0, QCoreApplication.translate("MainWindow", u"\ub3c4\uc218\uad00", None))
        self.select_pipe_type.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc1a1\uc218\uad00", None))
        self.select_pipe_type.setItemText(2, QCoreApplication.translate("MainWindow", u"\ubc30\uc218\uad00", None))

        self.select_dir.setText(QCoreApplication.translate("MainWindow", u"\ub514\ub809\ud130\ub9ac", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\ucd2c\uc601 \uc77c\uc790", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc74c\ud5a5 \ud30c\uc77c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uad00 \uc704\uce58", None))
        self.select_gov.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc81c\uc8fc\uc2dc", None))
        self.select_gov.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc2dc\ud765\uc2dc", None))
        self.select_gov.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc804\uc8fc\uc2dc", None))
        self.select_gov.setItemText(3, QCoreApplication.translate("MainWindow", u"\uc9c4\ub3c4\uad70", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CSV \ud30c\uc77c", None))
        self.select_csv.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\uc120\ud0dd", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uae30\ub2a5", None))
        self.check_mel.setText(QCoreApplication.translate("MainWindow", u"\ucc38\uace0 \uc774\ubbf8\uc9c0 \uc0dd\uc131", None))
        self.check_json.setText(QCoreApplication.translate("MainWindow", u"JSON \ud30c\uc77c \uc0dd\uc131", None))
        self.check_wav.setText(QCoreApplication.translate("MainWindow", u"Wav \ud30c\uc77c \uc790\ub974\uae30", None))
        self.check_stft.setText(QCoreApplication.translate("MainWindow", u"STFT \uc774\ubbf8\uc9c0 \uc0dd\uc131", None))
        self.push.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc778", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\uc74c\ud5a5 \uc790\ub974\uae30", None))
        self.select_excel_dir.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc120\ud0dd", None))
        self.select_wav_dir.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc120\ud0dd", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5 \ud30c\uc77c \uc774\ub984", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\uc74c\ud5a5 JSON \ud3f4\ub354", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Excel \uc800\uc7a5 \ud3f4\ub354", None))
        self.push_2.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc778", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\ub77c\ubca8\ub9c1 \ud655\uc778", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\uc678\ubd80\uc74c\ud5a5 JSON \ud3f4\ub354", None))
        self.select_save_dir.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc120\ud0dd", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\ub0b4\ubd80\uc74c\ud5a5 JSON \ud3f4\ub354", None))
        self.select_ai_dir.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc120\ud0dd", None))
        self.select_ao_dir.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc120\ud0dd", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5 \ud3f4\ub354", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 JSON \ud3f4\ub354", None))
        self.select_img_json_dir.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc120\ud0dd", None))
        self.push_3.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc778", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\ud1b5\ud569\ub77c\ubca8\ub9c1", None))
    # retranslateUi

