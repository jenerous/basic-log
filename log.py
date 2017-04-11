#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import localtime
from time import strftime
import sys
import os


def main(args):

    line_length = 80
    log_dir     = '.'

    if args:
        now          = localtime()
        time_string  = strftime('%H:%M:%S', now)
        log_file     = os.path.join(log_dir, '{}.log'.format(strftime('%Y-%m-%d', now)))
        out_text     = ''
        time_prefix  = '[{}]'.format(time_string)
        current_line = time_prefix

        if not os.path.isfile(log_file):
            out_text = '{:=^{l_len}}\n'.format(' ' + strftime('%Y-%m-%d', now) + ' ', l_len=line_length - 2)

        for i, a in enumerate(args):
            if len(current_line) + len(a) + 1 > line_length:
                out_text += current_line + '\n'
                current_line = ' ' * len(time_prefix)
            current_line += ' ' + a

        out_text += current_line + '\n'

        with open(log_file, 'a') as log_out:
            log_out.write(out_text)

    if os.path.isfile(log_file):
        os.system('tail -n 5 {}'.format(log_file))


if __name__ == '__main__':
    main(sys.argv[1:])
