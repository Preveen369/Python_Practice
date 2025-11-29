# inheritances and polymorphism in PYTHON:

# type of inheritance:
# 1. single-level, 2. multiple, 3. hierarchial, 4. multi-level

# single-level inheritance
class Parent:
    nationality = "Indian"
    native_state = 'Tamil Nadu'
    ethnicity = "Tamizh"
    
    def languages_known(self):
        languages = ["Tamizh", "Sinhala", "Hindi"]
        for lang in languages:
            print(lang, sep=', ')

    def known_skills(self):
        skills = ["Sports", "Music"]
        for skill in skills:
            print(skill, sep=', ')

class Child(Parent):
    def languages_known(self):
        languages = ["Tamizh", "Sinhala", "Malayalam", "Burmese"]
        for lang in languages:
            print(lang)

    def known_skills(self):
        skills = ["Sports", "Music", "Public Speaking"]
        for skill in skills:
            print(skill)

# p = Parent()
# print(p.ethnicity)
# print(p.nationality)
# print("Parent's known languages:")
# p.languages_known()

c = Child()
print(c.ethnicity)
print(c.nationality)
print("Child's known languages:")
c.languages_known()