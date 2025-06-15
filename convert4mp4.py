import sys
from moviepy.editor import VideoFileClip

def converter_mkv_para_mp4(entrada, saida):
    try:
        print(f"Convertendo '{entrada}' para '{saida}'...")
        clip = VideoFileClip(entrada)
        clip.write_videofile(saida, codec="libx264", audio_codec="aac")
        print("Conversão finalizada com sucesso!")
    except Exception as e:
        print("Erro durante a conversão:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python conversor.py <entrada.mkv> <saida.mp4>")
        sys.exit(1)

    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]
    converter_mkv_para_mp4(arquivo_entrada, arquivo_saida)
