# coding:utf-8
from typing import List

from .dao_base import DaoBase
from ..entity import Student


class StudentDao(DaoBase):
    """ Student information DAO """

    table = 'tbl_student'

    def createTable(self):
        return super().createTable(Student())
    
