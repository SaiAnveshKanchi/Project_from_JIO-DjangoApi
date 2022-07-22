from this import d
from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import datetime
import json

from .models import Version,Device,Data,DateSent,SensorValues
from .serializers import VersionSerializer,DeviceSerializer

# Create your views here.

def all_versions(request):
    if request.method == 'GET':
        versions = Version.objects.all()
        data = [version.vv for version in versions]
        return JsonResponse({
            'payload': data,
            'status' : 'versions extracted successfully'
        })

def all_devices(request):
    if request.method == 'GET':
        devices = Device.objects.all()
        data = [device.dd for device in devices]
        return JsonResponse({
            'payload': data,
            'status' : 'Device ids extracted successfully'
        })

def versions_date(request):
    if request.method == 'GET':
        sent_date = request.GET['date']
        sent_date = datetime.datetime.strptime(sent_date,"%d-%m-%Y")
        sent_date = sent_date.date()
        all_data = Data.objects.filter(sent_date=sent_date)
        versions = [data.version.vv for data in all_data]
        version = []
        for v in versions:
            if v not in version:
                version.append(v)

        return JsonResponse({
            'payload' : version,
            'status' : 'versions extracted successfully for required date'
        })


def highest_data(request):
    if request.method == 'GET':
        sent_date = request.GET['date']
        sent_date = datetime.datetime.strptime(sent_date,"%d-%m-%Y")
        sent_date = sent_date.date()
        all_data = Data.objects.filter(sent_date=sent_date)
        tm = 0.00
        hm = 0.00
        for data in all_data:
            if float(data.dt['tm']) > tm:
                tm = float(data.dt['tm'])
            if float(data.dt['hm']) > hm:
                hm = float(data.dt['hm'])
        output = [{'tm':tm},{'hm':hm}]
        return JsonResponse({
            'payload' : output,
            'status' : 'highest tm and hm values for given date extracted'
        })

def no_of_data(request):
    if request.method == 'GET':
        start_date = request.GET['start_date']
        start_date = datetime.datetime.strptime(start_date,"%d-%m-%Y")
        start_date = start_date.date()
        end_date = request.GET['end_date']
        end_date = datetime.datetime.strptime(end_date,"%d-%m-%Y")
        end_date = end_date.date()
        version = request.GET['vn']
        version = str(version)
        versions = Version.objects.all()
        for v in versions:
            if v.vv==version:
                version=v
                break
        all_data = Data.objects.filter(sent_date__range=[start_date, end_date],version=version)
        output = [{'datapoints':len(all_data)}]
        return JsonResponse({
            'payload' : output,
            'status' : 'number of data points for given version extracted'
        })

def no_of_days(request,n):
    if request.method == 'GET':
        n=int(n)
        data = DateSent.objects.filter(noof_versions=n)
        days = len(data)
        output = [{'days':days}]
        return JsonResponse({
            'payload' : output,
            'status' : 'required number of days extracted'
        })

def is_equal(dt,dt2):
    if str(dt.get("tm",0))==str(dt2.get("tm",0)) and str(dt.get("hm",0))==str(dt2.get("hm",0)) and str(dt.get("wd",0))==str(dt2.get("wd",0)) and str(dt.get("ws",0))==str(dt2.get("ws",0)) and str(dt.get("sm",0))==str(dt2.get("sm",0)) and str(dt.get("st",0))==str(dt2.get("st",0)) and str(dt.get("sc",0))==str(dt2.get("sc",0)) and str(dt.get("lt",0))==str(dt2.get("lt",0)) and str(dt.get("lw",0))==str(dt2.get("lw",0)) and str(dt.get("bl",0))==str(dt2.get("bl",0)) and str(dt.get("pv",0))==str(dt2.get("pv",0)) :
        return True

    return False

def update_versions():
    data = Data.objects.all()
    versions = Version.objects.all()
    data_vv = []
    version_vv = []
    for d in data:
        if d.version.vv not in data_vv:
            data_vv.append(d.version.vv)
    for v in versions:
        if v.vv not in version_vv:
            version_vv.append(v.vv)
    for v in version_vv:
        if v not in data_vv:
            version = Version.objects.get(vv=v).delete()
    return


