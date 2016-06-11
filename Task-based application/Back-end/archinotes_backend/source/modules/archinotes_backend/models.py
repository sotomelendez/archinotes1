# -*- coding: utf-8 -*-
from mongoengine import *

class User(Document):
    name = StringField()

class Overview(Document):
    project_background = StringField()
    purpose_scope = StringField()
    system_overview = StringField()

class Stakeholder(Document):
    project_background = StringField()
    purpose_scope = StringField()
    system_overview = StringField

class StakeholdersTypes(Document):
	name = StringField()
	
class Annotation(DynamicDocument):
    name = StringField()

class Diagram(Document):
    viewpoint = StringField()
    name = StringField()
    deleted = BooleanField()

class Diagram_Version(Document):
    viewpoint = StringField()
    diagram_name = StringField()
    version = StringField()
    date = StringField()
    deleted = BooleanField()

class Diagran_Element(Document):
    viewpoint = StringField()
    diagram_name = StringField()
    diagram_version = StringField()
    element_html_id = StringField()
    element_name = StringField()
    element_type = StringField()
    left = FloatField()
    top = FloatField()
    deleted = BooleanField()

class Diagram_Connection(Document):
    viewpoint = StringField()
    diagram_name = StringField()
    diagram_version = StringField()
    source_element_html_id = StringField()
    target_element_html_id = StringField()
    deleted = BooleanField()
