# Background Subtraction

Este projeto realiza a separação de fundo em vídeos usando três métodos:
1. **Fundo Fixo**: Usa o primeiro frame como referência.
2. **Modelo da Média**: Calcula a média dos valores de pixel.
3. **Modelo da Mediana**: Calcula a mediana dos valores de pixel.

## Estrutura

- `video.mp4`: Vídeo de entrada.
- `frames/`: Frames extraídos do vídeo.
- `output/`: Resultados para cada método.
- `main.py`: Código-fonte principal.

## Requisitos

- Python 3.x
- OpenCV
- NumPy

### Instalação das Dependências

```bash
pip install -r requirements.txt