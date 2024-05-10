import os, sys
from PySide6.QtWidgets import *
import sound_split
import label_check
import attach_json
from pyqt_ui2_ui import Ui_MainWindow
    
class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        
        #self.bindComponents()
        #set Tap1
        self.select_file.clicked.connect(self.click_select_file)
        self.select_dir.clicked.connect(self.click_select_dir)
        self.select_csv.clicked.connect(self.click_select_csv)
        self.push.clicked.connect(self.click_push)

        #set Tap2
        self.select_excel_dir.clicked.connect(self.click_select_excel_dir)
        self.select_wav_dir.clicked.connect(self.click_select_wav_dir)
        self.push_2.clicked.connect(self.click_push_2)

        #set Tap3
        self.select_ai_dir.clicked.connect(self.click_select_ai)
        self.select_ao_dir.clicked.connect(self.click_select_ao)
        self.select_img_json_dir.clicked.connect(self.click_select_img_json)
        self.select_save_dir.clicked.connect(self.click_select_save_dir)
        self.push_3.clicked.connect(self.click_push_3)

        self.show()

    def click_select_ai(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.ai_path_line.setText(folder)
        
    def click_select_ao(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.ao_path_line.setText(folder)

    def click_select_img_json(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.img_json_path_line.setText(folder)

    def click_select_save_dir(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.out_path_line.setText(folder)
    

    def click_select_file(self):
        file = QFileDialog.getOpenFileName(self, "Select File")
        self.file_line.setText(file[0])

    def click_select_csv(self):
        file = QFileDialog.getOpenFileName(self, "Select File")
        self.csv_line.setText(file[0])
    

    def click_select_dir(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.path_line.setText(folder)

    def click_select_wav_dir(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.wav_path_line.setText(folder)

    def click_select_excel_dir(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.excel_path_line.setText(folder)

    def one_radio(self):
        if self.radio_AI.isChecked() == True:
            return 'AI'
        else:
            return 'AO'

    def click_push(self):
        time = self.vedio_time.textFromDateTime(self.vedio_time.dateTime())
        self.push.setEnabled(False)
        # try:
        sound_split.split_main(file=self.file_line.text(), dir=self.path_line.text(), \
                                                    audiotype=self.one_radio(), gov=self.select_gov.currentText(), \
                                                        pipe=self.select_pipe_type.currentText(), is_json=self.check_json.isChecked(), \
                                                            is_mel=self.check_mel.isChecked(), is_stft=self.check_stft.isChecked(), \
                                                            is_wav=self.check_wav.isChecked(), vedio_time=time, csvfile=self.csv_line.text())
        # except:
        #     pass
        self.push.setEnabled(True)

    def click_push_2(self):
        self.push_2.setEnabled(False)
        path = os.path.join(self.excel_path_line.text(), self.save_file_name.text())
        try:
            label_check.write_xl(WAV_DIR=self.wav_path_line.text(), FILE_NAME=path)
        except:
            pass
        self.push_2.setEnabled(True)

    def click_push_3(self):
        self.push_3.setEnabled(False)
        try:
            attach_json.json_main(img_path=self.img_json_path_line.text(), ai_path=self.ai_path_line.text(), ao_path=self.ao_path_line.text(), out_path=self.out_path_line.text())
        except:
            pass
        self.push_3.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = App()
    sys.exit(app.exec())
