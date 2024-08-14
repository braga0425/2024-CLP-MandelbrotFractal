#include <complex>

extern "C"
{
    __declspec(dllexport) void calculate_mandelbrot(int width, int height, int max_iteration, float p_x1, float p_y1, float p_x2, float p_y2, int *output)
    {
        for (int y = 0; y < height; ++y)
        {
            for (int x = 0; x < width; ++x)
            {
                std::complex<float> z, c = {p_x1 + ((float)x / width) * (p_x2 - p_x1),
                                            p_y1 + ((float)y / height) * (p_y2 - p_y1)};
                int i = 0;
                while (abs(z) < 2 && ++i < max_iteration)
                    z = z * z + c;

                double t = (double)i / max_iteration;
                int r = (int)(9 * (1 - t) * t * t * t * 255);
                int g = (int)(15 * (1 - t) * (1 - t) * t * t * 255);
                int b = (int)(8.5 * (1 - t) * (1 - t) * (1 - t) * t * 255);

                output[(y * width + x) * 3 + 0] = r;
                output[(y * width + x) * 3 + 1] = g;
                output[(y * width + x) * 3 + 2] = b;
            }
        }
    }
}
