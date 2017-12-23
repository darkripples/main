# coding:utf8
## Some Func About 'Write Log'
## Use: flog or fls_log(log_file)
# 2016/6/7 Add fls_log()

import logging
from .fmt_utils import fmt_date

def _get_msg4log(*args):
    # Get LOG msg
    if len( args ) > 1: msg = args[0] % args[1:]
    elif len( args ) == 1: msg = args[0]
    else: msg = ''
    return msg

class Fls_Log:
    # Write LOG
    def __init__(self, log_filepath = 'fls.log.%s' % fmt_date()[:6]):
        logging.basicConfig(level   = logging.DEBUG,
                    #format   = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    format   = '%(asctime)s %(levelname)s %(message)s',
                    #datefmt = '%a, %d %b %Y %H:%M:%S',
                    filename = log_filepath,
                    filemode = 'a')
    def log_info(self, *args):
        # Write info msg
        logging.info(_get_msg4log(*args))
    
    def log_debug(self, *args):
        # Write debug msg
        logging.debug(_get_msg4log(*args))
    
    def log_warning(self, *args):
        # Write warning msg
        logging.warning(_get_msg4log(*args))
    
    def log_error(self, *args):
        # Write error msg
        logging.error(_get_msg4log(*args))

def fls_log( file_path = 'fls.log.%s' % fmt_date()[:8] ):
    return Fls_Log(file_path)

if __name__ == '__main__':
    # For test:
    #a = fls_log('a.dat')
    a = fls_log( )
    a.log_info('11212')
    a.log_debug('x')
    a.log_warning('11212')
    a.log_error('error:%s','test')
