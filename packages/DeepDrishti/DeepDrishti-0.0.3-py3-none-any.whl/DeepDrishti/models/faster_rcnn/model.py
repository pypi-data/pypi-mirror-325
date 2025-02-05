from tqdm import tqdm

import torch
from torch import optim
from torchvision import transforms as T
from torchvision.models.detection import fasterrcnn_resnet50_fpn,FasterRCNN_ResNet50_FPN_Weights, faster_rcnn

from torch.utils.data import DataLoader

from .dataloader import FasterRCNNDataset
from .utils import tensor_to_data, image_to_tensor
from ...utils import yaml_reader

transform = T.Compose([
    T.ToTensor()  
])

class FasterRCNN():
    def __init__(self, weight=None):
        self.model = fasterrcnn_resnet50_fpn(weights=FasterRCNN_ResNet50_FPN_Weights.COCO_V1)
        self.weight = weight
        self.checkpoint = None
        
        device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        
        if self.weight is not None:
            self.checkpoint = torch.load(self.weight, weights_only=True)
            in_features = self.model.roi_heads.box_predictor.cls_score.in_features
            self.model.roi_heads.box_predictor = faster_rcnn.FastRCNNPredictor(in_features, self.checkpoint['nc'])
            self.model.load_state_dict(self.checkpoint['model_state_dict'])
            
        self.model.to(device)

    def train(self, data, epochs):
        
        # yaml data
        config = yaml_reader(data)
        num_classes = config['dataset']['nc']
        image_dir = config['dataset']['image_dir']
        annotation_file = config['dataset']['annotation_file']
        
        device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        
        # dataset
        dataset = FasterRCNNDataset(image_dir=image_dir, annotation_file=annotation_file, transforms=transform )
        
        dataloader = DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=lambda x: tuple(zip(*x)))
        
        
        # pre-train
        in_features = self.model.roi_heads.box_predictor.cls_score.in_features
        self.model.roi_heads.box_predictor = faster_rcnn.FastRCNNPredictor(in_features, num_classes)
        
        # pre-train weights
        if self.weight is not None:
            self.checkpoint = torch.load(self.weight, weights_only=True)
            in_features = self.model.roi_heads.box_predictor.cls_score.in_features
            self.model.roi_heads.box_predictor = faster_rcnn.FastRCNNPredictor(in_features, self.checkpoint['nc'])
            self.model.load_state_dict(self.checkpoint['model_state_dict'])
          
        # model config
        self.model.to(device)   
        optimizer = optim.Adam(params=self.model.parameters(), lr=0.0001)
         
         
        # train loop
        for epoch in range(epochs):
            self.model.train()
            
            pbar = tqdm(dataloader, desc=f"Epoch [{epoch}/{epochs}]", total=len(dataloader))
            
            for images, targets in pbar:
                images = [img.to(device) for img in images]
                targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

                loss_dict = self.model(images, targets)
                loss = sum(loss for loss in loss_dict.values())

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                pbar.set_postfix({"Loss": f"{loss.item():.4f}"})
            
        print("training has been completed successfully")
        
    def __call__(self, image_path):
        device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        
        tensor_image = image_to_tensor(image_path=image_path, transform=transform)

        self.model.to(device)
        self.model.eval()
        with torch.no_grad():
            output = self.model(tensor_image.unsqueeze(0).to(device))
            return tensor_to_data(output)
        
    def export(self):
        torch.save({
                'model_state_dict': self.model.state_dict(),
                'nc': self.checkpoint['nc']}, 'best.pth')