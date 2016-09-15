import sys
sys.path.append("..")
import microflask

from unittest import TestCase, main

class BasicTestCase(TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Halo, Bandung!')

if __name__ == '__main__':
    main()