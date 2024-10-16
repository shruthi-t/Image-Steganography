# Image-Steganography
# Hidden in Plain Sight: Secure Communication with Image Steganography

## Overview

This project implements image steganography, a technique used to conceal text messages within images. It allows users to encrypt a message into an image and later decrypt it, ensuring secure communication. The application is built using HTML, CSS, JavaScript, and Django for the backend.

## Features

- **Encrypt Text into Image**: Users can upload an image and enter a message to encrypt. The message is embedded into the image pixels.
- **Download Encrypted Image**: After encryption, the modified image can be downloaded.
- **Decrypt Text from Image**: Users can upload an encrypted image and specify the length of the original message to extract the hidden text.
- **User-friendly Interface**: Simple and intuitive web interface for easy interaction.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **Canvas API**: For image manipulation and data extraction

## Getting Started

### Prerequisites

- Python 3.x
- Django

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/image-steganography.git
   cd image-steganography
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

4. Open your web browser and navigate to `http://127.0.0.1:8000/`.

## How to Use

1. **Encrypting a Message**:
   - Click on the "Encrypt" section.
   - Upload an image file.
   - Enter the text message you wish to encrypt.
   - Click on the "Encrypt" button to embed the text and download the modified image.

2. **Decrypting a Message**:
   - Go to the "Decrypt" section.
   - Upload the encrypted image.
   - Enter the length of the original text message.
   - Click the "Decrypt" button to reveal the hidden message.


## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.













