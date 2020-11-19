#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    key_to_frequency = {}
    frequency_to_key = {}
    res = []
    
    for query in queries:
        action = query[0]
        key = query[1]
        # print('query ', action, key)
        
        if action == 1:
            # print('action 1')
            # Update key to frequency
            key_to_frequency[key] = key_to_frequency[key] + 1 if key in key_to_frequency else 1 
            # print(key_to_frequency, key_to_frequency[key], frequency_to_key)

            # Update frequency to key            
            if not key_to_frequency[key] in frequency_to_key:
              frequency_to_key[key_to_frequency[key]] = []
            if key_to_frequency[key] - 1 > 0 and not key_to_frequency[key] - 1 in frequency_to_key:
              frequency_to_key[key_to_frequency[key] - 1] = []
            if not key in frequency_to_key[key_to_frequency[key]]:
                frequency_to_key[key_to_frequency[key]].append(key)
            if key_to_frequency[key] - 1 > 0 and  key in frequency_to_key[key_to_frequency[key] -1]:
                frequency_to_key[key_to_frequency[key] - 1].remove(key)
                
        if action == 2:
            # print('action 2')
            # Update key to frequency
            key_to_frequency[key] = key_to_frequency[key] - 1 if key in key_to_frequency and key_to_frequency[key] > 0 else 0
            new_freq = key_to_frequency[key]

            # Update frequency to key
            if not key_to_frequency[key] in frequency_to_key:
              frequency_to_key[key_to_frequency[key]] = []
            if not key_to_frequency[key] + 1 in frequency_to_key:
              frequency_to_key[key_to_frequency[key] + 1] = []
            if not key in frequency_to_key[new_freq]:
                frequency_to_key[new_freq] = [key]
            if key in frequency_to_key[new_freq +1]:
                frequency_to_key[new_freq + 1].remove(key)
        if action == 3:
            if not key in frequency_to_key: 
                res.append(0)
                # print('not 3 ', res)
            elif len(frequency_to_key[key]) <= 0: 
                res.append(0)
                # print('not 3 ', res)
            else: 
                res.append(1)
                # print('3 ', key, res)
                
        # print('key_frq', key_to_frequency, ' - frq_key', frequency_to_key)
        # print()
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print(ans)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
