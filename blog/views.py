from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from blog.models import Posts,PostImages
from portfolio.views import LayoutView

class BlogView(LayoutView, ListView):
	template_name = 'blog/blog.html'
	queryset = Posts.objects.prefetch_related('postimages_set').exclude(category='TU').order_by('-created')
	context_object_name = 'blog_posts'

	def get_context_data(self, **kwargs):
		context = super(BlogView, self).get_context_data(**kwargs)
		context['page_title'] = 'Blog'

		return context

class SingleView(LayoutView, DetailView):
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

class TutorialView(LayoutView, ListView):
	template_name = 'blog/tutorials.html'
	queryset = Posts.objects.prefetch_related('postimages_set').exclude(category='DE').order_by('-created')
	context_object_name = 'tutorial_posts'

	def get_context_data(self, **kwargs):
		context = super(TutorialView, self).get_context_data(**kwargs)
		context['page_title'] = 'Tutorials'
		return context