from django import forms

#class SignUpForm(UserCreationForm):
#    first_name = forms.CharField(max_length=100, help_text='First Name')
#    last_name = forms.CharField(max_length=100, help_text='Last Name')
#    email = forms.EmailField(max_length=150, help_text='Email')


#class Meta:
#    model = User
#    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=35, label="Username")
    password = forms.CharField(max_length=35, min_length=6, label="Password", widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=35, label="Username")
    password = forms.CharField(max_length=35, min_length=6, label="Password", widget=forms.PasswordInput())
    email = forms.EmailField(label="Email")


    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Username already exists')
        return username


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Email already exists')
        return email
