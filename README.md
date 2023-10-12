# Image_steganography

Python program based on stegonographical methods to hide text in images using the Least Significant Bit technique.

I used the most basic method which is the least significant bit. A colour pixel is composed of red, green and blue, encoded on one byte. The idea is to store information in the first bit of every pixel's RGB component. In the worst case, the decimal value is different by one which is not visible to the human eye. In practice, if you don't have space to store all of your data in the first bit of every pixel you should start using the second bit, and so on. You have to keep in mind that the more your store data in an image, the more it can be detected.

Installation
------------

```bash
pip install stegano
```

Encoding
--------

```bash
python <file>.py -encode <file_path> "message"
```
> *Now the python code will run and the output will be save as a file called `hide.png` in the current folder you are.*

Decoding
--------

```bash
python <file>.py -decode <file_path-hide.png>
```
> *Now the `hide.png` file will be decode and the output will be display on the terminal*
