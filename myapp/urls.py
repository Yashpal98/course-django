from . import views
from django.urls import path

urlpatterns = [
    path('home',views.index,name="base"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('download',views.download,name="download"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout/', views.logout,name='logout'),
    path('video_python', views.python,name='python'),
    path('video_html', views.html,name='html'),
    path('video_css', views.css,name='css'),
    path('video_django', views.django,name='django'),
    path('video_javascript', views.javascript,name='javascript'),
    path('video_java', views.java,name='java'),
    path('video_C', views.c,name='C'),
]