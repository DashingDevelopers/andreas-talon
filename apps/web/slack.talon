app: slack
-

edit last:               key(ctrl-up)
edit:                    key(e)

sidebar (show | hide):   key(ctrl-shift-d)
panel (show | hide):     key(ctrl-.)

all unreads:             key(ctrl-shift-a)
jump to:                 key(ctrl-k)
direct messages:         key(ctrl-shift-k)
please [<user.text>]$:
    key(ctrl-k)
    sleep(100ms)
    edit.delete()
    sleep(100ms)
    "{text or ''}"

channel prev:            key(alt-up)
channel next:            key(alt-down)
channel unread prev:     key(alt-shift-up)
channel unread [next]:   key(alt-shift-down)
next unread:             key(alt-shift-down)

format code:             key(ctrl-shift-c)
format code block:       key(ctrl-alt-shift-c)
format quote:            key(ctrl-shift-9)