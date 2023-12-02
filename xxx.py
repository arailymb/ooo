#lab 8

import requests
import random
import json

# Task 1

# 1.1
post_id = 1
url = f'https://jsonplaceholder.typicode.com/todos/{post_id}'

response = requests.get(url)

if response.status_code >= 400:
    print(f"Error: {response.status_code}")
else:
    print("1.1 - Response Content:")
    print(response.json())

# 1.2
class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

new_todo_object = ToDo(userId=1, id=1, title="Sample Todo", completed=False)

# 1.4
new_todo = {
    "userId": new_todo_object.userId,
    "title": new_todo_object.title,
    "completed": new_todo_object.completed
}

post_response = requests.post('https://jsonplaceholder.typicode.com/todos', json=new_todo)

if post_response.status_code >= 400:
    print(f"Error: {post_response.status_code}")
else:
    print("1.4 - POST Response Content:")
    print(post_response.json())

# 1.5
new_todo_object.title = "Updated Todo Title"
new_todo_object.completed = True

# 1.6
updated_todo = {
    "title": new_todo_object.title,
    "completed": new_todo_object.completed
}

put_response = requests.put(f'https://jsonplaceholder.typicode.com/todos/{new_todo_object.id}', json=updated_todo)

if put_response.status_code >= 400:
    print(f"Error: {put_response.status_code}")
else:
    print("1.6 - PUT Response Content:")
    print(put_response.json())

# Task 2

# 2.1 
random_character_id = random.randint(1, 826)
character_url = f'https://rickandmortyapi.com/api/character/{random_character_id}'

character_response = requests.get(character_url)

print(f"2.1 - JSON response for character {random_character_id}:")
print(character_response.json())

# 2.3 
filename = f"info_character_{random_character_id}.json"
with open(filename, 'w') as file:
    json.dump(character_response.json(), file)

# 2.4
episodes = character_response.json().get("episode", [])

episode_filename = f"all_episodes_with_character_{random_character_id}.txt"
with open(episode_filename, 'w') as episode_file:
    for episode_url in episodes:
        episode_file.write(f"{episode_url}\n")

# 2.5 
episode_id = 1
episode_url = f'https://rickandmortyapi.com/api/episode/{episode_id}'

episode_response = requests.get(episode_url)

print(f"2.5 - JSON response for episode {episode_id} structure:")
print(episode_response.json())

# 2.6
class Episode:
    def __init__(self, id, name, air_date, episode, characters):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters

# 2.7 
episode_objects = []
for episode_url in episodes:
    episode_data = requests.get(episode_url).json()
    episode_objects.append(Episode(
        id=episode_data["id"],
        name=episode_data["name"],
        air_date=episode_data["air_date"],
        episode=episode_data["episode"],
        characters=episode_data["characters"]
    ))

# 2.8 
class Episode:
    def __init__(self, id, name, air_date, episode, characters):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters

    def display_info(self):
        print(f"Episode {self.episode}: {self.name}, Air Date: {self.air_date}")




# 2.9
character_id = 1
character_url = f'https://rickandmortyapi.com/api/character/{character_id}'


character_response = requests.get(character_url)

print(f"2.9 - JSON response for character {character_id} structure:")
print(character_response.json())

# 2.10 
class Character:
    def __init__(self, id, name, status, species, type, gender, origin, location, image, episodes):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episodes = episodes

# 2.11
random_character_data = character_response.json()
random_character_object = Character(
    id=random_character_data["id"],
    name=random_character_data["name"],
    status=random_character_data["status"],
    species=random_character_data["species"],
    type=random_character_data["type"],
    gender=random_character_data["gender"],
    origin=random_character_data["origin"]["name"],
    location=random_character_data["location"]["name"],
    image=random_character_data["image"],
    episodes=random_character_data["episode"]
)

# 2.12 
class Character:
    def __init__(self, id, name, status, species, type, gender, origin, location, image, episodes):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episodes = episodes

    def display_info(self):
        print(f"Character: {self.name}, Status: {self.status}, Species: {self.species}")



