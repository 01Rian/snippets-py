import yt_dlp
import os

def download_video(url, output_path="youtube_downloader/downloads"):
    """
    Baixa um vídeo do YouTube na resolução escolhida pelo usuário usando yt-dlp.
    
    Args:
        url (str): URL do vídeo do YouTube
        output_path (str): Pasta onde o vídeo será salvo
    """
    try:
        # Criar pasta de downloads se não existir
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            
        # Configuração do yt-dlp
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,
        }
        
        # Obter informações do vídeo
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
        print(f"\nTítulo: {info['title']}")
        print(f"Duração: {info['duration']} segundos")
        
        # Configurações disponíveis para download
        formats = [
            {'format_id': 'best', 'desc': 'Melhor qualidade disponível'},
            {'format_id': '137+140', 'desc': '1080p com áudio (se disponível)'},
            {'format_id': '136+140', 'desc': '720p com áudio'},
            {'format_id': '135+140', 'desc': '480p com áudio'},
            {'format_id': '134+140', 'desc': '360p com áudio'},
        ]
        
        print("\nQualidades disponíveis:")
        for i, fmt in enumerate(formats, 1):
            print(f"{i}. {fmt['desc']}")
            
        # Solicitar escolha do usuário
        while True:
            try:
                escolha = int(input("\nEscolha o número da qualidade desejada: "))
                if 1 <= escolha <= len(formats):
                    break
                print("Opção inválida! Tente novamente.")
            except ValueError:
                print("Por favor, digite um número válido!")
        
        # Configurar o download com a qualidade escolhida
        format_escolhido = formats[escolha - 1]['format_id']
        ydl_opts = {
            'format': format_escolhido,
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'progress': True,
        }
        
        print(f"\nBaixando '{info['title']}'...")
        
        # Realizar o download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        print(f"\nDownload concluído! Arquivo salvo em: {output_path}")
        
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {str(e)}")
        print("\nDicas de solução:")
        print("1. Verifique sua conexão com a internet")
        print("2. Confirme se a URL do vídeo está correta")
        print("3. Verifique se o vídeo não está restrito ou privado")
        print("4. Tente atualizar o yt-dlp com: pip install -U yt-dlp")

if __name__ == "__main__":
    # Exemplo de uso
    url = input("Digite a URL do vídeo do YouTube: ")
    download_video(url)