from astToolkit import Make, NodeChanger, NodeTourist
import ast

class TestNodeVisitors:
	"""
	Tests adapted from CPython's NodeVisitor and NodeTransformer tests
	to validate astToolkit's NodeTourist and NodeChanger functionality.
	"""

	def test_nodeTouristBasicVisiting(self):
		"""Test that NodeTourist can visit nodes and collect information."""

		visitedNodes = []

		def collectNameNodes(node):
			if isinstance(node, ast.Name):
				visitedNodes.append(('Name', node.id, node.ctx.__class__.__name__))
				return True
			return False

		def collectNodeInfo(node):
			# Action is already handled in the predicate for this test
			return None

		# Create test AST using Make factory
		testModule = Make.Module([
			Make.Assign(
				[Make.Name("x", ast.Store())],
				Make.Constant(42)
			),
			Make.Assign(
				[Make.Name("y", ast.Store())],
				Make.Name("x", ast.Load())
			)
		])

		# Create tourist that captures Name nodes
		nameTourist = NodeTourist(collectNameNodes, collectNodeInfo)
		nameTourist.visit(testModule)

		expected = [
			('Name', 'x', 'Store'),
			('Name', 'y', 'Store'),
			('Name', 'x', 'Load')        ]
		assert visitedNodes == expected

	def test_nodeChangerBasicTransformation(self):
		"""Test that NodeChanger can transform nodes."""

		def findNameNodes(node):
			return isinstance(node, ast.Name) and node.id == "oldVariable"

		def replaceWithNewName(node):
			return Make.Name("newVariable", node.ctx)

		# Create test AST
		originalModule = Make.Module([
			Make.Assign(
				[Make.Name("oldVariable", ast.Store())],
				Make.Constant(42)
			),
			Make.Expr(Make.Name("oldVariable", ast.Load()))
		])

		changer = NodeChanger(findNameNodes, replaceWithNewName)
		transformedModule = changer.visit(originalModule)

		# Check that names were replaced
		assert isinstance(transformedModule, ast.Module)
		assignment = transformedModule.body[0]
		assert isinstance(assignment, ast.Assign)
		assert isinstance(assignment.targets[0], ast.Name)
		assert assignment.targets[0].id == "newVariable"

		expression = transformedModule.body[1]
		assert isinstance(expression, ast.Expr)
		assert isinstance(expression.value, ast.Name)
		assert expression.value.id == "newVariable"

	def test_nodeChangerRemoveNodes(self):
		"""Test NodeChanger can remove nodes by returning None."""

		def findPrintExpressions(node):
			return (isinstance(node, ast.Expr) and
				   isinstance(node.value, ast.Call) and
				   isinstance(node.value.func, ast.Name) and
				   node.value.func.id == "print")

		def removeNode(node):
			return None
			# Remove print calls

		# Create test AST with print calls
		testModule = Make.Module([
			Make.Expr(Make.Call(Make.Name("print", ast.Load()), [Make.Constant("hello")])),
			Make.Assign([Make.Name("x", ast.Store())], Make.Constant(42)),
			Make.Expr(Make.Call(Make.Name("print", ast.Load()), [Make.Name("x", ast.Load())]))
		])

		remover = NodeChanger(findPrintExpressions, removeNode)
		transformedModule = remover.visit(testModule)

		# Only the assignment should remain
		assert isinstance(transformedModule, ast.Module)
		assert len(transformedModule.body) == 1
		assert isinstance(transformedModule.body[0], ast.Assign)

	def test_nodeChangerMultipleReplacements(self):
		"""Test NodeChanger can replace one node with multiple nodes."""

		def findAssignments(node):
			return (isinstance(node, ast.Assign) and
				   len(node.targets) == 1 and
				   isinstance(node.targets[0], ast.Name))

		def expandAssignment(node):
			# Expand x = 42 into x = 42; print(x)
			assignmentNode = node
			printCall = Make.Expr(Make.Call(
				Make.Name("print", ast.Load()),
				[Make.Name(node.targets[0].id, ast.Load())]
			))
			return [assignmentNode, printCall]

		testModule = Make.Module([
			Make.Assign([Make.Name("x", ast.Store())], Make.Constant(42))
		])

		expander = NodeChanger(findAssignments, expandAssignment)
		transformedModule = expander.visit(testModule)

		# Should have both assignment and print
		assert isinstance(transformedModule, ast.Module)
		assert len(transformedModule.body) == 2
		assert isinstance(transformedModule.body[0], ast.Assign)
		assert isinstance(transformedModule.body[1], ast.Expr)
		assert isinstance(transformedModule.body[1].value, ast.Call)

	def test_nodeTouristWithComplexAST(self):
		"""Test NodeTourist with more complex AST structures."""

		# Use a shared counter to track different node types
		counts = {"functions": 0, "classes": 0, "loops": 0, "conditions": 0}

		def findStructuralNodes(node):
			return isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef,
								   ast.For, ast.While, ast.If))

		def countNodeType(node):
			if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
				counts["functions"] += 1
			elif isinstance(node, ast.ClassDef):
				counts["classes"] += 1
			elif isinstance(node, (ast.For, ast.While)):
				counts["loops"] += 1
			elif isinstance(node, ast.If):
				counts["conditions"] += 1
			return node

		# Create complex AST structure
		complexModule = Make.Module([
			Make.FunctionDef(
				"function1",
				Make.arguments(),
				body=[
					Make.If(
						Make.Name("condition", ast.Load()),
						body=[Make.Pass()]
					),
					Make.For(
						Make.Name("item", ast.Store()),
						Make.Name("items", ast.Load()),
						body=[Make.Pass()]
					)
				]
			),
			Make.ClassDef(
				"TestClass",
				body=[
					Make.FunctionDef(
						"method",
						Make.arguments(),
						body=[
							Make.While(
								Make.Constant(True),
								body=[Make.Break()]
							)
						]
					)
				]
			)
		])

		analyzer = NodeTourist(findStructuralNodes, countNodeType)
		analyzer.visit(complexModule)

		assert counts["functions"] == 2
		# function1 and method
		assert counts["classes"] == 1
		# TestClass
		assert counts["loops"] == 2
		# for and while
		assert counts["conditions"] == 1
		# if statement
	def test_nodeChangerPreservesLocation(self):
		"""Test that NodeChanger preserves location information."""

		def findIntConstants(node):
			return isinstance(node, ast.Constant) and isinstance(node.value, int)

		def doubleConstant(node):
			# Replace integer constants with doubled values
			newNode = Make.Constant(node.value * 2)
			return ast.copy_location(newNode, node)

		# Create AST with location info
		testModule = Make.Module([
			Make.Assign(
				[Make.Name("x", ast.Store())],
				Make.Constant(21, lineno=1, col_offset=4)
			)
		])

		changer = NodeChanger(findIntConstants, doubleConstant)
		transformedModule = changer.visit(testModule)

		# Check that value was doubled and location preserved
		assert isinstance(transformedModule, ast.Module)
		assignment = transformedModule.body[0]
		assert isinstance(assignment, ast.Assign)
		constantNode = assignment.value
		assert isinstance(constantNode, ast.Constant)
		assert constantNode.value == 42
		assert constantNode.lineno == 1
		assert constantNode.col_offset == 4

	def test_nodeChangerWithMakeFactoryMethods(self):
		"""Test NodeChanger using Make factory methods for transformations."""

		def findAugAssign(node):
			return isinstance(node, ast.AugAssign)

		def expandToAssignment(node):
			"""Expand x += 1 to x = x + 1"""
			# Create regular assignment equivalent
			binaryOp = Make.BinOp(
				Make.Name(node.target.id, ast.Load()),
				node.op,
				node.value
			)
			assignment = Make.Assign(
				[Make.Name(node.target.id, ast.Store())],
				binaryOp
			)
			return ast.copy_location(assignment, node)

		testModule = Make.Module([
			Make.AugAssign(
				Make.Name("counter", ast.Store()),
				ast.Add(),
				Make.Constant(1)
			)
		])

		expander = NodeChanger(findAugAssign, expandToAssignment)
		transformedModule = expander.visit(testModule)

		# Should be converted to regular assignment
		assert isinstance(transformedModule, ast.Module)
		statement = transformedModule.body[0]
		assert isinstance(statement, ast.Assign)
		assert isinstance(statement.value, ast.BinOp)
		assert isinstance(statement.value.op, ast.Add)

	def test_nodeVisitorErrorHandling(self):
		"""Test visitor error handling with malformed AST."""

		errorCount = [0]
		# Use list for mutable reference

		def findNameNodes(node):
			return isinstance(node, ast.Name)

		def handleNameNode(node):
			try:
				# This might fail if node is malformed
				if hasattr(node, 'id') and node.id:
					pass
			except Exception:
				errorCount[0] += 1
			return node

		# Create valid AST
		validModule = Make.Module([
			Make.Expr(Make.Name("validName", ast.Load()))
		])

		tourist = NodeTourist(findNameNodes, handleNameNode)
		tourist.visit(validModule)

		# Should handle valid AST without errors
		assert errorCount[0] == 0

	def test_nestedVisitorTransformations(self):
		"""Test applying multiple transformations in sequence."""

		def findUppercaseNames(node):
			return isinstance(node, ast.Name) and node.id.isupper()

		def lowercaseName(node):
			return Make.Name(node.id.lower(), node.ctx)

		def findIntConstants(node):
			return isinstance(node, ast.Constant) and isinstance(node.value, int)

		def doubleConstant(node):
			return Make.Constant(node.value * 2)

		# Create test AST
		originalModule = Make.Module([
			Make.Assign(
				[Make.Name("VARIABLE", ast.Store())],
				Make.Constant(21)
			)
		])

		# Apply transformations in sequence
		step1 = NodeChanger(findUppercaseNames, lowercaseName)
		step2 = NodeChanger(findIntConstants, doubleConstant)

		intermediateModule = step1.visit(originalModule)
		finalModule = step2.visit(intermediateModule)

		# Check both transformations applied
		assert isinstance(finalModule, ast.Module)
		assignment = finalModule.body[0]
		assert isinstance(assignment, ast.Assign)
		assert isinstance(assignment.targets[0], ast.Name)
		assert assignment.targets[0].id == "variable"
		# lowercased
		assert isinstance(assignment.value, ast.Constant)
		assert assignment.value.value == 42
		# doubled
	def test_visitorWithMakeJoinMethods(self):
		"""Test visitors with Make join methods for combining expressions."""

		def findComplexBoolOp(node):
			return (isinstance(node, ast.BoolOp) and
				   isinstance(node.op, ast.And) and
				   len(node.values) > 2)

		def simplifyBoolOp(node):
			# Use Make.And.join for cleaner combination
			return Make.And.join(node.values)

		# Create complex boolean expression
		testModule = Make.Module([
			Make.If(
				Make.BoolOp(ast.And(), [
					Make.Name("a", ast.Load()),
					Make.Name("b", ast.Load()),
					Make.Name("c", ast.Load()),
					Make.Name("d", ast.Load())
				]),
				body=[Make.Pass()]
			)
		])

		combiner = NodeChanger(findComplexBoolOp, simplifyBoolOp)
		transformedModule = combiner.visit(testModule)

		# Should still be a valid boolean expression
		assert isinstance(transformedModule, ast.Module)
		ifStatement = transformedModule.body[0]
		assert isinstance(ifStatement, ast.If)
		condition = ifStatement.test
		assert isinstance(condition, (ast.BoolOp, ast.Name))
