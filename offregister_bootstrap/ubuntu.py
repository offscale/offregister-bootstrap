from operator import __ge__ as gte
from fabric.operations import run
from offregister_fab_utils.apt import apt_depends
from offregister_fab_utils.misc import merge_funcs, require_os_version, fab_steps
from offregister_fab_utils.ubuntu.hostname import set_hostname


@require_os_version(16.04, op=gte)
def set_hostname0(cache, *args, **kwargs):
    hostname = run('hostname', quiet=True)
    if '.' in hostname:
        set_hostname(hostname.partition('.')[0])
    return {'os_version': cache['os_version']}


@require_os_version(16.04, op=gte)
def motd1(*args, **kwargs):
    apt_depends('landscape-common')


@require_os_version(16.04, op=gte)
def expand_partition2(*args, **kwargs):
    pass


'''from offregister_inline import ubuntu as offregister_inline_ubuntu


@merge_funcs(*fab_steps(offregister_inline_ubuntu))
def be_awesome1(cache, *args, **kwargs):
    return 'awesome', cache['os_version']
'''
