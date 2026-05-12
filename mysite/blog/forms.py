class SignUpForm(UserCreationForum):
    class Meta:
        model = User
        fields = ('usernam', 'email', 'password1', 'password2')