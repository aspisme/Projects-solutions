'''Mortgage Calculator
Calculate monthly payments in given term and print in month, weeks and days.
P.S. The most accurately is month.
08.08.17 (c)Andrew Polochanin'''

def chooser():
	choice = input("\nType 'yes' (default) to calculate the monthly payments or 'no' to exit: ") or 'yes'
	if choice == 'yes':
		mortgageInput()
		mortgageOutput()
	else:
		print('Exit...\n')
		return	
	chooser()

def surrounding():
	print('-'*70)

def mortgageInput():
	loan = int(input('Write the loan : '))
	term = int(input('Write the term (years): '))
	rate = int(input('Write the interest rate (%): '))
	
	statistic['month'] = calcPayments(loan, term*12, rate)	
	statistic['week'] = calcPayments(loan, term*int(365/7), rate)	
	statistic['day'] = calcPayments(loan, term*365, rate)	

def calcPayments(loan, term, rate):
	monthPay = loan / term 
	overPay = 0
	stat = {}
	for i in range(1, term + 1):
		monthInterestPay = (loan*(rate/100)) / term 
		overPay += monthInterestPay
		currentPay = monthPay + monthInterestPay
		loan = abs(loan - monthPay) 
		stat[i] = {'PerMonth': monthPay, 'Interest': monthInterestPay, 'Current': currentPay, 'Rest': loan}	
	stat['Over Payment'] = overPay	
	return stat	
	
def mortgageOutput():
	period =  input("\nView payments for the certain period?\n(default 'yes' or type 'no' to view all or 'exit'): ") or 'yes'
	if period == 'yes':
		print('Write the period in monthes')
		periodStart = int(input('  - Start: '))
		periodEnd = int(input('  - End: '))
	elif period == 'exit':
		return
	else:
		periodStart = 1
		periodEnd = list(statistic['month'].keys())[-2]

	choice = input("View payments for month (default), week or day? : ") or 'month'
	if choice == 'month':
		viewStat(statistic['month'], periodStart, periodEnd)
	elif choice == 'week':
		viewStat(statistic['week'], periodStart*4, periodEnd*4)
	elif choice == 'day':
		viewStat(statistic['day'], periodStart*30, periodEnd*30)
	mortgageOutput()

def viewStat(stat, periodStart, periodEnd):
	print(' {0:^7}{4:^10}{1:^10}{2:^10}{3:^10}'.format('N', 'Interest', 'Current', 'Rest', 'PerNumber'))
	for i in range(periodStart, periodEnd + 1):
		print(' {0:^7d}{4:^10.2f}{1:^10.2f}{2:^10.2f}{3:^10.2f}'.format(i, stat[i]['Interest'], stat[i]['Current'], stat[i]['Rest'], stat[i]['PerMonth']))
	print(' {0:^17}{1:^10.2f}'.format('Over payment:', stat['Over Payment']))


statistic = {}

if __name__ == '__main__':
	surrounding()
	chooser()
	surrounding()
	

