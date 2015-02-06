#!/usr/bin/env python
from charmhelpers.contrib.ansible import AnsibleHooks
from charmhelpers.contrib.ansible import install_ansible_support
from path import path
import sys


def hook_names(here=path(__file__).parent):
    for name in (x.basename() \
                 for x in here.files() if x.islink()):
        yield name


hooks = AnsibleHooks(playbook_path='playbook/main.yml',
                     default_hooks=list(hook_names()))


@hooks.hook('install', 'upgrade-charm')
def install():
    try:
        import ansible
    except ImportError:
        install_ansible_support(from_ppa=True)


if __name__ == "__main__":
    hooks.execute(sys.argv)
