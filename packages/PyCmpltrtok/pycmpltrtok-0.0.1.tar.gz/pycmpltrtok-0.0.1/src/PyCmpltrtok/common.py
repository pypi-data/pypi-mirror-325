"""
Common routines
"""
import re
import os
import sys
import datetime
import numpy as np
import math
import time
import hashlib
import json
import random
import copy
import glob
from typing import Tuple


def sep(label='', cnt=32, char='-', rchar=None):
    """Util function to print a separator line with label."""
    if rchar is None:
        rchar = char
    print(char * cnt, label, rchar * cnt, sep='', flush=True)


def sep_str(label):
    return '----------------%s----------------' % (str(label), )


def int_round(x):
    return int(round(x))


def int_ceil(x):
    return int(math.ceil(x))


def int_floor(x):
    return int(math.floor(x))


def get_dir_name_ext(path):
    xdir, xbase = os.path.split(path)
    xname, xext = os.path.splitext(xbase)
    xext = xext[1:]
    return xdir, xname, xext


_get_prefix_from_saved_path_xdict = {}  # Go along with function get_prefix_from_path


def divide_int(i):
    i = int(i)
    if i % 2 == 0:
        return i // 2, i // 2
    else:
        return i // 2, i // 2 + 1


def get_prefix_from_path(path, ext, force=True):
    """
    Example: ext=.pth, "xxx/yyy.pth" => "xxx/yyy"
    If ext=None, any ext name will be removed.
    """
    if path is None:
        return None

    if ext == '':
        return path
    elif ext is None:
        regexp = re.compile(r'(.+)\.[^\.]+')
    else:
        regexp = _get_prefix_from_saved_path_xdict.get(ext, None)
        if regexp is None:
            ext_escape = re.escape(ext)
            regexp = re.compile(r'^(.+)' + ext_escape + '$')
            _get_prefix_from_saved_path_xdict[ext] = regexp

    matcher = regexp.match(path)
    if matcher is None:
        if force:
            raise Exception('Path "%s" is not right!' % path)
        else:
            return path
    prefix = matcher.group(1)
    return prefix


def get_path_from_prefix(xprefix, ext):
    """ Example: ext=.pth, "xxx/yyy" => "xxx/yyy.pth" """
    if xprefix is None:
        return None
    if ext == '':
        return xprefix
    return str(xprefix) + str(ext)


def get_tmp_file_name(path, new_ext=None, tgt_dir=None):
    """
    Generate a temporary file name.

    Example: path=/xxx/yyy/zzz.jpg new_ext=txt tgt_dir=/tmp => /tmp/zzz.txt
    :param path: The path to refer to.
    :param new_ext: The extension name of the temporary file name. If it is None, that will be the extension of "path".
    :param tgt_dir: The direction of the temporary file name. If it is None, that will be the CWD.
    :return:
    """
    arr = os.path.split(path)
    if tgt_dir is None:
        dir = '.'
    else:
        dir = tgt_dir
    name = arr[1]
    arr2 = os.path.splitext(name)
    base = arr2[0]
    if new_ext is None:
        ext = arr2[1]
    else:
        ext = new_ext
    os.makedirs(dir, exist_ok=True)
    result = os.path.join(dir, base + '.tmp.' + ext)
    return result


regexp4filename = re.compile(r'[^a-zA-Z0-9_\-.,;]')  # Go along with function ensure_filename
regexp4filename_no_dash_dot = re.compile(r'[^a-zA-Z0-9_,;]')  # Go along with function ensure_filename


def ensure_filename(name, no_dash_dot=False):
    if no_dash_dot:
        rexexp = regexp4filename_no_dash_dot
    else:
        rexexp = regexp4filename
    name = rexexp.sub('_', name)
    return name


shrink_underscore_regexp = re.compile(r'_+')


def shrink_underscore(input):
    return shrink_underscore_regexp.sub('_', input)


def rand_name_on_now():
    return shrink_underscore(ensure_filename(str(datetime.datetime.now()), no_dash_dot=True))


def get_now_string():
    return '%s; %ld' % (datetime.datetime.now(), time.time_ns())


def get_now_string_short():
    return str(datetime.datetime.now())


def check_np(arr, name):
    print('%s: dtype: %s, shape: %s, nbytes: %d' % (name, arr.dtype, str(arr.shape), arr.nbytes))


