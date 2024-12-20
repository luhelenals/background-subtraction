import cv2
import numpy as np
import os

# Caminhos para o vídeo e pasta de frames
video_path = './video.mp4'
frame_folder = './frames'
output_folder = './frames_output'

def apply_background_sub(frames):
    # Criação da pasta de saída
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    # 1. Fundo fixo
    background_fixed = frames[0]  # Usa o primeiro frame como fundo fixo
    results_fixed = [cv2.absdiff(frame, background_fixed) for frame in frames]

    # 2. Modelo da média
    background_mean = np.mean(frames, axis=0).astype(np.uint8)  # Média de todos os frames
    results_mean = [cv2.absdiff(frame, background_mean) for frame in frames]

    # 3. Modelo da mediana
    background_median = np.median(frames, axis=0).astype(np.uint8)  # Mediana de todos os frames
    results_median = [cv2.absdiff(frame, background_median) for frame in frames]

    # Salvar os resultados para cada modelo
    for i in range(len(frames)):
        # Fundo fixo
        cv2.imwrite(os.path.join(output_folder, f"fixed_frame_{i}.png"), results_fixed[i])
        # Média
        cv2.imwrite(os.path.join(output_folder, f"mean_frame_{i}.png"), results_mean[i])
        # Mediana
        cv2.imwrite(os.path.join(output_folder, f"median_frame_{i}.png"), results_median[i])
    
    return results_fixed, results_mean, results_median

def get_frames():
    # Obter a lista de frames
    frame_files = sorted(
        [f for f in os.listdir(frame_folder) if f.endswith('.png')],
        key=lambda x: int(x.replace('frame_', '').replace('.png', '')))
    if not frame_files:
        raise ValueError("Nenhum frame encontrado na pasta de entrada.")
    
    return [cv2.imread(os.path.join(frame_folder, file), cv2.IMREAD_GRAYSCALE) for file in frame_files]

def video_to_frames():
    # Criação da pasta para salvar os frames
    if not os.path.exists(frame_folder):
        os.makedirs(frame_folder)

    # Abrir o vídeo
    video = cv2.VideoCapture(video_path)
    frame_number = 0

    # Ler frames e salvá-los
    while True:
        success, frame = video.read()
        if not success:
            break
        frame_path = os.path.join(frame_folder, f"frame_{frame_number}.png")
        cv2.imwrite(frame_path, frame)
        frame_number += 1

    video.release()

    print(f"{frame_number} frames salvos")

def main():
    print("Salvando o vídeo em frames")
    video_to_frames()
    frames = get_frames()
    print("Aplicando técnicas de separação de fundo nos frames obtidos")
    apply_background_sub(frames)
    print(f"Resultados salvos na pasta: {output_folder}")

if __name__ == '__main__':
    main()