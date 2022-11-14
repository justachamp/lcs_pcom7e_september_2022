from django.test import TestCase

from .resource import Resource


# Create your tests here.

class FullCycleTestCase(TestCase):
    def setUp(self):
        Resource.file_path = 'resources-test.json'
        Resource().delete_all()
        self.client.post('/create', dict(name='Ayub', phone='1234'))
        self.client.post('/create', dict(name='Ayub1', phone='12345'))
        self.client.post('/create', dict(name='Ayub2', phone='123456'))
        self.resource = Resource()

    def test_create_resource(self):
        # creating first  resource
        self.resource.delete_all()
        self.client.post('/create', dict(name='Ayub', phone='1234'))
        self.resource.load()
        self.assertEqual(len(self.resource.data), 1)
        # creating second  resource
        self.client.post('/create', dict(name='Ayub1', phone='12345'))
        self.resource.load()
        self.assertEqual(len(self.resource.data), 2)
        # should not create duplicate name
        self.client.post('/create', dict(name='Ayub1', phone='1234'))
        self.resource.load()
        self.assertEqual(len(self.resource.data), 2)
        # should not create duplicate phone number
        self.client.post('/create', dict(name='Ayub2', phone='1234'))
        self.resource.load()
        self.assertEqual(len(self.resource.data), 2)

    def test_get_resource(self):
        response = self.client.get('/get/1')
        assert response.status_code == 200
        response = self.client.get('/get/2')
        assert response.status_code == 200
        response = self.client.get('/get/4')
        assert response.status_code == 400

    def test_update_resource(self):
        response = self.client.post('/update/1', dict(name='Ayub', phone='1234'))
        assert response.status_code == 200
        response = self.client.post('/update/1', dict(name='Ayub1', phone='12345'))
        assert response.status_code == 200
        response = self.client.post('/update/2', dict(name='Ayub2', phone='123456'))
        assert response.status_code == 200
        response = self.client.post('/update/2', dict(name='Ayub2', phone='1234'))
        assert response.status_code == 400

    def test_delete_by_id(self):
        response = self.client.get('/delete/1')
        assert response.status_code == 200
        response = self.client.get('/delete/4')
        assert response.status_code == 400

        self.resource.load()
        self.assertEqual(len(self.resource.data), 2)

    def test_delete_all(self):
        response = self.client.get('/delete-all')
        assert response.status_code == 200
        self.resource.load()
        self.assertEqual(len(self.resource.data), 0)

    def test_search(self):
        self.assertEqual(len(self.resource.data), 3)
        response = self.client.get('/?search=Ayub2')
        assert response.status_code == 200
        assert b'Ayub2' in response.content
        response = self.client.get('/?search=Ayub10')
        assert response.status_code == 200
        assert b'Ayub10' not in response.content
