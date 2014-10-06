from django.db import models

class Posts(models.Model):
	title   		= models.CharField(max_length=250, blank=True, null=True)
	content 		= models.TextField(blank=True, null=True)
	created 		= models.DateTimeField(auto_now_add=True)
	CATEGORY_LIST 	= (('TU', 'Tutorials'),('DE','Default'))
	category 	    = models.CharField(max_length=2, choices=CATEGORY_LIST)
	slug   			= models.SlugField()

	def __unicode__(self):
		return unicode(self.title)

	class Meta:
		verbose_name_plural = 'posts'

	def get_images(self):
		return self.postimages_set.select_related('post')

class PostImages(models.Model):
	post  = models.ForeignKey(Posts)
	photo = models.ImageField(upload_to='blog/')

	def __unicode__(self):
		return unicode(self.post)

	class Meta:
		verbose_name_plural = 'postimages'