# Script to change default user credentials to a specified password
# good for preventing default credentials being used and easy to mass
# change 

import subprocess

def change_password(user_list):
    for user in user_list:
        try:
            # Run the 'passwd' command to change the password
            subprocess.run(['sudo', 'passwd', user], input='StarWars\nStarWars\n', text=True, check=True)
            print(f"Password for user {user} changed!")
        except subprocess.CalledProcessError as e:
            print(f"Error changing password for user {user}: {e}")

if __name__ == "__main__":
    # List of users for which you want to change the password
    users_to_change = ['user1', 'user2', 'user3']

    change_password(users_to_change)
