from ...errors import InvalidClassNameError, UndefinedBlockError, UndefinedTargetLocatorError
from ...structs import CodeFragment
from ...load_rough_spec.parse_lines import parse_lines
from ...structs import SemanticSpec
import re

def validate_semantic_spec(semanticSpec: SemanticSpec):
    return SemanticValidator(semanticSpec).validate()

class SemanticValidator:
    def __init__(self, semanticSpec: SemanticSpec):
        self.semanticSpec = semanticSpec
        self.errorList = []

    def validate(self) -> list:
        if (self._isCodeFragmentListEmpty()):
            return self.errorList

        for codeFragment in self.semanticSpec.codeFragmentList:
            self._checkForErrors(codeFragment)
        return self.errorList

    def _checkForErrors(self, codeFragment):
        if self._isTargetLocatorUndefined(codeFragment):
            self._appendUndefinedTargetLocatorError(codeFragment)
        else:
            self._checkTargetLocatorClassName(codeFragment)
        self._checkUndefinedBlock(codeFragment)

    def _checkTargetLocatorClassName(self, codeFragment: CodeFragment):
        if not re.match(r'^[A-Z][A-Za-z0-9_]*$', codeFragment.targetLocator.className):
            self.errorList.append(InvalidClassNameError(codeFragment.targetLocator.line))

    def _checkUndefinedBlock(self, codeFragment: CodeFragment):
        if codeFragment.block == None:
            self.errorList.append(UndefinedBlockError(codeFragment.targetLocator.line))

    def _appendUndefinedTargetLocatorError(self, codeFragment):
        self.errorList.append(UndefinedTargetLocatorError(codeFragment.block.lines[0]))

    def _isCodeFragmentListEmpty(self):
        return True if len(self.semanticSpec.codeFragmentList) == 0 else False

    def _isTargetLocatorUndefined(self, codeFragment: CodeFragment):
        return True if codeFragment.targetLocator == None else False
