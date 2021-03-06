# coding=utf-8
"""
Copyright (c) 2015 Stefan Braun

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE
AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import unittest

from metrics.hotspot import HotspotAnalyzer, InvalidDataException

INVALID_CSV = "test/analysis/data/invalidHotspot.csv"

VALID_CSV = "test/analysis/data/hotspot.csv"


class TestHotspotAnalyzer(unittest.TestCase):
    """Test cases for hot-spot analyzer."""

    def test_creating_invalid_data_format(self):
        """CSV file with missing required columns ."""
        with self.assertRaises(InvalidDataException):
            HotspotAnalyzer(INVALID_CSV)

    def test_creating_valid_data_format(self):
        """CSV file with missing required columns ."""
        HotspotAnalyzer(VALID_CSV)

    def test_number_of_records_read(self):
        """Read data file with 14 records."""
        hsa = HotspotAnalyzer(VALID_CSV)
        self.assertEqual(14, len(hsa.dta.get_values()))

if __name__ == '__main__':
    unittest.main()
