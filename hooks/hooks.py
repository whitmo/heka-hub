#!/usr/bin/env python
from charmhelpers.contrib.ansible import AnsibleHooks
from charmhelpers.contrib.ansible import install_ansible_support
import sys


hook_names = [
    'install',
    'start',
    'stop',
    'upgrade-charm',
    'config-changed',
    'heka_in-relation-joined',
    'heka_in-relation-changed',
    'logstash_out-relation-joined',
    'logstash_out-relation-changed',
    'schema_out-relation-joined',
    'schema_out-relation-changed',
    'stats_out-relation-joined',
    'stats_out-relation-changed',
]

hooks = AnsibleHooks(playbook_path='playbook/main.yml',
                     default_hooks=hook_names)


@hooks.hook('install', 'upgrade-charm')
def install():
    try:
        import ansible
    except ImportError:
        install_ansible_support(from_ppa=True)


if __name__ == "__main__":
    hooks.execute(sys.argv)
