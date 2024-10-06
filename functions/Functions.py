import json
import sys
import datetime

Tasks = []
def build_ids_for_tasks(task):
    #Get the numbers of date at moment to create a new task
    date =  datetime.datetime.now().strftime("%x")
    date_numb = date.replace("/", "")
    #Get words of the task
    task_words = task.split(" ")
    #Build the ID
    id = task_words[0] + date_numb + task_words[-1]
    return id, date, date

def add(task):
    id, createat, updateat = build_ids_for_tasks(task)

    task_format_dict = {"id": id,
                        "description": task, 
                        "status": "to do",
                        "createdAt": createat, 
                        "updatedAt": updateat}
    
    with open("../Tasks/Tasks.json", 'a', encoding='utf-8') as rd_json:
        json.dump(task_format_dict, rd_json, ensure_ascii=False)
        rd_json.write('\n')
    rd_json.close()

#Functions for the option LISTS

def read_file():
    Tasks.clear()
    with open("../Tasks/Tasks.json", "r", encoding='utf-8') as rd_json:
        for js in rd_json:
            Tasks.append( json.loads(js) )

    rd_json.close()

def Write_to_File(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        for item in data:
            json.dump(item, file, ensure_ascii=False)
            file.write('\n')
    file.close()
    
def list_by_status(status=None):
    read_file()
    if status == None:
        for item in Tasks:
            print(item)
    else:
        for task in Tasks:
            print(task) if task['status'] == status else None


def update(id_task, desc_task):
    read_file()
    updated_tasks = []
    for task in Tasks:
        if task['id'] == id_task:
            task['description'] = desc_task
            updated_tasks.append(task)
        else:
            updated_tasks.append(task)
    
    Write_to_File("../Tasks/Tasks.json", updated_tasks)

def delete_task(id_task):
    read_file()
    filtered_tasks = []
    for task in Tasks:
        filtered_tasks.append(task) if task['id'] != id_task else None
    
    Write_to_File("../Tasks/Tasks.json", filtered_tasks)

def mark_options(id_task, sts, param_adi=None):
    read_file()
    #print(Tasks)

    Tasks_with_changed_status = []
    for task in Tasks:
        task['status']=sts if task['id'] == id_task else task['status']
        Tasks_with_changed_status.append(task)
    
    Write_to_File("../Tasks/Tasks.json", Tasks_with_changed_status)
