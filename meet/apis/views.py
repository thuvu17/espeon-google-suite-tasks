from django.http import HttpResponse, HttpResponseRedirect

from google.services import *


def init(request):
    get_token()

    return HttpResponseRedirect('/')


async def create_space(request):
    obj = await sample_create_space()

    # 打印会议信息
    print(obj)

    # 直接打开会议室
    return HttpResponseRedirect(obj.meeting_uri)

    # 返回会议室信息
    # return HttpResponse(obj)


async def get_space(request):
    name = request.POST.get('name')
    obj = await sample_get_space(name)

    # 返回会议室信息
    return HttpResponse(obj, content_type="text/plain")


async def update_space(request):
    name = request.POST.get('name')
    obj = await sample_update_space(name)

    return HttpResponse(obj, content_type="text/plain")


async def end_active_conference(request):
    name = request.POST.get('name')
    await sample_end_active_conference(name)

    return HttpResponse('close')


async def list_conference_records(request):
    obj = await sample_list_conference_records()
    return HttpResponse(obj, content_type="text/plain")


async def get_conference_record(request):
    name = request.POST.get('name')
    obj = await sample_get_conference_record(name)

    # 返回会议室信息
    return HttpResponse(obj, content_type="text/plain")


async def list_participants(request):
    name = request.POST.get('name')
    obj = await sample_list_participants(name)

    # 返回会议室信息
    return HttpResponse(obj, content_type="text/plain")


async def get_participant(request):
    name = request.POST.get('name')
    obj = await sample_get_participant(name)

    # 返回会议室信息
    return HttpResponse(obj, content_type="text/plain")


async def list_participant_sessions(request):
    name = request.POST.get('name')
    obj = await sample_list_participant_sessions(name)

    # 返回会议室信息
    return HttpResponse(obj, content_type="text/plain")


async def get_participant_session(request):
    name = request.POST.get('name')
    obj = await sample_get_participant_session(name)

    # 返回会议室信息
    return HttpResponse(obj, content_type="text/plain")
