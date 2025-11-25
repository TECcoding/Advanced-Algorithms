#----------------------------------------------------------
# Lab #1: Steganography
# Image processing through bit manipulation.
#
# Date: 1-Sep-2025
# Authors:
#           A01801044 Yael Sinuhe Grajeda Martinez
#           A01800840 Tadeo Emanuel Arellano Conde
#----------------------------------------------------------


# type: ignore

from PIL import Image
import sys

def extractHiddenImages(input_file_name: str) -> None:  
    try:
        img = Image.open(input_file_name)
    except FileNotFoundError:
        print(f"Error: The file '{input_file_name}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: the image couldnt open: {e}")
        sys.exit(1)
    
    if img.mode != "RGB":
        print(f"Error: the image should be in RGB mode (actual: {img.mode}).")
        sys.exit(1)
    
    
    width, height = img.size
    pixels = img.load()
    
    red_img = Image.new('1', (width, height))
    green_img = Image.new('1', (width, height))
    blue_img = Image.new('1', (width, height))
    
    red_pixels = red_img.load()
    green_pixels = green_img.load()
    blue_pixels = blue_img.load()

    BLACK = 0
    WHITE = 255
    
    for row in range(height):
        for col in range(width):
            
            red, green, blue = pixels[col, row]
            
            rb = red & 1
            gb = green & 1
            bb = blue & 1
            
            red_pixels[col, row] = WHITE if rb else BLACK
            green_pixels[col, row] = WHITE if gb else BLACK
            blue_pixels[col, row] = WHITE if bb else BLACK
    
    base_name = input_file_name.split('.')[0]
    
    red_output_path = f"{base_name}_channel_1_red.png"
    green_output_path = f"{base_name}_channel_2_green.png"
    blue_output_path = f"{base_name}_channel_3_blue.png"
    
    red_img.save(red_output_path)
    green_img.save(green_output_path)
    blue_img.save(blue_output_path)



def main():
    if (len(sys.argv) != 2):
        print("Error: The name of the file was not provided as a command line argument.")
        sys.exit(1)
        
    path = sys.argv[1]
    
    if not path.lower().endswith(".png"):
        print("Error: The provided file name doesn’t have a .png extension.")
        sys.exit(1)
    
    extractHiddenImages(path)

if __name__ == '__main__':
    main()