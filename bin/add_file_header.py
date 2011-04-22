#!/usr/bin/python
import os

header = "#\n# This file is part of the MiniMVC package\n#\n# (c) dreamcraft.ch\n#\n# This source file is subject to the MIT license that is bundled\n# with this source code in the file LICENSE.\n#\n\n"
missing_header = []

for root, dirs, files in os.walk('.'):

    for file in [f for f in files if f.endswith(".py")]:
        f = open(root + '/' + file, "r+")
        try:
            content = f.read()
            if not content.startswith('#'):
                
                f.write(header + content)
                
        finally:
            f.close()
