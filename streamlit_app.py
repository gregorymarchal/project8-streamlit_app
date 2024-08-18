import streamlit as st
import os
from PIL import Image
import requests
from io import BytesIO

# Define the root directories where the images and their corresponding masks are stored
root_directory = "/mnt/c/Users/news/Documents/ai_engineer_path/project8/leftImg8bit/val"
root_dir_masks = "/mnt/c/Users/news/Documents/ai_engineer_path/project8/gtFine/val"

# Function to crawl through directories and get a list of image files
def crawl_image_files(directory):
    supported_formats = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(supported_formats):
                full_path = os.path.join(root, file)
                image_files.append(full_path)
    return image_files

# Function to send the image to the API and get the segmentation mask
def get_segmentation_mask(image_path):
    url = "https://aiep-p8.azurewebsites.net/upload"
    with open(image_path, "rb") as image_file:
        files = {"file": (os.path.basename(image_path), image_file, "image/png")}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return None

# Streamlit app
def main():
    st.title("Image Selector and Segmentation Mask Viewer")

    # Crawl the directory to get a list of all images
    image_files = crawl_image_files(root_directory)

    if image_files:
        # Let the user select an image file
        selected_image = st.selectbox("Select an image file", image_files)

        # Display the selected image
        image = Image.open(selected_image)
        st.image(image, caption=os.path.basename(selected_image), use_column_width=True)

        # Button to send the image to the API
        if st.button("Get Segmentation Mask"):
            with st.spinner('Processing...'):
                # Get the segmentation mask from the API
                segmentation_mask = get_segmentation_mask(selected_image)

                if segmentation_mask:
                    st.image(segmentation_mask, caption="Segmentation Mask", use_column_width=True)
    else:
        st.write("No images found in the directory.")

if __name__ == "__main__":
    main()
