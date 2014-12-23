from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from blog.models import Posts,PostImages
from portfolio.views import LayoutView
from social.views import JSONResponseMixin

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


"""
JSON Response to utilize with Backbone
"""
class ApiView(LayoutView, TemplateView):
	template_name = 'blog/api.html'

class ApiBlogView(JSONResponseMixin, View):
	def get(self, request, *args, **kwargs):

		posts_query = Posts.objects.prefetch_related('postimages_set').exclude(category='TU').order_by('-created')
		paginator   = Paginator(posts_query, 6)
		page        = request.GET.get('page')

		try:
			paginated_posts = paginator.page(page)
		except PageNotAnInteger:
			paginated_posts = paginator.page(1)
		except EmptyPage:
			paginated_posts = {}

		all_posts = []

		for post in paginated_posts:
			posts = {}
			post_images      = []
			posts['title']   = post.title
			posts['content'] = post.content
			posts['slug']    = post.slug
			posts['created'] = str(post.created)
			posts['id']      = post.id
			post.post_images = post_images

			for images in post.postimages_set.all():
				post_images.append(images.photo.url)

			posts['images'] = post_images
			all_posts.append(posts)

		return self.render_to_response(all_posts)




