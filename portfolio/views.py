from datetime import date
from django.views.generic import DetailView, TemplateView
from portfolio.models import Images, Categories, Videos
from blog.models import Posts
from francismitra import settings

"""
Mixin for layout template - pulls portfolio categories for menu,
current year for footer, and date of latest blog update
"""
class LayoutView(object):
    def get_context_data(self, **kwargs):
        layout_content = {
            'menu': Categories.objects.all().order_by('sorter'),
            'updated_at': Posts.objects.latest('created'),
            'year': date.today().year,
            # handles the loading of google analytics
            'development': settings.DEBUG
        }

        context = super(LayoutView, self).get_context_data(**kwargs)

        for key in layout_content:
            context[key] = layout_content[key]
                
        return context

class IndexView(LayoutView, TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['aside'] = ['abstract&', 'love&', 'fashion&', 'travel&']
        context['mobile_home'] = True 
        return context

class CategoryView(LayoutView, DetailView):
    template_name = 'portfolio/category.html'
    model = Categories

    meta_desc =  {}
    meta_desc['Singles'] = "A collection of conceptual photographs by New York creative and developer Francis Mitra."
    meta_desc['Life'] = "A private glance at New York 20-somethings by Francis Mitra."
    meta_desc['People'] = "Portraiture by New York photographer Francis Mitra."
    meta_desc['Places'] = "Street photography and documentary work by traveling photographer Francis Mitra."

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['page_title'] = 'Portfolio | %s' % (self.get_object().title)
        context['page_description'] = self.meta_desc[self.get_object().title]
        return context

class ResumeView(LayoutView, TemplateView):
    template_name = 'portfolio/resume.html'

    def get_context_data(self, **kwargs):
        context = super(ResumeView, self).get_context_data(**kwargs)
        context['page_title'] = 'Resume'
        context['page_description'] = 'Resume of New York based digital creative, Francis Mitra'
        return context

class InfoView(LayoutView, TemplateView):
    template_name = 'portfolio/info.html'

    def get_context_data(self, **kwargs):
        context = super(InfoView, self).get_context_data(**kwargs)
        context['page_title'] = 'Info'
        context['page_description'] = 'Street photographer and web developer. I often find myself juggling creative and technical ventures'
        return context

