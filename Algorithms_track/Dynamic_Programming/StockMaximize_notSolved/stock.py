#!/bin/python


# Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc. (WOT) will be for the next N days.

# Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own, or not make any transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?

# Input Format

# The first line contains the number of test cases T. T test cases follow:

# The first line of each test case contains a number N. The next line contains N integers, denoting the predicted price of WOT shares for the next N days.

# Constraints

# All share prices are between 1 and 100000
# Output Format

# Output T lines, containing the maximum profit which can be obtained for the corresponding test case.


import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    N = int(raw_input().strip())
    prices = map(int, raw_input().strip().split(' '))

    soma_gastos = prices[0]
    diferenca_precos = 0
    preco_inicial = prices[0]
    lucro = 0
    passos_andados = 1

    for i in range(1, N):
    	diferenca_precos = diferenca_precos + prices[i] - prices[i - 1]
    	if diferenca_precos >= 0:
    		soma_gastos = soma_gastos + prices[i]
    		passos_andados = passos_andados + 1
    	print "diferenca precos", diferenca_precos, "soma gastos", soma_gastos, "passos_andados", passos_andados
    	

    

    print lucro
