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

import os.path
import pandas as pd
import matplotlib.pyplot as plt


class InvalidDataException(Exception):
    """Data validation failed."""
    pass


class HotspotAnalyzer(object):
    """Perform a hot-spot analysis on a data set.

    The data set is expected as path to a csv file with - at least - following columns:
    * module - the file
    * revisions - number of revisions
    * code - number of code lines
    """

    def __init__(self, data_file_path: str):
        """Initialize the analyzer with the given data set.

        Parameters:

        :param data_file_path: path to csv file [module,revisions,code].
        """
        super().__init__()
        self.expected_columns = {"module", "revisions", "code"}
        self.path = data_file_path
        self.dta = self.__read_csv()
        self.__validate_data()

    def __read_csv(self):
        """Read csv file data.

            :return: data frame.
            :rtype: pd.DataFrame
            """
        dta = pd.read_csv(self.path)
        return dta

    def __validate_data(self):
        """Validate required columns.
        :raise InvalidDataException: in case of missing columns.
        """
        if not self.expected_columns.issubset(self.dta.columns):
            raise InvalidDataException("Required columns missing: {}".format(self.expected_columns))

    def plot_revisions_vs_lines_of_code(self):
        """Plot data."""
        fig = plt.figure(figsize=(15, 8))
        fig_line = fig.add_subplot(2, 1, 1)
        cdf = self.dta
        cdf.plot(kind='scatter', x='code', y='revisions',
                 title='revisions over lines of code',
                 color='b', ax=fig_line)
        #plt.show()
        # TODO provide method for plot and one for save
        pth = os.path.join(os.path.dirname(self.path), 'loc_vs_revs.png')
        plt.savefig(pth)
        plt.close()
