#!/usr/bin/python3
"""
Module for fetching and processing posts from JSONPlaceholder API.
This module provides functions to fetch posts and save them to CSV.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder API and print their titles.

    Sends a GET request to the JSONPlaceholder API, prints the status code,
    and if successful, prints the title of each post.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code : {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Error: Could not fetch data.")


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder API and save them to a CSV file.

    Sends a GET request to the JSONPlaceholder API, and if successful,
    saves the posts data (id, title, body) to a CSV file named posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        # Create simplified list with only id, title, and body
        simplified_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        # Write posts to CSV file
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(simplified_posts)
        print("Post have been saved to posts.csv")
    else:
        print(f"Error: Request failed with status code {response.status_code}")