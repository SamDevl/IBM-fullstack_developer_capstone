from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView
from .restapis import get_request, analyze_review_sentiments, post_review

app_name = 'djangoapp'
urlpatterns = [

     # path for getdealerdetails
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),
     # path for getdealers
    path(route='get_dealers/', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
     # path for getcars
    path(route='get_cars', view=views.get_cars, name ='getcars'),
    # path for registration
   path('register/', views.registration, name='register'),
    # path for login
    path(route='login', view=views.login_user, name='login'),
    # path for logout
    path('logout', view=views.logout_user, name='logout'),
    # path for dealer reviews view
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),
    # path for add a review view
    path(route='add_review', view=views.add_review, name='add_review')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
