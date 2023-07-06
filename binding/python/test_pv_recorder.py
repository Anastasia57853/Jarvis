#
#    Copyright 2023 Picovoice Inc.
#
#    You may not use this file except in compliance with the license. A copy of the license is located in the "LICENSE"
#    file accompanying this source.
#
#    Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
#    an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
#    specific language governing permissions and limitations under the License.
#

import unittest

from _pvrecorder import *


class PvLeopardTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        PvRecorder.set_default_library_path('../..')

    def test_invalid_device_index(self):
        with self.assertRaises(ValueError):
            _ = PvRecorder(-2, 512)

    def test_invalid_frame_length(self):
        with self.assertRaises(ValueError):
            _ = PvRecorder(0, -1)

    def test_invalid_buffered_frame_count(self):
        with self.assertRaises(ValueError):
            _ = PvRecorder(0, 512, 0)

    def test_start_stop(self):
        recorder = PvRecorder(0, 512)
        recorder.start()
        for i in range(5):
            frame = recorder.read()
            self.assertEqual(len(frame), 512)
        recorder.stop()
        recorder.delete()

    def test_set_debug_logging(self):
        recorder = PvRecorder(0, 512)
        recorder.set_debug_logging(True)
        recorder.set_debug_logging(False)
        self.assertIsNotNone(recorder)
        recorder.delete()

    def test_selected_device(self):
        recorder = PvRecorder(0, 512)
        device = recorder.selected_device
        self.assertIsNotNone(device)
        self.assertIsInstance(device, str)
        recorder.delete()

    def test_get_available_devices(self):
        recorder = PvRecorder(0, 512)
        devices = recorder.get_available_devices()
        self.assertIsNotNone(devices)
        for device in devices:
            self.assertIsNotNone(device)
            self.assertIsInstance(device, str)
        recorder.delete()

    def test_version(self):
        recorder = PvRecorder(0, 512)
        version = recorder.version
        self.assertGreater(len(version), 0)
        self.assertIsInstance(version, str)
        recorder.delete()

    def test_sample_rate(self):
        recorder = PvRecorder(0, 512)
        sample_rate = recorder.sample_rate
        self.assertGreater(sample_rate, 0)
        self.assertIsInstance(sample_rate, int)
        recorder.delete()


if __name__ == '__main__':
    unittest.main()
