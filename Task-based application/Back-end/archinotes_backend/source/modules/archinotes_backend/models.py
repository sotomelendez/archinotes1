# -*- coding: utf-8 -*-
from mongoengine import *

class User(Document):
    name = StringField()


class Annotation(DynamicDocument):
    name = StringField()

