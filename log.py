#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import localtime
from time import strftime
from glob import glob
import sys
import os


def get_file_len(fname):
    with open(fname, 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def main(args):

    line_length = 80   # max number of symbols to write in each line
    log_dir     = '.'  # log directory
    show_lines  = 5    # last x lines to show

    # create log directory
    if not os.path.isdir(log_dir):
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

    # show the last x lines in the current or last existing log file
    view_file = log_file

    if os.path.isfile(log_file):
        print 'Log of today:'
    else:
        # get old log files and sort them by time
        old_logs = glob(os.path.join(log_dir, '*.log'))
        old_logs.sort(key=os.path.getmtime)

        if old_logs:
            print 'Last log found:'
            view_file = old_logs[-1]

    if os.path.isfile(view_file):
        # check if there are more than x lines
        file_len = get_file_len(view_file)

        if file_len > show_lines:
            os.system('head -n 1 {}'.format(view_file))
        os.system('tail -n {} {}'.format(show_lines, view_file))


if __name__ == '__main__':
    main(sys.argv[1:])
