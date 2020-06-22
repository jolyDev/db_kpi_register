from mongoengine import *


class Person(Document):
    name = StringField(required=True, max_length=60)
    category = StringField(max_length=120)
    job = StringField(max_length=120)
    position = StringField(max_length=120)
    region = StringField(max_length=60)
    isPretender = BooleanField(required=True)


def get_person(id):
    person = Person.objects.get(id=id)
    if person is None:
        return -1
    else:
        return person


def get_all_persons():
    return Person.objects()


def add_new_person(name, category, job, position, region, isPretender=False):
    person = Person()

    exists = Person.objects(name=name, category=category, job=job, position=position, region=region, isPretender=isPretender)

    if exists:
        return exists[0]

    if len(name) != 0 and len(name) < 60:
        person.name = name
    else:
        return -1

    if len(category) != 0 and len(name) < 120:
        person.category = category
    else:
        return -1

    if len(job) != 0 and len(job) < 120:
        person.job = job
    else:
        return -1

    if len(position) != 0 and len(position) < 120:
        person.position = position
    else:
        return -1

    if len(region) != 0 and len(region) < 60:
        person.region = region
    else:
        return -1

    if isPretender is not None:
        person.isPretender = str2bool(isPretender)
    else:
        person.isPretender = False

    return person.save()


def update_person(id, name, category, job, position, region, isPretender=False):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        person = None

    if person is None:
        return -1

    if len(name) != 0 and len(name) < 60:
        person.update(**{"set__name": name})
    else:
        return -1

    if len(category) != 0 and len(name) < 120:
        person.update(**{"set__category": category})
    else:
        return -1
    if len(job) != 0 and len(job) < 120:
        person.update(**{"set__job": job})
    else:
        return -1

    if len(position) != 0 and len(position) < 120:
        person.update(**{"set__position": position})
    else:
        return -1

    if len(region) != 0 and len(region) < 60:
        person.update(**{"set__region": region})
    else:
        return -1

    if isPretender is not None:
        person.update(**{"set__isPretender": str2bool(isPretender)})
    else:
        return -1
    return 0


def delete_person(id):
    person = Person.objects(id=id)
    if person is None:
        return -1
    else:
        person.delete()
        return 0


def get_officials():
    return Person.objects(isPretender=False)


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1", "True")
