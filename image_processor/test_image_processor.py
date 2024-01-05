from .processor import load_image, resize_image, save_image

def main():
    # Carregando a imagem
    img = load_image('example.jpg')

    # Redimensionando a imagem
    resized_img = resize_image(img, (300, 300))

    # Salvando a imagem redimensionada
    save_image(resized_img, 'example_resized.jpg')

if __name__ == "__main__":
    main()