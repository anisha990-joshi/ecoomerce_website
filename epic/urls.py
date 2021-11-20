
from django.contrib import admin
from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='shoekart'),
    path('products', views.products, name='products'),
    path('customer', views.customer, name='customer'),
    path('category', views.category, name='category'),
    path('black_shoe',views.black_shoe,name='black_shoe')


]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)