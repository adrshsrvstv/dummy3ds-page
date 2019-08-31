from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

AccuCardholderId=""
AccuGuid=""
AccuReturnURL=""
session=""
AccuRequestId=""
AccuResponseCode=""

SUCCESS_RESPONSE_CODE=""

@csrf_exempt
def index(request):
    global AccuCardholderId
    global AccuGuid
    global AccuReturnURL
    global session
    global AccuRequestId
    global AccuResponseCode

    if request.method == 'POST':

        SUCCESS_RESPONSE_CODE=request.POST.get('AccuResponseCode')
        context = {'AccuCardholderId': AccuCardholderId, 'AccuGuid': AccuGuid, 'AccuReturnURL': AccuReturnURL, 'session': session, 'AccuRequestId': AccuRequestId, 'SUCCESS_RESPONSE_CODE': SUCCESS_RESPONSE_CODE}

        return HttpResponse('')

@csrf_exempt
def initotp(request):
    global AccuCardholderId
    global AccuGuid
    global AccuReturnURL
    global session
    global AccuRequestId
    global AccuResponseCode

    if request.method == 'POST':
        context = {'AccuCardholderId': AccuCardholderId, 'AccuGuid': AccuGuid, 'AccuReturnURL': AccuReturnURL, 'session':session, 'AccuRequestId': AccuRequestId, 'AccuResponseCode':AccuResponseCode  }
        AccuCardholderId="\""+request.POST.get('AccuCardholderId')+"\""
        AccuGuid = "\""+request.POST.get('AccuGuid')+"\""
        AccuReturnURL = request.POST.get('AccuReturnURL')
        if str(AccuReturnURL).startswith('http://') or str(AccuReturnURL).startswith('https://'):
            AccuReturnURL = "\""+request.POST.get('AccuReturnURL')+"\""
        session = "\""+request.POST.get('session')+"\""
        AccuRequestId = "\""+request.POST.get('AccuRequestId')+"\""

        return redirect(initotp)

    # display a form, collect otp, make a post request to submitotp and all other params including
    if request.method == 'GET':
        context = {'AccuCardholderId': AccuCardholderId, 'AccuGuid': AccuGuid, 'AccuReturnURL': AccuReturnURL, 'session':session, 'AccuRequestId': AccuRequestId, 'AccuResponseCode':AccuResponseCode  }
        return render(request, 'threeds.html', context)

def submitotp(request):
    global AccuCardholderId
    global AccuGuid
    global AccuReturnURL
    global session
    global AccuRequestId
    global AccuResponseCode

    # save the params provided, look at the otp. Based on OTP, populate AccuResponseCode and post to termURL
    if request.method == 'POST':
        AccuResponseCode="\'NULL\'"
        if request.POST.get('otp') == '1234':
            AccuResponseCode="\'ACCU000\'"
        elif request.POST.get('otp') == '0000':
            AccuResponseCode="\'ACCU100\'"

        context = {'AccuCardholderId': AccuCardholderId, 'AccuGuid': AccuGuid, 'AccuReturnURL': AccuReturnURL, 'session': session, 'AccuRequestId': AccuRequestId,
                   'AccuResponseCode': AccuResponseCode}
        if str(AccuReturnURL).startswith('\"http://') or str(AccuReturnURL).startswith('\"https://'):
            return render(request, 'interstitial.html', context)
        else:
            return render(request, 'webview_submit.html', context)



    if request.method == 'GET':
        return redirect(initotp)

def simulator(request):
    #make a post request to initotp page with some default values of params.
    return render(request, 'simulator.html', {})

@csrf_exempt
def termurl(request):
    global AccuCardholderId
    global AccuGuid
    global AccuReturnURL
    global session
    global AccuRequestId
    global AccuResponseCode
    # pass this url in the AccuReturnURL field from simulator/ and use this page to display the received values.
    context = { 'AccuGuid': AccuGuid,  'session': session, 'AccuRequestId': AccuRequestId,'AccuResponseCode': AccuResponseCode}
    return render(request, 'termurl.html', context)