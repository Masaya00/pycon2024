from ninja import Schema


class ValidationError(Schema):
    loc: list[str | int]
    msg: str
    type: str


class ValidationErrorResponse(Schema):
    detail: list[ValidationError]
