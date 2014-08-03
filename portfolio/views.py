from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404
# from django.template import RequestContext, loader
from django.views import generic
from portfolio.models import Images, Categories, Videos

# Mixin to create menu
class LayoutView(object):
	template_name = 'portfolio/layout.html'

	def get_context_data(self, **kwargs):
		context = super(LayoutView, self).get_context_data(**kwargs)
		context['menu'] = Categories.objects.all()
		return context


class IndexView(LayoutView, generic.TemplateView):
	template_name = 'portfolio/index.html'


class CategoryView(LayoutView, generic.DetailView):
	template_name = 'portfolio/category.html'
	model = Categories

	@property
	def category(self):
		return get_object_or_404(Categories, slug=self.kwargs['slug'])

	def get_context_data(self, **kwargs):
		context = super(CategoryView, self).get_context_data(**kwargs)
		context['portfolio'] = Images.objects.filter(category_id=self.category)
		return context


	

