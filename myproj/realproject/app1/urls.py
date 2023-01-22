from django.urls import path 
from . import views

urlpatterns = [
    path('',views.renderhtml),
    path('contact/',views.viewhtml , name="contact"),
    path('Donation/' , views.viewDonation , name ="viewDonation"),
    path('createdonation/' , views.createDonation , name ="createDonation"),
    path('showdonation/<id>' , views.showDonationWithID , name ="showDonation"),
    path('deletedonation/<id>' , views.deleteDonationWithID , name ="deleteDonation"),
    path('updatedonation/<id>' , views.updateDonationWithID , name ="updateDonation") ,
    path('login/' , views.loginPage , name ="Login") ,
    path('register/' , views.registerPage , name ="Register") 
     



    
]  