def check_np_detailed(arr, name):
    print('min: %.2e,\tmax: %.2e,\tmean: %.2e,\tstd: %.2e,\tdtype: %s,\tshape: %s,\tnbytes: %d,\t%s' % (arr.min(), arr.max(), arr.mean(), arr.std(), arr.dtype, str(arr.shape), arr.nbytes, name))


def rand_color(low=0, high=256):
    return (
        np.random.randint(low, high),
        np.random.randint(low, high),
        np.random.randint(low, high),
    )


def rand_palette(n):
    pallette = np.array([2 ** 25 - 1, 2 ** 15 - 1, 2 ** 21 - 1], dtype=int)
    colors = np.array([pallette * i % 255 for i in range(n)], dtype=np.uint8)
    return colors


IMG_FORMATS = 'bmp', 'dng', 'jpeg', 'jpg', 'mpo', 'png', 'tif', 'tiff', 'webp', 'pfm'  # include image suffixes
VID_FORMATS = 'asf', 'avi', 'gif', 'm4v', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'ts', 'wmv'  # include video suffixes


class MyTimer(object):

    def __init__(self):
        self.time1 = None
        self.time2 = None
        self.duration = None

    def __enter__(self):
        self.time1 = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.time2 = datetime.datetime.now()
        self.duration = self.time2 - self.time1
        print('Duration: %s' % str(self.duration))


def parse_ids_list(list_str):
    indexes = list_str.split(',')
    ids = []
    for idx in indexes:
        try:
            id = int(idx)
            ids.append(id)
        except ValueError:
            pass
    ids = sorted(ids)
    return ids


def remove_tail_newline(line):
    if '\r\n' == line[-2:]:
        return line[:-2]
    elif '\n' == line[-1:]:
        return line[:-1]
    else:
        return line


def long_text_to_block(xm_text: str, xm_width: int) -> str:
    assert isinstance(xm_text, str)
    assert isinstance(xm_width, int)

    xi_len_of_text = len(xm_text)
    xi_n_lines = int(np.ceil(xi_len_of_text / xm_width))
    xi_lines = [xm_text[i * xm_width:(i + 1) * xm_width] for i in range(xi_n_lines)]
    xm_text = '\n'.join(xi_lines)
    return xm_text


def translate_ns(ns):
    ms = ns // 1000
    mili = ms // 1000
    s = mili // 1000
    ms_ = mili % 1000
    dt = datetime.datetime.fromtimestamp(s)
    xstr = dt.strftime('%Y-%m-%d %H:%M:%S')
    return '%s.%03d' % (xstr, ms_)


def translate_s(s):
    dt = datetime.datetime.fromtimestamp(s)
    xstr = dt.strftime('%Y-%m-%d %H:%M:%S')
    return xstr


def delta2milli(delta):
    if delta is None:
        return 0
    d = delta.days
    s = delta.seconds
    m = delta.microseconds
    res = (3600. * 24. * d + s) * 1000. + m / 1000.
    return res


def md5(xstr):
    """https://stackoverflow.com/questions/5297448/how-to-get-md5-sum-of-a-string-using-python"""
    xmd5 = hashlib.md5(xstr.encode('utf-8')).hexdigest()
    return xmd5


def prefix(value, prefix):
    return str(prefix) + str(value)


def is_prefix(value, prefix):
    res = prefix == value[:len(prefix)]
    return res


def suffix(value, suffix):
    return str(value) + str(suffix)


def is_suffix(value, suffix):
    res = suffix == value[-len(suffix):]
    return res


def get_proxy():
    hp = os.environ.get('http_proxy', '')
    hsp = os.environ.get('https_proxy', '')
    HP = os.environ.get('HTTP_PROXY', '')
    HSP = os.environ.get('HTTPS_PROXY', '')
    return hp, hsp, HP, HSP


def turn_off_proxy():
    set_proxy('', '', '', '')


def set_proxy(hp, hsp, HP, HSP):
    os.environ['http_proxy'] = hp
    os.environ['https_proxy'] = hsp
    os.environ['HTTP_PROXY'] = HP
    os.environ['HTTPS_PROXY'] = HSP


def print_log(*cont, **kwargs):
    print(translate_ns(time.time_ns()), *cont, **kwargs)


