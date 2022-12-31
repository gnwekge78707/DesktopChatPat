import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class loadingGif(QWidget):
    def __init__(self):
        super(loadingGif, self).__init__()
        self.label = QLabel("", self)
        # fixed  adj. 确定的；固执的
        self.setFixedSize(128, 128)
        self.resize(400, 300)  # 设置了固定尺寸之后，尺寸便不可修改！
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie = QMovie(r'C:\Users\fuxue\Downloads\desktop-randy-main\desktop-randy-main\cat_animation\drageft.gif')
        self.label.setMovie(self.movie)
        self.movie.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = loadingGif()
    form.show()
    sys.exit(app.exec_())
