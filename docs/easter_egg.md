# Easter Egg (Garfield Timeout)

To protect against infinite expansion in **eager evaluation**, this module introduces a timeout system.

## Components

### `with_timeout(func, *args, seconds=3)`
- Runs `func` with a max runtime.
- Displays error and ASCII Garfield on timeout.

### `TimeoutException`
- Raised when the time limit is exceeded.

### Garfield Output

```

              --      --           Z
            .:"  | .:'" |      Z
          --  ___   ___  -        Z
        /:.  /___\ /___\ .\
       |:|. ;\___/O\___/  :|
       |:|. |  `__|__'  | .|
       |:|.  \_,     ,_/  /
        \______       |__/
         |:.           \
        /.:,|  |        \
       /.:,.|  |         \
       |::.. \_;_\-;       |
 _____|::..    .::|       |
/   ----,     .::/__,    /__,
\_______|,...____;_;_|../_;_|

Sometimes laziness is the best option!

```

Use this only for non-lazy fallback or debugging infinite reduction.

---


---

## 🔨 Crowbar (Half-Life)

```bash
lambda-toolkit crowbar
```

Outputs a Half-Life-inspired ASCII crowbar, a nod to Gordon Freeman.

For core CLI routing, see [index.md](index.md).
