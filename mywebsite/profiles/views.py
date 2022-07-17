# from email import message
# import re
from turtle import update
from django.shortcuts import redirect, render
# Create your views here.
from .models import UserProfile
from .forms import UpdateProfileForm
from django.contrib import messages

# get the profile by their primary key
def profile(request, pk):
    user_profile = UserProfile.objects.get(profile_id = pk)
    context = {
        'profile' : user_profile
    }
    return render(request, 'profiles/profile.html', context)


def account(request):
    # ===> the user profile is from the model it is been turn to lowercase
    user_account = request.user.userprofile
    context = {'account' : user_account}
    return render(request, 'profiles/account.html', context)



def UpdateUserProfile(request):
    # Todo: want to get the [instance] of the currently logged in user.
    # * want to prefiled the update profile form.
    updateprofile = request.user.userprofile
    updateform = UpdateProfileForm(instance= updateprofile)
    if request.method == 'POST':
        updateform = UpdateProfileForm(request.POST, request.FILES, instance=updateprofile)
        if updateform.is_valid():
            updateform.save()
            messages.info(request, 'You have successfully updated your profile')
            return redirect('account')
    
    context = {'updateform' : updateform}
    return render(request, 'profiles/updateprofile.html', context)