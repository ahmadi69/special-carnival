input_mass = input('enter the mass(kg): ')
while input_mass.isdigit() == False: 
    input_mass = input('please enter a valid number: ')
    
kg_mass = float(input_mass)
lb_mass = kg_mass*2.2

print(f'the mass is {lb_mass} pounds')