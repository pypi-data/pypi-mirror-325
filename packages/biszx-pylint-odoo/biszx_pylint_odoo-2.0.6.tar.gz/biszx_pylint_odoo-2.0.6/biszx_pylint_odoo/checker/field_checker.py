import astroid
from pylint.checkers import utils

from .. import messages
from .base_checker import BaseChecker


class FieldChecker(BaseChecker):
    name: str = 'biszx-odoolint-field'
    msgs: dict = messages.FIELD_CHECKER_MSGS
    validators: dict = {
        'Many2one': {
            're': '^.*_id$',
            'msg_id': 'biszx-relation2one-field-name',
        },
        'Many2one_user': {
            're': '^.*_uid|^.*_id$',
            'msg_id': 'biszx-relation2one-field-name',
        },
        'One2many': {
            're': '^.*_ids$',
            'msg_id': 'biszx-relation2many-field-name',
        },
        'One2many_user': {
            're': '^.*_uids|^.*_ids$',
            'msg_id': 'biszx-relation2many-field-name',
        },
        'Many2many': {
            're': '^.*_ids$',
            'msg_id': 'biszx-relation2many-field-name',
        },
        'Many2many_user': {
            're': '^.*_uids|^.*_ids$',
            'msg_id': 'biszx-relation2many-field-name',
        },
        'Boolean': {
            're': '^is_*|^active$',
            'msg_id': 'biszx-boolean-field-name',
        },
        'Date': {
            're': '^.*_date$',
            'msg_id': 'biszx-date-field-name',
        },
        'Datetime': {
            're': '^.*_datetime$',
            'msg_id': 'biszx-datetime-field-name',
        },
    }

    @utils.only_required_for_messages(
        'biszx-relation2one-field-name',
        'biszx-relation2many-field-name',
        'biszx-boolean-field-name',
        'biszx-date-field-name',
        'biszx-datetime-field-name',
    )
    def visit_assign(self, node: astroid.Assign):
        find: tuple = tuple(self.validators.keys())
        value = node.value
        if (
            value
            and isinstance(value, astroid.Call)
            and isinstance(value.func, astroid.Attribute)
            and isinstance(value.func.expr, astroid.Name)
            and value.func.expr.name == 'fields'
            and (key := value.func.attrname) in find
        ):
            if self._is_relation_user(key, value):
                self._validate_match_name(
                    node, f'{key}_user', node.targets[0].name
                )
            else:
                self._validate_match_name(node, key, node.targets[0].name)

    def _is_relation_user(self, key: str, value: astroid.Call) -> bool:
        return key in ('Many2one', 'One2many', 'Many2many') and any(
            [
                (
                    len(value.args)
                    and getattr(value.args[0], 'value', None) == 'res.users'
                ),
                (
                    len(value.keywords)
                    and (
                        model := list(
                            filter(
                                lambda v: v.arg == 'comodel_name',
                                value.keywords,
                            )
                        )
                    )
                    and getattr(model[0].value, 'value', None) == 'res.users'
                ),
            ]
        )
