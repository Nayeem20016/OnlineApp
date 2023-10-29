from django.shortcuts import render


def Admin(request):
    return render(request, 'OnlineApp/Admin.html')
def Home(request):
    # data_obj = read model data
    return render(request, 'OnlineApp/Home.html')
# , {'data': data_obj})
