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
from .students_new_dialog import DialogStudent
from ...common.database.service.student_service import StudentService
from PyQt5.QtSql import QSqlDatabase
from ...common.database.db_initializer import DBInitializer as DB
from ...common.database.dao.student_dao import Student

class StudentInterface(GalleryInterface):
    """ Student interface """

    def __init__(self, parent=None):
        self.db = parent.db
        self.trans = Translate(Lang().current).text

        super().__init__(
            title='',
            subtitle='',
            parent=parent
        )
        
        self.db = QSqlDatabase.database(self.db.CONNECTION_NAME, True)
        self.studentService = StudentService(self.db)
        self.parent = parent
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
        self.searchLineStudent.textChanged.connect(self.searchStudent)
        
        col = Frame(HORIZONTAL, COL+str(1),parent=parent)
        self.btnAdd =  PushButton('Ajouter', self, FIF.ADD)
        self.btnAdd.setObjectName(u"PrimaryToolButton")
        self.btnAdd.clicked.connect(self.showDialog)

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
        #listsT = self.studentService.listAll()
        students = self.listStudent()
        self.tbStudent = Table(parent, students.get("header"), students.get("data"))
        self.table = self.tbStudent.widget()
        self.container.addWidget(self.tbStudent.widget())
        self.hBoxLayout.addWidget(self.container)
        self.dialog = None

    def listStudent(self):
        header = ["Firstname", "Lastname", "Gender", "Birthday", "Birthplace", "Address", "phone"]
        listStudent = [[
                student.get("firstname"),
                student.get("lastname"),
                student.get("gender"),
                student.get("birthday"),
                student.get("birthplace"),
                student.get("address"),
                student.get("phone")]
                    for student in self.studentService.listAll()]
        return {
            "header": header,
            "data": listStudent
        }
    
    def refreshTable(self):
        listStudent = self.listStudent()
        self.tbStudent.refresh(self.table, listStudent.get("header"), listStudent.get("data"))

    def showDialog(self):
        self.dialog = DialogStudent(self.parent)
        self.dialog.yesButton.clicked.connect(lambda: self.createStudent(self.dialog.studentData()))
        self.dialog.show()

    def createStudent(self, student: Student):
        if (self.studentService.create(student)):
            self.dialog.accept()
            self.dialog = None
            self.refreshTable()
        else:
            print("error")

    
    def searchStudent(self, text:str):
        if '\'' not in text:
            if text == "gino":
                print(text)
            #self.table_student.refresh(self.table,
            #                          self.studentCtrl.label,
            #                         self.studentCtrl.search(text))
        