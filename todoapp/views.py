 
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Todo,Profile
from .forms import RegistrationForm, TodoForm, TodoEditForm, ProfileForm, TodoEditStatusForm,ProfileUpdateForm

#from django.contrib.auth.decorators import login_required


#Dashboard
class HomeView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'dashboard.html'
    paginate_by = 3


#Sign Up
class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # mengambil input dari form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, self.template_name, {'form':form})



# All To-Do
class TodoAllView(LoginRequiredMixin, ListView):
    model=Todo
    template_name='todoes/todo_list.html'
    paginate_by = 3


# Detail To-Do
class DetailTodoView(DetailView):
    model = Todo
    template_name = 'todoes/todo_detail.html'



#Edit To-Do
class TodoEditView(LoginRequiredMixin, TemplateView):
    template_name = 'todoes/todo_edit.html'
    id = None

    def get(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
            form = TodoEditForm(instance=todo)
            return render(request, self.template_name, {'form':form, 'todo':todo})
        except Exception as error:
            messages.error(request, error)
            return HttpResponseRedirect(reverse('home'))

    def post(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
            form = TodoEditForm(request.POST, instance=todo)
            if form.is_valid():
                updated_todo = form.save()
                messages.success(request, "Post successfully updated")
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.error(request, "Please correct your input")
                return render(request, self.template_name, {'form':form, 'todo':todo} )
        except Exception as error:
                messages.error(request, error)
                return render(request, self.template_name, {'form':form, 'todo':todo} )


#Create To-Do
class TodoCreateView(LoginRequiredMixin ,TemplateView):
    template_name = 'todoes/todo_create.html'

    def get(self, request):
        form = TodoEditForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = TodoEditForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Yeay To-do successfully added")
            return HttpResponseRedirect(reverse('todo-all'))
        else:
            messages.error(request, "Please correct your input")
            return render(request, self.template_name, {'form':form})


#Profile User
class ProfileView(TemplateView):
    template_name = 'profiles/profile.html'

    def get(self, request):
        return render(request, self.template_name)



# Update Profile
class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    templat_ename = 'profiles/profile_edit.html'
    id = None

    def get(self, request, id):
        try:
            profile_update = Profile.objects.get(id=id)
            form = ProfileUpdateForm(instance=profile_update)
            return render(request, self.template_name, {'form':form, 'profile_update':profile_update})
        except Exception as error:
            messages.error(request, error)
            return HttpResponseRedirect(reverse('profile'))

    def post(self, request, id):
        try:
            profile_update = Profile.objects.get(id=id)
            form = ProfileUpdateForm(request.POST, instance=profile_update)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile successfully updated")
                return HttpResponseRedirect(reverse('profile'))
            else:
                messages.error(request, "Please correct your input")
                return render(request, self.template_name, {'form':form, 'profile_update':profile_update} )
        except Exception as error:
                messages.error(request, error)
                return render(request, self.template_name, {'form':form, 'profile_update':profile_update} )


# Status Update (Complete or Not Complete)
class TodoEditStatusView(LoginRequiredMixin, TemplateView):
    template_name = 'todoes/todo_update.html'
    id = None

    def get(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
            form = TodoEditStatusForm(instance=todo)
            return render(request, self.template_name, {'form':form, 'todo':todo})
        except Exception as error:
            messages.error(request, error)
            return HttpResponseRedirect(reverse('home'))

    def post(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
            form = TodoEditStatusForm(request.POST, instance=todo)
            if form.is_valid():
                updated_todo = form.save()
                messages.success(request, "Status successfully updated")
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.error(request, "Please correct your input")
                return render(request, self.template_name, {'form':form, 'todo':todo} )
        except Exception as error:
                messages.error(request, error)
                return render(request, self.template_name, {'form':form, 'todo':todo} )