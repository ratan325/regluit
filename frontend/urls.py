from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from regluit.core.models import Campaign
from regluit.frontend.views import CampaignFormView, GoodreadsDisplayView

urlpatterns = patterns(
    "regluit.frontend.views",
    url(r"^$", "home", name="home"),
    url(r"work/(?P<work_id>.+)/$", "work", name="work"),
    url(r"^supporter/(?P<supporter_username>.+)/$", "supporter", {'template_name': 'supporter.html'}, name="supporter"),
    url(r"^supporter2/(?P<supporter_username>.+)/$", "supporter", {'template_name': 'supporter_panel.html'}, name="supporter2"),
    url(r"^search/$", "search", name="search"),
    url(r"^privacy/$", TemplateView.as_view(template_name="privacy.html"),
        name="privacy"),
    url(r"^rightsholders/$", TemplateView.as_view(template_name="rhtools.html"),
        name="rightsholders"), 
    url(r"^wishlist/$", "wishlist", name="wishlist"),
    url(r"^campaigns/$", ListView.as_view(
        model=Campaign,template_name="campaign_list.html", context_object_name="campaign_list")),
    url(r"^campaigns/(?P<pk>\d+)/$",CampaignFormView.as_view(), name="campaign_by_id"),
    url(r"^goodreads/$", GoodreadsDisplayView.as_view(), name="goodreads_display"),
    url(r"^goodreads/auth_cb/$", "goodreads_cb", name="goodreads_cb"),
    url(r"^goodreads/flush/$","goodreads_flush_session", name="goodreads_flush_session"),
    url(r"^stub/", "stub", name="stub")
)
