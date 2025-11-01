# ruff: noqa
from astToolkit import Find
import ast

namespace = 'state'
identifier = 'groupsOfFolds'

Find.While.test.Compare.left.Attribute.value.Name.id.equal(namespace).attr.equal(identifier).ops.at(0).Gt.comparators.at(0).Constant.value.equal(0)

# `id` attribute is type `str`. `str` has an `__eq__` method. Rename/alias it to `equal` to be user friendly.
# id.__eq__(namespace)
# id.equal(namespace)

ast.Call(ast.Attribute(
	ast.Attribute(
		ast.Attribute(
			ast.Call(ast.Attribute(
				ast.Attribute(
					ast.Attribute(
						ast.Call(ast.Attribute(
							ast.Attribute(
								ast.Call(ast.Attribute(
									ast.Attribute(
										ast.Call(ast.Attribute(
											ast.Attribute(
												ast.Attribute(
													ast.Attribute(
														ast.Attribute(
															ast.Attribute(
																ast.Attribute(
																	ast.Attribute(
																		ast.Attribute(ast.Name('Find')
																					, attr='While') # isinstance(node, ast.While)
																		, attr='test')					# node = node.test  # I don't think I mean this in the literal sense: I am trying to illustrate "fungibility".
																	, attr='Compare')				# isinstance(node, ast.Compare)
																, attr='left')								# node = node.left
															, attr='Attribute')						# isinstance(node, ast.Attribute)
														, attr='value')											# node = node.value
													, attr='Name')									# isinstance(node, ast.Name)
												, attr='id')														# node = node.id
											, attr='equal'), args=[ast.Name('namespace')])			# node == `namespace`
										, attr='attr')														# node = ..node..node.attr  # Traversing "up" the chain to find an ast class with the named attribute is no different than identifier scope resolution.
									, attr='equal'), args=[ast.Name('identifier')])					# node == `identifier`
								, attr='ops')															# node = ..node.ops
							, attr='at'), args=[ast.Constant(0)])											# node = node[0]
						, attr='Gt')																# isinstance(node, ast.Gt)
					, attr='comparators')																# node = ..node.comparators
				, attr='at'), args=[ast.Constant(0)])														# node = node[0]
			, attr='Constant')																		# isinstance(node, ast.Constant)
		, attr='value')																							# node = node.value
	, attr='equal'), args=[ast.Constant(0)])														# node == 0

# Matches this

ast.While(
	test=ast.Compare(
		left=ast.Attribute(
			value=ast.Name(
                id='state'),
			attr='groupsOfFolds'),
		ops=[
			ast.Gt()],
		comparators=[
			ast.Constant(
                value=0)]),
	body=[])

