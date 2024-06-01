import sys

import osmium

DOWNLOAD_AT = "https://wiki.openstreetmap.org/wiki/Downloading_data#All_data_at_once"

class NamesHandler(osmium.SimpleHandler):
    def node(self, n):
        if 'website' in n.tags:
            print(n.tags['website'])

def main(pnfile):
    NamesHandler().apply_file(pnfile)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} file.osm.pbf")
        print(f"See {DOWNLOAD_AT}")
