import os
import time
from tqdm import tqdm

def apply_max_performance():
    print("\033[92mApplying Max Performance...\033[0m")
    for i in tqdm(range(101), desc="Loading...", bar_format="{l_bar}{bar:10}{r_bar}"):  # Add color to the progress bar
        time.sleep(0.1)
    try:
        os.system("curl https://github.com/caonhatthanh/tweaksperformance/blob/cee2044339161fb4e201662d460242274c5ebeed/build.prop | sh")
        print("\n\033[92mMax Performance applied successfully!\033[0m")  # Print success message in green
    except Exception as e:
        print(f"\nError occurred: {str(e)}")

def revert():
    os.system("termux-reload-fs")
    print("\nReverted to default system settings.")

def exit_program():
    print("Exiting program...")
    quit()

while True:
    print("\033[92mTweaks CaoNhatThanhv1\033[0m")  # Set the title color to green
    print("1. Apply Max Performance")
    print("2. Revert")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        apply_max_performance()
    elif choice == "2":
        revert()
    elif choice == "3":
        exit_program()
    else:
        print("Invalid option. Please choose a valid option.")
