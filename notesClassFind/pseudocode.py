from collections.abc import Callable

# pseudo-code

# "attr" is the `str` that the user typed in after a dot, `.`: "attr" is _not_ a diminutive of attribute.
# It is a proper noun, so case must be preserved; do not use "attr" to mean anything else.
# attribute is a method, class, or property of Find.

class Find:

	FindInstance = list[Callable]
	attrChain: list[str] = list()
	attributesForMatching = '1st level attributes'
	attrActive: str = __getattr__(self, attr)

	node = '.'.join(['node', *attrChain])
	attrActive = Find.attrActive
	FindInstance = [Find(attrActive(node)), *FindInstance]
	attrChain.append(attrActive)

	# chain_attr is not None, so do this loop until no more attr

	attrActive: str = __getattr__(self, attr)
	attributesForMatching = attrChain[-1] + '<- this attr: valid attributes from Find.attr and from type[Find.attr]. I think of this as a very localized namespace.'
	if attrActive not in attributesForMatching:
		attrChain.pop()
		# repeat

	attrParent = attrChain.pop()
	_localAttribute = Find.attrParent.attrActive() # The value of `Find._localAttribute` is stored in `Find.attrParent.attrActive`, so "resolve" the name.
	attrActive = Find._localAttribute
	node = '.'.join(['node', *attrChain])
	if args:
		FindInstance = [Find(attrActive(node, args)), *FindInstance]
	else:
		FindInstance = [Find(attrActive(node)), *FindInstance]
		attrChain.append(attrActive)
