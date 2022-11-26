import sys

from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget

from UI import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.can_paint = False
        self.setWindowTitle('Git и случайные окружности')
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.can_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.can_paint:
            self.can_paint = False
            qp = QPainter()
            qp.begin(self)
            for _ in range(randint(1, 5)):
                size = randint(50, 150)
                qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
                try:
                    qp.drawEllipse(randint(0, self.width() - size),
                                   randint(0, self.height() - size), size, size)
                except ValueError:
                    pass
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())