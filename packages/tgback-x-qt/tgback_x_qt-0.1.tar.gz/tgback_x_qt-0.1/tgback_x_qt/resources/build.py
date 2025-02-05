#!/usr/bin/env python3

from pathlib import Path
from subprocess import check_call

ABSPATH = Path(__file__).parent.absolute()
BUILD_P = ABSPATH / '_build'

BUILD_P.mkdir(exist_ok=True)

for file in ABSPATH.iterdir():
    if str(file).endswith('.qrc'):
        outf = str(BUILD_P / file.name.rstrip('.qrc')) + '_rc.py'
        file = str(file.absolute())

        print(f'Building {file}\n\tto {outf}')
        check_call(['pyside6-rcc', file, '-o', outf])
