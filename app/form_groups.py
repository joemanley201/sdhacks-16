import itertools
total_size = 500

def pick_one_person(combination, fields, csvFile):
    for row in csvFile:
        matched = False
        for idx in xrange(len(fields)):
            if row[fields[idx]] != combination[idx]:
                continue
        email = row['email']
        del row
        return email
    return None


def form_groups(fields, number_of_groups, csv_file):
    headers = uploaded_csv_file.next()

    combinations = []
    for field in fields:
        combinations.append(output[field].keys())

    combinations = list(itertools.product(*combinations))
    group_size = total_size / number_of_groups
    output_groups = []
    for i in xrange(number_of_groups):
        output_groups.append([])
        for j in xrange(group_size):
            selected_person = None
            while selected_person == None:
                random_group = random.randrange(0, len(combinations))
                selected_person = pick_one_person(combinations[random_group], fields, csvFile)    
                output_groups[i].append(selected_person)        
    print output_groups