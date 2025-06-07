import ast
import pytest
from astToolkit import Make


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

    def test_functionDefValidation(self):
        """Test FunctionDef validation with various configurations."""
        # Empty body should fail
        argumentsEmpty = Make.arguments(kw_defaults=[])  # Fix: empty kw_defaults to match empty kwonlyargs
        functionEmpty = Make.FunctionDef("testFunction", argumentsEmpty, body=[])
        self.validateStatement(functionEmpty, "empty body on FunctionDef")

        # Decorator with Store context should fail
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
        self.validateStatement(functionWithBadReturn, "must have Load context")

        # Valid function should compile
        validFunction = Make.FunctionDef("testFunction", argumentsEmpty, body=[Make.Pass()])
        self.validateStatement(validFunction)

    # def test_classDefValidation(self):
    #     """Test ClassDef validation with various configurations."""
    #     # Base with Store context should fail
    #     classWithBadBase = Make.ClassDef(
    #         "TestClass",
    #         bases=[Make.Name("BaseClass", ast.Store())]
    #     )
    #     self.validateStatement(classWithBadBase, "must have Load context")

    #     # Keyword with Store context should fail
    #     classWithBadKeyword = Make.ClassDef(
    #         "TestClass",
    #         list_keyword=[Make.keyword("metaclass", Make.Name("Meta", ast.Store()))]
    #     )
    #     self.validateStatement(classWithBadKeyword, "must have Load context")

    #     # Empty body should fail
    #     classWithEmptyBody = Make.ClassDef("TestClass", body=[])
    #     self.validateStatement(classWithEmptyBody, "empty body on ClassDef")

    #     # Decorator with Store context should fail
    #     classWithBadDecorator = Make.ClassDef(
    #         "TestClass",
    #         decorator_list=[Make.Name("decorator", ast.Store())]
    #     )
    #     self.validateStatement(classWithBadDecorator, "must have Load context")

    #     # Valid class should compile
    #     validClass = Make.ClassDef("TestClass", body=[Make.Pass()])
    #     self.validateStatement(validClass)

    def test_assignValidation(self):
        """Test Assign validation."""
        # Empty targets should fail
        assignEmpty = Make.Assign([], Make.Constant(42))
        self.validateStatement(assignEmpty, "empty targets on Assign")

        # Target with Load context should fail
        assignBadTarget = Make.Assign(
            [Make.Name("variable", ast.Load())],
            Make.Constant(42)
        )
        self.validateStatement(assignBadTarget, "must have Store context")

        # Value with Store context should fail
        assignBadValue = Make.Assign(
            [Make.Name("variable", ast.Store())],
            Make.Name("value", ast.Store())
        )
        self.validateStatement(assignBadValue, "must have Load context")

        # Valid assignment should compile
        validAssign = Make.Assign(
            [Make.Name("variable", ast.Store())],
            Make.Constant(42)
        )
        self.validateStatement(validAssign)

    def test_augAssignValidation(self):
        """Test AugAssign validation."""
        # Target with Load context should fail
        augAssignBadTarget = Make.AugAssign(
            Make.Name("variable", ast.Load()),
            ast.Add(),
            Make.Name("value", ast.Load())
        )
        self.validateStatement(augAssignBadTarget, "must have Store context")

        # Value with Store context should fail
        augAssignBadValue = Make.AugAssign(
            Make.Name("variable", ast.Store()),
            ast.Add(),
            Make.Name("value", ast.Store())
        )
        self.validateStatement(augAssignBadValue, "must have Load context")

        # Valid augmented assignment should compile
        validAugAssign = Make.AugAssign(
            Make.Name("variable", ast.Store()),
            ast.Add(),
            Make.Constant(1)
        )
        self.validateStatement(validAugAssign)

    def test_deleteValidation(self):
        """Test Delete validation."""
        # Empty targets should fail
        deleteEmpty = Make.Delete([])
        self.validateStatement(deleteEmpty, "empty targets on Delete")

        # Target with Load context should fail
        deleteBadTarget = Make.Delete([Make.Name("variable", ast.Load())])
        self.validateStatement(deleteBadTarget, "must have Del context")

        # Valid delete should compile
        validDelete = Make.Delete([Make.Name("variable", ast.Del())])
        self.validateStatement(validDelete)

    def test_forValidation(self):
        """Test For loop validation."""
        target = Make.Name("item", ast.Store())
        iterable = Make.Name("items", ast.Load())
        body = [Make.Pass()]

        # Empty body should fail
        forEmpty = Make.For(target, iterable, body=[])
        self.validateStatement(forEmpty, "empty body on For")

        # Target with Load context should fail
        forBadTarget = Make.For(
            Make.Name("item", ast.Load()),
            iterable,
            body
        )
        self.validateStatement(forBadTarget, "must have Store context")

        # Iterable with Store context should fail
        forBadIterable = Make.For(
            target,
            Make.Name("items", ast.Store()),
            body
        )
        self.validateStatement(forBadIterable, "must have Load context")

        # Valid for loop should compile
        validFor = Make.For(target, iterable, body)
        self.validateStatement(validFor)

    def test_whileValidation(self):
        """Test While loop validation."""
        # Empty body should fail
        whileEmpty = Make.While(Make.Constant(True), body=[])
        self.validateStatement(whileEmpty, "empty body on While")

        # Test with Store context should fail
        whileBadTest = Make.While(
            Make.Name("condition", ast.Store()),
            body=[Make.Pass()]
        )
        self.validateStatement(whileBadTest, "must have Load context")

        # Valid while loop should compile
        validWhile = Make.While(Make.Constant(True), body=[Make.Pass()])
        self.validateStatement(validWhile)

    def test_ifValidation(self):
        """Test If statement validation."""
        # Empty body should fail
        ifEmpty = Make.If(Make.Constant(True), body=[])
        self.validateStatement(ifEmpty, "empty body on If")

        # Test with Store context should fail
        ifBadTest = Make.If(
            Make.Name("condition", ast.Store()),
            body=[Make.Pass()]
        )
        self.validateStatement(ifBadTest, "must have Load context")

        # Valid if statement should compile
        validIf = Make.If(Make.Constant(True), body=[Make.Pass()])
        self.validateStatement(validIf)

    def test_withValidation(self):
        """Test With statement validation."""
        passStatement = Make.Pass()

        # Empty items should fail
        withEmpty = Make.With([], body=[passStatement])
        self.validateStatement(withEmpty, "empty items on With")

        # Empty body should fail
        withItem = Make.withitem(Make.Constant(42))
        withEmptyBody = Make.With([withItem], body=[])
        self.validateStatement(withEmptyBody, "empty body on With")

        # Context expression with Store context should fail
        withBadContext = Make.With(
            [Make.withitem(Make.Name("context", ast.Store()))],
            body=[passStatement]
        )
        self.validateStatement(withBadContext, "must have Load context")

        # Optional vars with Load context should fail
        withBadVars = Make.With(
            [Make.withitem(Make.Constant(42), Make.Name("variable", ast.Load()))],
            body=[passStatement]
        )
        self.validateStatement(withBadVars, "must have Store context")

        # Valid with statement should compile
        validWith = Make.With(
            [Make.withitem(Make.Constant(42))],
            body=[passStatement]
        )
        self.validateStatement(validWith)

    def test_raiseValidation(self):
        """Test Raise statement validation."""
        # Cause without exception should fail
        raiseBadCause = Make.Raise(cause=Make.Constant("cause"))
        self.validateStatement(raiseBadCause, "Raise with cause but no exception")

        # Exception with Store context should fail
        raiseBadException = Make.Raise(Make.Name("exception", ast.Store()))
        self.validateStatement(raiseBadException, "must have Load context")

        # Cause with Store context should fail
        raiseBadCauseContext = Make.Raise(
            Make.Constant("exception"),
            Make.Name("cause", ast.Store())
        )
        self.validateStatement(raiseBadCauseContext, "must have Load context")

        # Valid raise should compile
        validRaise = Make.Raise(Make.Name("exception", ast.Load()))
        self.validateStatement(validRaise)

    def test_tryValidation(self):
        """Test Try statement validation."""
        passStatement = Make.Pass()

        # Empty body should fail
        tryEmpty = Make.Try(body=[], handlers=[], finalbody=[passStatement])
        self.validateStatement(tryEmpty, "empty body on Try")

        # Try without handlers or finalbody should fail
        tryNoHandlers = Make.Try(body=[passStatement], handlers=[])
        self.validateStatement(tryNoHandlers, "Try has neither except handlers nor finalbody")

        # Try with orelse but no handlers should fail
        tryOrElseNoHandlers = Make.Try(
            body=[passStatement],
            handlers=[],
            orElse=[passStatement],
            finalbody=[passStatement]
        )
        self.validateStatement(tryOrElseNoHandlers, "Try has orelse but no except handlers")

        # ExceptHandler with empty body should fail
        tryEmptyHandler = Make.Try(
            body=[passStatement],
            handlers=[Make.ExceptHandler(body=[])]
        )
        self.validateStatement(tryEmptyHandler, "empty body on ExceptHandler")

        # Valid try statement should compile
        validTry = Make.Try(
            body=[passStatement],
            handlers=[Make.ExceptHandler(body=[passStatement])]
        )
        self.validateStatement(validTry)

    def test_assertValidation(self):
        """Test Assert statement validation."""
        # Test with Store context should fail
        assertBadTest = Make.Assert(Make.Name("condition", ast.Store()))
        self.validateStatement(assertBadTest, "must have Load context")

        # Message with Store context should fail
        assertBadMessage = Make.Assert(
            Make.Name("condition", ast.Load()),
            Make.Name("message", ast.Store())
        )
        self.validateStatement(assertBadMessage, "must have Load context")

        # Valid assert should compile
        validAssert = Make.Assert(Make.Name("condition", ast.Load()))
        self.validateStatement(validAssert)

    # def test_importValidation(self):
    #     """Test Import statement validation."""
    #     # Empty dotModule should fail
    #     importEmpty = Make.Import()
    #     self.validateStatement(importEmpty, "empty names on Import")

    #     # Valid import should compile
    #     validImport = Make.Import([Make.alias("module")])
    #     self.validateStatement(validImport)

    # def test_argumentsValidation(self):
    #     """Test that arguments validation works with Make factory."""
    #     # Arguments with annotation Store context should fail
    #     argsWithBadAnnotation = [Make.arg("parameter", Make.Name("type", ast.Store()))]

    #     def createFunctionWithArgs(argumentsList):
    #         argumentsNode = Make.arguments(list_arg=argumentsList)
    #         return Make.FunctionDef("testFunction", argumentsNode, body=[Make.Pass()])

    #     functionBadArgs = createFunctionWithArgs(argsWithBadAnnotation)
    #     self.validateStatement(functionBadArgs, "must have Load context")

    #     # More defaults than args should fail
    #     argumentsNodeBadDefaults = Make.arguments(defaults=[Make.Constant(42)])
    #     functionBadDefaults = Make.FunctionDef("testFunction", argumentsNodeBadDefaults, body=[Make.Pass()])
    #     self.validateStatement(functionBadDefaults, "more positional defaults than args")

    #     # Valid arguments should compile
    #     validArgs = [Make.arg("parameter", Make.Name("type", ast.Load()))]
    #     validFunction = createFunctionWithArgs(validArgs)
    #     self.validateStatement(validFunction)

    def test_compoundExpressionValidation(self):
        """Test compound expressions created with Make factory."""
        # BinOp with valid operands should compile
        validBinOp = Make.BinOp(
            Make.Constant(1),
            ast.Add(),
            Make.Constant(2)
        )
        self.validateExpression(validBinOp)

        # BoolOp with valid operands should compile
        validBoolOp = Make.BoolOp(
            ast.And(),
            [Make.Name("x", ast.Load()), Make.Name("y", ast.Load())]
        )
        self.validateExpression(validBoolOp)

        # Compare with valid operands should compile
        validCompare = Make.Compare(
            Make.Name("x", ast.Load()),
            [ast.Lt()],
            [Make.Name("y", ast.Load())]
        )
        self.validateExpression(validCompare)

        # Call with valid arguments should compile
        validCall = Make.Call(
            Make.Name("function", ast.Load()),
            [Make.Constant("argument")]
        )
        self.validateExpression(validCall)

    def test_contextValidation(self):
        """Test that context validation works properly with Make factory."""
        # Names in different contexts
        loadName = Make.Name("variable", ast.Load())
        storeName = Make.Name("variable", ast.Store())
        delName = Make.Name("variable", ast.Del())

        # Load context is valid for expressions
        self.validateExpression(loadName)

        # Store context is valid for assignment targets
        assignment = Make.Assign([storeName], Make.Constant(42))
        self.validateStatement(assignment)

        # Del context is valid for delete targets
        deletion = Make.Delete([delName])
        self.validateStatement(deletion)
