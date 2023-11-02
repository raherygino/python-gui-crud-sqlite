# coding:utf-8
from ..utils.gallery_interface import GalleryInterface
from ...common.translator import Translator
from ...common.Translate import Translate
from ...common.config import Lang
from ...common.keys import *
from ...components import *
from qfluentwidgets import (SubtitleLabel, SearchLineEdit, PushButton,MenuAnimationType, 
                            PrimaryPushButton, RoundMenu, Action, MessageBox, InfoBar, InfoBarPosition)
from qfluentwidgets import FluentIcon as FIF
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QTableWidgetItem, QAction
from PyQt5.QtCore import Qt, QSize, QCoreApplication, QModelIndex, QPoint
from ...common.config import *

class StudentInterface(GalleryInterface):
    """ Student interface """

    def __init__(self, parent=None):
        t = Translator()
        self.trans = Translate(Lang().current).text
        super().__init__(
            title='',
            subtitle='',
            parent=parent
        )
        
        self.hBoxLayout = QVBoxLayout(self)
        self.titleContainte(parent)
        self.container(parent)
        self.setObjectName('studentInterface')

    def titleContainte(self, parent):
        row = Frame(VERTICAL, ROW+str(1), parent=parent)
        label = SubtitleLabel("Liste des élèves", parent)
        row.setMargins(9,0,9,0)
        row.addWidget(label)
        self.hBoxLayout.addWidget(row)

    def container(self, parent):
        self.container = Frame(VERTICAL, STUDENT+CONTAINER, parent=parent)
        self.row_2 = Frame(HORIZONTAL, ROW+str(2), parent=parent)
        self.searchLineStudent = SearchLineEdit(self)
        self.searchLineStudent.setPlaceholderText(QCoreApplication.translate(FORM, u"Recherche", None))
        self.searchLineStudent.setMaximumSize(QSize(240, 50))
        #self.searchLineStudent.textChanged.connect(self.searchStudent)
        
        col = Frame(HORIZONTAL, COL+str(1),parent=parent)
        self.btnAdd =  PushButton('Ajouter', self, FIF.ADD)
        self.btnAdd.setObjectName(u"PrimaryToolButton")
        #self.btnAdd.clicked.connect(self.showDialog)

        self.btnFlux =  PrimaryPushButton('Seed', self, FIF.DEVELOPER_TOOLS)
        self.btnFlux.setObjectName(u"PrimaryToolButton")
        #self.btnFlux.clicked.connect(self.seed)

        col.layout.addWidget(self.btnAdd)
        col.layout.addWidget(self.btnFlux)
        col.setMargins(0,0,0,0)
        
        self.row_2.setMargins(0,0,0,0)
        self.row_2.addWidget(self.searchLineStudent)
        self.row_2.layout.addWidget(col, 0, Qt.AlignRight)
        
        self.container.addWidget(self.row_2)
        self.tbStudent = Table(parent, ["Name", "Age"], [["Georgino", "26"],["Armelin", "18"]])
        self.container.addWidget(self.tbStudent.widget())
        self.hBoxLayout.addWidget(self.container)
        self.dialog = None

    
    def searchStudent(self, text:str):
        if '\'' not in text:
            if text == "gino":
                print(text)
            #self.table_student.refresh(self.table,
            #                          self.studentCtrl.label,
            #                         self.studentCtrl.search(text))
        