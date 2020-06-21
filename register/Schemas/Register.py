from mongoengine import *
from register.Schemas.Person import *


class Register(Document):
    person_id = ReferenceField('Person')
    result = StringField(max_length=240)
    ban_time = StringField(max_length=90)


def add_new_register(person, result='-', ban_time='-'):
    register = Register()

    exists = Register.objects(person_id=person, result=result, ban_time=ban_time)

    if exists:
        return exists[0].id

    if person is None:
        return -1
    else:
        register.person_id = person

    if (result is None) or (len(result) > 240):
        return -1
    else:
        register.result = result

    if (ban_time is None) or (len(ban_time) > 90):
        return -1
    else:
        register.ban_time = ban_time

    register.save()


def get_register(this_id):
    register = Register.objects.get(this_id)
    if register is None:
        return -1
    else:
        return register


def get_all_register():
    return Register.objects()


def update_register(this_id, result, ban_time):
    if this_id is None:
        return -1

    register = Register.objects.get(this_id)
    if register is None:
        return -1

    if result is not None:
        register.update(**{"set__result" : result})

    if ban_time is not None:
        register.update(**{"set__ban_time" : ban_time})

    return 0


def update_register_with_person(this_id, name, category, job, position, region, result, ban_time, isPretender=False):

    if this_id is None:
        return -1

    register = Register.objects(id=this_id)[0]

    if not register:
        return -1

    if update_person(register.person_id.id, name, category, job, position, region, isPretender) == -1:
        return -1

    if result is not None and len(result) < 240:
        register.update(**{"set__result": result})

    if ban_time is not None and len(result) < 90:
        register.update(**{"set__ban_time": ban_time})

    return 0


def delete_register(this_id):
    register = Register.objects(id=this_id)[0]

    if register:
        if delete_person(register.person_id.id) == -1:
            return -1
        register.delete()
        return 0
    else:
        return -1


def find_register_by_person_name(request):
    temp = Person.objects(name__icontains=request)
    _return = Register.objects(person_id__in=temp)
    return _return
