#!/usr/bin/env python

import unittest
from bs4 import BeautifulSoup
import urllib2
import time


class TestACIFlask(unittest.TestCase):

    def test_health_score_range(self):
        link = urllib2.urlopen("http://localhost:5000/date")
        Html = link.read()
        link.close()

        u_date = time.strftime("%d/%m/%Y")

        soup = BeautifulSoup(Html,"lxml")
        cdate = soup.find('div',{'class':'date'}).text

        print cdate
        self.assertTrue(cdate == u_date)


if __name__ == '__main__':
    unittest.main()

