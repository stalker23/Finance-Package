import sys
import os

global mortDict
global mortList

mortDict = dict(mortgage=dict(name=str(),principle=str(),interest=str(),computedPeriod=str(),monthlyMin=str()))
mortList = list()

def printMortgages ():
    print('\n   Mortgage Printer\n_______________________')
    for eachMort in mortList:
        print(' Mortgage Label -> '+eachMort)
        print('     principle:      '+mortDict[eachMort]['principle'])
        print('     interest:       '+mortDict[eachMort]['interest'])
        print('     computedPeriod: '+mortDict[eachMort]['computedPeriod'])
        print('     monthlyMin:     '+mortDict[eachMort]['monthlyMin'])
        print('')

def mortgageParser(filename):
    global mortDict
    global mortList
    
    try:
        fnHandle = open(filename)
        fnLines = fnHandle.readlines()
        
        seperateMortgage = None 
        newMortgage = None
        tempName = None
    except:
        print('Use a correct file...\nYou used: '+filename)
        
    for eachLine in fnLines:
        if (('[' in eachLine) and (']')):
            if 'mortgage' in eachLine:
                if newMortgage == None:
                    newMortgage = True
                    continue
                    
                elif newMortgage == False:
                    pass
                    
                elif newMortgage:
                    print('This should never print.\nYou suck at making a config file mother fucker...\n\n')
                    sys.exit()
                    
        if newMortgage == True:
            newMortgage = False
        
        def attributeParser(type,line):
            line = line.strip()
            if type.lower() == ('-name'):
                pass
            elif type.lower() == '-principle':
                pass
            elif type.lower() == '-interest':
                pass
            elif type.lower() == '-computed period':
                pass
            elif type.lower() == '-monthly minimum':
                pass
            
            else:
                print('type: '+type)
                print('line: ' +line)
                print('attribute error...')
                sys.exit()
                
            typeLen = len((type+':'))
            return(line[typeLen:len(line)].strip())
            
        
        if newMortgage == False:
           
            if '-Name:' in eachLine:
                tempName = attributeParser('-Name',eachLine)
                print('     Parsing: '+tempName)
                mortDict[tempName]=dict(principle=str(),interest=str(),computedPeriod=str(),monthlyMin=str())
                mortList.append(attributeParser('-Name',eachLine))
            elif '-Principle:' in eachLine:
                mortDict[tempName]['principle']=attributeParser('-Principle',eachLine)
                print(tempName+'-> Principle Parsed')
            elif '-Interest:' in eachLine:
                mortDict[tempName]['interest']=attributeParser('-Interest',eachLine)
                print(tempName+'-> Interest')
            elif '-Computed Period:' in eachLine:
                mortDict[tempName]['computedPeriod']=attributeParser('-Computed Period',eachLine)
                print(tempName+'-> Computed Period Parsed')
            elif '-Monthly Minimum:' in eachLine:
                mortDict[tempName]['monthlyMin']= attributeParser('-Monthly Minimum',eachLine)
                newMortgage = None
                print(tempName+'-> Monthly Minimum Parsed')
                print('')
            else:
                pass
                #comment logic maybe?
               
                
            
            


if __name__ == '__main__':

    #Jake's Contribution
    mortgageParser('C:\\Users\\Eddie\\Desktop\\MoneyOptimization\\mortgage_config.txt')
    printMortgages()
    
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)
    
    

  ### Setup

