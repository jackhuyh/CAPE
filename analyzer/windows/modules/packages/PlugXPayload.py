# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import os
import shutil
import logging

from lib.common.abstracts import Package

log = logging.getLogger(__name__)

class PlugXPayload(Package):
    """DLL analysis package."""
    #PATHS = [
    #    ("SystemRoot", "system32"),
    #]

    def start(self, path):
        loaderpath = "bin\\loader.exe"
        #arguments = path
        arguments = "plugx " + path
        
        # we need to move out of the analyzer directory
        # due to a check in monitor dll
        basepath = os.path.dirname(path)
        newpath = os.path.join(basepath, os.path.basename(loaderpath))
        shutil.copy(loaderpath, newpath)
               
        log.info("[-] newpath : "+newpath)
        log.info("[-] arguments : "+arguments)
        #log.info("[-] Path: "+path)

        return self.execute(newpath, arguments, newpath)
