from PIL import Image

def tensor_to_data(tensor_data):
    for item in tensor_data:
        item['boxes'] = item['boxes'].cpu().numpy()
        item['labels'] = item['labels'].cpu().numpy()
        item['scores'] = item['scores'].cpu().numpy()
    return item

def image_to_tensor(image_path,transform):
    image = Image.open(image_path)
    return transform(image)