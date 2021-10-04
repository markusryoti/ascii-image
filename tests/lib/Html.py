import os
import subprocess
import configparser


class Html:
    def remove_old_image(self):
        if os.path.exists("ascii.html"):
            os.remove("ascii.html")

    def create_image(self):
        config = configparser.RawConfigParser()
        config.read('tests/lib/config.cfg')
        conf = dict(config.items('PYTHON'))

        subprocess.run([conf['python'],
                       'ascii.py', 'tests/resources/kitty.jpeg'])

    def image_should_exist(self):
        if not os.path.exists('ascii.html'):
            raise Exception("Image doesn't exist")
