import json
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django import http
from social.models import PersonalInstagram, AuthenticateInstagram
from francismitra.settings import INSTAGRAM_CONFIG
from portfolio.views import LayoutView
from django.http import JsonResponse


"""
Begin authentication to allow viewers to 'comment' and 'like' media.
Authentication is completed after user requests access token through
class SocialView and verified through checking session['access_token']
"""
instagram_user = AuthenticateInstagram(INSTAGRAM_CONFIG['client_id'], 
                                       INSTAGRAM_CONFIG['client_secret'], 
                                       INSTAGRAM_CONFIG['redirect_uri'])

"""
Personal Instagram feed rendered as JSON response.
Does not require authentication and is an instance of
a separate model
""" 
class InstagramFeed(View):
    def get(self, request, *args, **kwargs):
        my_instagram = PersonalInstagram(INSTAGRAM_CONFIG['user_id'], 
                                         INSTAGRAM_CONFIG['client_id'])
        
        max_id = request.GET.get('max_id', '')

        try: 
            instagram_feed = my_instagram.find_feed(max_id)
            json_response  = {'result':'success', 'content':instagram_feed}
        except Exception:
            json_response = {'result':'fail', 'content':'Failure in Django class InstagramFeed'}

        context = json_response
        return JsonResponse(context)


"""
Allow visitors the option to connect via
the API to perform authenticated actions on model PersonalInstagram
"""
class SocialView(LayoutView, TemplateView):
    template_name = 'social/social.html'

    def get_context_data(self, **kwargs):
        context = super(SocialView, self).get_context_data(**kwargs)
        context['page_title'] = 'Social'
        context['page_description'] = 'Mobile photography from around the world by digital creative Francis Mitra'

        # Check if code parameter is available and retrieve token
        if self.request.GET.get('code'):
            code = self.request.GET.get('code') 

            try:
                access_token = instagram_user.find_access_token(code)
                self.request.session['access_token'] = access_token
            except Exception:
                print 'Code not available in Django class SocialView'

        # Create visible button to authenticate users
        if not self.request.session.get('access_token'):
            context['link'] = instagram_user.get_authorization_url()

        return context

"""
Allow authenticated users to 'like' personal Instagram feed
"""
class MediaLike(View):
    def get(self, request, *args, **kwargs):
        if self.request.session.get('access_token'):
            token = self.request.session.get('access_token');

            id = self.request.GET.get('id')

            try: 
                status = instagram_user.media_check(token, id)

                json_response = {'result':'success', 'previously_liked':status}

            except Exception:
                json_response = {'result':'fail', 'message':'Failure in Django class MediaLike'}

        else:
            json_response = {'result':'fail', 'message':'Not logged in'}

        context = json_response

        return JsonResponse(context)









