from django.urls import path
from .views import login_view, register_view, logout_view, member_view

app_name = 'accounts'
urlpatterns = [
    #hey, wenn eine Anfrage an / reinkommt,dann übergebe das der
    # funktion xy aus der views.py
    # path('', xy),
    # path('signup/', signup_view, name="signup"),
    # path('', home_view, name="home")
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('member/', member_view, name='member'),
]
