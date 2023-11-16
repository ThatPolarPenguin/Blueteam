# Basic backup script that will first create a backup folder and copy the
# contents of the specific source directory, then will copy the backup folder
# contents to the source folder every 30 seconds
# Note: be sure to update file paths to make sure you have accurate source files

import subprocess
import time

def copy_directory(source_dir, destination_dir):
    try:
        # Use rsync to copy the contents of the source directory to the destination directory
        subprocess.run(['rsync', '-a', source_dir, destination_dir], check=True)
        print(f"Contents of {source_dir} copied to {destination_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def restore(source_dir, destination_dir):
    try:
        # Use rsync to copy the contents of the source directory to the destination directory
        subprocess.run(['rsync', '-a', '--specials', source_dir, destination_dir], check=True)
        print(f"Contents of {source_dir} copied to {destination_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Specify the source and destination directories
    source_directory = '/home/user/Desktop/testing'
    destination_directory = '/backup'

    # Create the destination directory if it doesn't exist
    subprocess.run(['mkdir', '-p', destination_directory], check=True)

    # Copy the contents of the source directory to the destination directory
    copy_directory(source_directory, destination_directory)

    #while True:
        restore('/backup/testing', '/home/user/Desktop')
        time.sleep(30)

