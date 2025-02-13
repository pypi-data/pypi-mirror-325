import sys
import os
import glob
import pickle
import numpy as np
import struct
from PyCmpltrtok.common import *

sub_dirs = __name__.split('.')[:-1]


def _load(xbase_url, xtrain, xtest, xtrain_size, xtest_size):
    """

    """
    sep('Load Cifar10 dataset')

    # decide data dir
    user_dir = os.environ['HOME']
    data_dir = os.path.join(user_dir, '.cache', *sub_dirs)
    os.makedirs(data_dir, exist_ok=True)

    # download the tar
    for xname, xsize in zip([*xtrain,  *xtest], [*xtrain_size, *xtest_size]):
        tar_path = os.path.join(data_dir, xname)
        if os.path.exists(tar_path):
            xact_size = os.path.getsize(tar_path)
            if xsize == xact_size:
                print(f'{tar_path} already downloaded')
                continue
            elif xsize < xact_size:
                print(f'{tar_path} is bigger than expected. Something should be wrong. Stop.', flush=True, file=sys.stderr)
                sys.exit(1)
        xurl = xbase_url + '/' + xname
        print(f'Downloading ...')
        xcmd = f'wget -O "{tar_path}" -c "{xurl}"'
        print(xcmd)
        os.system(xcmd)
        print('Downloaded.')

    # decompress the tar
    for xname in [*xtrain,  *xtest]:
        tar_path = os.path.join(data_dir, xname)
        tgt_path = glob.glob(data_dir + '/' + xname[:-3])
        n_tgt = len(tgt_path)
        if n_tgt >= 1:
            print(f'{tgt_path} is already there.')
        else:
            print('Decompressing ...')
            xcmd = f'gunzip -f -k "{tar_path}"'
            print(xcmd)
            os.system(xcmd)
            print('Decompressed.')

    # load data
    def load_data(type, xname):
        tgt_path = os.path.join(data_dir, xname[:-3])
        is_label = xname.split('-')[1] == 'labels'
        xdata = []
        with open(tgt_path, 'rb') as f:
            xbytes = f.read(8)
            # https://docs.python.org/3/library/struct.html#struct-format-strings
            mn, num = struct.unpack('>ii', xbytes)
            if is_label:
                for _ in range(num):
                    xlabel = struct.unpack('>B', f.read(1))
                    xdata.append(xlabel)
                xdata = np.array(xdata, dtype=np.uint8)
            else:
                xbytes = f.read(8)
                n_rows, n_cols = struct.unpack('>ii', xbytes)
                for _ in range(num):
                    buff = f.read(n_rows * n_cols)
                    xone = np.frombuffer(buff, dtype=np.uint8).reshape(n_rows, n_cols)
                    xdata.append(xone)
                xdata = np.array(xdata, dtype=np.uint8)
        return xdata

    xdict = {}
    for xname, type in zip([*xtrain,  *xtest], ['x_train', 'y_train', 'x_test', 'y_test']):
        # https://stackoverflow.com/questions/8028708/dynamically-set-local-variable
        xdict[type] = load_data(type, xname)

    return xdict['x_train'], xdict['y_train'], xdict['x_test'], xdict['y_test']


def load(only_meta=False):
    xbase_url = 'http://yann.lecun.com/exdb/mnist'
    xtrain = (
        'train-images-idx3-ubyte.gz',
        'train-labels-idx1-ubyte.gz'
    )
    xtrain_size = (9912422, 28881)
    xtest = (
        't10k-images-idx3-ubyte.gz',
        't10k-labels-idx1-ubyte.gz'
    )
    xtest_size = (1648877, 4542)
    return _load(xbase_url, xtrain, xtest, xtrain_size, xtest_size)


shape_ = (28, 28)  # The shape of very image
