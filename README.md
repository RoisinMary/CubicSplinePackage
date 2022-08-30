Cubic Spline Package

Computes the cubic spline and the derivatives at a grid specified by the user.

The user can specify two input files and a title for the output file.

The first file ('-xy) is a collection of x and y values (given as a .txt file with commas separating successive values, and the x and y vectors separated by '\n') and the second ('-g') is a list of x values (separated by commas), which specifies the x-values at which to evaluate the cubic spline. The result is saved as a .txt file containing the values of the and the values of the first and second derivatives. The user can specify a title for the output using the ('-o') option, otherwise the result is stored as 'out.txt'.

Example:


