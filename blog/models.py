from django.db import models

class Posts(models.Model):
	title   = models.CharField(max_length=250, blank=True, null=True)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	slug    = models.SlugField()

	def __unicode__(self):
		return unicode(self.title)

	class Meta:
		verbose_name_plural = "posts"
