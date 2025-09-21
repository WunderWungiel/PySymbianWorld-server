import os

import yaml

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "config.yml"), "r") as f:
    config = yaml.safe_load(f)
