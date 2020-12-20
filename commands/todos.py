import json
from datetime import datetime


def get_data(list_name):
    data=[]
    with open(list_name,'r') as todo_list:
        data=json.load(todo_list)
    return data


def add_item(args):
    data=get_data('list1.json')
    title=args[0]
    data.append({
        'title':title,
        'created_at':datetime.now(),

    })


def show_item(args):
    data = get_data('list1.json')
    if(len(data)==0):
        print("No todo items in the list")
        return
    for index,todo_item in enumerate(data):
        print(index+1,todo_item['title'])
    print(args)