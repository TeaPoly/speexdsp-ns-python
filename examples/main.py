#!/usr/bin/env python3
# Copyright 2022 Lucky Wong
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

"""Acoustic Noise Suppression for wav files.

Modified from https://github.com/xiongyihui/speexdsp-python
"""

import wave
import sys
from speexdsp_ns import NoiseSuppression


if len(sys.argv) < 3:
    print('Usage: {} near.wav out.wav'.format(sys.argv[0]))
    sys.exit(1)


frame_size = 256

near = wave.open(sys.argv[1], 'rb')

if near.getnchannels() > 1:
    print('Only support mono channel')
    sys.exit(2)

out = wave.open(sys.argv[2], 'wb')
out.setnchannels(near.getnchannels())
out.setsampwidth(near.getsampwidth())
out.setframerate(near.getframerate())


print('near - rate: {}, channels: {}, length: {}'.format(
        near.getframerate(),
        near.getnchannels(),
        near.getnframes() / near.getframerate()))

noise_suppression = NoiseSuppression.create(frame_size, near.getframerate())

in_data_len = frame_size
in_data_bytes = frame_size * 2

while True:
    in_data = near.readframes(in_data_len)
    if len(in_data) != in_data_bytes:
        break

    in_data = noise_suppression.process(in_data)

    out.writeframes(in_data)

near.close()
out.close()
