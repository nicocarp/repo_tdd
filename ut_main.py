import unittest
import test_expr_aritmetica
import test_calculadora
import ut_supercalculadora

if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite( test_calculadora.TestsCalculadora))
	suite.addTest(unittest.makeSuite( test_expr_aritmetica.TestsExprAritmetica))
	suite.addTest(unittest.makeSuite( ut_supercalculadora.TestsSuperCalculadora))
	unittest.TextTestRunner(verbosity=3).run(suite)