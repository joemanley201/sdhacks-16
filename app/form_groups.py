import itertools
import csv
import random
total_size = 500
from sparkpost_impl import send_email

def pick_one_person(combination, fields, csvFile):
	fields = [3, 4]
	for row in csvFile:
		matched = False
		for idx in xrange(len(fields)):
			if row[fields[idx]] != combination[idx]:
				continue
		email = row[1]
		del row
		return email
	return None


def form_groups(fields, number_of_groups, csv_file_stream, analyzed_result):
	csv_file_stream.seek(0)
	csv_file = csv.reader(csv_file_stream)


	headers = csv_file.next()

	combinations = []
	for field in fields:
		combinations.append(analyzed_result[field].keys())

	combinations = list(itertools.product(*combinations))
	group_size = total_size / number_of_groups
	output_groups = []
	for i in xrange(number_of_groups):
		output_groups.append([])
		for j in xrange(group_size):
			selected_person = None
			while selected_person == None:
				random_group = random.randrange(0, len(combinations))
				selected_person = pick_one_person(combinations[random_group], fields, csv_file)    
				output_groups[i].append(selected_person)
	team_group_members = ['joemanley201@gmail.com', 'sweetha.k.kumar@gmail.com', 'melvix_2020@yahoo.co.in', 'sriniavireddy@gmail.com']
	for team_member in team_group_members:
		temp_group = team_group_members[:]
		temp_group.remove(team_member)
		send_email(team_member, temp_group)
	return output_groups