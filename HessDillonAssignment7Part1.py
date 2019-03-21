FIRST_INDEX = 0
SECOND_INDEX = 1

# Takes a given list of tuples and compiles into single dictionary
def tuple_list_to_dict(input_list):
  new_grade_dict = {}
  new_tuple = ()

  for i in range(len(input_list)):
  	current_tuple = input_list[i]
  	#('Zaphod', [33, 20])print(current_tuple)

  	# If 2 keys overlap, will add the values to be under a single key
  	if current_tuple[FIRST_INDEX] in new_grade_dict:
  		'''
  		key = current_tuple[0]
  		grades = current_tuple[SECOND_INDEX]
  		new_grade_dict[key] = grades
			'''
  	#else:

  		#new_tuple = current_tuple + tuple(new_grade_dict[current_tuple[FIRST_INDEX]])
  		#new_grade_dict.update(new_tuple)
  		#print(current_tuple)
  		#print(new_tuple)
  		#print(new_grade_dict[current_tuple[FIRST_INDEX]])
  		#print(current_tuple[1])
  		overlapping_key = current_tuple[FIRST_INDEX]
  		grades_list_with_same_name = new_grade_dict[overlapping_key]
  		for grade_to_add in grades_list_with_same_name:
  			current_tuple[SECOND_INDEX].append(grade_to_add)
  			#print(current_tuple)
  		"""
  		key = current_tuple[0]
  		grades = current_tuple[SECOND_INDEX]
  		new_grade_dict[key] = grades
  		#print(current_tuple)
  		#current_tuple.append()
  		"""
  	key = current_tuple[0]
  	grades = current_tuple[SECOND_INDEX]
  	new_grade_dict[key] = grades
  return new_grade_dict


def get_sorted_key_list(dictionary_to_be_sorted):
	list_to_be_sorted = list(dictionary_to_be_sorted.keys())

	sorted_list = sorted(list_to_be_sorted)

	#print(sorted_list)



	return sorted_list

def compute_average(number_list):
	average = 0
	how_many_numbers = len(number_list)
	for num in number_list:
		average += num
	average = average / how_many_numbers if how_many_numbers != 0 else 0.00


	return average

def get_sorted_list_of_tuples(unsorted_list):
		sorted_list = sorted(unsorted_list)
		#print(sorted(unsorted_list))
		return sorted_list

def main():
	grade_list = [ ('Zaphod', [33, 20]), ('Zaphod', [75, 48]), ('Slartibartfast',[]),

      ('Trillian', [98, 88]), ('Trillian', [97, 77]), ('Slartibartfast', []),

      ('Marvin', [2000, 500]) , ('Arthur', [42, 20]), ('Arthur', [64]),

      ('Trillian', [99]), ('Marvin', [450]), ('Marvin', [550]),

      ('Agrajag', []), ('Agrajag', []), ('Agrajag', [0]),

      ('Ford',[50]), ('Ford', [50]), ('Ford', [50]) ]  


	grade_dict = tuple_list_to_dict(grade_list)
	#print(type(grade_list[0]))
	#print(new_grade_dict)
	#print(grade_dict.keys())
	#print(grade_dict.values())

	list_of_names = get_sorted_key_list(grade_dict)

	#compute_average([1,2,3])
	#print(compute_average([1,2,3]))

	
	#print(grade_dict)

	#print(list_of_names)
	print("""\tName\t\tGrade Count\t\t Average Grade
---------------------------------------------------------------\n""" )
	
	
	for name in list_of_names :
		number_of_grades = len(grade_dict[name])
		average_grade = compute_average(grade_dict[name])
		print(" %15s %15d %25.2f" % (name, number_of_grades, average_grade))

		#print(number_of_grades)


#======================================= PART 2 ============================

	list_of_grades = list(grade_dict.items())
	#print(type(list_of_grades))
	#print(list_of_grades)
	sorted_list_of_grades = get_sorted_list_of_tuples(list_of_grades)
	#print(sorted_list_of_grades)

	print("""\n\n\tName\t\tGrade Count\t\t Average Grade
---------------------------------------------------------------\n""" )
	for i in range(len(sorted_list_of_grades)) :
		#print(sorted_list_of_grades[i])
		name = sorted_list_of_grades[i][FIRST_INDEX]
		number_of_grades = len(sorted_list_of_grades[i][SECOND_INDEX])
		average_grade = compute_average(sorted_list_of_grades[i][SECOND_INDEX])
		print(" %15s %15d %25.2f" % (name, number_of_grades, average_grade))


main()
