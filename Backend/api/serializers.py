from rest_framework import serializers
from api.models import Patient_1,PatientImage,DoctorData,ReportResult

# Intializing an image serializer for the uploaded images by the user
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientImage
        fields = ['image_upload']

# Initializing a report serializer for the patient's report
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportResult
        fields = ['id','result']

# Intializing a patient serializer 
class PatientSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True,read_only=True)
    results = ReportSerializer(many=True,read_only=True)
    class Meta:
        model = Patient_1
        fields = ['id','name','birthdate','nationality','gender','visitReason','captured_image','images','consent','results']
        read_only_fields = ('images','results')

# Intializing a doctor serializer
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorData
        fields = ['id','user_name','email','phone_number','password']

        def create(self, validated_data):
            user = DoctorData.objects.create(
                user_name= validated_data['user_name'],
                email = validated_data['email'],
                phone_number= validated_data['phone_number'],
            )
            user.set_password(validated_data['password'])
            user.save()
            return user

