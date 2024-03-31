# -*- coding: utf-8 -*-
from operator import __ge__ as gte

from offregister_fab_utils.apt import apt_depends
from offregister_fab_utils.misc import require_os_version
from offregister_fab_utils.ubuntu.hostname import set_hostname


@require_os_version(16.04, op=gte)
def set_hostname0(c, cache, *args, **kwargs):
    hostname = c.run("hostname", hide=True).stdout
    if "." in hostname:
        set_hostname(c, hostname.partition(".")[0])
    return {"os_version": cache["os_version"]}


@require_os_version(16.04, op=gte)
def motd1(c, *args, **kwargs):
    if c.run("grep -Fqzw 18.10 /etc/lsb-release", warn=True, hide=True).exited != 0:
        apt_depends(c, "landscape-common")


@require_os_version(16.04, op=gte)
def expand_partition2(c, *args, **kwargs):
    pass


"""from offregister_inline import ubuntu as offregister_inline_ubuntu


@merge_funcs(*fab_steps(offregister_inline_ubuntu))
def be_awesome1(cache, *args, **kwargs):
    return 'awesome', cache['os_version']
"""

__all__ = ["set_hostname0", "motd1", "expand_partition2"]
