from django.shortcuts import render
from django.views import generic
from blog.models import Posts
from portfolio.views import LayoutView

class BlogView(LayoutView, generic.ListView):
	model = Posts

class TutorialView(LayoutView, generic.TemplateView):
	template_name = 'blog/tutorials.html'