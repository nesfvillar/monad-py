from monads.monad import Monad


class Result(Monad):
    def __init__(self, value, error=None):
        super().__init__(value)
        self._error = error if error is not None else {}

    def bind(self, *funcs):
        if self.isError():
            return self

        try:
            return super().bind(*funcs)

        except Exception as e:
            error = {
                "exception": e,
            }

            return Result(self._value, error)

    def isOk(self):
        return self._error == {}

    def isError(self):
        return not self.isOk()

    def getError(self):
        return self._error
