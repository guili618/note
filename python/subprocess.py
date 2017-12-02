import subprocess
results = subprocess.check_output(
    'ps -ef  | grep java', shell=True)
print(results)

import os
import subprocess
import shlex
proc1 = subprocess.Popen(shlex.split('help(os)'), stdout=subprocess.PIPE)
proc2 = subprocess.Popen(shlex.split('grep walk'), stdin=proc1.stdout,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)

proc1.stdout.close()  # Allow proc1 to receive a SIGPIPE if proc2 exits.
out, err = proc2.communicate()
print('out: {0}'.format(out))
print('err: {0}'.format(err))
