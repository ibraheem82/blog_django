from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    
    class Meta:
        # we are using our user model
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
        
        
        
        
        
        
        
        
        
           # ! GETTING rid of the django helpertext
        # * [EXPLANATIONS] ===> the init method id taking in (self, *args, **kwargs)
    # def __init__(self, *args, **kwargs):
        #  * so we are overwriting the whole funtionalities of that method
        # super(SignUpForm, self).__init__(*args, **kwargs)

        # for fieldname in ['username', 'email', 'password1', 'password2']:
        #     self.fields[fieldname].help_text = None 
        
        
        
        
        
        
        
        
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       