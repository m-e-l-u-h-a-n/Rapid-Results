from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

# Create your views here.
class HomeView(LoginRequiredMixin, ListView):
    """Home view is  used for listing of all the Items present for selling in the website."""
    paginate_by = 10
    template_name = "home.html"
    queryset = []

class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'profile.html'
