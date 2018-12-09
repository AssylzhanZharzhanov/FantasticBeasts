from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


class UserForm(View):
    form_class = UserForm
    template_name = 'authentication/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print(user)

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})

