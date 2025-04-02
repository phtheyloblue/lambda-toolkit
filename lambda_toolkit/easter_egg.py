
# Standard library imports
import signal

GARFIELD_ASCII = """
              --      --           Z
            .:"  | .:'" |      Z
          --  ___   ___  -        Z
        /:.  /___\ /___\ .\\
       |:|. ;\___/O\___/  :|
       |:|. |  `__|__'  | .|
       |:|.  \_,     ,_/  /
        \______       |__/
         |:.           \\
        /.:,|  |        \\
       /.:,.|  |         \\
       |::.. \_;_\-;       |
 _____|::..    .::|       |
/   ----,     .::/__,    /__,
\_______|,...____;_;_|../_;_|

Sometimes laziness is the best option!
"""

CROWBAR_ASCII ="""
      _______
     /      /\\
    /      / /
   /      / /
  /      / /
 /      / /
(======| /
 \      \\ \\
  \______\\ \\

"Oh, and before I forget, I think you dropped this back in Black Mesa!"
 - Barney Calhoun
"""

class TimeoutException(Exception):
    pass

DEFAULT_TIMEOUT_SECONDS = 3

def timeout_handler(signum, frame):
    raise TimeoutException("Error 504: Infinite recursion detected.")

def with_timeout(func, *args, seconds=DEFAULT_TIMEOUT_SECONDS, **kwargs):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(seconds)
    try:
        result = func(*args, **kwargs)
        signal.alarm(0)
        return result
    except TimeoutException as e:
        print(f"\n{e}")
        print(GARFIELD_ASCII)
        return None
    finally:
        signal.alarm(0)
