# basic-log
quickly log a thought 

## Install (command line)
Clone repo.
```bash
git clone https://github.com/jhertfe/basic-log.git
cd basic-log
```

Adapt log.py to your needs with a text editor of your choice
```python
line_length = 80                         # max number of symbols to write in each line
log_dir     = '/place/to/store/logs/in'  # log directory
show_lines  = 5                          # last x lines to show
```

copy log.py to a folder which is in PATH variable and make it executeable
```bash
cp log.py $HOME/bin/log  # just an example directory!
chmod 750 $HOME/bin/log
```
**Hint PATH**

PATH variable can be shown by
```bash
echo $PATH
```


## Usage
hit log and what ever you want to remember to the commandline

```bash
log "Oh that's important. I should write it down!"
```
## Preview
```
Log of today:
================================= 2017-04-12 =================================
[10:22:16] Oh that's important. I should write it down!
[10:24:26] Found some cool stuff on https://github.com/jhertfe/basic-log/. Check
           this out later
```
