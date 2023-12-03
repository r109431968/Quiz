from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import random


# Create your views here.
def Home(request):
    # return HttpResponse('Hello d-Jango.')
    context = {'categories': Category.objects.all()}
    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    return render(request, 'home.html', context)


def quiz(request):
    context = {'category': request.GET.get('category')}
    return render(request, 'quiz.html', context)


def get_quiz(request):
    try:
        category_name = request.GET.get('category')

        if category_name:
            question_objs = Question.objects.filter(category__category_name__icontains=category_name)
            # in above line we can see double underscore(__) why it is used ? because agar ap kisi foreign key table ka data access krna chate hain to double underscore(__) lgana padega
            # icontains ek django ka filter hai jo sql me "like" hota hai us ke jaisa behave krta hai.
        else:
            question_objs = Question.objects.all()

        question_objs = list(question_objs)
        random.shuffle(question_objs)

        data = []
        for question_obj in question_objs:
            data.append({
                "uid": question_obj.uid,
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answers": question_obj.get_answers()
            })

        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
        print(f"Error occurred: {e}")
        return HttpResponse('Something went wrong !!.')
