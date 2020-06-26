from django.shortcuts import render,redirect
from .models import Users, techque, commque
#from django.http import JsonResponse
from django.contrib.auth.models import User , auth 
import pyrebase
import numpy as np
import math
import os
from grammarbot import GrammarBotClient
from django.db.models import Max
from sklearn.feature_extraction.text import CountVectorizer


Config = {
    'apiKey' : "AIzaSyBQa5jX7LlGCiPofRzEPXcOHfXjO_BjhI4",
    'authDomain' : "interviewerque.firebaseapp.com",
    'databaseURL' : "https://interviewerque.firebaseio.com",
    'projectId' : "interviewerque",
    'storageBucket' : "interviewerque.appspot.com",
    'messagingSenderId' : "998220278717",
    'appId' : "1:998220278717:web:ff1aff70ff03888e59c0d4",
    'measurementId' : "G-XLDT5HZLYV"
}

firebase=pyrebase.initialize_app(Config)

authe=firebase.auth()
database=firebase.database()

count=0
final_que_score=[]
def signIn(request):
    return render(request, "login.html")

def newuser(request):
    return render(request, "register.html")    

'''def postsign(request):
    if request.method=='POST':
        email=request.POST.get('Mail id')
        passw = request.POST.get("password")
        
        try:
            user = authe.sign_in_with_email_and_password(email,passw)
        except:
            message = "invalid cerediantials"
            return render(request,"login.html",{"msg":message})
        #print(user['idtoken'])
        session_id=user['idtoken']
        request.session_id['uid']=str(session_id)
        return render(request, "onlinetest.html",{})'''

def logout(request):
    auth.logout(request)
    return render(request, "login.html",{})


def signup(request):
    return render(request, "register.html")


def test(request):
    return render(request, "writeup.html")

def post_list(request):
    #max_users=Users.objects.aggregate(Max('id'))
    #print(max_users)
    
    return render(request, 'post_list.html',{} )


def scores(request):
    return render(request, 'scores.html', {} )

def exam(request):
    return render(request, 'exam.html', {} )    

def section_url(request):
    proglist=Users.objects.all().order_by('-progscore')
    #print(proglist)
    oopslist=Users.objects.all().order_by('-oopsscore')
    
    netlist=Users.objects.all().order_by('-networkscore')
    return render(request,'sections.html',{'prog':proglist,'oop':oopslist,'net':netlist})

def profile_url(request):
    profile_lst=Users.objects.all()
    comm_questions=database.child("Communications").child("questions").get().val()
    comm_questions=comm_questions[1:]
    comm_response=database.child("Communications").child("response").get().val()
    comm_response=comm_response[3:]
    
    return render(request,'profile.html',{'proflis':profile_lst,'quest':comm_questions,'res':comm_response} )


def register(request):
    
    if request.method == 'POST':
        name1=request.POST.get('name')
        Mail=request.POST.get('mailid')
        passw = request.POST.get("password")
        para = request.POST.get("text")
        dept=request.POST.get("Department")
        fathername=request.POST.get("Fathername")
        collegename=request.POST.get("collegename")
        collegeid=request.POST.get("collegeid")
 
        print("hello:")
        user= User.objects.create_user(username=name1,password=passw,email=Mail)
        user.save()
        user_obj=Users(name=name1,Department=dept,mailid=Mail,text=para,writeuperrors='0',Fathername=fathername,collegename=collegename,collegeid=collegeid)
        user_obj.save()
        print("user created")
        user=authe.create_user_with_email_and_password(Mail,passw)
        user = authe.sign_in_with_email_and_password(Mail,passw)
        sessionid=user['idToken']
        request.session['uid']=str(sessionid)
        uid=user['localId']
                
                #database.child("communication").child("s").set(data)
        '''Techque=techque.objects.values_list('id','question')
        que_lst=list(Techque)
        print(que_lst)

        Commque=commque.objects.values_list('id','question')
        cque_lst=list(Commque)
        print(cque_lst)'''

            #return JsonResponse(communicationque, safe=False)
            #str(communicationque)
            #idtoken=request.session['uid']
            #a=authe.get_account_info(idtoken)
            #print(a)
            #a=a['users']
            #dict1=a[0]
            #res=dict1['localId']
        print("Hello:")
            #print(res)
        '''que_dict={}
        que_dict.update(que_lst)
        cque_dict={}
        cque_dict.update(cque_lst)
        print("hello again {}".format(que_dict))
        database.child('technical').child('questions').set(que_dict)
        database.child('Communications').child('questions').set(cque_dict)'''
                
        sampleres=techque.objects.values_list('response','sample1','sample2','sample3')
        print(sampleres)

        field=Users.objects.filter().order_by('-id')[0]
        return render(request,'writeup.html',{"fie":field})
    else:    
        return render(request, 'register.html', {} )   
    

