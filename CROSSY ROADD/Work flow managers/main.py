from prefect import task, flow
import requests
import json

@task(retries=2, retry_delay_seconds=5)
def fetch_posts():
    response = requests.get("https://jsonplaceholder.cypress.io/posts")
    response.raise_for_status()  # Manejo de errores
    return response.json()

@task
def filter_posts_by_user(posts, user_id=1):
    return [post for post in posts if post["userId"] == user_id]

@task
def save_to_file(data, filename="filtered_posts.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Datos guardados en {filename}")

@flow
def jsonplaceholder_flow(user_id=1):
    posts = fetch_posts()
    filtered_posts = filter_posts_by_user(posts, user_id)
    save_to_file(filtered_posts)

if __name__ == "__main__":
    jsonplaceholder_flow(user_id=1)
