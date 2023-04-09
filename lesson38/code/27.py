from dajngo.contrib.contenttypes.fields import GenericRelation

class Machine(models.Model):
		...
		notes = GenericRelation("Note")