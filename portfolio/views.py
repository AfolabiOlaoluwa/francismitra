from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404
# from django.template import RequestContext, loader
from django.views import generic
from portfolio.models import Images, Categories, Videos
from blog.models import Posts

# Mixin to create menu
class LayoutView(object):
	template_name = 'portfolio/layout.html'

	def get_context_data(self, **kwargs):
		context = super(LayoutView, self).get_context_data(**kwargs)
		context['menu'] = Categories.objects.all().order_by('sorter')
		context['updated_at'] = Posts.objects.latest('created')
		return context

class IndexView(LayoutView, generic.TemplateView):
	template_name = 'portfolio/index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['aside'] = ['abstract&', 'love&', 'fashion&', 'travel&']
		return context

class CategoryView(LayoutView, generic.DetailView):
	template_name = 'portfolio/category.html'
	model = Categories

class ResumeView(LayoutView, generic.TemplateView):
	template_name = 'portfolio/resume.html'

