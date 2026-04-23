import os

def rename_files(folder_path, prefix):
    try:
        # Get a list of all files in the folder
        files = os.listdir(folder_path)
        
        # Sort files to ensure consistency
        files.sort()
        
        for i, filename in enumerate(files):
            # Define the file extension (keeps the original extension)
            extension = os.path.splitext(filename)[1]
            
            # New name format: Prefix_Number.extension
            new_name = f"{prefix}_{i+1}{extension}"
            
            # Paths
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
            
        print("\n✅ All files renamed successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

# Usage Instructions:
# 1. Change path to your actual folder path
# 2. Change 'Project_Alpha' to your desired name
path = "./test_folder" 
rename_files(path, "Project_Alpha")
