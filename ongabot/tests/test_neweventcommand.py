import unittest
from datetime import date
from handler import neweventcommand

class NewEventCommandTest(unittest.TestCase):
    def setUp(self):
        self.upcomingTestDates = [
            (date(2021, 2, 25), date(2021, 3, 3)),
            (date(2021, 3, 12), date(2021, 3, 17)),
            (date(2021, 3, 17), date(2021, 3, 17)),
            (date(2021, 3, 18), date(2021, 3, 24))]


    def test_getUpcomingWednesdayDate(self):
        for today, expected_next_onga_date in self.upcomingTestDates:
            next_wednesday = neweventcommand.getUpcomingWednesdayDate(today)
            self.assertEqual(next_wednesday.weekday(), 2, 'Wrong day of week. Should be 2 as 0 is monday and 6 is sunday')
            self.assertEqual(next_wednesday, expected_next_onga_date, f'Wrong calculated date! Expected: {expected_next_onga_date}. Actual: {next_wednesday}')

if __name__ == '__main__':
    unittest.main()
