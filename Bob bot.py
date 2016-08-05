print("\n" * 100)
print('Welcome to BOB-BOT')
print('By: HSD IT Dept')
print('')
print('1) Computer Screen black or not responding')
print('2) No Internet or Documents/Desktop missing')

problem = input('Enter Corresponding Number: ')

if problem == '1':
    print('- Have you tried turning it off and on again?')
    print('- 1) Yes')
    print('- 2) No')
    numberinput = input('#: ')
    if numberinput == '1':
        print('-- Call 12002 or 12003 or put in a helpdesk request')
    elif numberinput == '2':
        print('-- Please try that, then consult helpdesk services')
    else:
        print('Invalid Responce')
elif problem == '2':
    print('- Do you have internet')
    print('- 1) Is there a red X next to the network icon?')
    print('- 2) Are your Desktop icons present?')
else:
    print('Problem Not Found')
