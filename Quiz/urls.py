from django.contrib import admin
from django.urls import path
from QuizApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('api/get-quiz/', get_quiz, name='get_quiz'),
    path('quiz/', quiz, name='quiz'),
]