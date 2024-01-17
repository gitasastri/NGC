#Task 1
print('\n===Task 1===\n')
customer_id = ['B818', 'A461', 'A092', 'A082', 'B341', 'A005', 'A092', 'A461','B219', 'B904', 'A901', 'A083', 'B904', 'A092', 'B341', 'B821','B341', 'B821', 'B904', 'B818', 'A901', 'A083', 'B818', 'A082','B219', 'B219', 'A083', 'A901', 'A082', 'B341', 'B341', 'A083','A082', 'B219', 'B439', 'A461', 'A005', 'A901', 'B341', 'A082','A083', 'A461', 'A083', 'A901', 'A461', 'A083', 'A082', 'A083','B341', 'A901', 'A082', 'A461', 'B219', 'A083', 'B818', 'B821','A092', 'B341', 'A461', 'A092', 'A083', 'B821', 'A092']
num_values = len(set(customer_id))
print('How many unique customer_id from the list?', num_values)

#Task 2
print('\n===Task 2===\n')
data = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print('a.', data[3])
print('b.', data[5:8])

data = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
data.reverse()
print('c.', data,'\n')

#Task 3
print('\n===Task 3===\n')
Provinsi = {'Nanggroe Aceh Darussalam': 'Aceh','Sumatera Selatan': 'Palembang','Kalimantan Barat': 'Pontianak','Jawa Timur': 'Madiun','Sulawesi Selatan': 'Makassar','Maluku': 'Ambon'}
print('a.', Provinsi.keys(), '\n')
Provinsi['Jawa Timur'] = 'Surabaya'
print('b.', Provinsi)