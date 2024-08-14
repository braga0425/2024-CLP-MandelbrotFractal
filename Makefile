PYTHON = python
PIP = pip
SCRIPT = gui.py
DLL_PATH = mandelbrot/x64/Release/mandelbrot.dll

all: install-dependencies run

install-dependencies:
	$(PIP) install numpy pillow

run:
	$(PYTHON) $(SCRIPT)

# Caso de Estudo 1: Visão ampla padrão
study1:
	$(PYTHON) $(SCRIPT) --width 800 --height 800 --max_iter 100 --x1 -2.0 --y1 -1.5 --x2 1.0 --y2 1.5

# Caso de Estudo 2: Zoom em uma ramificação
study2:
	$(PYTHON) $(SCRIPT) --width 800 --height 800 --max_iter 1000 --x1 -0.75 --y1 -0.1 --x2 -0.74 --y2 0.1

# Caso de Estudo 3: Zoom extremo em uma característica específica
study3:
	$(PYTHON) $(SCRIPT) --width 1200 --height 1200 --max_iter 2000 --x1 -0.748 --y1 0.1 --x2 -0.7475 --y2 0.1

# Limpa arquivos temporários (se houver)
clean:
	@echo "Não há arquivos temporários para limpar."
