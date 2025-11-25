# type: ignore

from PIL import Image

def redify_image(input_file_name: str, output_file_name: str) -> None:
    with Image.open(input_file_name) as input_file:
        pixin = input_file.load()
        width, height = input_file.size
    output_file = Image.new('RGB', (width, height))
    pixout = output_file.load()
    for row in range(height):
        for col in range(width):
            red, _, _ = pixin[col, row]
            pixout[col, row] = (red, 0, 0)
    output_file.save(output_file_name)


if __name__ == '__main__':
    redify_image('scarlett.png', 'scarlett_red.png')