from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response 
from api.serializers import PatientSerializer, DoctorSerializer
from api.models import Patient_1, PatientImage, DoctorData
from api.ImageReceptor import down_syndrom_classification
from api.serializers import ReportSerializer
from api.models import ReportResult
import requests

# Creating Patient View
class AddPatientView(generics.ListCreateAPIView): #ListCreate : get and post methods, but Create : post only
    queryset = Patient_1.objects.all()
    serializer_class = PatientSerializer

    # Override the post function in ListCreateAPIView 
    def post(self,request):
        super().post(request) # Call the function defined in super class "ListCreateAPIView" 
        imgs = []
        patient = Patient_1.objects.last()
        for image in request.FILES.getlist('image_upload'):
            PatientImage.objects.create(image_upload = image, patient = patient)
            imgs.append(image)
        diagnosis = down_syndrom_classification(imgs,request.data["nationality"])
        ReportResult.objects.create(patient = patient,result = diagnosis)
        return Response(status=200)

# Creating Doctor View
class AddDoctorView(generics.ListCreateAPIView):
    queryset = DoctorData.objects.all()
    serializer_class = DoctorSerializer

# Creating Report View
class ReportView(generics.ListCreateAPIView):
    queryset = ReportResult.objects.all()
    serializer_class = ReportSerializer   

# class ReportDetails(generics.RetrieveUpdateDestroyAPIView): # Make 3 actions retrieve(get) , update (put) , Destroy (delete request)
#     queryset = ReportResult.objects.all()
#     serializer_class = ReportSerializer 