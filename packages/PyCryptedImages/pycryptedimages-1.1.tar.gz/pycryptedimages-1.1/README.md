
# PyCryptedImages

**PyCryptedImages** is a Python package designed to hide text in fake image files. It allows you to encode text into a file that appears to be an image, making it useful for various applications, such as steganography or protecting sensitive data.

## Features
- Encode text into a fake image file (JPEG format).
- User-friendly function for specifying the file path and name.
- Compatible with Windows and other operating systems.

## Installation
You can install **PyCryptedImages** using `pip`:

```bash
pip install PyCryptedImages
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/R-D-R248/PyCryptedImages.git
```

## Usage
Here’s how you can use **PyCryptedImages** to encode text into a fake image:

```python
import PyCryptedImages

# Generate a fake image path
pycrypt_image = PyCryptedImages.Encode(path="C:/Users/YourUser/Desktop", name="hidden_message")

# Save text into the generated fake image path
PyCryptedImages.Save(text="Hello, world!", pycrypt_image=pycrypt_image)

# Directly encode and save text into a fake image
PyCryptedImages.EncodeFile(text="Hello, world!", path="C:/Users/YourUser/Desktop", name="hidden_message")
```

## Example Output
This will create a file named **hidden_message.jpg** on your Desktop, but it will actually contain the text `"Hello, world!"`.

## Decode Function
To decode the hidden text from a fake image file, use the following code:

```python
import PyCryptedImages

# Decode text from the fake image
text = PyCryptedImages.Decode(path="C:/Users/YourUser/Desktop", name="hidden_message")
print("Decoded Text:", text)
```

## Contributing
Feel free to submit issues or contribute by making pull requests on [GitHub](https://github.com/R-D-R248/PyCryptedImages).

## License
This project is licensed under the **MIT License**.
