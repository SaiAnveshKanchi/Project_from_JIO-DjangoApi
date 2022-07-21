
from django.apps import AppConfig

class VersionManagementAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'version_management_app'
    
    '''def ready(self):
        from .models import Device, Version, Data, SensorValues, VersionAbstract, DateSent
        import json
        import datetime
        try:
            file1 = open("version_management_app/raw_data.txt","r")
            lines_read = file1.readlines()
            for lines in lines_read:
                line = lines
                json_object = json.loads(line)
                device = json_object.get("dd")
                device=str(device)
                version = json_object.get("vn")
                version=str(version)
                try:
                    device=Device.objects.get(dd=device)
                except:
                    device=Device.objects.create(dd=device)
                try:
                    version=Version.objects.get(vv=version)
                except:
                    version=Version.objects.create(vv=version)
                print(version._id)
                print(device._id)
                dt = json_object.get("dt")
                ep = json_object.get("ep")
                sent_date = datetime.date.fromtimestamp(ep)
                ep=str(ep)
                tm = str((dt.get("tm",0)))
                hm = str((dt.get("hm",0)))
                pp = str((dt.get("pp",0)))
                wd = str((dt.get("wd",0)))
                ws = str((dt.get("ws",0)))
                sm = str((dt.get("sm",0)))
                st = str((dt.get("st",0)))
                sc = str((dt.get("sc",0)))
                lt = str((dt.get("lt",0)))
                lw = str((dt.get("lw",0)))
                bl = str((dt.get("bl",0)))
                pv = str((dt.get("pv",0)))
                
                data = Data.objects.create(
                        ep=ep,
                        sent_date=sent_date,
                        dt={
                            "tm":tm,
                            "hm":hm,
                            "pp":pp,
                            "wd":wd,
                            "ws":ws,
                            "sm":sm,
                            "st":st,
                            "sc":sc,
                            "lt":lt,
                            "lw":lw,
                            "bl":bl,
                            "pv":pv
                        },
                        version=version,
                        device=device)
                
                print(data._id)
                
                try:
                    date = DateSent.objects.get(date=sent_date)
                    print(date._id)
                    try:
                        f=0
                        all_versions = date.versions
                        for v in all_versions:
                            if v["version"]==version.vv:
                                v["no"] = v["no"]+1
                                f=1
                                break
                        if f == 0:
                            date.versions.append({"version":version.vv,"no":1 })
                            date.noof_versions=date.noof_versions+1
                        else:
                            date.versions=all_versions
                        date.save()
                        print(date.versions)
                        print(date.noof_versions)
                    except Exception as e:
                        print(e)
                        print("error in list embedded datesent.")

                except Exception as e:
                    date = DateSent.objects.create(date=sent_date,noof_versions=1,versions=[{"version":version.vv,"no":1}])
                    print(date._id)
                
                print("_____________")
        except Exception as e:
            print(e)
            print("File Not Opened. Something went wrong.")
     
        line = '{"dd":"861480034784845","vn":"4.1.3.3","ep":1617235200,"dt":{"tm":27.1,"hm":82.6,"pp":374.00,"wd":92,"ws":0.0,"sm":439.6,"st":284.8,"sc":637,"lt":0.0,"lw":0.0,"bl":7.9,"pv":0.0}}'
        json_object = json.loads(line)
        device = json_object.get("dd")
        device=str(device)
        version = json_object.get("vn")
        version=str(version)
        try:
                    device=Device.objects.get(dd=device)
        except:
                    device=Device.objects.create(dd=device)
        try:
                    version=Version.objects.get(vv=version)
        except:
                    version=Version.objects.create(vv=version)
        print(version._id)
        print(device._id)
        dt = json_object.get("dt")
        ep = json_object.get("ep")
        sent_date = datetime.date.fromtimestamp(ep)
        ep=str(ep)
        tm = float(dt.get("tm",0))
        hm = float(dt.get("hm",0))
        pp = float(dt.get("pp",0))
        wd = float(dt.get("wd",0))
        ws = float(dt.get("ws",0))
        sm = float(dt.get("sm",0))
        st = float(dt.get("st",0))
        sc = float(dt.get("sc",0))
        lt = float(dt.get("lt",0))
        lw = float(dt.get("lw",0))
        bl = float(dt.get("bl",0))
        pv = float(dt.get("pv",0))
                
        data = Data.objects.create(
                        ep=ep,
                        sent_date=sent_date,
                        dt={
                            "tm":tm,
                            "hm":hm,
                            "pp":pp,
                            "wd":wd,
                            "ws":ws,
                            "sm":sm,
                            "st":st,
                            "sc":sc,
                            "lt":lt,
                            "lw":lw,
                            "bl":bl,
                            "pv":pv
                        },
                        version=version,
                        device=device)
                
        print(data._id)
        print(data)
        print(data.dt)
        print(data.dt['tm'])
        data1=Data.objects.filter(version=version)[0]
        print(data1)
        print(data1.dt)
        
                
        try:
                    date = DateSent.objects.get(date=sent_date)
                    print(date._id)
                    try:
                        f=0
                        all_versions = date.versions
                        for v in all_versions:
                            if v["version"]==version.vv:
                                v["no"] = v["no"]+1
                                f=1
                                break
                        if f == 0:
                            date.versions.append({"version":version.vv,"no":1 })
                            date.noof_versions=date.noof_versions+1
                        else:
                            date.versions=all_versions
                        date.save()
                        print(date.versions)
                        print(date.noof_versions)
                    except Exception as e:
                        print(e)
                        print("error in list embedded datesent.")

        except Exception as e:
                    date = DateSent.objects.create(date=sent_date,noof_versions=1,versions=[{"version":version.vv,"no":1}])
                    print(date._id)
                
        print("_____________")'''