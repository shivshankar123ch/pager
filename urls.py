from django.urls import path
from portpolio import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('blog',views.handleblog,name='handleblog'),
    path('certificate',views.certificate_View,name='certificate'),
    
    path('internshipdetails',views.internshipdetails,name='internshipdetails'),
    path('show_file',views.show_file,name='show_file'),
    # path('chatroomom ',views.chatbot,name='chatroom')
    
    
]




