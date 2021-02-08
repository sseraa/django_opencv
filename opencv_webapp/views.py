from django.shortcuts import render
from .forms import SimpleUploadForm, ImageUploadForm
from django.core.files.storage import FileSystemStorage # file 저장을 위한 Function
from django.conf import settings
from .cv_functions import cv_detect_face
# Create your views here.
def first_view(request):
    return render(request,'opencv_webapp/first_view.html',{})#template/opencv_webapp/..

#직접 만들어낸 form -- DB 안쓰고 작업할때
def simple_upload(request):

    if request.method =='POST':
        # print(request.POST) #csrf_token, title
        # print(request.FILES) #<MultiValueDict: {'image': [<InMemoryUploadedFile: beatles_big.jpg (image/jpeg)>]}>
        # print(request.FILES['image']) #forms.py 의 image -- request memory 안에 임시로 떠있음 .
        form = SimpleUploadForm(request.POST, request.FILES) #filled form

        if form.is_valid(): #saving
            myfile = request.FILES['image'] # ses.jpg 파일 자체
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile) #.name "ses.jpg" (이름)
            uploaded_file_url = fs.url(filename)

            context= {'form': form, 'uploaded_file_url':uploaded_file_url }
            return render(request, 'opencv_webapp/simple_upload.html',context)

    else:   #get요청 일때
        form = SimpleUploadForm() #empty forms
        context= {'form': form }
        return render(request, 'opencv_webapp/simple_upload.html',context)

#models.py의 "DB" class 기준으로 끌어옴
def detect_face(request): #FileSystemStorage를 버리고 과거방식대로 model->form->usr ; 이게 더 나음.

    if request.method == 'POST': #usr가 제출한 경우
        form = ImageUploadForm(request.POST, request.FILES)#description,document -- filled forms

        if form.is_valid():
            # Form에 채워진 데이터를 DB에 실제로 저장하기 전에 변경하거나 추가로 다른 데이터를 추가할 수 있음 #commit=Flase
            post = form.save(commit=False)
            # 얼굴과 눈을 찾는 예측 모델 적용 line typing
            post.save() # DB에 실제로 Form 객체('form')에 채워져 있는 데이터를 저장
	        # post는 save() 후 DB에 저장된 ImageUploadModel 클래스 객체 자체를 갖고 있게 됨 (record 1건에 해당)
            # post.document # 이번에 저장한 row의 document 꺼냄 ..
            imageURL = settings.MEDIA_URL + form.instance.document.name # '/media/' + 'ses.jpg'
            # document : ImageUploadModel Class에 선언되어 있는 “document”에 해당
            # print(form.instance, form.instance.document.name, form.instance.document.url)
            cv_detect_face(settings.MEDIA_ROOT_URL + imageURL) # './media/ses.jpg' -- 꺼내서 줘라
            # cv_detect_face('./media/ses.jpg') #./ root directory(cv_project)
            context = {'form':form, 'post':post}
            return render(request,'opencv_webapp/detect_face.html', context)

    else:
        form = ImageUploadForm() #empty form
        return render(request,'opencv_webapp/detect_face.html',{'form':form})
