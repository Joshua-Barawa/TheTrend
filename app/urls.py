from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='index'),
    path('post-question/', post_question, name='post-question'),
    path('add-comment/<int:id>', add_comment, name='add-comment'),
    path('register-user/', register_user, name='register-user'),
    path('login-user/', login_user, name='login-user'),
    path('logout-user/', logout_user, name='logout-user'),
    path('profile/', my_profile, name='profile'),
    path('delete-account/<int:id>', delete_account, name='delete-account'),
    path('like/<int:id>', like, name='like'),
    path('dislike/<int:id>', dislike, name='dislike'),
    path('submit-project/', submit_project, name='submit-project'),
]