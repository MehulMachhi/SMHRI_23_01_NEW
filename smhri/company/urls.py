from django.urls import path
from company import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_company_data', views.add_company_data, name='add_company_data'),
    path('view_company_data', views.view_company_data, name='view_company_data'),
    path('edit_company_data/<int:id>', views.edit_company_data, name='edit_company_data'),
    path('update_company_data/<int:id>/', views.update_company_data, name='update_company_data'),
    path('delete_company_data/<int:id>/', views.delete_company_data, name='delete_company_data'),

]