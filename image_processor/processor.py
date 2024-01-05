from PIL import Image

def load_image(file_path):
    """
    Carrega uma imagem do caminho especificado.
    """
    return Image.open(file_path)

def resize_image(image, size):
    """
    Redimensiona a imagem para o tamanho especificado.
    """
    return image.resize(size)

def save_image(image, file_path):
    """
    Salva a imagem no caminho especificado.
    """
    image.save(file_path)