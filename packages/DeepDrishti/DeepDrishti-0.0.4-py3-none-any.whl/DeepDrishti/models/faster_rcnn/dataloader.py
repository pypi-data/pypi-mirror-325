import json
import os 
from PIL import Image

import torch
from torch.utils.data import Dataset

class FasterRCNNDataset(Dataset):
    def __init__(self, image_dir, annotation_file, transforms=None):
        self.image_dir = image_dir
        with open(annotation_file, "r") as f:
            self.coco = json.load(f)
            
        self.transforms = transforms
        self.image_data = {img["id"]: img for img in self.coco["images"]}
        self.annotations = self._group_annotations(self.coco["annotations"])
        
    def _group_annotations(self, annotations):
        ann_dict = {}
        for ann in annotations:
            image_id = ann["image_id"]
            if image_id not in ann_dict:
                ann_dict[image_id] = []
            ann_dict[image_id].append(ann)
        return ann_dict
    
    def __len__(self):
        return len(self.annotations)
    
    def __getitem__(self, idx):
        image_id = list(self.image_data.keys())[idx]
        image_info = self.image_data[image_id]
        image_path = os.path.join(self.image_dir, image_info["file_name"])

        image = Image.open(image_path).convert("RGB")

        boxes = []
        labels = []
        if image_id in self.annotations:
            for ann in self.annotations[image_id]:
                x, y, w, h = ann["bbox"]
                boxes.append([x, y, x + w, y + h]) 
                labels.append(ann["category_id"]) 

        boxes = torch.as_tensor(boxes, dtype=torch.float32)
        labels = torch.as_tensor(labels, dtype=torch.int64)

        target = {
            "boxes": boxes,
            "labels": labels,
            "image_id": torch.tensor([image_id])
        }

        if self.transforms:
            image = self.transforms(image)

        return image, target
        