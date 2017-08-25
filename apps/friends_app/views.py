# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User,UserManager,Friend
from django.shortcuts import render,redirect,HttpResponse

def dashboard(request):
    active=User.objects.get(id=request.session['id'])
    print active.friended.all()
    friended = active.friended.all()
    friend_of = active.friend_of.all()
    print friend_of
    print friended
    friends =[active.name]
    for each in friended:
            name = each.reciever.name
            friends.append(name)
    for each in friend_of:
        name = each.initiator.name
        friends.append(name)
    print friends
    not_friends= User.objects.all().exclude(name__in=friends)
    cur_friends=User.objects.filter(name__in=friends).exclude(name=active.name)
    print not_friends
    print cur_friends
    context = {
        'all':not_friends,
        'active':User.objects.get(id=request.session['id']),
        'curr_friends':cur_friends
    }
    return render(request,'friends_app/index.html',context)
def add(request,number):
    active=User.objects.get(id=request.session['id'])
    target=User.objects.get(id=number)
    friended = active.friended.all()
    
    print friended
    print target.name
    friends ={}
    print friends
    if len(friended)==0:
        print "friended empty"
        friend = Friend.objects.create(initiator=active,reciever=target)
        friend.save()
    else:
        for each in friended:
            print "in each loop"
            name = each.reciever.name
            friends[name]=1
            print name
        if not target.name in friends:
            print friends
            print "in if not loop"
            friend = Friend.objects.create(initiator=active,reciever=target)
            friends[name]=1
            print friend.initiator.name
            print friend.reciever.name
            friend.save()
            
        print friends
    return redirect('/friends')

def remove(request,number):
    print "in remove"
    active=User.objects.get(id=request.session['id'])
    target=User.objects.get(id=number)
    print target
    relationship = active.friended.filter(reciever=target)
    reverse = target.friended.filter(reciever=active)
    print relationship
    try:
        relationship[0].delete()
    except:
        reverse[0].delete()
    return redirect('/friends')

def profile(request,number):
    context={"user":User.objects.get(id=number)}
    return render(request,'friends_app/profile.html',context)