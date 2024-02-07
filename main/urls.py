from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path("поддержка", views.about, name = "about"),
    path("анкета", views.health, name = "health"),
    path("врачи", views.doctors, name = "doctors"),
    path("терапевт", views.therapist, name = "therapist"),
    path("гастроэнтеролог", views.gastroenterologist, name = "gastroenterologist"),
    path("офтальмолог", views.ophthalmologist, name = "ophthalmologist"),
    path("акушер-гинеколог", views.obstetriciangynecologist, name = "obstetriciangynecologist"),
    path("инфекционист", views.infectious, name = "infectious"),
    path("невролог", views.neurologist, name = "neurologist"),
    path("эндокринолог", views.Endocrinologist, name = "endocrinologist"),
    path("кардиолог", views.cardiologist, name = "cardiologist"),
    path("хирург", views.surgeon, name = "surgeon"),
    path("оториноларинголог", views.otorhinolaryngologist, name = "otorhinolaryngologist"),
    path("травматолог", views.traumatologist, name="traumatologist"),
    path("уролог", views.urologist, name="urologist"),
    path("онколог", views.oncologist, name="oncologist"),
    path("психиатр", views.psychiatrist, name="psychiatrist"),
    path("педиатр", views.pediatrician, name="pediatrician"),
]


