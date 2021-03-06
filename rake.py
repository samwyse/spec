#!/usr/bin/env python

"""Build JSON versions of the specs.

This is a Python implementation of the Ruby Rakefile.
"""

import glob, json, os, yaml

class Code(yaml.YAMLObject, dict):
    yaml_tag = u'!code'
    def __setstate__(self, state):
        self.update(state, __tag__=self.yaml_tag[1:])

for name_yml in glob.glob('specs/*.yml'):
    stat_yml = os.stat(name_yml)
    name_json = name_yml[:-3] + 'json'
    try:
        stat_json = os.stat(name_json)
    except:
        pass
    else:
        if stat_yml.st_mtime == stat_json.st_mtime:
            continue
    with open(name_yml) as input:
        with open(name_json, 'w') as output:
            spec = yaml.load(input)
            spec["__ATTN__"] = 'Do not edit this file; changes belong in the appropriate YAML file.'
            json.dump(spec, output, sort_keys=True)
    os.utime(name_json, (stat_yml.st_mtime, stat_yml.st_mtime))
