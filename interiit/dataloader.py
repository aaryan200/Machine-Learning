def load_data(path_to_csv):
    """
    Return a dataframe of classes listed in real.txt from Data.csv
    Dataframe consists of Class Name, Volume, Weight(kg)
    """
    import pandas as pd
    df = pd.read_csv(path_to_csv)
    df = df.drop(['True Weight Ibs','Length','Width','Height','Length(cm)','Width(cm)','Height(cm)'],axis=1)
    a = open("real.txt","r")
    real = a.read()
    a.close()
    real_li = real.split('\n')
    li = []
    for i in range(df.shape[0]):
        if df['Class'][i] not in real_li:
            li.append(i)
    df = df.drop(li)
    return df

from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
from torchvision import transforms
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_imgs(path_to_imgDir, path_to_csv):
    """
    a tuple with first element as name of class and second element is
    """
    df = pd.read_csv(path_to_csv)
    df = df.drop(['True Weight Ibs','Length','Width','Height','Volume','Weight(kg)'],axis=1)
    a = open("real.txt","r")
    real = a.read()
    a.close()
    real_li = real.split('\n')
    li = []
    for i in range(df.shape[0]):
        if df['Class'][i] not in real_li:
            li.append(i)
    df = df.drop(li)
    df.set_index("Class", inplace = True)
    resize = transforms.Resize(size=(255,255))
    transform = transforms.Compose([resize,
                                transforms.CenterCrop(255),
                                transforms.ToTensor()])
    dataset = ImageFolder(root=path_to_imgDir,transform=transform)
    for i in range(0,len(dataset.classes)):
        if dataset.classes[i] in list(df.index):
            temp = df.loc[dataset.classes[i]]
            # dataset.classes[i] = (dataset.classes[i],np.array([temp[0],temp[1]]))
            dataset.classes[i] = np.array([temp[0],temp[1],temp[2],temp[3]])
            # print(dataset.classes[i])
    for i in range(0,len(dataset.targets)):
        dataset.targets[i] = dataset.classes[dataset.targets[i]]
    return dataset

def visualize_batch(batch, classes, dataset_type):
	# initialize a figure
	fig = plt.figure("{} batch".format(dataset_type),
        figsize=(10, 10))
	# loop over the batch size
	for i in range(0, 30):
		# create a subplot
		# ax = plt.subplot(2, 5, i + 1)
		# grab the image, convert it from channels first ordering to
		# channels last ordering, and scale the raw pixel intensities
		# to the range [0, 255]
		image = batch[0][i].cpu().numpy()
		image = image.transpose((1, 2, 0))
		image = (image * 255.0).astype("uint8")
		# grab the label id and get the label from the classes list
		idx = batch[1][i]
		label = classes[idx];# print(image); print(label)
        # print(image)
        # print(label)
		# show the image along with the label
		# plt.imshow(image)
		# plt.title(label)
		# plt.axis("off")
	# show the plot
	# plt.tight_layout()
	# plt.show()

def main():
    dataset = load_imgs('../../data/interiit/data/','Data1.csv')
    print(dataset.targets)
    # print('\n\n')
    # print(dataset.classes)
    # dataLoad = DataLoader(dataset, batch_size=30, shuffle=False)
    # trainBatch = next(iter(dataLoad))
    # visualize_batch(trainBatch, dataset.classes, "train")

if __name__ == "__main__":
    main()
