import os
a = 1
print 'DOSSIER GENERATOR'
print 'By Lorenzo Giampi AKA Zkill'
print ''
print ' __/\/\/\/\/\/\/\/\/\/\/\/\__'
print '|     __              __     |'
print '|    /  \            /  \    |'
print '|   | 0  |          |  0 |   |'
print '|    \__/            \__/    |'
print '|                            |'
print '|    ____________________    |'
print '|    \__________________/    |'
print ' __                        __'
print '   \/\/\/\/\/\/\/\/\/\/\/\/'
print''
print'________________________________'
print''
print''
print''
print'start : Start program'
print'ex : Example'
print'web : Website for new updates'
print''
print''
while a != 0:
	P = raw_input('Command> ')
	if P == 'start':
		Name = raw_input('Victim Name> ')
		Surname = raw_input('Victim Surname> ')
		Town = raw_input('Victim Town> ')
		Age = raw_input('Victim age> ')
		Birth = raw_input('Victim date of birth> ')
		IP = raw_input('Victim IP> ')
		Phone = raw_input('Phone Number> ')
		add = raw_input('Want to add some informations? y/n > ')
		if add == 'y':
			Family = raw_input('Want to add family options? y/n > ')
			if Family == 'y':
				momname = raw_input('Mother name > ')
				momusurname = raw_input('Mother surname > ')
				dadname = raw_input('Dad name > ')
				dadusername = raw_input('Dad surname > ')
			if Family == 'n':
				add = 'n'
		if add ==  'n':
			continue1 = raw_input('Do you want to save? y/n > ')
			if continue1 == 'y':
				f = open('Dossier.txt', 'w')
				output1 = ('Hello,my victim is ', Name, Surname, ' from ', Town, ' and he/she is ', Age, ' years old. ', ' date of birth is ', Birth, '. His/Her ip is ', IP, ', his/her phone number is ', Phone, '.')
				print output1
				f.write(output1)
				if family == 'y':
					f.write(' Mom full name is ', momname, momsurname, ' and dad full name is ', dadname, dadusername, '. ')
					f.write (' Dossier made with Dossier.py by lorenzo giampi AKA ZKill. Please copy this line or donate to my tool.')
					f.close()
				if family == 'n':
					f.write (' Dossier made with Dossier.py by lorenzo giampi AKA ZKill. Please copy this line or donate to my tool.')
					f.close()
				Readfile = raw_input('Do you want to read the file? y/n > ')
				if Readfile == 'y':
					os.system('sudo gedit', 'dossier.txt')
				if Readfile == 'n':
					quit('Program quit,file saved: ', 'dossier.txt')
				
				
				
				
		
		