def tidy_arr_from_f_readlines(arr):
    arr = [x[:-1] if x[-1] == '\n' else x for x in arr]
    return arr


def clone(src):
    dest = copy.deepcopy(src)
    return dest


def check_env(names):
    for name in names:
        print('|%s|=|%s|' % (name, os.environ.get(name, '<None>')))


def uuid():
    xns = time.time_ns()
    xns = '%020d' % xns
    xrand = random.randint(0, 999999)
    xrand = '%06d' % xrand
    xuuid = xns + '_' + xrand
    return xuuid


def ensure_decode_of_str(xbytes):
    xres = xbytes.decode('utf8', 'replace')
    return xres


def to_decode(x, enc='utf8', default=''):
    if x is None:
        return default
    else:
        return x.decode(enc)
    
    
def to_int(x, default=0):
    if x is None:
        return default
    else:
        return int(x)


def encode_set(xset):
    """
    编码集合
    """
    if not xset:
        return ''
    return '|'.join(sorted(xset))


def decode_set(xstr):
    """
    解码编码后的集合。（注意返回是列表。）
    """
    if not xstr:
        return []
    return xstr.split('|')


def list2str_with_limit(xlist, xlimit):
    """
    以xlimit个字符为限制，把列表转字符串。
    """
    assert(isinstance(xlimit, int) and xlimit > 0)
    xstr = ''
    xfirst = True
    for xelement in xlist:
        if len(xstr) + 2 + len(xelement) > xlimit:
            return xstr + '……'
        if xfirst:
            xfirst = False
        else:
            xstr += ', '
        xstr += str(xelement)
    return xstr


def dl2ld(dl):
    """
    https://stackoverflow.com/questions/5558418/list-of-dicts-to-from-dict-of-lists

    :param dl:
    :return:
    """
    # return [dict(zip(dl, t)) for t in zip(*dl.values())]
    return [dict(zip(dl.keys(), t)) for t in zip(*dl.values())]


def ld2dl(ld):
    """
    https://stackoverflow.com/questions/5558418/list-of-dicts-to-from-dict-of-lists

    :param ld:
    :return:
    """
    return {k: [dic[k] for dic in ld] for k in ld[0]}


def glob_dir(xdir):
    paths = glob.glob(f'{xdir}/**', recursive=True)
    paths = sorted(paths)
    return paths

    
def has_content(path: str) -> Tuple[bool, bool]:
    """
    Check if a path exists and has content.
    
    :param path: The path
    :return: (bool, bool)
        bool 01: if the path is a directory.
        bool 02: if the path exists if path is not a directory
                 or if the directory has content
    """
    if not os.path.isdir(path):
        result = os.path.exists(path)
        return False, result
    
    paths = glob_dir(path)
    for p in paths:
        if not os.path.isdir(p):
            return True, True
    return True, False


def is_debug_mode():
    return sys.gettrace() is not None


def find_null_byte(byte_string):
    """
    Finds the position of the first null byte (b'\0') in a byte string.

    Args:
        byte_string: The byte string to search.

    Returns:
        The index of the first null byte, or -1 if no null byte is found.
    """
    try:
        return byte_string.index(b'\0')
    except ValueError:
        return -1
    
    
if '__main__' == __name__:

    def _main():
        print(os.environ['PYTHONPATH'])

        """Unit tests for some routines declared in this file."""
        
        ##############################################################
        # glob_dir
        paths = glob_dir('/home/yunpeng/models/hf/m3e-base')
        print('\n'.join(paths))
        
        sys.exit(0)
        
        ##############################################################
        # get_prefix_from_path and get_path_from_prefix
        # ext = '.pth'
        ext = '/saved_model.pb'
        xpaths = [
            '/aaa/bbb/ccc/weights.100',
            '/aaa/bbb/ccc/weights.100/saved_model.pb',
            '/aaa/bbb/ccc/weights.100.pth',
            '/aaa/bbb/ccc/weights.100.index',
        ]
        for xpath in xpaths:
            sep()
            xprefix = get_prefix_from_path(xpath, ext, False)
            print(xpath, '=>', xprefix)
            xpath = get_path_from_prefix(xprefix, ext)
            print(xprefix, '=>', xpath)

    _main()
    