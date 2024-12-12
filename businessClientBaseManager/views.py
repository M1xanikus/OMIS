from django.shortcuts import render

from businessClientBaseManager.models import Message


def main_menu(request):
    return render(request, 'businessClientBaseManager/main_menu.html')

def clients_list(request):
    return render(request, 'businessClientBaseManager/clients_list.html')

def client_details(request, id):
    return render(request, 'businessClientBaseManager/client_details.html', {'client_id': id})


def messages_history(request, client_id):
    messages = Message.objects.filter(client_id=client_id).order_by('-timestamp')  # Сообщения клиента, отсортированные по времени
    return render(request, 'businessClientBaseManager/messages_history.html', {'messages': messages})

def campaigns_list(request):
    return render(request, 'businessClientBaseManager/campaigns_list.html')

def campaign_details(request, id):
    return render(request, 'businessClientBaseManager/campaign_details.html', {'campaign_id': id})

def tasks_list(request):
    return render(request, 'businessClientBaseManager/tasks.html')

def task_detail(request, id):
    return render(request, 'businessClientBaseManager/task_detail.html', {'task_id': id})

def task_delete(request, id):
    return render(request, 'businessClientBaseManager/task_confirm_delete.html', {'task_id': id})

def clients_select(request):
    return render(request, 'businessClientBaseManager/clients_select.html')

def campaign_message_create(request):
    return render(request, 'businessClientBaseManager/campaign_message_create.html')