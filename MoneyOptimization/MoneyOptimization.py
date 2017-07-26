from ClassDefinitions import *
import sys
import os
import numpy as np
import time
import copy

############ Inputs ############
monthlyDisposableIncome   = 1000    # dollars
numMonthlyPayments        = 2      # number of the amount ($) of payments to consider for the monthly payments
timeHorizons              = np.arange(1,10) # number of months to consider
############ Outputs ############

# def financeSimulation (recursionsRemaining,currentPaymentPlan):
#     global loanDictSim
#     # Iterate over each monthlyPayment (c1, c2,...n) for each loan
#     for payment in loanDict[loanList[recursionsRemaining]]['monthlyPayment']:
#         currentPaymentPlan[recursionsRemaining] = payment
#         if (recursionsRemaining > 1):
#             financeSimulation(recursionsRemaining-1,currentPaymentPlan)
#         else:
#             for payment in loanDict[loanList[0]]['monthlyPayment']:
#                 currentPaymentPlan[0] = payment
#                 # Iterate over each time horizon
#                 for timeHorizon in timeHorizons:
#                     loanDictSim=copy.deepcopy(loanDict)
#                     # Begin simulation for given paymentPlan and timeHorizon
#                     for n in range(timeHorizon):
#                         #Update each account every month
#                         for eachLoan in loanList:
#                             loanDictSim[eachLoan]['principle'] = loanDictSim[eachLoan]['principle']*(1+loanDict[eachLoan]['monthlyInterest'])

if __name__ == '__main__':

    #Load Loans and Investments
    #loanParser('C:\\Users\\Eddie\\Desktop\\MoneyOptimization\\loan_config.txt')
    dir = os.path.dirname(__file__)
    loanParser(os.path.join(dir,'loan_config.txt'))
    printLoans()
# ################## Method 1 (incomplete) Begin ###################
#     # Define disposable_income allocations
#     for eachLoan in loanList:
#         loanDict[eachLoan]['monthlyPayment']  = np.linspace(loanDict[eachLoan]['monthlyMin'],float(loanDict[eachLoan]['monthlyMax']),numMonthlyPayments)
#         loanDict[eachLoan]['monthlyInterest'] = loanDict[eachLoan]['interest']/(12*100)
#
#     numberOfLoans       = len(loanList)
#     numberOfRecursions  = numberOfLoans
#     currentPaymentPlan  = np.zeros(numberOfLoans)
#     financeSimulation(numberOfRecursions-1, currentPaymentPlan)
#
#     for eachLoan in loanList:
#         print('')
#         print('loanDict')
#         print(loanDict[eachLoan]['principle'])
#         print('loanDictSim')
#         print(loanDictSim[eachLoan]['principle'])
# ################## Method 1 (incomplete) End ###################

################### Method 2 (incomplete) Begin ###################

# payOrder = permutations(loanList)
# for i in payOrder:
#     print(i)

################## My Mortgage/Investment ###################
