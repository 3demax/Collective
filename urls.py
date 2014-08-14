from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from post.views import *

from django.conf import settings
from django.conf.urls.static import static

# handler404 = custom404

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drwc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = urlpatterns + patterns('',
    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html.django'}, name="login"),
    # url(r'^register/$', RegistrationView.as_view(), name="register"),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/register/'}, name="logout"),
    # url(r'^$', IndexView.as_view(), name="index"),
    # url(r'^whatis/$', DirectTemplateView.as_view(template_name='whatis.html.django', extra_context=None), name="whatis"),
    # url(r'^rules/$', DirectTemplateView.as_view(template_name='rules.html.django', extra_context=None), name="rules"),
    # url(r'^schedule/$', CompetitionList.as_view(), name="schedule"),
    # url(r'^events/$', EventList.as_view(), name="events"),
    # url(r'^event/(?P<pk>[\d]+)/.*$', EventView.as_view(), name="event"),
    # # url(r'^rating/$', DirectTemplateView.as_view(template_name='rating.html.django', extra_context=None), name="rating"),
    # url(r'^rating/$', RatingView.as_view(), name="rating"),
    # url(r'^photos/$', DirectTemplateView.as_view(template_name='photos.html.django', extra_context=None), name="photos"),
    # url(r'^contacts/$', DirectTemplateView.as_view(template_name='contacts.html.django', extra_context=None), name="contacts"),
    # url(r'^faq/$', DirectTemplateView.as_view(template_name='faq.html.django', extra_context=None), name="faq"),
    # # url(r'^login/$', DirectTemplateView.as_view(template_name='login.html.django', extra_context=None), name="login"),
    # url(r'^profile/$', profile_user_view, name="profile"),
    # url(r'^profile/id(?P<pk>[\d]+)/$', ProfileView.as_view(), name="profile_id"),
    # url(r'^settings/$', ProfileUpdateView.as_view(), name="profile_settings"),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^add/$', AddView.as_view(), name="add_post"),
    url(r'^edit/(?P<pk>[\d]+)/$', EditView.as_view(), name="edit_post"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)