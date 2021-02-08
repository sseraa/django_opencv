from django import forms
from .models import ImageUploadModel
#before .. class Meta(forms.ModelForm) #<-- modles.py 의 class 상속

class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    # file = forms.FileField()
    image = forms.ImageField() #FileField기능 + is 이미지 검증 + 이미지 세부 정보 저장 (가로세로..etc)

class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageUploadModel
        fields = ('description','document')
