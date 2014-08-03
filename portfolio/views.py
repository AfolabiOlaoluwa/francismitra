from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# from django.template import RequestContext, loader
from django.views import generic

from portfolio.models import Images, Categories, Videos

# Function Based Views
# def index(request):
	# categories = Categories.objects.all()
	# return render(request, 'portfolio/index.html', {'categories':categories})

# def categories(request, title):
# 	try:

# 	    cat = Categories.objects.get(title=title)
# 	    portfolio = Images.objects.filter(category_id=cat.id)

# 	except Categories.DoesNotExist:
# 	    raise Http404
# 	return render(request, 'portfolio/category.html', {'portfolio': portfolio})


# Class Based Views
class LayoutView(object):

	template_name = 'portfolio/layout.html'

	def get_context_data(self, **kwargs):
		context = super(LayoutView, self).get_context_data(**kwargs)
		context['menu'] = Categories.objects.all()
		return context

class IndexView(LayoutView, generic.TemplateView):
	template_name = 'portfolio/index.html'


class CategoryView(LayoutView, generic.DetailView):
	model = Categories
	template_name = 'portfolio/category.html'

