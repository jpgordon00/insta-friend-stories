#!/usr/bin/env python3
import argparse
import random
import time
from instagrapi import Client
from typing import List
import os
from pathlib import Path

def init_client(username: str, password: str) -> Client:
    """Initialize and login to Instagram client"""
    cl = Client()
    cl.delay_range = [2, 3]  # Random delay between requests
    
    # Try to load session if exists
    session_path = Path("session.json")
    if session_path.exists():
        cl.load_settings("session.json")
        cl.login(username, password)
    else:
        cl.login(username, password)
        # Save session for future use
        cl.dump_settings("session.json")
    
    return cl

def get_followers(cl: Client, max_followers: int = None) -> List[int]:
    """Get list of follower IDs with pagination"""
    user_id = cl.user_id
    followers = []
    
    try:
        followers = cl.user_followers(user_id, amount=max_followers)
        return list(followers.keys())
    except Exception as e:
        print(f"Error getting followers: {e}")
        return []

def add_to_close_friends(cl: Client, follower_ids: List[int]) -> None:
    """Add followers to close friends list"""
    try:
        # Get current close friends to avoid duplicates
        current_close_friends = cl.close_friends()
        new_friends = set(follower_ids) - set(current_close_friends)
        
        if not new_friends:
            print("No new followers to add to close friends")
            return
            
        # Add followers in batches with random delays
        for follower_id in new_friends:
            time.sleep(random.uniform(2, 3))
            try:
                cl.close_friend_add(follower_id)
                print(f"Added user {follower_id} to close friends")
            except Exception as e:
                print(f"Failed to add user {follower_id}: {e}")
                
    except Exception as e:
        print(f"Error managing close friends: {e}")

def main():
    parser = argparse.ArgumentParser(description='Instagram Follower Manager')
    parser.add_argument('--max', type=int, help='Maximum number of followers to process')
    args = parser.parse_args()
    
    # Get credentials from environment or prompt
    username = os.getenv('IG_USERNAME')
    password = os.getenv('IG_PASSWORD')
    
    if not username:
        username = input("Enter Instagram username: ")
    if not password:
        password = input("Enter Instagram password: ")
    
    try:
        # Initialize client
        cl = init_client(username, password)
        
        # Get followers
        print("Fetching followers...")
        follower_ids = get_followers(cl, args.max)
        print(f"Found {len(follower_ids)} followers")
        
        # Add to close friends
        print("Adding followers to close friends...")
        add_to_close_friends(cl, follower_ids)
        
        print("Process completed successfully")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 
