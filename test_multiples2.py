# -*- coding: utf-8 -*-
"""
Created on Mon Mar 4 21:02:22 2019

@author: Admin
"""

import unittest

from unittest.mock import patch
from multiples2 import multiples_of_five_upto_hundred

class MultiplesTestCase(unittest.TestCase):
    '''
    def test_multiples_of_five_upto_hundred(self):
        expected = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        actual =  multiples_of_five_upto_hundred(51)
        self.assertEqual(actual, expected)        
    
        
    def test_numbers_below_one(self):
        self.assertFalse(multiples_of_five_upto_hundred(0), msg = 'Hey, this number is below zero. Try again later!')
    
    def test_numbers_above_hundred(self):
        self.assertFalse(multiples_of_five_upto_hundred(102), msg = 'Hey, this number is above one hundred. Try again later!')
        
    def test_returns_false_if_input_is_empty(self):
        self.assertFalse(multiples_of_five_upto_hundred(''))

    def test_returns_false_if_input_is_not_numeric(self):
        self.assertFalse(multiples_of_five_upto_hundred("kanumber"), msg = "Please enter a numeric number")
     '''
       
    @patch('multiples2.logging')
    def test_multiples2_logs_error(self, mock_logging):
        multiples_of_five_upto_hundred(1000)
        import pdb;pdb.set_trace()
        self.assertTrue(mock_logging.error.called)
        mock_logging.error.assert_called_with('Enter a nuumber between  2 and 100!')
    
   
     
if __name__ =="__main__":
	unittest.main()

