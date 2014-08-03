from django.db import models

class Categories(models.Model):
	title		= models.CharField(max_length=250)
	content		= models.TextField(blank=True)

	def __unicode__(self):
		return self.title

	'''
	Use this to generate your views
	'''
	# def get_absolute_url(self):
		# from django.core.urlresolvers import reverse
		# return reverse('portfolio.views.category', args=[str(self.title)])

	class Meta:
		verbose_name_plural = 'categories'

	def check_content(self):
		if self.content:
			return "something is here"
		else:
			return "nothing is here"

# Abstract base class for video and image content
class BaseMedia(models.Model):
	category 	= models.ForeignKey(Categories)
	title   	= models.CharField(max_length=250)
	caption		= models.CharField(max_length=250)
	date 		= models.DateTimeField('date published')

	class Meta:
		abstract = True

class Images(BaseMedia):
	photo = models.ImageField(upload_to='images/')

	class Meta:
		verbose_name_plural = 'images'
	
	def __unicode__(self):
		return self.category

class Videos(BaseMedia):
	PROVIDER_LIST_CHOICES	= (('YU','YouTube'),('VI','Vimeo'))
	provider 				= models.CharField(max_length=2, choices=PROVIDER_LIST_CHOICES)
	url						= models.CharField(max_length=250)

	class Meta:
		verbose_name_plural = 'videos'

	def __unicode__(self):
		return self.category

