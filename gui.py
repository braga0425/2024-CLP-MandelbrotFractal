import ctypes
import numpy as np
from PIL import Image
import tkinter as tk
import os
import argparse

# Configurações de argparse
parser = argparse.ArgumentParser(description='Gera uma imagem do Conjunto de Mandelbrot.')
parser.add_argument('--width', type=int, default=800, help='Largura da imagem')
parser.add_argument('--height', type=int, default=800, help='Altura da imagem')
parser.add_argument('--max_iter', type=int, default=100, help='Número máximo de iterações')
parser.add_argument('--x1', type=float, default=-2.0, help='Coordenada x1')
parser.add_argument('--y1', type=float, default=-2.0, help='Coordenada y1')
parser.add_argument('--x2', type=float, default=2.0, help='Coordenada x2')
parser.add_argument('--y2', type=float, default=2.0, help='Coordenada y2')

args = parser.parse_args()

current_dir = os.path.dirname(os.path.abspath(__file__))

dll_path = os.path.join(current_dir, 'mandelbrot', 'x64', 'Release', 'mandelbrot.dll')

mandelbrot_lib = ctypes.CDLL(dll_path)

mandelbrot_lib.calculate_mandelbrot.argtypes = [
    ctypes.c_int,   # width
    ctypes.c_int,   # height
    ctypes.c_int,   # max_iteration
    ctypes.c_float, # p_x1
    ctypes.c_float, # p_y1
    ctypes.c_float, # p_x2
    ctypes.c_float, # p_y2
    ctypes.POINTER(ctypes.c_int) # output array
]

def generate_mandelbrot_image(width, height, max_iteration, p_x1, p_y1, p_x2, p_y2):
    output = np.zeros((width * height * 3), dtype=np.int32)
    mandelbrot_lib.calculate_mandelbrot(width, height, max_iteration, p_x1, p_y1, p_x2, p_y2, output.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))
    return output.reshape((height, width, 3))

def display_image(image_data):
    img = Image.fromarray(image_data.astype('uint8'))
    img.show()

def main():
    width, height = args.width, args.height
    max_iteration = args.max_iter
    p_x1, p_y1 = args.x1, args.y1
    p_x2, p_y2 = args.x2, args.y2

    root = tk.Tk()
    root.title("Mandelbrot Set")

    def on_generate():
        image_data = generate_mandelbrot_image(width, height, max_iteration, p_x1, p_y1, p_x2, p_y2)
        display_image(image_data)

    generate_button = tk.Button(root, text="Generate Mandelbrot", command=on_generate)
    generate_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
