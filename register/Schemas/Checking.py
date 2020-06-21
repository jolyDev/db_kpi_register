from mongoengine import *
from register.Schemas.Person import *
from register.Schemas.Register import *


class Checking(Document):
    person_id = ReferenceField('Person')
    solution = StringField(max_length=240)
    date_accept_ban = StringField()
    date_refuse_ban = StringField()
    resolution = StringField(max_length=240)


def add_new_checking(person, solution, resolution='-', date_refuse_ban='-', date_accept_ban='-'):
    checking = Checking()

    exists = Checking.objects(person_id=person, solution=solution, resolution=resolution,
                              date_refuse_ban=date_refuse_ban, date_accept_ban=date_accept_ban)

    if exists:
        return exists[0].id

    if person is None:
        return -1
    else:
        checking.person_id = person

    if (solution is None) or (len(solution) > 240):
        return -1
    else:
        checking.solution = solution

    checking.resolution = resolution
    checking.date_accept_ban = date_accept_ban
    checking.date_refuse_ban = date_refuse_ban

    checking.save()
    return 0


def get_checking(this_id):
    try:
        checking = Checking.objects.get(id=this_id)
    except Checking.DoesNotExist:
        checking = None
    return checking


def get_all_checking():
    return Checking.objects()


def get_all_checking_where(is_pretendent):
    if is_pretendent:
        temp = Person.objects(isPretender=True)
        _return = Checking.objects(person_id__in=temp)
        return _return
    else:
        temp = Person.objects(isPretender=False)
        _return = Checking.objects(person_id__in=temp)
        return _return


def update_checking(this_id, solution, resolution, date_refuse_ban, date_accept_ban):
    if this_id is None:
        return -1

    checking = Checking.objects(id=this_id)

    if checking is None:
        return -1

    if solution is not None and len(solution) < 240:
        checking[0].update(**{"set__solution": solution})
    else:
        return -1

    if resolution is not None and len(resolution) < 240:
        checking[0].update(**{"set__resolution": resolution})
    else:
        return -1

    if date_accept_ban is not None:
        checking[0].update(**{"set__date_refuse_ban": date_refuse_ban})
    else:
        return -1

    if date_refuse_ban is not None:
        checking[0].update(**{"set__date_accept_ban": date_accept_ban})
    else:
        return -1

    return 0


def update_checking_with_person(this_id, name, category, job, position, region, solution, resolution, date_refuse_ban,
                                date_accept_ban, isPretender=False):
    if this_id is None:
        return -1

    checking = Checking.objects(id=this_id)[0]

    if checking is None:
        return -1

    if update_person(checking.person_id.id, name, category, job, position, region, isPretender) == -1:
        return -1

    if solution is not None and len(solution) < 240:
        checking.update(**{"set__solution": solution})
    else:
        return -1

    if resolution is not None and len(solution) < 240:
        checking.update(**{"set__resolution": resolution})
    else:
        return -1

    if date_accept_ban is not None:
        checking.update(**{"set__date_refuse_ban": date_refuse_ban})
    else:
        return -1

    if date_refuse_ban is not None:
        checking.update(**{"set__date_accept_ban": date_accept_ban})
    else:
        return -1

    return 0


def delete_checking(this_id):
    checking = Checking.objects(id=this_id)
    if checking:
        delete_person(checking[0].person_id.id)
        checking.delete()
        return 0
    else:
        return -1


def move_checking(this_id, result, ban_time):
    checking = Checking.objects(id=this_id)

    if checking:
        add_new_register(checking[0].person_id, result, ban_time)
        checking[0].delete()
        return 0
    else:
        return -1


def find_checking_by_person_name(request):
    temp = Person.objects(name__icontains=request)
    _return = Checking.objects(person_id__in=temp)
    return _return
