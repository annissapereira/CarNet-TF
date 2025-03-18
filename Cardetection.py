import os
import shutil
import random

# Define the path to the imgs folder
base_folder_path = r'C:\Users\annis\OneDrive\Desktop\Github repo\CarNet-TF\archive (2)\imgs_zip\imgs'

# List of selected car brands
selected_brands = ['BMW', 'Audi', 'Porsche', 'Bentley', 'Aston Martin']

# Create a new folder to store the split images (if not exists)
base_output_folder = r'C:\Users\annis\OneDrive\Desktop\Github repo\CarNet-TF\split_images'
train_folder = os.path.join(base_output_folder, 'train')
val_folder = os.path.join(base_output_folder, 'val')
test_folder = os.path.join(base_output_folder, 'test')

# Create directories for train, val, test
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Check if the imgs folder exists
if os.path.exists(base_folder_path):
    print(f"Folder tracking was successful. Found: {base_folder_path}")

    # Loop through the selected brands
    for brand in selected_brands:
        brand_folder_path = os.path.join(base_folder_path, brand)
        if os.path.exists(brand_folder_path):
            # Get the list of all images in the brand folder
            image_files = [f for f in os.listdir(brand_folder_path) if os.path.isfile(os.path.join(brand_folder_path, f))]
            
            # Select 50 images randomly from the folder
            selected_images = random.sample(image_files, 50)
            print(f"Selected 50 images for {brand}.")

            # Create subfolders for each brand in the train, val, test folders
            brand_train_folder = os.path.join(train_folder, brand)
            brand_val_folder = os.path.join(val_folder, brand)
            brand_test_folder = os.path.join(test_folder, brand)
            os.makedirs(brand_train_folder, exist_ok=True)
            os.makedirs(brand_val_folder, exist_ok=True)
            os.makedirs(brand_test_folder, exist_ok=True)

            # Split the selected images into 70% for train, 20% for validation, and 10% for test
            num_train = int(0.7 * len(selected_images))
            num_val = int(0.2 * len(selected_images))
            num_test = len(selected_images) - num_train - num_val  # Remaining images for test set

            # Split the selected images
            train_images = selected_images[:num_train]
            val_images = selected_images[num_train:num_train + num_val]
            test_images = selected_images[num_train + num_val:]

            # Copy the images into the respective folders
            for img in train_images:
                shutil.copy(os.path.join(brand_folder_path, img), os.path.join(brand_train_folder, img))
            for img in val_images:
                shutil.copy(os.path.join(brand_folder_path, img), os.path.join(brand_val_folder, img))
            for img in test_images:
                shutil.copy(os.path.join(brand_folder_path, img), os.path.join(brand_test_folder, img))

            print(f"Images for {brand} have been split into train, validation, and test folders.")
        else:
            print(f"Folder for {brand} not found in {base_folder_path}")
else:
    print(f"Folder {base_folder_path} not found.")

