# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Progressbar.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Util(object):
    def setupUi(self, Util):
        if not Util.objectName():
            Util.setObjectName(u"Util")
        Util.resize(796, 64)
        self.verticalLayout = QVBoxLayout(Util)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Util)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(Util)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)


        self.retranslateUi(Util)

        QMetaObject.connectSlotsByName(Util)
    # setupUi

    def retranslateUi(self, Util):
        Util.setWindowTitle(QCoreApplication.translate("Util", u"Form", None))
        self.label.setText(QCoreApplication.translate("Util", u"TextLabel", None))
    # retranslateUi

