global loanDict
global loanList

#loanDict = dict(name=dict(principle=str(),interest=str(),computedPeriod=str(),monthlyMin=str(),monthlyMax=str()))
loanDict = dict()
loanList = list()

def printLoans ():
    print('\n   Loan Printer\n_______________________')
    for eachLoan in loanList:
        print(' Loan Label -> '+eachLoan)
        print('     principle:      '+str(loanDict[eachLoan]['principle']))
        print('     interest:       '+str(loanDict[eachLoan]['interest']))
        print('     computedPeriod: '+loanDict[eachLoan]['computedPeriod'])
        print('     monthlyMin:     '+str(loanDict[eachLoan]['monthlyMin']))
        print('     monthlyMax:     '+str(loanDict[eachLoan]['monthlyMax']))
        print('')

def loanParser(filename):

    try:
        fnHandle = open(filename)
        fnLines = fnHandle.readlines()

        seperateLoan = None
        newLoan = None
        tempName = None
    except:
        print('Use a correct file...\nYou used: '+filename)

    for eachLine in fnLines:
        if (('[' in eachLine) and (']')):
            if 'loan' in eachLine:
                if newLoan == None:
                    newLoan = True
                    continue

                elif newLoan == False:
                    pass

                elif newLoan:
                    print('This should never print.\nYou suck at making a config file mother fucker...\n\n')
                    sys.exit()

        if newLoan == True:
            newLoan = False

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
            elif type.lower() == '-monthly maximum':
                pass

            else:
                print('type: '+type)
                print('line: ' +line)
                print('attribute error...')
                sys.exit()

            typeLen = len((type+':'))
            return(line[typeLen:len(line)].strip())


        if newLoan == False:

            if '-Name:' in eachLine:
                tempName = attributeParser('-Name',eachLine)
                print('     Parsing: '+tempName)
                loanDict[tempName]=dict(principle=float(),interest=float(),computedPeriod=str(),monthlyMin=float(),monthlyMax=float())
                loanList.append(attributeParser('-Name',eachLine))
            elif '-Principle:' in eachLine:
                loanDict[tempName]['principle']=float(attributeParser('-Principle',eachLine))
                print(tempName+'-> Principle Parsed')
            elif '-Interest:' in eachLine:
                loanDict[tempName]['interest']=float(attributeParser('-Interest',eachLine))
                print(tempName+'-> Interest')
            elif '-Computed Period:' in eachLine:
                loanDict[tempName]['computedPeriod']=attributeParser('-Computed Period',eachLine)
                print(tempName+'-> Computed Period Parsed')
            elif '-Monthly Minimum:' in eachLine:
                loanDict[tempName]['monthlyMin']=float(attributeParser('-Monthly Minimum',eachLine))
                print(tempName+'-> Monthly Minimum Parsed')
            elif '-Monthly Maximum' in eachLine:
                loanDict[tempName]['monthlyMax']=float(attributeParser('-Monthly Minimum',eachLine))
                newLoan = None
                print(tempName+'-> Monthly Maximum Parsed')
                print('')
            else:
                pass
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)

def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
