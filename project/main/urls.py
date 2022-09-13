from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('home', views.index, name='home'),
    path('About-us', views.about, name='about'),
    path('login', views.loginpage, name='login_page'),
    path('Add_a_dish', views.create, name='create'),
    path('Update_a_dish/<str:pk>', views.update, name='update'),
    path('Delete_a_dish/<str:pk>', views.delete, name='delete'),
    path('logout', views.logout_user, name='logout_user'),
    path('Register', views.register, name='register_page'),
    path('popup', views.popup, name='popup_window'),
    path('menu', views.menu, name='menu_page'),
    path('', views.home, name='home_page2'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
