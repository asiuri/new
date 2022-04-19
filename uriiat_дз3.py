import fractions

fract = fractions.Fraction(122, 124) + fractions.Fraction(1, 2)
print("Numerator: {}".format(fract.numerator))
print("Denominator: {}".format(fract.denominator))


fract = fractions.Fraction(122, 124) - fractions.Fraction(1, 2)
print("Numerator: {}".format(fract.numerator))
print("Denominator: {}".format(fract.denominator))


fract = fractions.Fraction(122, 124)  *fractions.Fraction(1, 2)
print("Numerator: {}".format(fract.numerator))
print("Denominator: {}".format(fract.denominator))


fract = fractions.Fraction(122, 124) / fractions.Fraction(1, 2)
print("Numerator: {}".format(fract.numerator))
print("Denominator: {}".format(fract.denominator))


fract = fractions.Fraction(122, 124) // fractions.Fraction(1, 2)
print("Numerator: {}".format(fract.numerator))
print("Denominator: {}".format(fract.denominator))