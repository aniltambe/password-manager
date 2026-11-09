import os
import string
import secrets
from datetime import datetime

def generate_password(length=16, use_uppercase=True, use_numbers=True, use_special=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*()-_=+"
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def save_password(platform, username, password):
    file_name = "passwords.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Platform: {platform} | Username: {username} | Password: {password}\n"
    
    with open(file_name, "a") as file:
        file.write(log_entry)
    print(f"\n[✔] Credentials for {platform} saved successfully to '{file_name}'!")

def view_passwords():
    file_name = "passwords.txt"
    if not os.path.exists(file_name) or os.stat(file_name).st_size == 0:
        print("\n[!] No saved passwords found.")
        return
        
    print("\n--- Saved Credentials ---")
    with open(file_name, "r") as file:
        print(file.read())

def main():
    while True:
        print("\n==================================")
        print("   Secure Password Utility Kit    ")
        print("==================================")
        print("1. Generate & Save New Password")
        print("2. View Saved Credentials")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            platform = input("Enter Platform/Website name: ").strip()
            username = input("Enter Username/Email: ").strip()
            try:
                length = int(input("Enter password length (default 16): ") or 16)
            except ValueError:
                length = 16
                
            pwd = generate_password(length)
            print(f"\nGenerated Password: {pwd}")
            
            save_opt = input("Do you want to save this credentials locally? (y/n): ").strip().lower()
            if save_opt == 'y':
                save_password(platform, username, pwd)
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("\nExiting Secure Password Utility Kit. Stay Safe!")
            break
        else:
            print("\n[!] Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
