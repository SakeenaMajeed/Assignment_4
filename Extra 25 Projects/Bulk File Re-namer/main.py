import os

def rename_files(folder_path, prefix, file_extension):
    if os.path.isfile(folder_path):
        files_to_rename = [folder_path]
    else:
        files_to_rename = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(file_extension)]

    for count, file_path in enumerate(files_to_rename, start=1):
        if os.path.isfile(file_path):
            directory, filename = os.path.split(file_path)
            new_name = f"{prefix}{count}{file_extension}"
            new_path = os.path.join(directory, new_name)
            
            print(f"🔧 Renaming: {file_path} → {new_path}")
            os.rename(file_path, new_path)
            print(f"✅ Renamed: {filename} → {new_name}")
    print("🎉 Bulk renaming complete!")

folder_path = input("📂 Enter the full folder path (or file path): ").strip()
prefix = input("📝 Enter a prefix for the new filenames: ").strip()
file_extension = input("🔍 Enter the file extension (e.g., .txt, .jpg, .pdf): ").strip()

rename_files(folder_path, prefix, file_extension)
