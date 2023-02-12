import cv2
import numpy as np
import matplotlib.pyplot as plt
import pickle
import os
import torch
import numpy as np
from torch.utils.data import TensorDataset, DataLoader
from read_data import get_compressed_object
from torchvision import transforms

def make_dataset(root):
    INCH_TO_CM = 2.54
    LBS_TO_G = 453.592
    files = os.listdir(root)
    cmprsd_objects = np.array([get_compressed_object(os.path.join(root,filename)) for filename in files])
    img_data = np.array([cv2.cvtColor(cv2.imdecode(np.frombuffer(obj['image_data'],np.uint8),-1),cv2.COLOR_RGB2BGR) for obj in cmprsd_objects])
    dimens_data = np.array([np.array([float(obj['dimensions'][0])*INCH_TO_CM,
                                    float(obj['dimensions'][1])*INCH_TO_CM,
                                    float(obj['dimensions'][2])*INCH_TO_CM,
                                    float(obj['weight'][0])*LBS_TO_G/((INCH_TO_CM**3)*float(obj['dimensions'][0])*float(obj['dimensions'][1])*float(obj['dimensions'][2]))]) for obj in cmprsd_objects])
    tensor_img = torch.Tensor(img_data).to(torch.long) # transform to torch tensor
    tensor_dimens = torch.Tensor(dimens_data)
    dataset = TensorDataset(tensor_img,tensor_dimens) # create your dataset
    return dataset

def main():
    train_ds = make_dataset('../../data/interiit/amazon_data/train_data/')
    val_ds = make_dataset('../../data/interiit/amazon_data/val_data/')
    trainDataLoader = DataLoader(train_ds, batch_size = 64)
    valDataLoader = DataLoader(val_ds, batch_size = 64)

if __name__ == "__main__":
    main()