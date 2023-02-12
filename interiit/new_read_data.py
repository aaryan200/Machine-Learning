import cv2
import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

try:
    # try using the new lz4 API
    import lz4.block
    lz4_compress = lz4.block.compress
    lz4_decompress = lz4.block.decompress
except ImportError:
    # fall back to old one
    lz4_compress = lz4.LZ4_compress
    lz4_decompress = lz4.LZ4_uncompress

def get_compressed_object(filename):
    with open(filename, 'rb') as fp:
        compressed_bytes = fp.read()
    decompressed = lz4_decompress(compressed_bytes)
    pickled_object = pickle.loads(decompressed)
    return pickled_object

def read_data(root):
    files = os.listdir(root)
    print(len(files))
    for filename in files:
        f = os.path.join(root,filename)
        record = get_compressed_object(f)
        # print(record)
        print(record.keys())
        im = cv2.imdecode(np.frombuffer(record['image_data'], np.uint8), -1)
        # print(im)
        # print(im.shape)
        # thickness_mask = record['thickness_mask']
        # sp = plt.subplot(121)
        # plt.imshow(im)
        # sp.set_xlabel(str(record['weight'])+' lbs')
        # sp=plt.subplot(122)
        # plt.imshow(thickness_mask)
        dims = record['dimensions']
        print(dims)
        print(record['weight'])
        # dimstr = ' inches by '.join(dims)+' inches'
        # sp.set_xlabel(dimstr)
        # # matplotlib.use('TkAgg')
        plt.show()
        break
        


if __name__=='__main__':
    read_data('../../data/interiit/amazon_data/fun/')