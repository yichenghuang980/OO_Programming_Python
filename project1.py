#
# CS 177 - project1.py
# Wilson Huang - 0031114130
# This is a demonstration of the basic Python file functions.
# The program accepts specific values and then displays results as table
# through function operations.
#

# initialize any necessary variables

# define main function
def main():

    # display information about the prgram function
    print("The program accepts specific values and then displays results as table.")
    
    # prompt user for purchase price,down payment,APR,periods per year,term of loan,and first payment date 
    price = eval(input("Enter total sale price of property:"))
    payment = eval(input("Enter cash down payment amount:"))
    APR = eval(input("Enter loan interest charged per year:"))
    numberPerYear = eval(input("Enter number of payments per year:"))
    term = eval(input("Enter length of loan in years:"))
    firstDate = str(input("Enter first payment date in MM/DD/YY:"))

    # calculate the loan amount and number of payments
    loan = price - payment
    numberOfPayment = term*numberPerYear
    paymentAmount = round((APR/numberPerYear)*loan/(1-(1+APR/numberPerYear)**(-numberOfPayment)),2)

    # define loanInfo function
    def loanInfo(loanAmount,period,paymentTimes,annualRate,beginningDate):

        # initialize any necessary variables and then perform calculations 
        rate1 = annualRate/period 
        totalPayment1 = paymentAmount*paymentTimes
        totalInterest1 = totalPayment1 - loanAmount

        # calculate endDate using split()
        separation = firstDate.split("/")
        year = int(separation[2]) + (term-1)
        for i in range(numberOfPayment):
            if (int(separation[0])+12/period*i<=12 and i%12!=0):
                endDate1 = "{0}/1/{1}".format(int(separation[0])+12/numberOfPayment*i,int(separation[2])+(i-1)//12)
            elif (i%12==0):
                endDate1 = "{0}/1/{1}".format(1,int(separation[2])+(i+1)//12)
            else:
                endDate1 = "{0}/1/{1}".format(int(separation[0])+12/period*i-12*(term-1),int(separation[2])+(i-1)//12)
            return rate1,totalPayment1,totalInterest1,endDate1 

    # call loanInfo function and assign variables to the results
    rate,totalPayment,totalInterest,endDate = loanInfo(loan,numberPerYear,numberOfPayment,APR,firstDate)   

    # define loanOptions function
    def loanOption(annualRate,period,lengthOfLoan,loanAmount):

        # initialize any necesssary variables
        differentRate = ""
        payment = ""
        format1 = ""

        # display table headers
        print("\t\t\tAlternative Loan Payment Table")
        print("\t\t\t","="*40)
        print("\t\t\t\tInterest Rates")

        # construct loop for headlines of different rate
        for indexOfRate in range(-3,4):
            format1 = "{0:10}%".format((annualRate+0.005*indexOfRate)*100)
            differentRate += format1
        print(differentRate)
        print("# Payments","="*50)

        # define a for loop based on the specified range for the number of loan payments
        for i in range(-2,3):
            n = round(period*lengthOfLoan + period*i/2)
            payment += "\n" + str(n)

            # define a for loop based on the specified range of interest rates
            for j in range(-3,4):
                r = (annualRate + 0.005*j)/period
                amount = "$"+str(round((r*loanAmount)/(1-(1+r)**(-n)),2))
                finalAmount = "{0:>11}".format(amount)
                payment += finalAmount
        print(payment)

    # call loanOption function
    loanOption(APR,numberPerYear,term,loan)

    # define amortize function
    def amortize(beginningDate,loanAmount,paymentPerMonth,annualRate,period):

        # initialize any necessary variables
        startingBalance = loanAmount
        separation = beginningDate.split("/")
        format2 = ""
        
        # display table headers
        print("\t\t\tLoan Amortization Table\n","="*70,
              "\n\tpayment\tstarting paymentinterest principle ending",
              "\n#\tdate\tbalance\tamount\tpaid\tpaid\tbalance",
              "\n====\t=====\t=====\t=====\t=====\t=====\t=====")

        # define a for loop based on the number of payments in the loan
        for i in range(numberOfPayment):
            number = str(1 + i)
            if (int(separation[0])+12/period*i<=12 and i%12!=0):
                paymentDate = "{0}/1/{1}".format(round(int(separation[0])+12/period*i),int(separation[2])+(i-1)//12)
            elif (i%12==0):
                paymentDate = "{0}/1/{1}".format(1,int(separation[2])+(i+1)//12)
            else:
                paymentDate = "{0}/1/{1}".format(round(int(separation[0])+12/period*i-12*(term-1)),int(separation[2])+(i-1)//12)
            interestPerMonth = round(startingBalance*(annualRate/period),2)
            principle = round(paymentPerMonth - interestPerMonth,2)
            endBalance = round(startingBalance - principle,2)
            format2 = "{0:>1}{1:>10}{2:>10}{3:>10}{4:>10}{5:>10}{6:>10}".format(number,paymentDate,"$"+str(startingBalance),"$"+str(paymentPerMonth),"$"+str(interestPerMonth),"$"+str(principle),"$"+str(endBalance))
            print(format2)
            startingBalance = endBalance 

    # call amortize function
    amortize(firstDate,loan,paymentAmount,APR,numberPerYear)
    
main()
