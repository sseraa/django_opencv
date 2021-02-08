from django.db import models

# Create your models here.
class ImageUploadModel(models.Model):

    description = models.CharField(max_length=255,blank=True) #null 이어도 ㄱㅊ
    # upload_to : 저장될 파일의 경로를 지정 (ex. ‘images/2020/02/21/test_image.jpg’)
    document = models.ImageField(upload_to='images/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True) #등록시점 자동 저장
