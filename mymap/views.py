import csv
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # CSV 파일 경로 설정
    csv_file_path = 'squash_courts_level1.csv'
    
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)
            
        context = {
            'csv_data': data
        }
        return render(request, 'mymap/home.html', context)
        
    except FileNotFoundError:
        return HttpResponse("CSV 파일을 찾을 수 없습니다.", status=404)
    except Exception as e:
        return HttpResponse(f"에러가 발생했습니다: {str(e)}", status=500)