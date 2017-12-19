ects_earned=138
points_earned=44
points_max=60
ects_required_for_ba=180
ects_missing=ects_required_for_ba-ects_earned
ects_6_courses=ects_missing/6
grade=(points_earned/points_max)*5+1


print("So far you earned", ects_earned, "ECTS points.")
print("In the exam you got", points_earned, "of", points_max ,"points.")
print("You need", ects_missing ,"ECTS more to get the bachelor.")
print("You have to take", ects_6_courses ,"more courses with 6 ECTS to get the bachelor.")
print("You've got a", grade ,"in the exam.")