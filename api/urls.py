from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BooksViewset

router = DefaultRouter() 
router.register('books', BooksViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('authentication/', include('user.urls')),
    path('api/books/', include('books.urls'))
]
