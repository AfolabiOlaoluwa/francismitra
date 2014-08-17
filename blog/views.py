from django.shortcuts import render, get_object_or_404
from django.views import generic
from blog.models import Posts,PostImages
from portfolio.views import LayoutView

class BlogView(LayoutView, generic.ListView):
	template_name = 'blog/blog.html'
	model = Posts

	def get_context_data(self, **kwargs):
		context = super(BlogView, self).get_context_data(**kwargs)
		context['blog_posts'] = Posts.objects.exclude(category='TU')
		context['page_title'] = 'Blog'
		return context

class SingleView(LayoutView, generic.DetailView):
	template_name = 'blog/single.html'
	model = Posts

	def get_context_data(self, **kwargs):
		post = self.get_object()
		title = post.title

		context = super(SingleView, self).get_context_data(**kwargs)

		if post.category == 'TU':
			context['page_title'] = 'Tutorials | %s' % (title)
		else:
			context['page_title'] = 'Blog | %s' % (title)

		return context

class TutorialView(LayoutView, generic.ListView):
	template_name = 'blog/tutorials.html'
	model = Posts

	def get_context_data(self, **kwargs):
		context = super(TutorialView, self).get_context_data(**kwargs)
		context['tutorial_posts'] = Posts.objects.exclude(category='DE')
		context['page_title'] = 'Tutorials'
		return context