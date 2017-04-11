#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import localtime
from time import strftime
import sys
import os


def main(args):

    line_length = 80   # max number of symbols to write in each line
    log_dir     = '.'  # log directory

    # create log directory
    if not os.path.isdir:
        os.mkdir(log_dir)
    now         = localtime()
    log_file    = os.path.join(log_dir, '{}.log'.format(strftime('%Y-%m-%d', now)))

    if args:
        # split args into words if it was passed with quotes
        if len(args) == 1:
            args = args[0].split(' ')

        time_string  = strftime('%H:%M:%S', now)
        out_text     = ''
        time_prefix  = '[{}]'.format(time_string)
        current_line = time_prefix

        # create a file for each day
        if not os.path.isfile(log_file):
            out_text = '{:=^{l_len}}\n'.format(' ' + strftime('%Y-%m-%d', now) + ' ', l_len=line_length - 2)

        # split text into lines depending on line_length
        for i, a in enumerate(args):
            if len(current_line) + len(a) + 1 > line_length:
                out_text += current_line + '\n'
                current_line = ' ' * len(time_prefix)
            current_line += ' ' + a

        out_text += current_line + '\n'

        # write text to logfile
        with open(log_file, 'a') as log_out:
            log_out.write(out_text)

    # show the last 5 entries in the current log file
    if os.path.isfile(log_file):
        os.system('tail -n 5 {}'.format(log_file))


if __name__ == '__main__':
    main(sys.argv[1:])

