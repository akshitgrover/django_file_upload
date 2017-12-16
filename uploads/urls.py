from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'fdc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^upload/', view.upload.as_view()),
    url(r'^home/',view.home.as_view())
]
