# license: CC0
import os
import sys
from urllib.parse import quote_plus

Basedirs = set()

def _other_url(_url):
    url = "https://s3.amazonaws.com/repo.mongodb.org?list-type=2"
    url += "&prefix=" + quote_plus("/".join(_url.split("/")[3:]))
    url += "&delimiter=" + quote_plus("/")
    return url


def main():
    basedirs = set()
    for line in sys.stdin:
        path = os.path.dirname(line.strip())
        basedirs.add(path.replace("s3.amazonaws.com/", ""))
    for basedir in basedirs:
        Basedirs.add(basedir)
        paths = basedir.replace("https://repo.mongodb.org/", "")
        paths = paths.split("/")
        for i in range(1, len(paths)):
            Basedirs.add("https://repo.mongodb.org/" + "/".join(paths[:i]) + "/")
        Basedirs.add("https://repo.mongodb.org/" + "/".join(paths) + "/")

    print("\n".join(Basedirs))
    for basedir in Basedirs:
        print(_other_url(basedir))


if __name__ == "__main__":
    main()
