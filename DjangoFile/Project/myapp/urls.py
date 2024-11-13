
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

# User Details
    path('create_user/',UserCreate.as_view(),name='create_user'),
    path('update_user/<int:pk>/',UserUpdate.as_view(),name='update_user'),
    path('details_user/<int:pk>/',UserDetails.as_view(),name='details_user'),
    path('delete_user/<int:pk>/',UserDelete.as_view(),name='delete_user'),
# Book Details
    path('book_create/',BookCreate.as_view(),name='book_create'),
    path('book_update/<int:pk>/',Bookupdate.as_view(),name='book_update'),
    path('book_details/<int:pk>/',BookDetails.as_view(),name='book_details'),
    path('book_delete/<int:pk>/',BookDelete.as_view(),name='book_delete'),
# Admin Register
    path('register/',Register.as_view(),name='register'),
    path('register_delete/',RegisterDelete.as_view(),name='register_delete'),
# Admin Login
    path('login/',Login.as_view(),name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
