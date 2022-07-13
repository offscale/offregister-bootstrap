from offregister_fab_utils.apt import apt_depends


def set_hostname0(c, cache, *args, **kwargs):
    """
    Set the hostname to original hostname sans everything following first `.`

    :param c: Connection
    :type c: ```fabric.connection.Connection```

    :param cache: Cache dict var, persisted throughout all tasks, to share state
    :type cache: ```dict```

    :return: {"os_version": os_version}
    :rtype: ```dict```
    """
    apt_depends(c, "base-files")
    hostname = c.run("hostname", hide=True)
    first_dot = hostname.stdout.find(".")
    if first_dot != -1:
        apt_depends(c, "systemd")
        c.sudo("hostnamectl set-hostname {}".format(hostname[:first_dot]))
    return {"os_version": cache["os_version"]}


__all__ = ["set_hostname0"]
