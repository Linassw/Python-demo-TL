from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', login_required(views.DesktopView.as_view()), name="desktop"),
    url(r'^saveDesktop', login_required(views.SaveView.as_view())),
    url(r'^loadDesktop', login_required(views.LoadView.as_view())),
    url(r'^crons/UpdateCurrencies', views.UpdateCurrencies.as_view()),
    url(r'^loadSidebar', views.LoadSidebar.as_view()),
    url(r'^crons/UpdateGlobal', views.UpdateGlobal.as_view()),
]
