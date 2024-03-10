#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import psutil
import netifaces

from i3pystatus import Status

green="#98c379"
red="#e06c75"
yellow="#d19a66"

cores = psutil.cpu_count()
usage_bar_strings = ["{usage_bar_cpu" + str(i) + "}" for i in range(cores)]
usage_bar_string = "".join(usage_bar_strings)
nf = netifaces.gateways()
gw = nf['default'][netifaces.AF_INET][1]

status = Status(standalone=True)

# Tue 30 Jul 11:59:46 PM KW31
# status.register("clock", format = [ ('%a %b %-d %b %X', 'UTC'), ("%a %-d %b %R", "%X") ])
    # format="%a %-d %b %R",)
status.register("clock", format = ("%H:%M ", "Europe/Paris"))
# status.register("clock", format = ("%H:%M"))
# status.register("clock", format = ("%a %-d %b %R", "Asia/Singapore"))
    # format="%a %-d %b %R",)


# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load",
    format="LOAD {avg1}")

status.register("swap",
    format="SWP {percent_used}%",
    color="#aaaaaa"
)

status.register("mem",
    format="MEM {percent_used_mem}%",
    color="#aaaaaa",
    warn_percentage=80,
    alert_percentage=90)

def gpu_monitor(s):
    d=s.split(' ')
    try:
        w = int(d[0])
    except ValueError:
        w = 0
    try:
        d[1]
    except IndexError:
        d.append("0")
        d.append("0")
    return f'{" " if w < 10 else ""}{w}W {d[1]}ºC'

status.register("file",
        interval=1,
        components={ "gpu": (gpu_monitor, "/run/crom/gpu-monitor"), },
        format="GPU {gpu}")

def cpu_monitor(s):
    d=s.split(' ')
    clocks = d[0].split('-')
    min_c = int(clocks[0])
    # two spaces as one int in font is about two spaces wide
    return f'{"  " if min_c < 1000 else ""}{min_c}-{clocks[1]} MHz {d[1]}ºC'

status.register("file",
        interval=1,
        components={ "cpu": (cpu_monitor, "/run/crom/cpu-monitor"), },
        format="{cpu}")


status.register("cpu_usage_bar",
    format=usage_bar_string,
    bar_type="vertical",
    start_color=green,
    end_color=red
)

# Shows pulseaudio default sink volume
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    format="{volume} ♪",)

status.register("network",
    interface=gw,
    format_up="{interface} {bytes_sent} k↑ {bytes_recv} k↓",
    format_down="X",
    dynamic_color = True,
    start_color=green,
    end_color=yellow,
    color_down=red,
)

status.run()
