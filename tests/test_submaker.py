import unittest
import os.path
from app.SubMaker import submaker


class Tests(unittest.TestCase):
    def setUp(self):
        self.xml = '''<?xml version="1.0" encoding="utf-8" ?>
                 <transcript>
                 <text start="8.58" dur="3.889">Hello</text>
                 </transcript>'''

    def test_crated_empty_time(self):
        sub = submaker.SubMaker()
        self.assertEqual('00:00:00,000 --> 00:00:00,000\n',
                            sub.generate_time(0, 0))

    def test_crated_time(self):
        sub = submaker.SubMaker()
        self.assertEqual('00:00:08,580 --> 00:00:12,469\n',
                        sub.generate_time(8.58, 3.889))

    def test_generated_subs(self):
        sub = submaker.SubMaker()
        ret = sub.fromstring(self.xml)
        sub_list = ['1\n', '00:00:08,580 --> 00:00:12,469\n', 'Hello\n', '\n']
        self.assertEqual(4, len(ret))
        self.assertEqual(sub_list, ret)

    def test_srt_file_is_created(self):
        sub = submaker.SubMaker()
        ret = sub.fromstring(self.xml)
        sub.tofile()
        self.assertTrue(os.path.isfile('sub.srt'))


if __name__ == '__main__':
    unittest.main()
