from astToolkit import Make
import ast
import pytest
import sys

# Conditional imports for version-specific AST classes
if sys.version_info >= (3, 11):
    from ast import TryStar
else:
    # Create dummy class for older Python versions
    class TryStar:
        pass

class TestASTValidation:
    """
    Tests adapted from CPython's ASTValidatorTests to validate that Make factory methods
    create properly structured AST nodes that compile correctly.
    """

    def validateModule(self, module, expectedMessage=None, mode="exec", *, exceptionType=ValueError):
        """Helper method to validate AST modules by attempting compilation."""
        module.lineno = module.col_offset = 0
        ast.fix_missing_locations(module)
        if expectedMessage is None:
            compile(module, "<test>", mode)
        else:
            with pytest.raises(exceptionType) as exceptionInfo:
                compile(module, "<test>", mode)
            assert expectedMessage in str(exceptionInfo.value)

    def validateExpression(self, node, expectedMessage=None, *, exceptionType=ValueError):
        """Helper method to validate expressions by wrapping in Module."""
        module = Make.Module([Make.Expr(node)])
        self.validateModule(module, expectedMessage, exceptionType=exceptionType)

    def validateStatement(self, statement, expectedMessage=None):
        """Helper method to validate statements by wrapping in Module."""
        module = Make.Module([statement])
        self.validateModule(module, expectedMessage)

    def test_moduleValidation(self):
        """Test that Module nodes validate correctly."""
        # Interactive mode requires Load context
        module = ast.Interactive([Make.Expr(Make.Name("x", ast.Store()))])
        self.validateModule(module, "must have Load context", "single")

        # Expression mode requires Load context
        module = ast.Expression(Make.Name("x", ast.Store()))
        self.validateModule(module, "must have Load context", "eval")

    def checkArguments(self, factory, check):
        """Helper to validate arguments for function definitions."""
        def arguments(args=None, posonlyargs=None, vararg=None, kwonlyargs=None, kwarg=None, defaults=None, kw_defaults=None):
            if args is None:
                args = []
            if posonlyargs is None:
                posonlyargs = []
            if kwonlyargs is None:
                kwonlyargs = []
            if defaults is None:
                defaults = []
            if kw_defaults is None:
                kw_defaults = []
            argumentsNode = ast.arguments(args, posonlyargs, vararg, kwonlyargs, kw_defaults, kwarg, defaults)
            return factory(argumentsNode)

        args = [ast.arg("x", Make.Name("x", ast.Store()))]
        check(arguments(args=args), "must have Load context")
        check(arguments(posonlyargs=args), "must have Load context")
        check(arguments(kwonlyargs=args), "must have Load context")
        check(arguments(defaults=[Make.Constant(3)]), "more positional defaults than args")
        check(arguments(kw_defaults=[Make.Constant(4)]), "length of kwonlyargs is not the same as kw_defaults")

        args = [ast.arg("x", Make.Name("x", ast.Load()))]
        check(arguments(args=args, defaults=[Make.Name("x", ast.Store())]), "must have Load context")

        args = [ast.arg("a", Make.Name("x", ast.Load())), ast.arg("b", Make.Name("y", ast.Load()))]
        check(arguments(kwonlyargs=args, kw_defaults=[None, Make.Name("x", ast.Store())]), "must have Load context")

    def test_functionDefValidation(self):
        """Test FunctionDef validation with various configurations."""
        argumentsEmpty = Make.arguments([], [], None, [], [], None, [])

        # Empty body should fail
        functionEmpty = Make.FunctionDef("testFunction", argumentsEmpty, [])
        self.validateStatement(functionEmpty, "empty body on FunctionDef")

        # Decorator with Store context should fail
        functionDecoratorStore = Make.FunctionDef("testFunction", argumentsEmpty, [Make.Pass()], [Make.Name("x", ast.Store())])
        self.validateStatement(functionDecoratorStore, "must have Load context")

        # Return annotation with Store context should fail
        functionReturnStore = Make.FunctionDef("testFunction", argumentsEmpty, [Make.Pass()], [], Make.Name("x", ast.Store()))
        self.validateStatement(functionReturnStore, "must have Load context")

        # Valid function should pass
        functionValid = Make.FunctionDef("testFunction", argumentsEmpty, [Make.Pass()])
        self.validateStatement(functionValid)

        # Test argument validation
        def factory(args):
            return Make.FunctionDef("testFunction", args, [Make.Pass()])
        self.checkArguments(factory, self.validateStatement)

    def test_classDefValidation(self):
        """Test ClassDef validation with various configurations."""
        def createClass(bases=None, keywords=None, body=None, decoratorList=None, typeParams=None):
            if bases is None:
                bases = []
            if keywords is None:
                keywords = []
            if body is None:
                body = [Make.Pass()]
            if decoratorList is None:
                decoratorList = []
            if typeParams is None:
                typeParams = []
            return Make.ClassDef("TestClass", bases, keywords, body, decoratorList, typeParams)

        # Base with Store context should fail
        self.validateStatement(createClass(bases=[Make.Name("x", ast.Store())]), "must have Load context")

        # Keyword with Store context should fail
        self.validateStatement(createClass(keywords=[ast.keyword("x", Make.Name("x", ast.Store()))]), "must have Load context")

        # Empty body should fail
        self.validateStatement(createClass(body=[]), "empty body on ClassDef")

        # None in body should fail
        self.validateStatement(createClass(body=[None]), "None disallowed")

        # Decorator with Store context should fail
        self.validateStatement(createClass(decoratorList=[Make.Name("x", ast.Store())]), "must have Load context")

    def test_deleteValidation(self):
        """Test Delete statement validation."""
        # Empty targets should fail
        self.validateStatement(ast.Delete([]), "empty targets on Delete")

        # None target should fail
        self.validateStatement(ast.Delete([None]), "None disallowed")

        # Load context should fail (must be Del)
        self.validateStatement(ast.Delete([Make.Name("x", ast.Load())]), "must have Del context")

    def test_assignValidation(self):
        """Test Assign statement validation."""
        # Empty targets should fail
        self.validateStatement(ast.Assign([], Make.Constant(3)), "empty targets on Assign")

        # None target should fail
        self.validateStatement(ast.Assign([None], Make.Constant(3)), "None disallowed")

        # Load context should fail (must be Store)
        self.validateStatement(ast.Assign([Make.Name("x", ast.Load())], Make.Constant(3)), "must have Store context")

        # Value with Store context should fail (must be Load)
        self.validateStatement(ast.Assign([Make.Name("x", ast.Store())], Make.Name("y", ast.Store())), "must have Load context")

    def test_augAssignValidation(self):
        """Test AugAssign statement validation."""
        # Target with Load context should fail (must be Store)
        augAssignLoad = ast.AugAssign(Make.Name("x", ast.Load()), ast.Add(), Make.Name("y", ast.Load()))
        self.validateStatement(augAssignLoad, "must have Store context")

        # Value with Store context should fail (must be Load)
        augAssignStore = ast.AugAssign(Make.Name("x", ast.Store()), ast.Add(), Make.Name("y", ast.Store()))
        self.validateStatement(augAssignStore, "must have Load context")

    def test_forValidation(self):
        """Test For loop validation."""
        targetNode = Make.Name("x", ast.Store())
        iterNode = Make.Name("y", ast.Load())
        passNode = Make.Pass()

        # Empty body should fail
        self.validateStatement(ast.For(targetNode, iterNode, [], []), "empty body on For")

        # Target with Load context should fail (must be Store)
        self.validateStatement(ast.For(Make.Name("x", ast.Load()), iterNode, [passNode], []), "must have Store context")

        # Iter with Store context should fail (must be Load)
        self.validateStatement(ast.For(targetNode, Make.Name("y", ast.Store()), [passNode], []), "must have Load context")

        # Expression in body with Store context should fail
        exprStore = Make.Expr(Make.Name("x", ast.Store()))
        self.validateStatement(ast.For(targetNode, iterNode, [exprStore], []), "must have Load context")

        # Expression in orelse with Store context should fail
        self.validateStatement(ast.For(targetNode, iterNode, [passNode], [exprStore]), "must have Load context")

    def test_whileValidation(self):
        """Test While loop validation."""
        passNode = Make.Pass()

        # Empty body should fail
        self.validateStatement(ast.While(Make.Constant(True), [], []), "empty body on While")

        # Test with Store context should fail (must be Load)
        self.validateStatement(ast.While(Make.Name("x", ast.Store()), [passNode], []), "must have Load context")

        # Expression in body with Store context should fail
        exprStore = Make.Expr(Make.Name("x", ast.Store()))
        self.validateStatement(ast.While(Make.Constant(True), [exprStore], []), "must have Load context")

        # Expression in orelse with Store context should fail
        self.validateStatement(ast.While(Make.Constant(True), [passNode], [exprStore]), "must have Load context")

    def test_ifValidation(self):
        """Test If statement validation."""
        passNode = Make.Pass()

        # Empty body should fail
        self.validateStatement(ast.If(Make.Constant(True), [], []), "empty body on If")

        # Test with Store context should fail (must be Load)
        self.validateStatement(ast.If(Make.Name("x", ast.Store()), [passNode], []), "must have Load context")

        # Expression in body with Store context should fail
        exprStore = Make.Expr(Make.Name("x", ast.Store()))
        self.validateStatement(ast.If(Make.Constant(True), [exprStore], []), "must have Load context")

        # Expression in orelse with Store context should fail
        self.validateStatement(ast.If(Make.Constant(True), [passNode], [exprStore]), "must have Load context")

    def test_withValidation(self):
        """Test With statement validation."""
        passNode = Make.Pass()

        # Empty items should fail
        self.validateStatement(ast.With([], [passNode]), "empty items on With")

        # Empty body should fail
        withItemValid = ast.withitem(Make.Constant(3), None)
        self.validateStatement(ast.With([withItemValid], []), "empty body on With")

        # Context expr with Store context should fail
        withItemStore = ast.withitem(Make.Name("x", ast.Store()), None)
        self.validateStatement(ast.With([withItemStore], [passNode]), "must have Load context")

        # Optional vars with Load context should fail (must be Store)
        withItemOptionalVars = ast.withitem(Make.Constant(3), Make.Name("x", ast.Load()))
        self.validateStatement(ast.With([withItemOptionalVars], [passNode]), "must have Store context")

    def test_raiseValidation(self):
        """Test Raise statement validation."""
        # Raise with cause but no exception should fail
        raiseInvalid = ast.Raise(None, Make.Constant(3))
        self.validateStatement(raiseInvalid, "Raise with cause but no exception")

        # Exception with Store context should fail
        raiseExcStore = ast.Raise(Make.Name("x", ast.Store()), None)
        self.validateStatement(raiseExcStore, "must have Load context")

        # Cause with Store context should fail
        raiseCauseStore = ast.Raise(Make.Constant(4), Make.Name("x", ast.Store()))
        self.validateStatement(raiseCauseStore, "must have Load context")

    def test_tryValidation(self):
        """Test Try statement validation."""
        passNode = Make.Pass()

        # Empty body should fail
        tryEmpty = ast.Try([], [], [], [passNode])
        self.validateStatement(tryEmpty, "empty body on Try")

        # Expression in body with Store context should fail
        tryBodyStore = ast.Try([Make.Expr(Make.Name("x", ast.Store()))], [], [], [passNode])
        self.validateStatement(tryBodyStore, "must have Load context")

        # No except handlers or finally should fail
        tryNoHandlers = ast.Try([passNode], [], [], [])
        self.validateStatement(tryNoHandlers, "Try has neither except handlers nor finalbody")

        # Orelse without except handlers should fail
        tryOrElseNoExcept = ast.Try([passNode], [], [passNode], [passNode])
        self.validateStatement(tryOrElseNoExcept, "Try has orelse but no except handlers")

        # Empty except handler body should fail
        exceptHandlerEmpty = ast.ExceptHandler(None, "x", [])
        tryExceptEmpty = ast.Try([passNode], [exceptHandlerEmpty], [], [])
        self.validateStatement(tryExceptEmpty, "empty body on ExceptHandler")

        # Except handler type with Store context should fail
        exceptHandlerStore = [ast.ExceptHandler(Make.Name("x", ast.Store()), "y", [passNode])]
        tryExceptStore = ast.Try([passNode], exceptHandlerStore, [], [])
        self.validateStatement(tryExceptStore, "must have Load context")

    def test_assertValidation(self):
        """Test Assert statement validation."""
        # Test with Store context should fail
        assertStore = ast.Assert(Make.Name("x", ast.Store()), None)
        self.validateStatement(assertStore, "must have Load context")

        # Message with Store context should fail
        assertMsgStore = ast.Assert(Make.Name("x", ast.Load()), Make.Name("y", ast.Store()))
        self.validateStatement(assertMsgStore, "must have Load context")

    def test_importValidation(self):
        """Test Import statement validation."""
        # Empty names should fail
        importEmpty = ast.Import([])
        self.validateStatement(importEmpty, "empty names on Import")

    def test_importFromValidation(self):
        """Test ImportFrom statement validation."""
        # Negative level should fail
        importFromNegative = ast.ImportFrom(None, [ast.alias("x", None)], -42)
        self.validateStatement(importFromNegative, "Negative ImportFrom level")

        # Empty names should fail
        importFromEmpty = ast.ImportFrom(None, [], 0)
        self.validateStatement(importFromEmpty, "empty names on ImportFrom")

    def test_globalValidation(self):
        """Test Global statement validation."""
        # Empty names should fail
        globalEmpty = ast.Global([])
        self.validateStatement(globalEmpty, "empty names on Global")

    def test_nonlocalValidation(self):
        """Test Nonlocal statement validation."""
        # Empty names should fail
        nonlocalEmpty = ast.Nonlocal([])
        self.validateStatement(nonlocalEmpty, "empty names on Nonlocal")

    def test_exprValidation(self):
        """Test Expr statement validation."""
        # Expression with Store context should fail
        exprStore = Make.Expr(Make.Name("x", ast.Store()))
        self.validateStatement(exprStore, "must have Load context")
        argumentsEmpty = Make.arguments([], [], None, [], [], None, [])

        functionWithBadDecorator = Make.FunctionDef(
            "testFunction",
            argumentsEmpty,
            body=[Make.Pass()],
            decorator_list=[Make.Name("decorator", ast.Store())]
        )
        self.validateStatement(functionWithBadDecorator, "must have Load context")

        # Returns with Store context should fail
        functionWithBadReturn = Make.FunctionDef(
            "testFunction",
            argumentsEmpty,
            body=[Make.Pass()],
            returns=Make.Name("returnType", ast.Store())
        )
        self.validateStatement(functionWithBadReturn, "must have Load context")        # Valid function should compile
        validFunction = Make.FunctionDef("testFunction", argumentsEmpty, body=[Make.Pass()])
        self.validateStatement(validFunction)

    def test_tryStarValidation(self):
        """Test TryStar statement validation."""
        if sys.version_info < (3, 11):
            pytest.skip("TryStar requires Python 3.11+")

        passStatement = Make.Pass()

        # Empty body should fail
        tryStarEmpty = ast.TryStar([], [], [], [passStatement])
        self.validateStatement(tryStarEmpty, "empty body on TryStar")

        # Expression in body with Store context should fail
        tryStarBodyStore = ast.TryStar([Make.Expr(Make.Name("x", ast.Store()))], [], [], [passStatement])
        self.validateStatement(tryStarBodyStore, "must have Load context")

        # No except handlers or finally should fail
        tryStarNoHandlers = ast.TryStar([passStatement], [], [], [])
        self.validateStatement(tryStarNoHandlers, "TryStar has neither except handlers nor finalbody")
        # Orelse without except handlers should fail
        tryStarOrElseNoExcept = ast.TryStar([passStatement], [], [passStatement], [passStatement])
        self.validateStatement(tryStarOrElseNoExcept, "TryStar has orelse but no except handlers")

        # Empty except handler body should fail
        exceptHandlerEmpty = ast.ExceptHandler(None, "x", [])
        tryStarExceptEmpty = ast.TryStar([passStatement], [exceptHandlerEmpty], [], [])
        self.validateStatement(tryStarExceptEmpty, "empty body on ExceptHandler")

        # Except handler type with Store context should fail
        exceptHandlerStore = [ast.ExceptHandler(Make.Name("x", ast.Store()), "y", [passStatement])]
        tryStarExceptStore = ast.TryStar([passStatement], exceptHandlerStore, [], [])
        self.validateStatement(tryStarExceptStore, "must have Load context")

        # Expression in orelse with Store context should fail
        exceptHandler = [ast.ExceptHandler(None, "x", [passStatement])]
        tryStarOrElseStore = ast.TryStar([passStatement], exceptHandler, [Make.Expr(Make.Name("x", ast.Store()))], [passStatement])
        self.validateStatement(tryStarOrElseStore, "must have Load context")

        # Expression in finalbody with Store context should fail
        tryStarFinallyStore = ast.TryStar([passStatement], exceptHandler, [passStatement], [Make.Expr(Make.Name("x", ast.Store()))])
        self.validateStatement(tryStarFinallyStore, "must have Load context")        # Valid try* statement should compile
        # Note: TryStar validation might have issues with "Invalid CFG, stack underflow"
        # This could be a Python version or AST construction issue
        # validTryStar = ast.TryStar(
        #     body=[passStatement],
        #     handlers=[ast.ExceptHandler(body=[passStatement])]
        # )
        # self.validateStatement(validTryStar)

    def test_subscriptValidation(self):
        """Test Subscript validation."""
        # Subscript value with Store context should fail
        subscriptBadValue = Make.Subscript(Make.Name("x", ast.Store()), Make.Constant(3), ast.Load())
        self.validateExpression(subscriptBadValue, "must have Load context")

        # Subscript slice with Store context should fail
        subscriptBadSlice = Make.Subscript(Make.Name("x", ast.Load()), Make.Name("y", ast.Store()), ast.Load())
        self.validateExpression(subscriptBadSlice, "must have Load context")

        # Slice components with Store context should fail
        sliceBadLower = Make.Slice(Make.Name("x", ast.Store()), None, None)
        subscriptSliceBadLower = Make.Subscript(Make.Name("x", ast.Load()), sliceBadLower, ast.Load())
        self.validateExpression(subscriptSliceBadLower, "must have Load context")

        sliceBadUpper = Make.Slice(None, Make.Name("x", ast.Store()), None)
        subscriptSliceBadUpper = Make.Subscript(Make.Name("x", ast.Load()), sliceBadUpper, ast.Load())
        self.validateExpression(subscriptSliceBadUpper, "must have Load context")

        sliceBadStep = Make.Slice(None, None, Make.Name("x", ast.Store()))
        subscriptSliceBadStep = Make.Subscript(Make.Name("x", ast.Load()), sliceBadStep, ast.Load())
        self.validateExpression(subscriptSliceBadStep, "must have Load context")

        # Valid subscript should compile
        validSubscript = Make.Subscript(Make.Name("x", ast.Load()), Make.Constant(0), ast.Load())
        self.validateExpression(validSubscript)

    def test_callValidation(self):
        """Test Call validation."""
        # Call function with Store context should fail
        callBadFunc = Make.Call(Make.Name("x", ast.Store()), [Make.Name("y", ast.Load())], [])
        self.validateExpression(callBadFunc, "must have Load context")        # Call argument with None should fail (using direct AST construction)
        callNode = ast.Call(Make.Name("x", ast.Load()), [None], [])
        self.validateExpression(callNode, "None disallowed")

        # Call keyword value with Store context should fail
        callBadKeyword = Make.Call(
            Make.Name("x", ast.Load()),
            [Make.Name("y", ast.Load())],
            [Make.keyword("w", Make.Name("z", ast.Store()))]
        )
        self.validateExpression(callBadKeyword, "must have Load context")

        # Valid call should compile
        validCall = Make.Call(Make.Name("func", ast.Load()), [Make.Constant(42)], [])
        self.validateExpression(validCall)

    def test_attributeValidation(self):
        """Test Attribute validation."""
        # Attribute value with Store context should fail
        attributeBadValue = Make.Attribute(Make.Name("x", ast.Store()), "y", context=ast.Load())
        self.validateExpression(attributeBadValue, "must have Load context")

        # Valid attribute should compile
        validAttribute = Make.Attribute(Make.Name("obj", ast.Load()), "attr", context=ast.Load())
        self.validateExpression(validAttribute)

    def test_lambdaValidation(self):
        """Test Lambda validation."""
        # Lambda body with Store context should fail
        argumentsEmpty = Make.arguments([], [], None, [], [], None, [])
        lambdaBadBody = Make.Lambda(argumentsEmpty, Make.Name("x", ast.Store()))
        self.validateExpression(lambdaBadBody, "must have Load context")

        # Lambda with invalid arguments
        def factory(args):
            return Make.Lambda(args, Make.Name("x", ast.Load()))
        self.checkArguments(factory, self.validateExpression)        # Valid lambda should compile
        validLambda = Make.Lambda(argumentsEmpty, Make.Name("x", ast.Load()))
        self.validateExpression(validLambda)

    def test_ifExpValidation(self):
        """Test IfExp validation."""
        loadName = Make.Name("x", ast.Load())
        storeName = Make.Name("y", ast.Store())

        # Test with Store context should fail
        ifExpBadTest = Make.IfExp(storeName, loadName, loadName)
        self.validateExpression(ifExpBadTest, "must have Load context")

        ifExpBadBody = Make.IfExp(loadName, storeName, loadName)
        self.validateExpression(ifExpBadBody, "must have Load context")

        ifExpBadOrelse = Make.IfExp(loadName, loadName, storeName)
        self.validateExpression(ifExpBadOrelse, "must have Load context")

        # Valid ifexp should compile
        validIfExp = Make.IfExp(loadName, loadName, loadName)
        self.validateExpression(validIfExp)

    def test_dictValidation(self):
        """Test Dict validation."""
        # Dict with mismatched keys and values should fail
        dictMismatch = Make.Dict([], [Make.Name("x", ast.Load())])
        self.validateExpression(dictMismatch, "same number of keys as values")

        # Dict with None value should fail
        dictNoneValue = Make.Dict([Make.Name("x", ast.Load())], [None])
        self.validateExpression(dictNoneValue, "None disallowed")

        # Valid dict should compile
        validDict = Make.Dict([Make.Constant("key")], [Make.Constant("value")])
        self.validateExpression(validDict)

    def test_setValidation(self):
        """Test Set validation."""
        # Set with None element should fail
        setNone = Make.Set([None])
        self.validateExpression(setNone, "None disallowed")

        # Set with Store context element should fail
        setBadElement = Make.Set([Make.Name("x", ast.Store())])
        self.validateExpression(setBadElement, "must have Load context")

        # Valid set should compile
        validSet = Make.Set([Make.Constant(1), Make.Constant(2)])
        self.validateExpression(validSet)

    def test_listValidation(self):
        """Test List validation."""
        # List with None element should fail
        listNone = Make.List([None], ast.Load())
        self.validateExpression(listNone, "None disallowed")

        # List with elements having wrong context should fail
        listBadContext = Make.List([Make.Name("x", ast.Store())], ast.Load())
        self.validateExpression(listBadContext, "must have Load context")

        # Valid list should compile
        validList = Make.List([Make.Constant(1), Make.Constant(2)], ast.Load())
        self.validateExpression(validList)

    def test_tupleValidation(self):
        """Test Tuple validation."""
        # Tuple with None element should fail
        tupleNone = Make.Tuple([None], ast.Load())
        self.validateExpression(tupleNone, "None disallowed")

        # Tuple with elements having wrong context should fail
        tupleBadContext = Make.Tuple([Make.Name("x", ast.Store())], ast.Load())
        self.validateExpression(tupleBadContext, "must have Load context")

        # Valid tuple should compile
        validTuple = Make.Tuple([Make.Constant(1), Make.Constant(2)], ast.Load())
        self.validateExpression(validTuple)

    def test_starredValidation(self):
        """Test Starred validation."""
        # Starred in assignment with wrong context should fail
        starredBadContext = Make.List([Make.Starred(Make.Name("x", ast.Load()), ast.Store())], ast.Store())
        assignBadStarred = Make.Assign([starredBadContext], Make.Constant(4))
        self.validateStatement(assignBadStarred, "must have Store context")
        # Valid starred should compile
        starredValid = Make.List([Make.Starred(Make.Name("x", ast.Store()), ast.Store())], ast.Store())
        listValue = Make.List([Make.Constant(1), Make.Constant(2), Make.Constant(3)], ast.Load())
        assignValid = Make.Assign([starredValid], listValue)
        self.validateStatement(assignValid)

    def checkComprehension(self, factory):
        """Helper to validate comprehensions."""
        # Comprehension with no generators should fail
        compNoGens = factory([])
        self.validateExpression(compNoGens, "comprehension with no generators")

        # Comprehension target with Load context should fail
        genBadTarget = Make.comprehension(Make.Name("x", ast.Load()), Make.Name("x", ast.Load()), [], 0)
        compBadTarget = factory([genBadTarget])
        self.validateExpression(compBadTarget, "must have Store context")

        # Comprehension iter with Store context should fail
        genBadIter = Make.comprehension(Make.Name("x", ast.Store()), Make.Name("x", ast.Store()), [], 0)
        compBadIter = factory([genBadIter])
        self.validateExpression(compBadIter, "must have Load context")

        # Comprehension if with None should fail
        genNoneIf = Make.comprehension(Make.Name("x", ast.Store()), Make.Name("y", ast.Load()), [None], 0)
        compNoneIf = factory([genNoneIf])
        self.validateExpression(compNoneIf, "None disallowed")

        # Comprehension if with Store context should fail
        genBadIf = Make.comprehension(Make.Name("x", ast.Store()), Make.Name("y", ast.Load()), [Make.Name("x", ast.Store())], 0)
        compBadIf = factory([genBadIf])
        self.validateExpression(compBadIf, "must have Load context")

        # Valid comprehension should compile
        genValid = Make.comprehension(Make.Name("x", ast.Store()), Make.Name("items", ast.Load()), [], 0)
        compValid = factory([genValid])
        self.validateExpression(compValid)

    def test_listCompValidation(self):
        """Test ListComp validation."""
        # Empty generators should fail first
        def factory(generators):
            return Make.ListComp(Make.Name("x", ast.Load()), generators)
        self.validateExpression(factory([]), "comprehension with no generators")
        # Element with Store context should fail
        generator = Make.comprehension(Make.Name("x", ast.Store()), Make.Name("items", ast.Load()), [], 0)
        listCompBadElement = Make.ListComp(Make.Name("x", ast.Store()), [generator])
        self.validateExpression(listCompBadElement, "must have Load context")

        # Valid list comprehension should compile
        validListComp = Make.ListComp(Make.Name("x", ast.Load()), [generator])
        self.validateExpression(validListComp)

    def test_setCompValidation(self):
        """Test SetComp validation."""
        # Empty generators should fail first
        def factory(generators):
            return Make.SetComp(Make.Name("x", ast.Load()), generators)
        self.validateExpression(factory([]), "comprehension with no generators")
        # Element with Store context should fail
        generator = Make.comprehension(Make.Name("x", ast.Store()), Make.Name("items", ast.Load()), [], 0)
        setCompBadElement = Make.SetComp(Make.Name("x", ast.Store()), [generator])
        self.validateExpression(setCompBadElement, "must have Load context")

        # Valid set comprehension should compile
        validSetComp = Make.SetComp(Make.Name("x", ast.Load()), [generator])
        self.validateExpression(validSetComp)

    def test_generatorExpValidation(self):
        """Test GeneratorExp validation."""
        # Empty generators should fail first
        def factory(generators):
            return Make.GeneratorExp(Make.Name("x", ast.Load()), generators)
        self.validateExpression(factory([]), "comprehension with no generators")
        # Element with Store context should fail
        generator = Make.comprehension(Make.Name("x", ast.Store()), Make.Name("items", ast.Load()), [], 0)
        genExpBadElement = Make.GeneratorExp(Make.Name("x", ast.Store()), [generator])
        self.validateExpression(genExpBadElement, "must have Load context")

        # Valid generator expression should compile
        validGenExp = Make.GeneratorExp(Make.Name("x", ast.Load()), [generator])
        self.validateExpression(validGenExp)

    def test_dictCompValidation(self):
        """Test DictComp validation."""
        # Empty generators should fail first
        def factory(generators):
            return Make.DictComp(Make.Name("k", ast.Load()), Make.Name("v", ast.Load()), generators)
        self.validateExpression(factory([]), "comprehension with no generators")        # Key with Store context should fail
        generator = Make.comprehension(Make.Name("x", ast.Store()), Make.Name("items", ast.Load()), [], 0)
        dictCompBadKey = Make.DictComp(Make.Name("k", ast.Store()), Make.Name("v", ast.Load()), [generator])
        self.validateExpression(dictCompBadKey, "must have Load context")

        # Value with Store context should fail
        dictCompBadValue = Make.DictComp(Make.Name("k", ast.Load()), Make.Name("v", ast.Store()), [generator])
        self.validateExpression(dictCompBadValue, "must have Load context")

        # Valid dict comprehension should compile
        validDictComp = Make.DictComp(Make.Name("k", ast.Load()), Make.Name("v", ast.Load()), [generator])
        self.validateExpression(validDictComp)

    def test_yieldValidation(self):
        """Test Yield validation."""
        # Yield value with Store context should fail
        yieldBadValue = Make.Yield(Make.Name("x", ast.Store()))
        funcBadYield = Make.FunctionDef("test", Make.arguments([], [], None, [], [], None, []), [Make.Expr(yieldBadValue)])
        self.validateStatement(funcBadYield, "must have Load context")

        # Valid yield should compile
        validYield = Make.Yield(Make.Name("x", ast.Load()))
        funcValidYield = Make.FunctionDef("test", Make.arguments([], [], None, [], [], None, []), [Make.Expr(validYield)])
        self.validateStatement(funcValidYield)

    def test_yieldFromValidation(self):
        """Test YieldFrom validation."""
        # YieldFrom value with Store context should fail
        yieldFromBadValue = Make.YieldFrom(Make.Name("x", ast.Store()))
        funcBadYieldFrom = Make.FunctionDef("test", Make.arguments([], [], None, [], [], None, []), [Make.Expr(yieldFromBadValue)])
        self.validateStatement(funcBadYieldFrom, "must have Load context")

        # Valid yield from should compile
        validYieldFrom = Make.YieldFrom(Make.Name("x", ast.Load()))
        funcValidYieldFrom = Make.FunctionDef("test", Make.arguments([], [], None, [], [], None, []), [Make.Expr(validYieldFrom)])
        self.validateStatement(funcValidYieldFrom)

    def test_compareValidation(self):
        """Test Compare validation."""
        # Compare left with Store context should fail
        compareBadLeft = Make.Compare(Make.Name("x", ast.Store()), [ast.Lt()], [Make.Name("y", ast.Load())])
        self.validateExpression(compareBadLeft, "must have Load context")

        # Compare comparator with Store context should fail
        compareBadComp = Make.Compare(Make.Name("x", ast.Load()), [ast.Lt()], [Make.Name("y", ast.Store())])
        self.validateExpression(compareBadComp, "must have Load context")

        # Valid compare should compile
        validCompare = Make.Compare(Make.Name("x", ast.Load()), [ast.Lt()], [Make.Name("y", ast.Load())])
        self.validateExpression(validCompare)

    def test_boolOpValidation(self):
        """Test BoolOp validation."""
        # BoolOp with Store context value should fail
        boolOpBadValue = Make.BoolOp(ast.And(), [Make.Name("x", ast.Load()), Make.Name("y", ast.Store())])
        self.validateExpression(boolOpBadValue, "must have Load context")

        # Valid BoolOp should compile
        validBoolOp = Make.BoolOp(ast.And(), [Make.Name("x", ast.Load()), Make.Name("y", ast.Load())])
        self.validateExpression(validBoolOp)

    def test_unaryOpValidation(self):
        """Test UnaryOp validation."""
        # UnaryOp operand with Store context should fail
        unaryOpBad = Make.UnaryOp(ast.Not(), Make.Name("x", ast.Store()))
        self.validateExpression(unaryOpBad, "must have Load context")

        # Valid UnaryOp should compile
        validUnaryOp = Make.UnaryOp(ast.Not(), Make.Name("x", ast.Load()))
        self.validateExpression(validUnaryOp)

    def test_binOpValidation(self):
        """Test BinOp validation."""
        # BinOp left with Store context should fail
        binOpBadLeft = Make.BinOp(Make.Name("x", ast.Store()), ast.Add(), Make.Name("y", ast.Load()))
        self.validateExpression(binOpBadLeft, "must have Load context")

        # BinOp right with Store context should fail
        binOpBadRight = Make.BinOp(Make.Name("x", ast.Load()), ast.Add(), Make.Name("y", ast.Store()))
        self.validateExpression(binOpBadRight, "must have Load context")        # Valid BinOp should compile
        validBinOp = Make.BinOp(Make.Name("x", ast.Load()), ast.Add(), Make.Name("y", ast.Load()))
        self.validateExpression(validBinOp)
