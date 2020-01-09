from django.shortcuts import render
from django.http import HttpResponse
def navigation(request):
    s = '<head><style>#chakra{color:blue}#block{text-align:center;border:2px solid black;margin:100px;}#amz{color:orange;text-decoration:none;}#google{color:#9e9e9e;text-decoration:none;}#gmail{color:green;text-decoration:none;}</style></head>' \
        '<div id="block"><h1><a href="https://amazon.com" id="amz">AMAZON</h1>' \
        '<h1><a href="https://google.com" id="google">GO<span id = "chakra">O</span>GLE</h1>' \
        '<h1><a href="https://gmail.com" id="gmail">Gmail</h1></div>'

    return HttpResponse(s)
def nav(request):
    return render(request,'nav.html')
def inputData(request):
    return render(request,'textArea.html')
def outputData(request):
    result = request.GET.get('text_val', 'default')
    print(result)
    opt = request.GET.get('removepunc','off')
    print(opt)
    analyzed = result
    punctuation = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    analyzed = ""
    if opt == "on":
        for chr in result:
            if chr  not in punctuation:
                analyzed = analyzed + chr
        param = {"pusporse":"Removed punctuation","analyzed_text":analyzed}
        return render(request,'analyze.html',param)
    else:
        return HttpResponse("Error")

