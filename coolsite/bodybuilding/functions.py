from .models import *

def AllRelations():
    relations = Relation.objects.all()
    return relations