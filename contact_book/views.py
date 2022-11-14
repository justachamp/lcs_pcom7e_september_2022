# Create your views here.
import datetime as dt

from django.shortcuts import render

from contact_book.resource import Resource, ResourceCreateData


def skip():
    pass


def render_error(request, data: dict):
    return render(request, 'error.html', data, status=400)


def get_by_id(request, index: int = 0):
    if index == 0 or request.method != 'GET':
        return render_error(request, {'message': 'Bad request'})
    resource = Resource()
    exists, resource = resource.get(index)
    if not exists:
        return render_error(request, {'message': 'Not found'})
    return render(request, 'resource.html', {'resource': resource})


def list_all(request):
    if request.method != 'GET':
        return render_error(request, {'message': 'Bad request'})

    resource = Resource()
    resources = resource.all()

    if len(resources) == 0:
        return render(request, 'resources.html', {'resources': resources})

    sorting = request.GET.get('sorting', 'name')
    if sorting == 'rid':
        sorting = 'id'
    ordering = request.GET.get('ordering', 'asc')
    search: str = request.GET.get('search', '')

    if search:
        if search.isdigit():
            resources = resource.search_in_phone_number(resources, search)
        else:
            resources = resource.search_in_names(resources, search)

    if sorting not in ('name', 'id', 'created_at'):
        return render_error(request, {'message': 'Incorrect value given for sorting'})

    if ordering not in ('asc', 'desc'):
        return render_error(request, {'message': 'Incorrect value given for ordering'})

    resources = resource.sort(resources, sorting, ordering)
    return render(request, 'resources.html', {'resources': resources})


def update_by_id(request, index: int = 0):
    if index == 0:
        return render_error(request, {'message': 'Bad request'})
    resource = Resource()
    exists, r = resource.get(index)
    if not exists:
        return render_error(request, {'message': 'Not found'})

    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        if not any([name, phone, email, address]):
            return render_error(request, {'message': 'Empty fields'})
        if phone:
            r['phone_number'] = phone
        if name:
            r['name'] = name
        if email:
            r['email_address'] = email
        if address:
            r['address'] = address
        r['updated_at'] = dt.datetime.now().isoformat()
        resources = resource.all()

        duplicate = resource.search_in_names(resources, name)
        if duplicate and duplicate[0]['id'] != index:
            return render_error(request, {'message': 'Contact already exists'})

        duplicate = resource.search_in_phone_number(resources, phone)
        if duplicate and duplicate[0]['id'] != index:
            return render_error(request, {'message': 'Contact already exists'})
        resource.update(r)
    return render(request, 'resource.html', {'resource': r})


def delete_by_id(request, index: int = 0):
    if index == 0 or request.method != 'GET':
        return render_error(request, {'message': 'Bad request'})

    resource = Resource()
    exists, r = resource.get(index)
    if not exists:
        return render_error(request, {'message': 'Not found'})

    resource.delete(r)
    return list_all(request)


def delete_all(request):
    resource = Resource()
    resource.delete_all()
    return list_all(request)


def create(request):
    if request.method == 'GET':
        return render(request, 'create.html', {'create': 'create'})
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        if not all([name, phone]):
            return render_error(request, {'message': 'Name and Phone are required'})
        r = ResourceCreateData(
            name=name,
            phone_number=phone,
            email_address=email,
            created_at=dt.datetime.now().isoformat(),
            address=address
        )
        resource = Resource()
        resources = resource.all()
        if resource.search_in_names(resources, name) or resource.search_in_phone_number(resources, phone):
            return render_error(request, {'message': 'Contact already exists'})
        resource.create(r)
        return render(request, 'resources.html', {'resources': resource.all()})