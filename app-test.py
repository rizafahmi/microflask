from app import app, mongo

from unittest import TestCase, main

class BasicTestCase(TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Halo, Bandung!')

    def test_404(self):
        tester = app.test_client(self)
        response = tester.get('/404', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_database(self):
        """ Test database connections """
        with app.app_context():
            tester = mongo.db.posts.find({})
            self.assertEqual(str(type(tester)), "<class 'pymongo.cursor.Cursor'>")

if __name__ == '__main__':
    main()
