from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views import View
from .models import *
from .forms import *
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class LoginView(FormView):
    form_class = LoginForm
    success_url = reverse_lazy('index')
    template_name = 'login.html'

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return super().form_valid(form)


class LogoutView(View):
    def get(self,  request):
        logout(request)
        return redirect('index')


class CreateUserView(FormView):
    form_class = UserForm
    success_url = reverse_lazy('index')
    template_name = 'create_user.html'

    def form_valid(self, form):
        User.objects.create_user(
            username=form.cleaned_data['user_name'],
            password=form.cleaned_data['password'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email']
        )
        return super().form_valid(form)


class CreateKennelView(View):
    def get(self, request):
        form = KennelForm()
        ctx = {
            'form': form
        }
        return render(request, 'add_kennel.html', ctx)

    def post(self, request):
        form = KennelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        ctx = {
            'form': form
        }
        return render(request, 'add_kennel.html', ctx)



class CreateDogView(View):
    def get(self, request):
        form = DogForm()
        ctx = {
            'form': form
        }
        return render(request, 'add_dog.html', ctx)

    def post(self, request):
        form = DogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        ctx = {
            'form': form
        }
        return render(request, 'add_dog.html', ctx)