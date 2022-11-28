import json
import os
import typing


# Type hinting for the income data
class ResourceCreateData(typing.TypedDict):
    name: str
    phone: int
    created: str
    email: typing.Optional[str]


class ResourceData(ResourceCreateData):
    id: int
    updated: typing.Optional[str]


# class to work with loading and dumping data into file in json format
class ResourceMeta:
    def __init__(self, file_path: str):
        self.data: dict[str, ResourceData] = {}
        if not os.path.exists(file_path):
            raise Exception("File not found")
        self.path = file_path

    def load(self):
        """ Read stored data from resources.json file"""
        with open(self.path, 'r') as f:
            self.data = json.load(f)

    def save(self):
        """ Save data into resources.json file """
        with open(self.path, 'w') as f:
            json.dump(self.data, f)

    def __len__(self):
        """ Get total count of contacts stored."""
        return len(self.data)


# class which has crud, sorting and search methods
class Resource(ResourceMeta):
    file_path = 'resources.json'

    def __init__(self):
        super().__init__(self.file_path)
        self.load()

    def all(self) -> list[typing.Optional[ResourceData]]:
        """ Get all contacts """
        return list(self.data.values())

    def get(self, r_id: int) -> tuple[bool, typing.Union[ResourceData, None]]:
        """ Get contact by id"""
        r_id = str(r_id)
        if r_id not in self.data:
            return False, None
        return True, self.data[r_id]

    def create(self, data: ResourceCreateData) -> ResourceData:
        """ Create new contact"""
        r_id = 1 if len(self.data) == 0 else len(self.data) + 1
        data = ResourceData(id=r_id, **data)
        self.data[str(r_id)] = data
        self.save()
        return data

    def update(self, data: ResourceData) -> ResourceData:
        """ Update existing contact by id"""
        self.data[str(data['id'])] = data
        self.save()
        return self.data[str(data['id'])]

    def delete(self, contact_id: int) -> bool:
        """ Delete existing contact by id"""
        contact_id = str(contact_id)
        del self.data[contact_id]
        self.save()
        return True

    def delete_all(self) -> bool:
        """ Delete all contacts books"""
        self.data = {}
        self.save()
        return True

    @staticmethod
    def sort(data: list[ResourceData], sorting: str, ordering: typing.Literal['asc', 'desc']):
        """ Sort contacts by name, created, updated and order by asc or desc"""
        return sorted(data, key=lambda x: x[sorting], reverse=ordering == 'desc')

    @staticmethod
    def search_in_names(data: list[ResourceData], search: str) -> list[ResourceData]:
        """ Search in name"""
        return [x for x in data if search.lower() in x['name'].lower()]

    @staticmethod
    def search_in_phone_number(data: list[ResourceData], search: str) -> list[ResourceData]:
        """ Search in phone number"""
        return [x for x in data if search in str(x['phone'])]
