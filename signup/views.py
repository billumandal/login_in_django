from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import TemplateView, FormView
from .forms import SignupForm


class HomePageView(TemplateView):
    template_name = "signup/product.html"


class Register_user(FormView):

    '''
    To add a user
    '''

    def post(self, request):

        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)


class Login_view(TemplateView):

    '''
    Login user code
    '''
    template_name = 'signup/login.html'

    def post(self, request):
        print('in post')
        u_name = request.POST['u_name']

        password = request.POST['login_password']
        print(u_name)
        print(password)
        user = authenticate(username=u_name, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(status=200)
        else:

            return HttpResponse(status=400)
