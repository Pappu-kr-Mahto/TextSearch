from django.urls import path
from . import views


urlpatterns = [
    path('',views.loginUI,name="app-login"),

    #urls for navagating UI
    path('app-home/',views.home,name="app-home"),
    path('app-login/',views.loginUI,name="app-login"),
    path('app-signup/',views.signupUI,name="app-signup"),

    path('api/signup/',views.signup,name="signup"),
    path('api/login/',views.login,name="login"),

    path('api/all-paragraph/',views.allParagraph,name="all-paragraph"),
    path('api/add-paragraph/',views.addParagraph,name="add-paragraph"),
    path('api/word-search/<word>',views.wordSearch,name="word-search"),
]
