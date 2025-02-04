import astroid
from pylint.checkers import utils

from .. import messages
from .base_checker import BaseChecker


class FunctionChecker(BaseChecker):
    name: str = 'biszx-odoolint-function'
    msgs: dict = messages.FUNCTION_CHECKER_MSGS
    validators: dict = {
        'search': {
            're': '^_search_*',
            'msg_id': 'biszx-search-func-name',
        },
        'default': {
            're': '^_default_*',
            'msg_id': 'biszx-default-func-name',
        },
        'compute': {
            're': '^_compute_*|False',
            'msg_id': 'biszx-compute-func-name',
        },
        'onchange': {
            're': '^_onchange_*',
            'msg_id': 'biszx-onchange-func-name',
        },
        'constrains': {
            're': '^_check_*',
            'msg_id': 'biszx-constrains-func-name',
        },
        'domain': {
            're': '^_domain_*',
            'msg_id': 'biszx-domain-func-name',
        },
        'inverse': {
            're': '^_inverse_*',
            'msg_id': 'biszx-inverse-func-name',
        },
    }

    @utils.only_required_for_messages(
        'biszx-onchange-func-name',
        'biszx-constrains-func-name',
    )
    def visit_functiondef(self, node: astroid.FunctionDef):
        decorators = node.decorators
        if not decorators:
            return

        find: tuple = ('onchange', 'constrains')
        for decorator in decorators.nodes:
            if (
                isinstance(decorator, astroid.Call)
                and isinstance(decorator.func, astroid.Attribute)
                and isinstance(decorator.func.expr, astroid.Name)
                and decorator.func.expr.name == 'api'
                and (key := decorator.func.attrname) in find
            ):
                self._validate_match_name(node, key, node.name)

    @utils.only_required_for_messages(
        'biszx-default-func-name',
        'biszx-domain-func-name',
        'biszx-compute-func-name',
        'biszx-inverse-func-name',
    )
    def visit_assign(self, node: astroid.Assign):
        value = node.value
        if (
            not value
            or not isinstance(value, astroid.Call)
            or not value.keywords
            or not isinstance(value.func, astroid.Attribute)
            or not isinstance(value.func.expr, astroid.Name)
            or value.func.expr.name != 'fields'
        ):
            return

        find_str_value: tuple = ('search', 'compute', 'inverse')
        find: tuple = ('default', 'domain')
        for keyword in value.keywords:
            if (key := keyword.arg) in find + find_str_value:
                is_str_value = key in find_str_value
                arg = keyword.value
                if (
                    isinstance(arg, astroid.Lambda)
                    and isinstance(arg.body, astroid.Call)
                    and isinstance(arg.body.func, astroid.Attribute)
                    and isinstance(arg.body.func.expr, astroid.Name)
                    and arg.body.func.expr.name == 'self'
                ):
                    self._validate_match_name(
                        arg, key, getattr(arg.body.func, 'attrname', '')
                    )
                elif isinstance(arg, astroid.Name):
                    self._validate_match_name(arg, key, arg.name)
                elif is_str_value and isinstance(arg, astroid.Const):
                    self._validate_match_name(arg, key, arg.value)
