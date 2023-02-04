import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import dataloader as CustomDataLoader
from torch.utils.data import random_split, DataLoader
from dataloader import load_imgs


def load_data(valid_size=0.1, shuffle=True, resize = 255, random_seed=2008, batch_size = 64):
    
    transform_train = torchvision.transforms.Compose([
        torchvision.transforms.Resize(resize),
        torchvision.transforms.RandomHorizontalFlip(),
        torchvision.transforms.RandomVerticalFlip(),
        torchvision.transforms.RandomRotation(10),
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    
    transform_test = torchvision.transforms.Compose([
        torchvision.transforms.Resize(resize),
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    
    # TODO: Load data from image_set
    # print(os.listdir('data'))
    image_set = torchvision.datasets.ImageFolder(root='data', transform=transform_train)
    print(image_set.classes)
    image_label = pd.read_csv('modified.csv')
    image_label = image_label.sort_values(by='Class')
    # print(image_label)
    label_set = torch.Tensor(image_label[['Volume', 'Weight(kg)']].values)
    print(image_set.classes)
    # print(label_set)
    data_loader = torch.utils.data.DataLoader(image_set, batch_size=batch_size, shuffle=shuffle)
    
    return data_loader


# Regressor Model for the image
class ModelClass(nn.Module):
    def __init__(self, image_size=255):
        super(ModelClass, self).__init__()
        
        # TODO: Complete the model
        self.model = torchvision.models.efficientnet_v2_l()
        self.image_size = image_size
        # self.weight_embedding = nn.Embedding(2, self.image_size * self.image_size)
        self.model.classifier = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(in_features=1280, out_features=2)
        )
        
        
        self.loss_function_huber = nn.HuberLoss() 
        self.loss_function_l1 = nn.L1Loss()
        self.model.features[0][0] = nn.Conv2d(4, 32, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
        self.optimizer = torch.optim.Adam(self.parameters(), lr=0.0001)
        
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        if torch.cuda.is_available():
            self.model = self.model.cuda()
                    
                    
    # TODO: Complete the forward function
    def forward(self, x, weight=0):
        weight_channel = torch.Tensor()
        for val in weight:
            weight_channel = torch.cat((weight_channel, val.repeat(1,1, self.image_size, self.image_size)))
        x = torch.cat((x, weight_channel), dim=1)
        x = self.model(x)
        return x

    # TODO: Complete the training function
    def train(self, train_loader, val_loader, epochs=10):
        self.model.train()
        best_val_acc = 0
        loss = []
        for epoch in range(epochs):
            self.train_epoch(train_loader, epoch)
        
            if val_loader is not None:
                val_loss, val_acc = self.evaluate(val_loader)
                print('Epoch: {} \tValidation Loss: {:.6f} \tValidation Accuracy: {:.2f}%'.format(epoch, val_loss, val_acc))
                loss.append(val_loss)
                if val_acc > best_val_acc:
                    best_val_acc = val_acc
                    torch.save(self.model.cpu(), 'best_model.pt')
                    
        plt.plot(loss)
        plt.title('Validation Loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.savefig('loss.png')
        print('Best Validation Accuracy: {:.2f}%'.format(best_val_acc))
        return
    
    def train_epoch(self, train_loader, epoch):
        self.model.train()
        
        for batch_idx, (data, target) in enumerate(train_loader):
            # print(batch)
            data, target = data.float(), target.float()
            data, target = data.to(self.device), target.to(self.device)
            print(target)
            
            output = self(data)
            loss = self.loss_function_huber(output, target) + self.loss_function_l1(output, target)
            loss.backward()
            self.optimizer.step()
            self.optimizer.zero_grad()
            
            if batch_idx % 100 == 0:
                print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                    epoch, batch_idx * len(data), len(train_loader.dataset),
                    100. * batch_idx / len(train_loader), loss.item()))
        
        return
               

    # TODO: Complete the evaluation function
    def evaluate(self, test_loader, criterion):
        self.eval()
        test_loss = 0
        correct = 0
        with torch.no_grad():
            for data, target in test_loader:
                data, target = data.float(), target.float()
                data, target = data.to(self.device), target.to(self.device)
                output = self(data)
                test_loss += criterion(output, target).item()
                pred = output.round()
                correct += pred.eq(target.view_as(pred)).sum().item()

        test_loss /= len(test_loader.dataset)
        accuracy = 100. * correct / len(test_loader.dataset)
        return test_loss, accuracy

    # TODO: Complete the prediction function
    def predict(self, data):
        self.eval()
        with torch.no_grad():
            output = self(data)
            pred = output.round()
        return pred
    
        


def main():
    # TODO: Complete the main function
    GS_Model = ModelClass()
    # print(GS_Model)
    dataset = load_imgs('data/','Data.csv')
    # print(dataset.targets)
    train_ds, val_ds = dataset, dataset
    # train_ds.dataset.targets = train_ds.dataset.classes
    train_loader = DataLoader(train_ds, batch_size= 64, shuffle=False, num_workers=4, pin_memory=True)
    val_loader = DataLoader(val_ds, batch_size= 64, num_workers=4, pin_memory=True)
    GS_Model.train(train_loader, val_loader, epochs=10)
    

if __name__ == '__main__':
    main()