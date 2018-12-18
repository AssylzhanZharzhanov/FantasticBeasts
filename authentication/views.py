from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from shopping_cart.models import create_cart


class UserForm(View):
    # form_class = UserForm
    template_name = 'authentication/registration.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            create_cart(request)
            return redirect('/')
        # form = self.form_class(request.POST)
        #
        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        #     user = authenticate(username=username, password=password)
        #     if user is not None:
        #         if user.is_active:
        #             login(request,user)
        #             return redirect('/')
        #         else:
        #             return redirect('/login')

        return render(request, self.template_name, {'form': form})

