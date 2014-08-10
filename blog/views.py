from django.shortcuts import render, get_object_or_404
from django.views import generic
from blog.models import Posts,PostImages
from portfolio.views import LayoutView

class BlogView(LayoutView, generic.ListView):
	template_name = 'blog/blog.html'
	model = Posts
	context_object_name = 'all_posts'

class SingleView(LayoutView, generic.DetailView):
	template_name = 'blog/single.html'
	model = Posts

	def get_context_data(self, **kwargs):
		context = super(SingleView, self).get_context_data(**kwargs)
	
		context['images'] = PostImages.objects.filter(post_id=self.object)
		return context

class TutorialView(LayoutView, generic.TemplateView):
	template_name = 'blog/tutorials.html'