import os
import time
from tqdm import tqdm

def apply_max_performance():
    print("\033[92mApplying Max Performance...\033[0m")
    for i in tqdm(range(101), desc="Loading...", bar_format="{l_bar}{bar:10}{r_bar}"):
        time.sleep(0.1)
    try:
        os.system("curl https://raw.githubusercontent.com/caonhatthanh/tweaksperformance/master/build.prop | sh")
        print("\n\033[92mMax Performance applied successfully!\033[0m")
    except Exception as e:
        print(f"\nError occurred: {str(e)}")

def apply_ram_boost():
    print("\033[92mApplying Ram Boost...\033[0m")
    for i in tqdm(range(101), desc="Loading...", bar_format="{l_bar}{bar:10}{r_bar}"):
        time.sleep(0.1)
    try:
        os.system("curl https://github.com/caonhatthanh/tweaksperformance/blob/cabaf81f7faaf14e99a9e069af50cc9aa2aee55f/ram.prop | sh")
        print("\n\033[92mRam Boost applied successfully!\033[0m")
    except Exception as e:
        print(f"\nError occurred: {str(e)}")

def revert():
    os.system("termux-reload-fs")
    print("\nReverted to default system settings.")

def exit_program():
    print("Exiting program...")
    quit()

while True:
    print("\033[92mTweaks CaoNhatThanhv1\033[0m")
    print("1. Apply Max Performance")
    print("2. Apply Ram Boost")
    print("3. Revert")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        apply_max_performance()
    elif choice == "2":
        apply_ram_boost()
    elif choice == "3":
        revert()
    elif choice == "4":
        exit_program()
    else:
        print("Invalid option. Please choose a valid option.")
