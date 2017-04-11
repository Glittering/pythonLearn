from django.conf.urls import url,patterns
from views import *

urlpatterns = patterns('',
    url(r'hello/$',hello),
    url(r'teacher/$',teacher)
)