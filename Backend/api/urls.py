from django.urls import path
from api.views import AddPatientView,AddDoctorView,ReportView

# Importing Token Views for JWT Authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('PatientForm/', AddPatientView.as_view() , name = "Patient"),
    path('PatientForm/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('PatientForm/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('PatientForm/Doctor/', AddDoctorView.as_view() , name = "Doctor"),
    path('ReportResult/', ReportView.as_view(), name = "Report"),
]