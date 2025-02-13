import sys
import os
import glob
import pickle
import numpy as np
from PyCmpltrtok.common import *

sub_dirs = __name__.split('.')[:-1]


def _load(xurl, xname, only_meta=False):
    """
    Download cifar10 data tar file, decompress it, and extract data form it.
    Note: If a former downloading process is terminated by accidence and the partial tar file is decompressed, please
    remove the partial tar file and files that it releases, and retry this again.

    :param xurl: The URL of the compressed data tar file.
    :param xname: The file name of the compressed data tar file.
    :param only_meta: Is only load meta-data.
    :return:
    If only_meta=True: label_names: a list of label names.
    Otherwise:
    x_train, y_train, x_test, y_test, label_names
    """
    sep('Load Cifar10 dataset')

    # decide data dir
    user_dir = os.environ['HOME']
    data_dir = os.path.join(user_dir, '.cache', *sub_dirs)
    os.makedirs(data_dir, exist_ok=True)

    # download the tar
    tar_path = os.path.join(data_dir, xname)
    if not os.path.exists(tar_path):
        print(f'Downloading ...')
        xcmd = f'wget "{xurl}" -O "{tar_path}"'
        print(xcmd)
        os.system(xcmd)
        print('Downloaded.')

    # decompress the tar
    base_name = 'cifar-10-batches-py'
    tgt_dir = os.path.join(data_dir, base_name)
    tgt_glob = f'{tgt_dir}/*batch*'
    tgt_paths = glob.glob(tgt_glob)
    n_tgt = len(tgt_paths)
    if n_tgt < 7:
        print('Decompressing ...')
        xcmd = f'tar --skip-old-files --warning=no-existing-file -zxv -f "{tar_path}" -C "{data_dir}"'
        print(xcmd)
        os.system(xcmd)
        print('Decompressed.')

    # load data
    if not only_meta:
        tgt_paths = sorted(glob.glob(tgt_glob))
    else:
        tgt_paths = [os.path.join(tgt_dir, 'batches.meta')]
    x_train, y_train, x_test, y_test = None, None, None, None
    for tgt_path in tgt_paths:

        print(f'Loading {tgt_path}')
        with open(tgt_path, 'rb') as f:
            xdict = pickle.load(f, encoding='bytes')

        """
        xset:
        For file batches.meta:
        ['num_cases_per_batch', 'label_names', 'num_vis']
        Or otherwise:
        ['batch_label', 'labels', 'data', 'filenames']
        """
        xset = set(xdict.keys())

        if b'label_names' in xset:
            """
            ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
            """
            label_names = [k.decode() for k in xdict[b'label_names']]
            if only_meta:
                return label_names
        else:
            batch_label = xdict[b'batch_label'].decode()
            key = 'testing'
            if key == batch_label[:len(key)]:
                # testing data
                if x_test is None:
                    x_test = xdict[b'data']
                    y_test = np.asarray(xdict[b'labels'], dtype=np.uint8)
                else:
                    x_test = np.concatenate([x_test, xdict[b'data']], axis=0)
                    y_test = np.concatenate([y_test, np.asarray(xdict[b'labels'], dtype=np.uint8)], axis=0)
            else:
                # training data
                if x_train is None:
                    x_train = xdict[b'data']
                    y_train = np.asarray(xdict[b'labels'], dtype=np.uint8)
                else:
                    x_train = np.concatenate([x_train, xdict[b'data']], axis=0)
                    y_train = np.concatenate([y_train, np.asarray(xdict[b'labels'], dtype=np.uint8)], axis=0)
        print(f'Loaded.')

    return x_train, y_train, x_test, y_test, label_names


def load(only_meta=False):
    xurl = 'http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz'
    xname = 'cifar-10-python.tar.gz'
    return _load(xurl, xname, only_meta=only_meta)


shape_ = (3, 32, 32)  # The shape of very image
