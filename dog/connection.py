def check(name , ports, timeout = None, ips = None):

    problems = []

    if not ips:
        ips = [name]

    if timeout:
        timeout = timeout

    if not isinstance(ports, list):
        ports = [ports]

    chk_con_res = __salt__['connection.check'](ips, ports, timeout)
    flag = False

    for key in chk_con_res.keys():
           val = chk_con_res[key]

           if isinstance(val, dict):
              for sub_key in val.keys():

                  if not isinstance(val[sub_key], bool):
                     problems.append('%s:%s %s' %(key, sub_key, val[sub_key]))

           elif isinstance(val, str):
               flag = True
               problems.append('%s %s' %(key, val))

    if problems:
        return {'name': name,
               'changes': {},
               'result': False,
               'comment': ' \n'.join(problems)}