'''def postsignup(request):
    if request.method=='POST':
        
        name=request.POST.get('name')
        email=request.POST.get('mailid')
        passw=request.POST.get('password')

        user=authe.create_user_with_email_and_password(email,passw)

        uid=user['localId']

        data={"name":name,"status":"1"}
        database.set(data)

        
        return render(request,"onlinetest.html")
    else:
        
        return render(request,'register.html')'''


def storepara(request):
    if request.method=='POST':
        name1=request.POST.get('name')
        Mail=request.POST.get('mailid')
        passw = request.POST.get("password")
        para = request.POST.get("text")
        #dept=request.POST.get("Department")
        #fathername=request.POST.get("fathername")
        #collegename=request.POST.get("collegename")
        #collegeid=request.POST.get("collegeid")

        
            
        print("hello:")
            #user= User.objects.create_user(username=name1,password=passw,email=Mail)
            #user.save()
        '''user_obj=Users(name=name1,Department="cse",mailid=Mail,text=para,writeuperrors='0')
        user_obj.save()'''
        user_obj=Users.objects.filter(name=name1).update(text=para)
        print('details updated')
        print(user_obj)
        
        #print(user_obj)

        
        print("hi:")
        
        client = GrammarBotClient(api_key='KS9C5N3Y')

        text = para

        res = client.check(text)
        errors = len(res.matches)
        print('No of Errors', errors)
        

        for match in res.matches:
            print(text[match.replacement_offset: match.replacement_offset+match.replacement_length], match.category, match.rule)
        
        Techque=techque.objects.values_list('id','question')
        que_lst=list(Techque)
        print(que_lst)

        Commque=commque.objects.values_list('id','question')
        cque_lst=list(Commque)
        print(cque_lst)
        

        que_dict={}
        que_dict.update(que_lst)
        cque_dict={}
        cque_dict.update(cque_lst)
        print("hello again {}".format(que_dict))
        database.child('technical').child('questions').set(que_dict)
        database.child('Communications').child('questions').set(cque_dict)
            
        print("click world")
        return render(request,'print.html')
        
 
    else:
        #communicationque=commque.objects.all()
        #print(communicationque)
        # idtoken=request.session['uid']
        field=Users.objects.filter().order_by('-id')[0]
        return render(request,'writeup.html',{"fie":field})

def frm_fire():
       
        main=database.child("technical").child("response").get().val()
       
        return(main)

def click():
        print("hello 1")
        user_res=frm_fire()
        global count
        for i in user_res:
            print(i)
            if i is not None:
                samp_ans_lst=[]
                count+=1
                samp_ans_lst=frm_postgre(count)
                bow(i,samp_ans_lst)
        to_postgre()
        
       
def to_postgre():
    
        print("Final question scores")
        latest=Users.objects.filter().order_by('-id')[0]
        Candidate_name=latest.name
        user_obj=Users.objects.filter(name=Candidate_name).update(networkscore=final_que_score[0],oopsscore=final_que_score[1],progscore=final_que_score[2])
        print(user_obj)
        #print(final_que_score)
        #user_obj.save()
        #print(scr_lst)
        #print(final_lst)
def frm_postgre(que_id):
        ans_lst=[]
        sampleres=techque.objects.filter(id=que_id).values('sample1','sample2','sample3')
        for i in sampleres[0].values():
            ans_lst.append(i.rstrip())
        return ans_lst

def bow(a,b_lst):
        bow_lst=[]
        scr_lst=[]
        corpus=[
            str(a),b_lst[0],b_lst[1],b_lst[2]
        ]
        vect=CountVectorizer()
        bow_lst=vect.fit_transform(corpus).todense()
        sen1=np.squeeze(np.array(bow_lst[0]))
        sen2=np.squeeze(np.array(bow_lst[1]))
        sen3=np.squeeze(np.array(bow_lst[2]))
        sen4=np.squeeze(np.array(bow_lst[3]))
        
        a=cos_sim(sen1,sen2)
        scr_lst.append(a)
        b=cos_sim(sen1,sen3)
        scr_lst.append(b)
        c=cos_sim(sen1,sen4)
        scr_lst.append(c)
        dept_lst=techque.objects.values_list('quetype')
    
        temp_val=max(scr_lst)*100
       
        real_val=math.trunc(temp_val)
        global final_que_score
        final_que_score.append(real_val)
        print("hello:{}".format(count),max(scr_lst))
        

def cos_sim(a,b):
        print(a,b)
        dot_product = np.dot(a, b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        return dot_product / (norm_a * norm_b)

def persprof(request):
    profile_data=Users.objects.filter(name='aldini').values_list("id","name","mailid","Department","Fathername","oopsscore","progscore","networkscore")
    print(profile_data)
    return render(request,'prof.html',{'datai':profile_data})

def loadque(request):
    
    click()

    return render(request,'dummy.html')