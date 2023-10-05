# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'picachooserTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1746, 839)
        MainWindow.setMinimumSize(QtCore.QSize(0, 100))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.translation_graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.translation_graphicsView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.translation_graphicsView.sizePolicy().hasHeightForWidth()
        )
        self.translation_graphicsView.setSizePolicy(sizePolicy)
        self.translation_graphicsView.setMinimumSize(QtCore.QSize(400, 100))
        self.translation_graphicsView.setMaximumSize(QtCore.QSize(610, 1000))
        self.translation_graphicsView.setSizeIncrement(QtCore.QSize(1, 1))
        self.translation_graphicsView.setObjectName("translation_graphicsView")
        self.verticalLayout.addWidget(self.translation_graphicsView)
        self.rotation_graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.rotation_graphicsView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotation_graphicsView.sizePolicy().hasHeightForWidth())
        self.rotation_graphicsView.setSizePolicy(sizePolicy)
        self.rotation_graphicsView.setMinimumSize(QtCore.QSize(400, 100))
        self.rotation_graphicsView.setMaximumSize(QtCore.QSize(610, 1000))
        self.rotation_graphicsView.setSizeIncrement(QtCore.QSize(1, 1))
        self.rotation_graphicsView.setObjectName("rotation_graphicsView")
        self.verticalLayout.addWidget(self.rotation_graphicsView)
        self.timecourse_graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.timecourse_graphicsView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timecourse_graphicsView.sizePolicy().hasHeightForWidth())
        self.timecourse_graphicsView.setSizePolicy(sizePolicy)
        self.timecourse_graphicsView.setMinimumSize(QtCore.QSize(400, 100))
        self.timecourse_graphicsView.setMaximumSize(QtCore.QSize(610, 1000))
        self.timecourse_graphicsView.setSizeIncrement(QtCore.QSize(1, 1))
        self.timecourse_graphicsView.setObjectName("timecourse_graphicsView")
        self.verticalLayout.addWidget(self.timecourse_graphicsView)
        self.spectrum_graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.spectrum_graphicsView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spectrum_graphicsView.sizePolicy().hasHeightForWidth())
        self.spectrum_graphicsView.setSizePolicy(sizePolicy)
        self.spectrum_graphicsView.setMinimumSize(QtCore.QSize(400, 100))
        self.spectrum_graphicsView.setMaximumSize(QtCore.QSize(610, 1000))
        self.spectrum_graphicsView.setSizeIncrement(QtCore.QSize(1, 1))
        self.spectrum_graphicsView.setObjectName("spectrum_graphicsView")
        self.verticalLayout.addWidget(self.spectrum_graphicsView)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setSizeIncrement(QtCore.QSize(1, 1))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setMinimumSize(QtCore.QSize(100, 100))
        self.page.setSizeIncrement(QtCore.QSize(1, 1))
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.image_graphicsView = GraphicsLayoutWidget(self.page)
        self.image_graphicsView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_graphicsView.sizePolicy().hasHeightForWidth())
        self.image_graphicsView.setSizePolicy(sizePolicy)
        self.image_graphicsView.setMinimumSize(QtCore.QSize(600, 100))
        self.image_graphicsView.setMaximumSize(QtCore.QSize(16384, 8192))
        self.image_graphicsView.setSizeIncrement(QtCore.QSize(1, 1))
        self.image_graphicsView.setObjectName("image_graphicsView")
        self.horizontalLayout_2.addWidget(self.image_graphicsView)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy)
        self.page_2.setMinimumSize(QtCore.QSize(100, 100))
        self.page_2.setSizeIncrement(QtCore.QSize(1, 1))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.image_altgraphicsView = GraphicsLayoutWidget(self.page_2)
        self.image_altgraphicsView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_altgraphicsView.sizePolicy().hasHeightForWidth())
        self.image_altgraphicsView.setSizePolicy(sizePolicy)
        self.image_altgraphicsView.setMinimumSize(QtCore.QSize(600, 100))
        self.image_altgraphicsView.setMaximumSize(QtCore.QSize(16384, 8192))
        self.image_altgraphicsView.setSizeIncrement(QtCore.QSize(1, 1))
        self.image_altgraphicsView.setObjectName("image_altgraphicsView")
        self.horizontalLayout_3.addWidget(self.image_altgraphicsView)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1746, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(
            _translate(
                "MainWindow",
                'Right and left arrows step through components. Up and down arrows toggle component retention.  "r" to reset component.  "a", "c", and "s" select axial, coronal, or sagittal views.  ESC to write component file.',
            )
        )


from pyqtgraph import GraphicsLayoutWidget
