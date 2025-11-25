# type: ignore

from PIL import Image

def one_bit_image(input_file_name: str, output_file_name: str) -> None:
    BLACK: int = 0
    WHITE: int = 1
    THRESHOLD: int = 128
    with Image.open(input_file_name) as input_file:
        pixin = input_file.load()
        width, height = input_file.size
    output_file = Image.new('1', (width, height))
    pixout = output_file.load()
    for row in range(height):
        for col in range(width):
            red, green, blue = pixin[col, row]
            gray = (red + green + blue) // 3
            pixout[col, row] = BLACK if gray < THRESHOLD else WHITE
            # if gray < THRESHOLD:
            #     pixout[col, row] = BLACK
            # else:
            #     pixout[col, row] = WHITE
    output_file.save(output_file_name)
    


if __name__ == '__main__':
    one_bit_image('scarlett.png', 'scarlett_one_bit.png')