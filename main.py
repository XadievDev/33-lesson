#XadievDev
#33-lesson.Files

#----------------------------------------------------------#

# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close()

#----------------------------------------------------------#

# with open('pi.txt') as file:
#     pi = file.read()

# print(pi)

# pi = pi.rstrip()
# pi = pi.replace('\n','')
# pi = float(pi)
# print(pi)

#----------------------------------------------------------#

# filename = 'data/talabalar.txt'
# with open(filename) as file:
#     talabalar = file.readlines()
# print(talabalar)

# with open(filename) as file:
#     talabalar = file.readlines()
#     talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)

#----------------------------------------------------------#

# filename = 'data/new_file.txt'
# with open(filename,'w') as file:
#     file.write("Amirbek Xadiev\n")
#     file.write('2006')

# with open(filename,'a') as file:
#     file.write('\nMuhammadrizo Jumayev\n')
#     file.write('2007')

#----------------------------------------------------------#

# import pickle  

# talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
# talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

# with open('info','wb') as file:
#     pickle.dump(talaba1,file)
#     pickle.dump(talaba2,file)

# with open('info','rb') as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)

# print(talaba1)

#----------------------------------------------------------#

# with open('amaliyot/pi_million_digits.txt') as file:
#     pi = file.read()
# pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
# pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
# pi = pi.replace(' ','')

# # Tug'ilgan kunim pi da bormi?
# bdate = '20060905'
# print(bdate in pi)

