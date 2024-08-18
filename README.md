# Project 8: Image Selector and Segmentation Mask Viewer

This Streamlit app allows users to select images from a specified directory, send them to a remote API for semantic segmentation, and view the computed segmentation masks side by side with the corresponding ground truth masks.

## Features

- **Image Selection**: Browse and select images from a specified directory.
- **Semantic Segmentation**: Send selected images to a remote API for segmentation.
- **Mask Comparison**: View the computed segmentation mask alongside the ground truth (validation) mask.

## How It Works

1. **Image Selection**: The user selects an image from the provided directory. The selected image is displayed within the app.
2. **Segmentation Request**: After selecting an image, the user can send the image to a remote API to obtain a segmentation mask by clicking the "Get Segmentation Mask" button.
3. **Mask Display**: The app retrieves the computed mask from the API and loads the corresponding ground truth mask from the local directory. Both masks are displayed side by side for comparison.

## Installation

To run this app locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gregorymarchal/project8-streamlit_app.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd project8-streamlit_app
   ```
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit app**:
   ```bash
   streamlit run streamlit_app.py
   ```

## Configuration

Make sure to update the paths in the script to match the locations of your image directories:

- `root_directory`: The root directory where the images are stored.
- `root_dir_masks`: The root directory where the corresponding ground truth masks are stored.

The app assumes that the directory structure is consistent and that the naming convention follows this pattern:

- **Image**: `frankfurt/frankfurt_000000_001236_leftImg8bit.png`
- **Ground Truth Mask**: `frankfurt/frankfurt_000000_001236_gtFine_color.png`

## Usage

1. **Start the app** using the command `streamlit run streamlit_app.py`.
2. **Select an image** from the dropdown menu.
3. **View the selected image** displayed in the app.
4. **Click "Get Segmentation Mask"** to send the image to the API.
5. **Compare the segmentation masks**: The computed mask and the ground truth mask will be displayed side by side.

## Dependencies

- `streamlit`: For creating the web app.
- `PIL` (Pillow): For image processing.
- `requests`: For sending HTTP requests to the remote API.

You can install these dependencies using the provided `requirements.txt` file.

## Contributing

Contributions are welcome! If you have any improvements, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any issues or questions, please feel free to open an issue in this repository.
