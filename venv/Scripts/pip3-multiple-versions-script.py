#!C:\Users\ACOHEN\PycharmProjects\chinesePoker\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip3-multiple-versions==0.2.2','console_scripts','pip3-multiple-versions'
__requires__ = 'pip3-multiple-versions==0.2.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip3-multiple-versions==0.2.2', 'console_scripts', 'pip3-multiple-versions')()
    )
