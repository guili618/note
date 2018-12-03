with open('some_file_1.txt', 'r') as file1:
    with open('some_file_2.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('some_output_file.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)


def diff_file(file1,file2):
    	with open(file1,'r') as f1,open(file2,'r') as f2:
		f1_list = [line for line in f1]
		f2_list = [line for line in f2]
		for row1 in f1_list:
			for row2 in f2_list:
				if row1.strip() == row2.strip():
					print(row1)
				else:
					pass