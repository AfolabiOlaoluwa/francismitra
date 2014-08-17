from django.db import models

class Categories(models.Model):
	title		= models.CharField(max_length=250)
	content		= models.TextField(blank=True, null=True)
	sorter		= models.IntegerField(default=0)
	slug		= models.SlugField()

	def __unicode__(self):
		return unicode(self.title)

	class Meta:
		verbose_name_plural = 'categories'

	def get_images(self):
		return self.images_set.select_related('category')

	def check_content(self):
		if self.content:
			return "something is here"
		else:
			return "nothing is here"

class BaseMedia(models.Model):
	'''
	Base class for use with video and photo content
	'''
	category 	= models.ForeignKey(Categories)
	title   	= models.CharField(max_length=250)
	caption		= models.CharField(max_length=250, blank=True, null=True)
	year 		= models.CharField(max_length=4, blank=True, null=True)

	class Meta:
		abstract = True

class Images(BaseMedia):
	photo = models.ImageField(upload_to='portfolio/')
	# photo = models.ImageField(upload_to='images/')

	class Meta:
		verbose_name_plural = 'images'
	
	def __unicode__(self):
		return unicode(self.title)

class Videos(BaseMedia):
	PROVIDER_LIST_CHOICES	= (('YU','YouTube'),('VI','Vimeo'))
	provider 				= models.CharField(max_length=2, choices=PROVIDER_LIST_CHOICES)
	url						= models.CharField(max_length=250)

	class Meta:
		verbose_name_plural = 'videos'

	def __unicode__(self):
		return unicode(self.title)

