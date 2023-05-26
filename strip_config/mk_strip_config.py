#!/usr/bin/env python3

num_led_strips = 19
num_leds_per_strip = 300

v_step = 1 / num_leds_per_strip
h_step = 1 / num_led_strips

file_name_prefix = "led_strip_config"

current_h_step = 0
for x in range(1,num_led_strips + 1):
    current_v_step = 1
    strip_data = list()
    h_data = '"hmin": %1.2f, "hmax": %1.2f' % (current_h_step, current_h_step + h_step)
    for v in reversed(range(1, num_leds_per_strip +1)):
        v_data = '"vmax": %1.4f, "vmin": %1.4f' % (current_v_step, current_v_step - v_step)
        strip_data.append("{%s, %s}" % (h_data, v_data))
        current_v_step -= v_step

    with open(f"{file_name_prefix}_%02d" % x, 'w') as f:
        f.write("[\n" + ',\n'.join(strip_data) + "\n]")
    current_h_step += h_step
