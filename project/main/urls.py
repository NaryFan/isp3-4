from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('About-us', views.about, name='about'),
]