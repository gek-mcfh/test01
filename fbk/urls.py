from django.contrib import admin
from django.urls import path
from requests.views import extract_content

urlpatterns = [
    path('', extract_content),
    path('admin/', admin.site.urls),
]
