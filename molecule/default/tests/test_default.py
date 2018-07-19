import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_node_is_existed(host):
    assert host.check_output(
        '~/.nvm/versions/node/v7.8.0/bin/node -v') == 'v7.8.0'
