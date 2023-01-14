from django.urls import path 
from . import views

urlpatterns = [
    path('',views.renderhtml),
    path('Donation/' , views.viewDonation , name ="viewDonation"),
    path('createdonation/' , views.createDonation , name ="createDonation"),
    path('showdonation/<id>' , views.showDonationWithID , name ="showDonation"),
    path('deletedonation/<id>' , views.deleteDonationWithID , name ="deleteDonation"),
    path('updatedonation/<id>' , views.updateDonationWithID , name ="updateDonation") ,
     



    
]  
