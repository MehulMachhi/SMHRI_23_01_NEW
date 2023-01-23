from django.urls import path
from . import views

urlpatterns = [

    path('get_test', views.get_test, name='get_test'),
    # path('view_test_audiometerthresholddecimats', views.view_test_audiometerthresholddecimats,name='view_test_audiometerthresholddecimats'),
    # path('update_test_audiometerthresholddecimats/<int:id>', views.update_test_audiometerthresholddecimats,name='update_test_audiometerthresholddecimats'),
    # path('delete_test_audiometerthresholddecimats/<int:id>', views.delete_test_audiometerthresholddecimats,name='delete_test_audiometerthresholddecimats'),
    #
    path('add_test_audiometerthresholddecimats', views.add_test_audiometerthresholddecimats, name='add_test_audiometerthresholddecimats'),
    # path('view_test_audiometerthresholddecimats', views.view_test_audiometerthresholddecimats, name='view_test_audiometerthresholddecimats'),
    # path('update_test_audiometerthresholddecimats/<int:id>', views.update_test_audiometerthresholddecimats, name='update_test_audiometerthresholddecimats'),
    # path('delete_test_audiometerthresholddecimats/<int:id>', views.delete_test_audiometerthresholddecimats, name='delete_test_audiometerthresholddecimats'),

    path('add_test_bloodtest', views.add_test_bloodtest, name='add_test_bloodtest'),
    # path('view_test_bloodtest', views.view_test_bloodtest,name='view_test_bloodtest'),
    # path('update_test_bloodtest/<int:id>', views.update_test_bloodtest,name='update_test_bloodtest'),
    # path('delete_test_bloodtest/<int:id>', views.delete_test_bloodtest,name='delete_test_bloodtest'),
    #
    path('add_test_complaints', views.add_test_complaints, name='add_test_complaints'),
    # path('view_test_complaints', views.view_test_complaints, name='view_test_complaints'),
    # path('update_test_complaints/<int:id>', views.update_test_complaints, name='update_test_complaints'),
    # path('delete_test_complaints/<int:id>', views.delete_test_complaints, name='delete_test_complaints'),

    path('add_urine_examination', views.add_urine_examination, name='add_urine_examination'),
    # path('view_test_complaints', views.view_test_complaints, name='view_test_complaints'),
    # path('update_test_complaints/<int:id>', views.update_test_complaints, name='update_test_complaints'),
    # path('delete_test_complaints/<int:id>', views.delete_test_complaints, name='delete_test_complaints'),
    #
    path('add_test_hematology', views.add_test_hematology, name='add_test_hematology'),
    # path('view_test_hematology', views.view_test_hematology, name='view_test_hematology'),
    # path('update_test_hematology/<int:id>', views.update_test_hematology, name='update_test_hematology'),
    # path('delete_test_hematology/<int:id>', views.delete_test_hematology, name='delete_test_hematology'),
    #
    path('add_test_lungfunctiontest', views.add_test_lungfunctiontest, name='add_test_lungfunctiontest'),
    # path('view_test_lungfunctiontest', views.view_test_lungfunctiontest, name='view_test_lungfunctiontest'),
    # path('update_test_lungfunctiontest/<int:id>', views.update_test_lungfunctiontest, name='update_test_lungfunctiontest'),
    # path('delete_test_lungfunctiontest/<int:id>', views.delete_test_lungfunctiontest, name='delete_test_lungfunctiontest'),
    #
    path('add_test_microscopicexamination', views.add_test_microscopicexamination, name='add_test_microscopicexamination'),
    # path('view_test_microscopicexamination', views.view_test_microscopicexamination, name='view_test_microscopicexamination'),
    # path('update_test_microscopicexamination/<int:id>', views.update_test_microscopicexamination,name='update_test_microscopicexamination'),
    # path('delete_test_microscopicexamination/<int:id>', views.delete_test_microscopicexamination,name='delete_test_microscopicexamination'),
    #
    path('add_test_othertests', views.add_test_othertests,name='add_test_othertests'),
    # path('view_test_othertests', views.view_test_othertests,name='view_test_othertests'),
    # path('update_test_othertests/<int:id>', views.update_test_othertests,name='update_test_othertests'),
    # path('delete_test_othertests/<int:id>', views.delete_test_othertests,name='delete_test_othertests'),
    #
    path('add_test_physiologicaltest', views.add_test_physiologicaltest, name='add_test_physiologicaltest'),
    # path('view_test_physiologicaltest', views.view_test_physiologicaltest, name='view_test_physiologicaltest'),
    # path('update_test_physiologicaltest/<int:id>', views.update_test_physiologicaltest, name='update_test_physiologicaltest'),
    # path('delete_test_physiologicaltest/<int:id>', views.delete_test_physiologicaltest, name='delete_test_physiologicaltest'),
    #
    path('add_test_systematicexamination', views.add_test_systematicexamination, name='add_test_systematicexamination'),
    # path('view_test_systematicexamination', views.view_test_systematicexamination, name='view_test_systematicexamination'),
    # path('update_test_systematicexamination/<int:id>', views.update_test_systematicexamination,name='update_test_systematicexamination'),
    # path('delete_test_systematicexamination/<int:id>', views.delete_test_systematicexamination,name='delete_test_systematicexamination'),
    #
    path('add_test_visualtest', views.add_test_visualtest, name='add_test_visualtest'),
    # path('view_test_visualtest', views.view_test_visualtest, name='view_test_visualtest'),
    # path('update_test_visualtest/<int:id>', views.update_test_visualtest,name='update_test_visualtest'),
    # path('delete_test_visualtest/<int:id>', views.delete_test_visualtest,name='delete_test_visualtest'),
    #
    # path('add_test_testmaster', views.add_test_testmaster, name='add_test_testmaster'),
    # path('view_test_testmaster', views.view_test_testmaster, name='view_test_testmaster'),
    # path('update_test_testmaster/<int:id>', views.update_test_testmaster, name='update_test_testmaster'),
    # path('delete_test_testmaster/<int:id>', views.delete_test_testmaster, name='delete_test_testmaster'),

]

















