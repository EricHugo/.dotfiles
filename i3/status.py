#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os

from i3pystatus import Status

green="#98c379"
red="#e06c75"
yellow="#d19a66"

status = Status(standalone=True, click_events=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
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
    w = int(d[0])
    return f'{" " if w < 10 else ""}{w}W {d[1]}ºC'

status.register("file",
        interval=1,
        components={ "gpu": (gpu_monitor, "/run/crom/gpu-monitor"), },
        format="GPU {gpu}")

def auto_rgb():
    res="0" if os.system("xset -q | grep 'Monitor is On' > /dev/null") == 0 else "1"
    open("/run/crom/rgb-off", "w").write(str(res))

def case_monitor(s):
    auto_rgb()
    d=s.split(' ')
    return f'{d[0]}% {d[1]}% {d[2]}% {d[3]}x'

def cpu_monitor(s):
    d=s.split(' ')
    return f'{d[0]} MHz {d[1]}ºC'

status.register("file",
        interval=1,
        components={ "cpu": (cpu_monitor, "/run/crom/cpu-monitor"), },
        format="{cpu}")

# status.register("cpu_usage_graph",
#     format="CPU {usage:2}",
#     start_color=green,
#     end_color=green
# )

status.register("cpu_usage_bar",
    format="{usage_bar_cpu0}{usage_bar_cpu1}{usage_bar_cpu2}{usage_bar_cpu3}{usage_bar_cpu4}{usage_bar_cpu5}{usage_bar_cpu6}{usage_bar_cpu7}{usage_bar_cpu8}{usage_bar_cpu9}{usage_bar_cpu10}{usage_bar_cpu11}{usage_bar_cpu12}{usage_bar_cpu13}{usage_bar_cpu14}{usage_bar_cpu15}{usage_bar_cpu16}{usage_bar_cpu17}{usage_bar_cpu18}{usage_bar_cpu19}{usage_bar_cpu20}{usage_bar_cpu21}{usage_bar_cpu22}{usage_bar_cpu23}{usage_bar_cpu24}{usage_bar_cpu25}{usage_bar_cpu26}{usage_bar_cpu27}{usage_bar_cpu28}{usage_bar_cpu29}{usage_bar_cpu30}{usage_bar_cpu31}",
    bar_type="vertical",
    start_color=green,
    end_color=red
)

# Shows pulseaudio default sink volume
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    format="{volume} ♪",)

status.register("network",
    interface="enp7s0",
    format_up="{interface} {bytes_sent} k↑ {bytes_recv} k↓",
    format_down="X",
    dynamic_color = True,
    start_color=green,
    end_color=yellow,
    color_down=red,
)

status.run()
