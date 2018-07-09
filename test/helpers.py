# -*- coding: utf-8 -*-
#
import os
import requests
import shutil
import hashlib


def download_image(name, sha3):
    filename = os.path.join("/tmp", name)
    if not os.path.exists(filename):
        print("Downloading {}...".format(name))
        url = "https://github.com/nschloe/epicycler/raw/gh-pages/"
        r = requests.get(url + name, stream=True)
        if not r.ok:
            raise RuntimeError(
                "Download error ({}, return code {}).".format(r.url, r.status_code)
            )
        # save the mesh in /tmp
        with open(filename, "wb") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

    # check hash
    file_sha3 = hashlib.sha3_224(open(filename, "rb").read()).hexdigest()

    if file_sha3 != sha3:
        raise RuntimeError("Checksums not matching ({} != {}).".format(file_sha3, sha3))

    return filename
