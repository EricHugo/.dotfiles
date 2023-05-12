#!/usr/bin/env python

import sys
import datetime
import re
import os
from pathlib import Path, PurePath

DATEFMT = "%m%d"
TODAY = datetime.datetime.strftime(datetime.date.today(), DATEFMT)
USERPATH = Path("~").expanduser()
TODODIR = "TODO"
TODOPATH = USERPATH.joinpath(TODODIR)


def get_unfinised_tasks(file):
    unfinished = "-> [ ]"
    with open(file) as f:
        for line in f:
            matched = re.match("\s*" + re.escape(unfinished), line)
            if matched:
                print(line)
                yield line
    return

def rotate_TODO(new_todo, old_todo):
    with open(new_todo, "w+") as new_f:
        for each in get_unfinised_tasks(old_todo):
            print(each)
            new_f.write(each)
    return

if __name__ == "__main__":
    #  task = sys.argv[1]
    os.chdir(TODOPATH)
    todo_files = list(TODOPATH.glob("*.chk"))
    print(todo_files)
    if len(todo_files) > 1:
        sys.exit(1)
    for each in todo_files:
        print(each)
        rotate_TODO("test.todo", each)
