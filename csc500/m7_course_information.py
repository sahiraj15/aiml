import sys


class CourseLocation:
    def __init__(self):
        self.course_location = {}

    def add_course_location(self, name, location):
        self.course_location[name] = location


class CourseInstructor:
    def __init__(self):
        self.course_instructor = {}

    def add_course_instructor(self, name, instructor):
        self.course_instructor[name] = instructor


class CourseSchedule:
    def __init__(self):
        self.course_schedule = {}

    def add_course_schedule(self, name, instructor):
        self.course_schedule[name] = instructor


if __name__ == "__main__":
    cloc = CourseLocation()
    cloc.add_course_location('CSC101','3004')
    cloc.add_course_location('CSC102', '4501')
    cloc.add_course_location('CSC103', '6755')
    cloc.add_course_location('NET110', '1244')
    cloc.add_course_location('COM241', '1411')

    cins = CourseInstructor()
    cins.add_course_instructor('CSC101', 'Haynes')
    cins.add_course_instructor('CSC102', 'Alvarado')
    cins.add_course_instructor('CSC103', 'Rich')
    cins.add_course_instructor('NET110', 'Burke')
    cins.add_course_instructor('COM241', 'Lee')

    csch = CourseSchedule()
    csch.add_course_schedule('CSC101', '8:00 a.m.')
    csch.add_course_schedule('CSC102', '9:00 a.m.')
    csch.add_course_schedule('CSC103', '10:00 a.m.')
    csch.add_course_schedule('NET110', '11:00 a.m.')
    csch.add_course_schedule('COM241', '1:00 p.m.')

    # Process course details
    inp_course_number = input("Enter the course number: ")

    exception_value = True
    if inp_course_number not in cloc.course_location.keys():
        print("Location not available for the course number")
        exception_value = False

    if inp_course_number not in cins.course_instructor.keys():
        print("Instructor not available for the course number")
        exception_value = False

    if inp_course_number not in csch.course_schedule.keys():
        print("Schedule not available for the course number")
        exception_value = False

    if exception_value is False:
        print("Try with a different course number")

    else:
        print("\nYour course {} information: ".format(inp_course_number))
        print("Room Number: {}".format(cloc.course_location[inp_course_number]))
        print("Instructor Name: {}".format(cins.course_instructor[inp_course_number]))
        print("Meeting Time: {}".format(csch.course_schedule[inp_course_number]))
