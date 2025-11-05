import os
import shutil

def separate_files(folder_path):
    # Create destination folders
    images_folder = os.path.join(folder_path, "images")
    text_folder = os.path.join(folder_path, "text_files")

    os.makedirs(images_folder, exist_ok=True)
    os.makedirs(text_folder, exist_ok=True)

    # Define extensions
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}
    text_extensions = {".txt"}

    # Iterate through files
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file_name)
            ext = ext.lower()

            if ext in image_extensions:
                shutil.move(file_path, os.path.join(images_folder, file_name))
            elif ext in text_extensions:
                shutil.move(file_path, os.path.join(text_folder, file_name))

    print("Files separated successfully!")

# Example usage
separate_files(r"C:\Users\Vedadweep\OneDrive\ドキュメント\AI Img\JPG_IMAGES")
