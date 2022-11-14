import json
import os
import typing


class Address(typing.TypedDict):
    street: str
    city: str
    country: str
    postal_code: str


class ResourceCreateData(typing.TypedDict):
    name: str
    phone_number: list[int]
    created_at: str
    email_address: typing.Optional[str]
    address: typing.Optional[Address]


class ResourceData(ResourceCreateData):
    id: int
    updated_at: typing.Optional[str]


class ResourceMeta:
    def __init__(self, file_path: str):
        self.data: dict[str, ResourceData] = {}
        if not os.path.exists(file_path):
            raise Exception("File not found")
        self.path = file_path

    def load(self):
        with open(self.path, 'r') as f:
            self.data = json.load(f)

    def save(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f)

    def __len__(self):
        return len(self.data)


class Resource(ResourceMeta):
    file_path = 'resources.json'

    def __init__(self):
        super().__init__(self.file_path)
        self.load()

    def all(self) -> list[typing.Optional[ResourceData]]:
        return list(self.data.values())

    def get(self, r_id: int) -> tuple[bool, typing.Union[ResourceData, None]]:
        r_id = str(r_id)
        if r_id not in self.data:
            return False, None
        return True, self.data[r_id]

    def create(self, data: ResourceCreateData) -> ResourceData:
        r_id = max([int(k) for k in self.data.keys()]) + 1 if len(self.data) > 0 else 1
        data = ResourceData(id=r_id, **data)
        self.data[str(r_id)] = data
        self.save()
        return data

    def update(self, data: ResourceData) -> ResourceData:
        self.data[data['id']] = data
        self.save()
        return self.data[data['id']]

    def delete(self, data: ResourceData) -> bool:
        del self.data[str(data['id'])]
        self.save()
        return True

    def delete_all(self) -> bool:
        self.data = {}
        self.save()
        return True

    @staticmethod
    def sort(data: list[ResourceData], sorting: str, ordering: str):
        return sorted(data, key=lambda x: x[sorting], reverse=ordering == 'desc')

    @staticmethod
    def search_in_names(data: list[ResourceData], search: str) -> list[typing.Optional[ResourceData]]:
        return [x for x in data if search.lower() in x['name'].lower()]

    @staticmethod
    def search_in_phone_number(data: list[ResourceData], search: str) -> list[typing.Optional[ResourceData]]:
        return [x for x in data if search.lower() in x['phone_number']]
