#!/usr/bin/env python3
from random import randint

import numpy as np

values = [randint(0, 90000) for p in range(0, 120)]

values_series = np.array(values)

mean = np.mean(values_series, axis=0)
standard_d = np.std(values_series, axis=0)

new_data = [x for x in values if (x > mean - 2 * standard_d)]
new_data = [x for x in new_data if (x < mean + 2 * standard_d)]

print(sorted(new_data))
