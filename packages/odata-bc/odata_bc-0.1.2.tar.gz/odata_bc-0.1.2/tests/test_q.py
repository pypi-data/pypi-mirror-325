from datetime import date

from odata import Q


def test_eq_operator():
   """
   Test equality operator (==) on Q expressions.
   Verifies that Q("field") == value produces correct OData filter syntax.
   """
   expr = Q("Type") == "Sale"
   assert str(expr) == "(Type eq 'Sale')"

def test_date_comparison():
   """
   Test date comparison operations.
   Verifies date objects are properly formatted in ISO format.
   """
   expr = Q("Date") >= date(2024, 1, 1)
   assert str(expr) == "(Date ge 2024-01-01)"

def test_and_operator():
   """
   Test logical AND operator (&) between Q expressions.
   Verifies proper parentheses and 'and' keyword placement.
   """
   expr = (Q("Date") >= date(2024, 1, 1)) & (Q("Type") == "Sale")
   assert str(expr) == "((Date ge 2024-01-01) and (Type eq 'Sale'))"

def test_or_operator():
   """
   Test logical OR operator (|) between Q expressions.
   Verifies proper parentheses and 'or' keyword placement.
   """
   expr = (Q("Type") == "Sale") | (Q("Type") == "Purchase")
   assert str(expr) == "((Type eq 'Sale') or (Type eq 'Purchase'))"

def test_complex_expression():
   """
   Test complex nested expressions combining AND and OR operators.
   Verifies correct operator precedence and parentheses nesting.
   
   Tests the expression:
   ((date >= start) AND (date <= end)) AND (type == sale OR type == purchase)
   """
   expr = ((Q("Date") >= date(2024, 1, 1)) & (Q("Date") <= date(2024, 1, 31))) & \
          ((Q("Type") == "Sale") | (Q("Type") == "Purchase"))
   expected = "(((Date ge 2024-01-01) and (Date le 2024-01-31)) and ((Type eq 'Sale') or (Type eq 'Purchase')))"
   assert str(expr) == expected