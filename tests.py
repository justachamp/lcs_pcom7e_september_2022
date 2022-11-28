from datetime import datetime as dt

from resource import Resource, ResourceCreateData


class FullCycleTestCase:
    def __init__(self):
        # while testing change file path to test source and clear content of file.
        Resource.file_path = 'resources-test.json'
        Resource().delete_all()
        self.resource = Resource()

    def test_all(self):
        """All test functions in correct order"""
        print('Stating testing')
        print('Testing Creation of records')
        self.test_create_resource()
        print('Testing Retrieval of records')
        self.test_get_resource()
        print('Testing Search of records')
        self.test_search()
        print('Testing Updates on records')
        self.test_update_resource()
        print('Testing Deletion of records')
        self.test_delete_by_id()
        self.test_delete_all()
        print('Finished Testing all test cases succeeded')

    def test_create_resource(self):
        """Create some resources"""
        # creating first  resource
        c1 = ResourceCreateData(name='Contact', phone=1234, email='em@google.com', created=dt.now().isoformat())
        self.resource.create(c1)
        c1_found, c1_data = self.resource.get(1)
        assert c1_found
        assert c1_data['name'] == 'Contact'
        assert c1_data['phone'] == 1234
        assert c1_data['email'] == 'em@google.com'
        # create one more resource
        c2 = ResourceCreateData(name='2 Contact', phone=12345, email='emg@google.com', created=dt.now().isoformat())
        self.resource.create(c2)
        c2_found, c2_data = self.resource.get(2)
        assert c2_found
        assert c2_data['name'] == '2 Contact'
        assert c2_data['phone'] == 12345
        assert c2_data['email'] == 'emg@google.com'

    def test_get_resource(self):
        """Test retrieving of a record by id"""
        c2_found, c2_data = self.resource.get(2)
        assert c2_found
        assert c2_data['name'] == '2 Contact'
        assert c2_data['phone'] == 12345
        assert c2_data['email'] == 'emg@google.com'

    def test_update_resource(self):
        """Updating record fields of 1"""
        c2_found, c2_data = self.resource.get(1)
        assert c2_found
        c2_data['name'] = 'Contact 23'
        c2_data['phone'] = 12345554
        c2_data['email'] = 'em@google.com'
        c2_data['updated'] = dt.now().isoformat()

        self.resource.update(c2_data)

    def test_delete_by_id(self):
        """Number of records should be decreased by 1"""
        assert len(self.resource) == 2
        self.resource.delete(1)
        assert len(self.resource) == 1
        c2_found, c2_data = self.resource.get(2)
        assert c2_found
        assert c2_data['name'] == '2 Contact'
        assert c2_data['phone'] == 12345
        assert c2_data['email'] == 'emg@google.com'

    def test_delete_all(self):
        """There should be at least 1 record and after executing the operation the number of records should be 0"""
        assert len(self.resource) >= 1
        self.resource.delete_all()
        assert len(self.resource) == 0

    def test_search(self):
        result = self.resource.search_in_names(self.resource.data.values(), 'Con')
        assert len(result) == 2
        result = self.resource.search_in_names(self.resource.data.values(), '2 Con')
        assert len(result) == 1
        assert result[0]['id'] == 2
        result = self.resource.search_in_phone_number(self.resource.data.values(), '5')
        assert len(result) == 1
        assert result[0]['id'] == 2
        result = self.resource.search_in_phone_number(self.resource.data.values(), '4')
        assert len(result) == 2


if __name__ == '__main__':
    test = FullCycleTestCase()
    test.test_all()
