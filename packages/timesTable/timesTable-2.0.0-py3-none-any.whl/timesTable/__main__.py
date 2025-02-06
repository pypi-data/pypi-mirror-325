#!/usr/bin/env python3

# 3-Clause BSD License
# 
# Copyright (c) 2008-2025, James Philip Rowell,
# Alpha Eleven Incorporated
# www.alpha-eleven.com
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
#  1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
# 
#  2. Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
# 
#  3. Neither the name of the copyright holder, "Alpha Eleven, Inc.",
#     nor the names of its contributors may be used to endorse or
#     promote products derived from this software without specific prior
#     written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import argparse
import os
import sys
import subprocess
import textwrap
import math
import baseconv
import string

# MAJOR version for incompatible API changes
# MINOR version for added functionality in a backwards compatible manner
# PATCH version for backwards compatible bug fixes
#
VERSION = "2.0.0"     # Semantic Versioning 2.0.0

def main():

    kEpsilon = 1.0e-12
    kDigits = string.digits + string.ascii_uppercase + string.ascii_lowercase

    # Redefine the exception handling routine so that it does NOT
    # do a trace dump if the user types ^C while the command is running.
    #
    old_excepthook = sys.excepthook
    def new_hook(exceptionType, value, traceback):
        if exceptionType != KeyboardInterrupt and exceptionType != IOError:
            old_excepthook(exceptionType, value, traceback)
        else:
            pass
    sys.excepthook = new_hook

    p = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            Print n by n times table for any base from two to sixty-two.
            '''),
        usage="%(prog)s [OPTION]...")

    p.add_argument("--version", action="version", version=VERSION)
    p.add_argument("--base", "-b", action="store", type=int, dest="base",
        default=10, metavar="N",
        help="The base of the number system. Base must be in range [2, 62]. (default=10).")
    p.add_argument("--size", "-n", action="store", type=int, dest="n",
        default=13, metavar="N",
        help="The largest number in the table. Must be greater than 1. (default=13).")
    p.add_argument("--primes", action="store_true",
        dest="onlyPrimes", default=False,
        help="only print out the multiplication table for prime numbers" )
    p.add_argument("--limit", action="store", type=int, dest="maxDigits",
        default=-1, metavar="MAX",
        help="Limit printing the table to numbers of length MAX-digits or less")

    args = p.parse_args()

    if args.maxDigits == 0 :
        print(os.path.basename(sys.argv[0]),
            ": warning: max digits is 0, nothing to print.",
            sep='', file=sys.stderr)
        sys.exit(0)

    ## print(type(args.base))
    ## sys.exit(0)

    if args.base < 2 or args.base > 62:
        print(os.path.basename(sys.argv[0]),
            ": error: The base must be in the range [2, 62].",
            sep='', file=sys.stderr)
        sys.exit(1)

    if args.n < 2 :
        print(os.path.basename(sys.argv[0]),
            ": error: The largest number in the table must be at least 2.",
            sep='', file=sys.stderr)
        sys.exit(1)

    # Note: this "isPrime" array will be filled with True
    # in the case that we want to display ALL the integers
    # from 2,n - sorry, it's a bit of a cheat to use this list
    # this way, but it makes for clean code.
    #
    isPrime = [True]*(args.n+1)

    # Sieve of Eratosthenes - skipped when wanting to list ALL numbers
    #
    if args.onlyPrimes :
        p = 2
        while p < (args.n / 2) :
            i = 2
            while p*i <= args.n :
                isPrime[p*i] = False
                i += 1
            p += 1
            while not isPrime[p] :
                p += 1

    # Initialize base.
    #
    baseStr = kDigits[0: args.base]
    base = baseconv.BaseConverter(baseStr)

    # Find the largest prime in table
    #
    if not args.onlyPrimes :
        maxN = args.n
    else :
        i = len(isPrime)
        i -= 1
        while not isPrime[i] :
            i -= 1
        maxN = i

    numFormatMaxLen = len(base.encode(maxN * maxN))

    if args.maxDigits > 0 :
        if args.maxDigits < 3 and args.base == 2 :
            print(os.path.basename(sys.argv[0]),
                ": warning: Binary times-table with less than three digits will be empty. Skipping.",
                sep='', file=sys.stderr)
            sys.exit(0)

        x = 2
        while x <= maxN :
            if len(base.encode(x*2)) > args.maxDigits :
                x -= 1
                break
            x += 1

        if x < maxN :
            maxN = x

        numFormatMaxLen = args.maxDigits

    formatList = [0] # So the index and numbers match (Never use index 0)
    formatList.append(len(base.encode(maxN)))
    numFormatPad = "{:>" + str(formatList[-1]) + "}"
    outputLine = " " + numFormatPad.format("1").replace("1", "*") + " | "
    ## print(outputLine)
    ## sys.exit(0)

    n = 2
    while n <= maxN :
        formatList.append(numFormatMaxLen)

        numFormatPad = "{:>" + str(formatList[-1]) + "}"
        # Note the following is always true if we aren't filtering for ONLY primes. (hacky)
        if isPrime[n] :
            outputLine += numFormatPad.format(base.encode(n)) + "  "
            ## if args.maxDigits < 0 or len(base.encode(n)) <= args.maxDigits :
                ## outputLine += numFormatPad.format(base.encode(n)) + "  "
        n += 1

    ## print(outputLine)
    ## sys.exit(0)

    # Make the horizontal dividing line of the table
    #
    dividingLine = "-"*len(outputLine)
    s = list(dividingLine)
    s[formatList[1] + 2] = '+'

    # Print 2...n on the first row then the dividing line.
    #
    print(outputLine)
    print("".join(s))

    # sys.exit(0)

    # Print the multiplication table.
    #
    n = 2
    while n <= maxN :
        numFormatPad = "{:>"+ str(formatList[1]) + "}"
        outputLine = " " + numFormatPad.format(base.encode(n)) + " | "
        m = 2
        if isPrime[n] :
            while m <= maxN :
                if isPrime[m] :
                    x = n * m
                    numFormatPad = "{:>"+ str(formatList[m]) + "}"
                    if args.maxDigits > 0 :
                        if math.log(x, args.base) <= args.maxDigits - kEpsilon :
                            outputLine += numFormatPad.format(base.encode(x)) + ("* " if n == m else "  ")
                        else :
                            break
                    else :
                        outputLine += numFormatPad.format(base.encode(x)) + ("* " if n == m else "  ")
                m += 1
            ## if not (args.maxDigits > 0 and outputLine[-3:] == " | ") :
            print(outputLine)
        n += 1

if __name__ == '__main__':
    main()
