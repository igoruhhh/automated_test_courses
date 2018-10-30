"""
Задание 4 (на создание тестов c помощью unittest)
Создайте наборы тестов на тестирование класса ITEmployee, который вы реализовали в Задании 1
(или Employee, или Person в зависимости до куда вы дошли в выполнении Задания 1).
"""
import unittest
from automated_test_courses.homework_5.hw_5_task_1 import ITEmployee


class ITEmployeeTest(unittest.TestCase):
    def setUp(self):
        self.empl1 = ITEmployee(full_name="Igor Marinich", year_of_birth=1995, position="SW engineer", experience=2,
                               salary=500, skills=["English", "QA"])

    def test_add_skill(self):
        res = self.empl1.add_skill("Automation")
        self.assertEqual(res, self.empl1.skills)

    def test_add_skills(self):
        res = self.empl1.add_skills(["ISTQB", "CCNA", "CCNP"])
        self.assertEqual(res, self.empl1.skills)

    def test_name(self):
        res = self.empl1.name_from_full_name()
        self.assertEqual(res, "Igor")

    def test_surname(self):
        res = self.empl1.surname_from_full_name()
        self.assertEqual(res, "Marinich")


if __name__ == "__main__":
    unittest.main()
