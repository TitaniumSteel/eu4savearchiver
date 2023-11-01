import os
import time

def get_next_save_number(save_name):
    try:
        existing_saves = [f for f in os.listdir() if f.startswith(save_name) and f.endswith('.eu4')]
        if not existing_saves:
            return 1
        existing_numbers = []
        for f in existing_saves:
            try:
                number = int(f.replace(save_name, '').replace('.eu4', ''))
                existing_numbers.append(number)
            except ValueError:
                # Ignore files that don't have a numeric suffix
                continue
        return max(existing_numbers) + 1 if existing_numbers else 1
    except Exception as e:
        print(f"Error while getting next save number: {e}")
        return None

def main():
    try:
        save_name = input('Enter the name of the save (if autosave, input "/autosave"): ')
        save_new_name = input("Enter the name for the saves to be renamed to: ")
        save_number = get_next_save_number(save_new_name)
        if save_number is None:
            return
        print(f"Starting count from {save_number}")
        if save_name == "/autosave":
            for old_save in ["older_autosave.eu4", "old_autosave.eu4"]:
                if os.path.exists(old_save):
                    new_name = f"{save_new_name} {save_number}.eu4"
                    os.rename(old_save, new_name)
                    print(f"Detected old save file. Renamed to {new_name}")
                    save_number += 1
            save_name = "autosave"
        while True:
            time.sleep(1)
            if os.path.exists(f"{save_name}.eu4"):
                new_name = f"{save_new_name} {save_number}.eu4"
                os.rename(f"{save_name}.eu4", new_name)
                print(f"Detected new save file. Renamed to {new_name}")
                save_number += 1
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()