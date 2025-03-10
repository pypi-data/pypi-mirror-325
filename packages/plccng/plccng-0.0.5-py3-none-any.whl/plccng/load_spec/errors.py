from plccng.load_spec.structs import Line, SyntacticRule


from dataclasses import dataclass


@dataclass
class ValidationError:
    line: Line
    message: str


class MalformedBNFError(Exception):
    def __init__(self, line):
        self.line = line


@dataclass
class InvalidNameFormatError(ValidationError):
    def __init__(self, rule):
        self.line = rule.line
        self.message = f"Invalid name format for rule '{rule.name}' (Must be uppercase letters, numbers, and underscores, and cannot start with a number) on line: {rule.line.number}"


@dataclass
class DuplicateNameError(ValidationError):
    def __init__(self, rule):
        self.line = rule.line
        self.message = f"Duplicate rule name found '{rule.name}' on line: {rule.line.number}"


@dataclass
class InvalidPatternError(ValidationError):
    def __init__(self, rule):
        self.line = rule.line
        self.message = f"Invalid pattern format found '{rule.pattern}' on line: {rule.line.number} (Patterns can not contain closing closing quotes)"


@dataclass
class InvalidRuleError(ValidationError):
    def __init__(self, line):
        self.line = line
        self.message = f"Invalid rule format found on line: {line.number}"

@dataclass
class InvalidClassNameError(ValidationError):
    def __init__(self, line):
        self.line = line
        self.message = f"Invalid name format for ClassName {self.line.string} on line: {self.line.number} (Must start with an upper case letter, and may contain upper or lower case letters, numbers, and underscores)."

@dataclass
class UndefinedBlockError(ValidationError):
    def __init__(self, line):
        self.line = line
        self.message = f"Undefined Block for {self.line.string} on line: {self.line.number}"

@dataclass
class UndefinedTargetLocatorError(ValidationError):
    def __init__(self, line):
        self.line = line
        self.message = f"Undefined class name on line: {self.line.number}"

@dataclass
class InvalidLhsNameError(ValidationError):
    def __init__(self, rule):
        super().__init__(
            line=rule.line,
            message=f"Invalid LHS name format for rule: '{rule.line.string}' (must start with a lower-case letter, and may contain upper or lower case letters, numbers and/or underscore) on line: {rule.line.number}"
        )


@dataclass
class InvalidLhsAltNameError(ValidationError):
    def __init__(self, rule):
        super().__init__(
            line=rule.line,
            message=f"Invalid LHS alternate name format for rule: '{rule.line.string}' (must start with a upper-case letter, and may contain upper or lower case letters, numbers and/or underscore) on line: {rule.line.number}"
        )


@dataclass
class DuplicateLhsError(ValidationError):
    def __init__(self, rule):
        super().__init__(
            line=rule.line,
            message=f"Duplicate lhs name: '{rule.line.string}' on line: {rule.line.number}"
        )


@dataclass
class InvalidRhsNameError(ValidationError):
    def __init__(self, rule):
        super().__init__(
            line=rule.line,
            message=f"Invalid RHS name format for rule: '{rule.line.string}' (must start with a lower-case letter, and may contain upper or lower case letters, numbers, and underscore.) on line: {rule.line.number}"
        )


@dataclass
class InvalidRhsAltNameError(ValidationError):
    def __init__(self, rule):
        super().__init__(
            line=rule.line,
            message = f"Invalid RHS alternate name format for rule: '{rule.line.string}' (must start with a lower case letter, and may contain upper or lower case letters, numbers, and underscore. on line: {rule.line.number}"
        )


@dataclass
class InvalidRhsTerminalError(ValidationError):
    def __init__(self, rule):
        super().__init__(
            line=rule.line,
            message=f"Invalid RHS alternate name format for rule: '{rule.line.string}' (upper-case letters, numbers, and underscore and cannot start with a number. on line: {rule.line.number}"
        )


@dataclass
class UndefinedTerminalError(ValidationError):
    def __init__(self, rule):
        super().__init__(
            line=rule.line,
            message=f"Undefined terminal for rule: '{rule.line.string}' on line: {rule.line.number}. All terminals must be defined in the lexical section of the grammar file."
        )


@dataclass
class InvalidRhsSeparatorTypeError(ValidationError):
    def __init__(self, rule):
        super().__init__(
            line=rule.line,
            message=f"Invalid RHS separator, must be terminal: '{rule.line.string}'"
        )


@dataclass
class MissingNonTerminalError(ValidationError):
    def __init__(self, rule):
        super().__init__(
        line=rule.line,
        message = f"RHS Non-Terminal found that does not exist anywhere in LHS in rule: '{rule.line.string}' on line: {rule.line.number}"
        )

@dataclass
class LL1Error:
    def __init__(self, cell, production):
        self.cell = cell
        self.production = production
        self.message = f"Two production rules in the same parsing table cell: {cell} -> {production}"


@dataclass
class InvalidSyntacticSpecException(Exception):
    def __init__(self, rule):
        super().__init__(rule)
        self.message = f"Invalid Syntactic Spec: '{rule}' (must be a SyntacticSpec object)"


@dataclass
class InvalidSymbolException(Exception):
    def __init__(self, rule):
        super().__init__(rule)
        self.message = f"Invalid Symbol: '{rule}' (must be a Symbol object)"

