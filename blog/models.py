from django.db import models

class Posts(models.Model):
	title   = models.CharField(max_length=250, blank=True, null=True)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	# photo   = models.ImageField(upload_to='blog/')
	slug    = models.SlugField()

	def __unicode__(self):
		return unicode(self.title)

	class Meta:
		verbose_name_plural = 'posts'

class PostImages(models.Model):
	post  = models.ForeignKey(Posts, related_name='images')
	photo = models.ImageField(upload_to='blog/')

	def __unicode__(self):
		return unicode(self.post)

	class Meta:
		verbose_name_plural = 'postimages'