# from multiprocessing import context
from django.shortcuts import render, redirect

# ===> [UserCreationForm] is the django default forms that you can use to create {users}.


# TODO : [NOTE] ===>  Explain user creation form before explaining Signupform for the forms.py usercreationform should be first rendered in the templates before SignUpForm.



# from django.contrib.auth.forms import UserCreationForm


# TODO : [NOTE] ===> Replace usercreationform with Signupform after proper explanation
from .forms import SignUpForm


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        # ===> Grabing all the datas
        # form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = SignUpForm()

    context = {
        'form' : form,
    }
    return render(request, 'authentication/sign_up.html', context)