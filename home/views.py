from django.shortcuts import render,HttpResponse, redirect
from .forms import ImageForm
from random import randint,seed
from datetime import datetime
import cv2
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def home(request):
    if request.method == 'POST':
        request.FILES['image'].name = give_random() + request.FILES['image'].name.split('.')[-1]
        current_file = request.FILES['image'].name
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            converted_file_name,faces_found = process(current_file)
            if(converted_file_name == 0):
                return render(request, 'error.html')
            converted_file_name = "http://127.0.0.1:8000/"+"media/user_images/"+converted_file_name
            context = {
                'file_name' : converted_file_name,
                'fn': faces_found
            }
            return render(request, 'render.html', context)
    else:
        form = ImageForm()
    return render(request, 'home.html', {'form': form})

def give_random():
    seed(datetime.now())
    char_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    final_string = ""
    for x in range(20):
        final_string += char_list[randint(0,51)]
    final_string += '.'
    return final_string

def process(file_name):
    try:
        imagePath = os.path.join(BASE_DIR, "media/user_images/"+file_name)
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (randint(0,255), randint(0,255), randint(0,255)), 2)
        y = file_name.split('.')[-1]
        x = file_name.split('.')[0]
        x += "_converted."
        x += y
        print(x)
        cv2.imwrite(os.path.join(BASE_DIR, "media/user_images/"+x), image)
        return x,len(faces)
    except:
        return 0,0

