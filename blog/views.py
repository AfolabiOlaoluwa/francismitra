from django.shortcuts import render
from django.views import generic
from blog.models import Posts
from portfolio.views import LayoutView

class BlogView(LayoutView, generic.ListView):
	template_name = 'blog/blog.html'
	model = Posts
	context_object_name = 'all_posts'

class SingleView(LayoutView, generic.DetailView):
	template_name = 'blog/single.html'
	model = Posts
	# context_object_name = 'post'

class TutorialView(LayoutView, generic.TemplateView):
	template_name = 'blog/tutorials.html'