@csrf_exempt
def convert_version(request):
    if request.method == 'POST':
        request_body_unicode = request.body.decode('utf-8')
        request_body = json.loads(request_body_unicode)
        dataepoch = request_body['dataepoch']
        ep=str(dataepoch)
        dt = request_body['dd']
        new_vn = request_body['new_vn']
        version = str(new_vn)
        versions = Version.objects.all()
        f=0
        for v in versions:
            if v.vv==version:
                version=v
                f=1
                break
        if f==0:
            return JsonResponse(
                {
                    'status' : 'Version not found.'
                },
                status=400
            )
        values = {
                "tm" : str(dt.get("tm",0)),
                "hm" : str(dt.get("hm",0)),
                "pp" : str(dt.get("pp",0)),
                "wd" : str(dt.get("wd",0)),
                "ws" : str(dt.get("ws",0)),
                "sm" : str(dt.get("sm",0)),
                "st" : str(dt.get("st",0)),
                "sc" : str(dt.get("sc",0)),
                "lt" : str(dt.get("lt",0)),
                "lw" : str(dt.get("lw",0)),
                "bl" : str(dt.get("bl",0)),
               "pv" : str(dt.get("pv",0))
        }
        datas = Data.objects.filter(ep=ep)
        u=0
        for data in datas:
            data_values=data.dt
            if(is_equal(data_values,values)):
                version1=data.version
                data.version=version
                data.save()
                sent_date = data.sent_date
                u=1
                try:
                    date = DateSent.objects.get(date=sent_date)
                    versions = date.versions
                    f=0
                    for v in  versions:
                        if v["version"] == version1.vv:
                            v["no"] = v["no"]-1
                        if v["version"] == version.vv:
                            v["no"] = v["no"]+1
                            f=1
                        if v["no"] == 0:
                            versions.remove(v)
                    if f==0:
                        versions.append({'version':version.vv,'no':1})
                    date.noof_versions = len(versions)
                    date.versions = versions
                    date.save()
                except Exception as e:
                    print(e)
                print("saved")
        if u==1:
            update_versions()

        return JsonResponse(
            {
            'status' : 'Datapoint successfully updated with new version'
            },
            status=201
        )


@csrf_exempt
def exchange_tm_hm(request):
    if request.method == 'POST':
        request_body_unicode = request.body.decode('utf-8')
        request_body = json.loads(request_body_unicode)
        dataepoch = request_body['dataepoch']
        ep=str(dataepoch)
        dt = request_body['dd']
        values = {
                "tm" : str(dt.get("tm",0)),
                "hm" : str(dt.get("hm",0)),
                "pp" : str(dt.get("pp",0)),
                "wd" : str(dt.get("wd",0)),
                "ws" : str(dt.get("ws",0)),
                "sm" : str(dt.get("sm",0)),
                "st" : str(dt.get("st",0)),
                "sc" : str(dt.get("sc",0)),
                "lt" : str(dt.get("lt",0)),
                "lw" : str(dt.get("lw",0)),
                "bl" : str(dt.get("bl",0)),
               "pv" : str(dt.get("pv",0))
        }
        datas = Data.objects.filter(ep=ep)
        for data in datas:
            data_values=data.dt
            if(is_equal(data_values,values)):
                temp = data.dt['tm']
                data.dt['tm']=data.dt['hm']
                data.dt['hm'] = str(temp)
                data.save()
                print("saved")
        return JsonResponse(
            {
            'status' : 'tm and hm in data point are successfully exchanged'
            },
            status=201
        )

@csrf_exempt
def delete_data_point(request):
    if request.method == 'DELETE':
        request_body_unicode = request.body.decode('utf-8')
        request_body = json.loads(request_body_unicode)
        dataepoch = request_body['dataepoch']
        ep=str(dataepoch)
        dt = request_body['dd']
        values = {
                "tm" : str(dt.get("tm",0)),
                "hm" : str(dt.get("hm",0)),
                "pp" : str(dt.get("pp",0)),
                "wd" : str(dt.get("wd",0)),
                "ws" : str(dt.get("ws",0)),
                "sm" : str(dt.get("sm",0)),
                "st" : str(dt.get("st",0)),
                "sc" : str(dt.get("sc",0)),
                "lt" : str(dt.get("lt",0)),
                "lw" : str(dt.get("lw",0)),
                "bl" : str(dt.get("bl",0)),
               "pv" : str(dt.get("pv",0))
        }
        datas = Data.objects.filter(ep=ep)
        u=0
        for data in datas:
            data_values=data.dt
            if(is_equal(data_values,values)):
                u=1
                sent_date = data.sent_date
                version = data.version.vv
                date=DateSent.objects.get(date=sent_date)
                versions = date.versions
                for v in  versions:
                        if v["version"] == version:
                            v["no"] = v["no"]-1
                        
                        if v["no"] == 0:
                            versions.remove(v)
    
                date.noof_versions = len(versions)
                date.versions = versions
                date.save()
                data.delete()
                print("deleted.")
        if u==1:
            update_versions()
        return JsonResponse(
            {
            'status' : 'Datapoint deleted succesfully'
            },
            status=202
        )