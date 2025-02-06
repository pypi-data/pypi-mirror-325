from .exceptions import ParsionParseError, ParsionInternalError


class ParsionParser:
    def __init__(self, parse_grammar, parse_table, error_handlers):
        self.parse_grammar = parse_grammar
        self.parse_table = parse_table
        self.error_handlers = error_handlers

    def _call_reduce(self, obj, goal, accepts, parts):
        args = [p[0] for a, p in zip(accepts, parts) if a]

        if goal is None:
            assert len(args) == 1
            return args[0]
        else:
            return getattr(obj, goal)(*args)

    def _call_error_handler(self, obj, handler, error_stack, error_tokens):
        return getattr(obj, handler)(error_stack, error_tokens)

    def parse(self, input, handlerobj):
        tokens = [(tok.name, tok.value) for tok in input]
        stack = [('START', 0)]

        while len(tokens) > 0:
            tok_name, tok_value = tokens[0]
            cur_state = stack[-1][1]
            if tok_name not in self.parse_table[cur_state]:
                # Unexpected token, do error recovery
                try:
                    # First, pop stack until error handler
                    error_stack = []
                    while stack[-1][1] not in self.error_handlers:
                        error_stack.append(stack.pop())

                    error_handlers = self.error_handlers[stack[-1][1]]

                    error_tokens = []
                    while tokens[0][0] not in error_handlers:
                        error_tokens.append(tokens.pop(0))

                    # Call error handler, mimic a reduce operation
                    error_gen, error_handler = error_handlers[tokens[0][0]]
                    value = self._call_error_handler(
                        handlerobj,
                        error_handler,
                        error_stack,
                        error_tokens
                    )
                    tokens.insert(0, (error_gen, value))
                except IndexError:
                    expect_toks = ",".join(self.parse_table[cur_state].keys())
                    raise ParsionParseError(
                        f'Unexpected {tok_name}, expected {expect_toks}')
            else:
                op, id = self.parse_table[cur_state][tok_name]
                if op == 's':
                    # shift
                    tokens.pop(0)
                    stack.append((tok_value, id))
                elif op == 'r':
                    # reduce
                    gen, goal, accepts = self.parse_grammar[id]
                    tokens.insert(0, (
                        gen,
                        self._call_reduce(
                            handlerobj,
                            goal,
                            accepts,
                            stack[-len(accepts):]
                        )
                    ))
                    stack = stack[:-len(accepts)]
                else:
                    raise ParsionInternalError(
                        'Internal error: neigher shift nor reduce')

        # Stack contains three elements:
        #  0. ('START', ...) - bootstrap
        #  1. ('entry', ...) - excpeted result
        #  2. ('END', ...)   - terminination
        # Therefore, pick out entry value and return
        return stack[1][0]

    def print(self):  # pragma: no cover
        from tabulate import tabulate

        def _print_header(header):
            print("")
            print(f"{header}")

        _print_header("Lexer")
        print(tabulate(
            [
                (name, regexp.pattern)
                for name, regexp, handler in self.lex.rules
            ],
            tablefmt='simple_outline'
        ))

        _print_header("FSM grammar")
        print(tabulate(
            self.parse_grammar,
            headers=('generate', 'goal', 'parts'),
            tablefmt='simple_outline',
            showindex='always'
        ))
        _print_header("FSM states")

        print(tabulate(
            [
                {
                    k: " ".join(str(p) if p is not None else '-' for p in v)
                    for k, v in st.items()
                }
                for st in self.parse_table
            ],
            headers='keys',
            tablefmt='simple_outline',
            showindex='always'
        ))
