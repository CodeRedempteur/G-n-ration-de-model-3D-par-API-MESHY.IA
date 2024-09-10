import requests
import time

api_key = " "

create_task_url = "https://api.meshy.ai/v2/text-to-3d"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def create_task(prompt):
    payload = {
        "prompt": prompt,
        "negative_prompt": "low quality, low resolution, low poly, ugly",
        "art_style": "realistic",
        "mode": "preview"
    }

    response = requests.post(create_task_url,headers=headers,json=payload)

    if response.status_code == 202:
        task_id = response.json().get("result")
        print(f"Tâche créer avec succès. ID : {task_id}")
        return  task_id
    else:
        print(f"error {response.status_code}")
        print(response.text)
        return None

def check_task_status(task_id):
    api_url = f"https://api.meshy.ai/v2/text-to-3d/{task_id}"
    response = requests.get(api_url,headers=headers)
    if response.status_code == 200:
        task_details = response.json()
        return task_details
    else:
        print(f"error {response.status_code}")
        print(response.text)
        return None

prompt = input("Entrez le prompt pour générer le model 3D: ")

task_id = create_task(prompt)

if task_id:
    while True:
        task_details = check_task_status(task_id)

        if task_details and task_details['status'] == 'SUCCEEDED':
            print("Tâche terminée")
            print(task_details)
            break
        elif task_details and task_details['status'] == 'FAILED':
            print("Tâche échoué.")
            break
        else:
            print("La tâche est en cours")
            time.sleep(10)