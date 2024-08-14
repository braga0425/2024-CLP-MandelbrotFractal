#ifdef MANDELBROT_EXPORTS
#define DLL __declspec(dllexport)
#else
#define DLL __declspec(dllimport)
#endif // MANDELBROT_EXPORTS
