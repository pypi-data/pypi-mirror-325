import configparser
import os
from PyCmpltrtok.auth.redis import sub_dirs
from PyCmpltrtok.common_file_ops import change_file_mode
from PyCmpltrtok.common import get_dir_name_ext

if '__main__' == __name__:
    
    xdict = {
        'host': 'localhost',
        'port': '6379',
        'passwd': 'passwd',
        # 'None': None,  # TypeError: option values must be string
    }
    config = configparser.ConfigParser()
    for k, v in xdict.items():
        config['DEFAULT'][k] = v
    
    user_dir = os.environ['HOME']
    path = os.path.join(user_dir, '.data', *sub_dirs, f'redis.tpl.ini')
    xdir, _, _ = get_dir_name_ext(path)
    print('Make dir if needed')
    os.makedirs(xdir, exist_ok=True)
    print(f'Dumping to {path}')
    if os.path.exists(path):
        raise Exception(f'The file "{path}" already exists. And this code will not overwrite it. Please check in advance.')
    with open(path, 'w', encoding='utf8') as f:
        config.write(f)
    print('Change mode')
    change_file_mode(path, '0o600')
    print('Dumped')