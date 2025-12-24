import os
import shutil

def auto_rename_and_organize(source_folder, output_folder, prefix="img"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    files.sort()

    count = 1
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in [".jpg", ".jpeg", ".png", ".webp"]:
            new_name = f"{prefix}_{count:04d}{ext}"
            old_path = os.path.join(source_folder, file)
            new_path = os.path.join(output_folder, new_name)

            shutil.copy2(old_path, new_path)
            count += 1

    print("Renaming + Organizing Completed Successfully!")

# --------- EDIT ONLY THESE TWO PATHS --------- #
source_folder = r"C:\Users\dell\Desktop\img"
output_folder = r"C:\Users\dell\Desktop\img2"
# ---------------------------------------------- #

auto_rename_and_organize(source_folder, output_folder)
