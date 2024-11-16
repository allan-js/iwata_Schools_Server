from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

from .models import StudentWork
from .serializers import StudentWorkSerializer

def homepage(request):
    return render(request, 'index.html', {})

def get_student_works(request, username):
    try:
        # Get all non-archived works for the student
        works = StudentWork.objects.filter(
            student=username,
            is_archived=False
        ).order_by('-uploaded_on')
        
        # Prepare the data
        works_data = []
        for work in works:
            works_data.append({
                'name': work.name,
                'file_url': request.build_absolute_uri(work.file.url),
                'uploaded_on': work.uploaded_on.strftime('%Y-%m-%d %H:%M:%S'),
                'file_type': work.file.name.split('.')[-1].lower()
            })
        
        return JsonResponse({
            'status': 'success',
            'works': works_data
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)
    

@csrf_exempt  # or use proper CSRF handling
def student_work_upload(request):
    if request.method == 'POST':
        student_name = request.POST.get('student')
        name = request.POST.get('name')
        # print('File Name: ', name)
        # print('Student Name: ', student_name)
        file = request.FILES.get('file')
        # print('File: ', file)
        if student_name and file:
            try:
                # Create a new StudentWork instance
                student_work = StudentWork.objects.create(
                    name=name,
                    student=student_name,
                    file=file,
                )
                return JsonResponse({'file': student_work.file.url}, status=201)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        else:
            return JsonResponse({'error': 'Missing student or file data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)