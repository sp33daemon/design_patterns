class Company(object):

	def accept(self, visitor):
		visitor.visit(self)

	def employee(self, company_employee):
		print(self, "visited by ", company_employee)

	def candidate(self, interview_candidate):
		print(self, "visited by ", interview_candidate)

	def __str__(self):
		return self.__class__.__name__

class Visitor(object):

	def __str__(self):
		return self.__class__.__name__


class company_employee(Visitor):

	def visit(self, company):
		company.employee(self)

class interview_candidate(Visitor):

	def visit(self, company):
		company.candidate(self)


emp = company_employee()
ivc = interview_candidate()
company = Company()


company.accept(emp)
company.accept(ivc)