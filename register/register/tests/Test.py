import unittest
from register.Schemas import Checking
from register.Schemas import Person
from register.Schemas import Register

class Test(unittest.TestCase):

    def test_add_new_checking_person_none(self):
        result = Checking.add_new_checking(None, "Положення 6 Закону України", "Підстав для застосування заборон не знайдено",
                                           "11.01.2015", "-")
        self.assertEqual(result, -1)

    def test_add_new_checking_solution_gt240char(self):
        result = Checking.add_new_checking("5b0a7312dab78f22a8398311",
                                           "222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222",
                                           "Підстав для застосування заборон не знайдено",
                                           "11.01.2015", "-")
        self.assertEqual(result, -1)

    def test_get_checking_by_incorrect_id(self):
        result = Checking.get_checking("5b0a8d26dab78f1fd828c75c")
        self.assertEqual(result, None)

    def test_delete_checking_by_incorrect_id(self):
        result = Checking.delete_checking("5b0a8d26dab78f1fd828c75c")
        self.assertEqual(result, -1)

    def test_move_checking_by_incorrect_id(self):
        result = Checking.move_checking("5b0a8d26dab78f1fd828c75c", "blablabla", "blablabla")
        self.assertEqual(result, -1)

    def test_find_person_in_checking_with_incorrect_name(self):
        result = Checking.find_checking_by_person_name("Vasya Pupkin")
        self.assertEqual(len(result), 0)

    def test_add_new_person_empty_name(self):
        result = Person.add_new_person("", "dasda", "dsda", "dsdasd", "Dsadads")
        self.assertEqual(result, -1)

    def test_add_new_person_empty_category(self):
        result = Person.add_new_person("sadasd", "", "dsda", "dsdasd", "Dsadads")
        self.assertEqual(result, -1)

    def test_add_new_person_job_gt120char(self):
        result = Person.add_new_person("sadasd", "asfsf",
                                       "dsdadsfffffffffffffffffffffffdfsfsdfdsfsssssssssssssssssssdsfsdfdsfdsfdsfdsfdsfsdfdsfdsfdsfdsfdssssdfsdfdsfsdfsdfsdfdsfsdfsdfsdf",
                                       "dsdasd", "Dsadads")
        self.assertEqual(result, -1)

    def test_add_new_person_position_none(self):
        result = Person.add_new_person("sadasd", "asfsf",
                                       "dsdadsfffffffffffffffffffffffdfsfsdfdsfsssssssssssssssssssdsfsdfdsfdsfdsfdsfdsfsdfdsfdsfdsfdsfdssssdfsdfdsfsdfsdfsdfdsfsdfsdfsdf",
                                       None, "Dsadads")
        self.assertEqual(result, -1)

    def test_update_person_correct(self):
        result = Person.update_person("5b0a9a7bc42cd317d8e0a375",
                                      "ЛЮШЕНКО Ігор Васильович",
                                      "Фонд ",
                                      "Фонд державного майна",
                                      "начальник Регіонального відділення Фонду державного майна України по Хмельницькій області",
                                      "Хмельницька область",
                                      "False")
        self.assertEqual(result, 0)

    def test_get_officials(self):
        officials = Person.get_officials()
        flag = True
        for official in officials:
            if official.isPretender:
                flag = False
        self.assertEqual(flag, True)

    def test_add_new_register_incorrect_data(self):
        result = Register.add_new_register("5b0a7312dab78f22a8398311", None, None)
        self.assertEqual(result, -1)

    def test_find_register_by_person_name_uppercase(self):
        result = Register.find_register_by_person_name("ЛЮШЕНКО")
        self.assertEqual(len(result), 1)

    def test_find_register_by_person_name_lowercase(self):
        result = Register.find_register_by_person_name("люшенко")
        self.assertEqual(len(result), 1)

    def test_find_register_by_person_name_cammelcase(self):
        result = Register.find_register_by_person_name("ЛюШеНкО")
        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()