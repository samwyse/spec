#!/usr/bin/env python

"""Build JSON versions of the specs.

This is a Python implementation of the Ruby Rakefile.
"""

import json, yaml, glob

class Code(yaml.YAMLObject, dict):
    yaml_tag = u'!code'
    def __setstate__(self, state):
        self.update(state, __tag__=self.yaml_tag[1:])

for name_yml in glob.glob('specs/*.yml'):
    with open(name_yml) as input:
        name_json = name_yml[:-3] + 'json'
        with open(name_json, 'w') as output:
            spec = yaml.load(input)
            spec["__ATTN__"] = 'Do not edit this file; changes belong in the appropriate YAML file.'
            json.dump(spec, output, sort_keys=True)
