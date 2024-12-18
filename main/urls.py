from django.contrib import admin
from django.urls import include, path
from prediction.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', hello),
    path('', include('config.urls'))
]
