from ClassDefinitions import *
import sys
import os
import numpy as np
import time
import copy


# tsp_
# tsp_
# tsp_
# tsp_

global loanDictSim
loanDictSim = dict()

############ Inputs ############
monthlyDisposableIncome   = 1000    # dollars
numMonthlyPayments        = 2      # number of the amount ($) of payments to consider for the monthly payments
timeHorizons              = np.arange(1,3) # number of months to consider
############ Outputs ############

if __name__ == '__main__':

    #Load Loans and Investments
    loanParser('C:\\Users\\Eddie\\Desktop\\MoneyOptimization\\loan_config.txt')
    
    printLoans()
    
    #Define disposable_income allocations
    for eachLoan in loanList:
        if loanDict[eachLoan]['monthlyMax'] == 'max':
            #Jake was here.
            loanDict[eachLoan]['monthlyMax'] = monthlyDisposableIncome;        
        loanDict[eachLoan]['monthlyPayment']=np.linspace(loanDict[eachLoan]['monthlyMin'],float(loanDict[eachLoan]['monthlyMax']),numMonthlyPayments)
        loanDict[eachLoan]['monthlyInterest'] = loanDict[eachLoan]['interest']/(12*100)
        
    def financeSimulation (recursionsRemaining,currentPaymentPlan):
        global loanDictSim
        # Iterate over each monthlyPayment (c1, c2,...n) for each loan
        for payment in loanDict[loanList[recursionsRemaining]]['monthlyPayment']:
            currentPaymentPlan[recursionsRemaining] = payment
            if (recursionsRemaining > 1):
                financeSimulation(recursionsRemaining-1,currentPaymentPlan)
            else:
                for payment in loanDict[loanList[0]]['monthlyPayment']:
                    currentPaymentPlan[0] = payment
                    # Iterate over each time horizon
                    for timeHorizon in timeHorizons:
                        loanDictSim=copy.deepcopy(loanDict)
                        # Begin simulation for given paymentPlan and timeHorizon
                        for n in range(timeHorizon):
                            #Update each account every month
                            for eachLoan in loanList:
                                loanDictSim[eachLoan]['principle'] = loanDictSim[eachLoan]['principle']*(1-loanDict[eachLoan]['monthlyInterest'])
                                print('')
                                print('loanDict')
                                print(loanDict[eachLoan]['principle'])
                                print('loanDictSim')
                                print(loanDictSim[eachLoan]['principle'])

                                

    numberOfLoans       = len(loanList)
    numberOfRecursions  = numberOfLoans
    currentPaymentPlan  = np.zeros(numberOfLoans)
    financeSimulation(numberOfRecursions-1, currentPaymentPlan)


### Setup

