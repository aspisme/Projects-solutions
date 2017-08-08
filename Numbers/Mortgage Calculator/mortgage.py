
print()
principal = int(input('Write a principal: '))
period = int(input('Write a length (years): '))
interest = int(input('Write an interest (%): '))
print('Write a period')
durationStart = int(input('  - Start (default 1): ') or 1)
durationEnd = int(input('  - End (default end): ') or period) * 12
durationStart = 1 if durationStart == 1 else durationStart * 12

#principal = 135700
#period = 1
#interest = 11

overPay = 0
period = period * 12
monthPay = principal / period
statistic = {}

for i in range(1, period + 1):
	monthInterestPay = (principal*(interest/100)) / period
	overPay += monthInterestPay
	currentPay = monthPay + monthInterestPay
	principal = abs(principal-monthPay) 
	statistic[i] = {'Interest': monthInterestPay, 'Current': currentPay, 'Rest': principal}	

def viewStat():
	print('-'*50)
	print(' {0:^7}{4:^10}{1:^10}{2:^10}{3:^10}'.format('Month', 'Interest', 'Current', 'Rest', 'PerMonth'))

	for i in range(durationStart, durationEnd + 1):
		print(' {0:^7d}{4:^10.2f}{1:^10.2f}{2:^10.2f}{3:^10.2f}'.format(i, statistic[i]['Interest'], statistic[i]['Current'], statistic[i]['Rest'], monthPay))

	print('-'*50)
	print(' {0:^17}{1:^10.2f}'.format('Over payment:', overPay))

viewStat()
print()


