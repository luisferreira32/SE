from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import redirect_to_login

from .models import Profile
from django.contrib.auth.models import User


class SignUp(generic.CreateView):
    """ Extension of a generic creation class to create users """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserView(generic.DetailView):
    """ Extension of a generic detail class to view user profile """
    model = User
    context_object_name = 'userprofile'
    template_name = 'profile.html'

class ProfileUpdate(generic.UpdateView):
    """ Extension of a generic update class to view an update form of the profile """
    model = Profile
    fields = ['nickname', 'description', 'photo']
    template_name = "update.html"

    def user_passes_test(self, request):
        """ Verify if the user is seeing his own profile """
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        """ Only dispatches the view if the user is authenticated to update his profile """
        if not self.user_passes_test(request):
            return redirect_to_login(request.get_full_path())
        return super(ProfileUpdate, self).dispatch(
            request, *args, **kwargs)
