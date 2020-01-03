import cairosvg
from railroad import *

TRY_STATEMENT = Diagram(
    Terminal('try', 'skip'),
    Terminal(':'),
    NonTerminal('suite'),
    Choice(0,
           Sequence(
               OneOrMore(
                   Sequence(
                       Terminal('except'),
                       Optional(
                           Sequence(
                               NonTerminal('test'),
                               Optional(
                                   Sequence(
                                       Terminal('as'),
                                       NonTerminal('NAME')
                                   )
                               )
                           )
                       )
                   ), Arrow('<')
               ),
               Optional(
                   Sequence(
                       Terminal('else'),
                       Terminal(':'),
                       NonTerminal('suite')
                   )
               ),
               Optional(
                   Sequence(
                       Terminal('finally'),
                       Terminal(':'),
                       NonTerminal('suite')
                   )
               ),
           ),
           Sequence(
               Terminal('finally'),
               Terminal(':'),
               NonTerminal('suite')
           )
           )
)

WITH_STATEMENT = Diagram(
    Terminal('with', 'skip'),
    NonTerminal('test'),
    Optional(
        Sequence(
            Terminal('as'),
            NonTerminal('expr')
        )),
    Optional(OneOrMore(Sequence(
        Terminal(', as'),
        NonTerminal('expr')
    ), Arrow('<'))),
    Terminal(':'),
    NonTerminal('suite')
)

statements = {
    'try-statement': TRY_STATEMENT,
    'with-statement': WITH_STATEMENT
}


def main():
    for key, value in statements.items():
        with open('{0}.svg'.format(key), 'w') as out_svg:
            diagram = value
            diagram.writeSvg(out_svg.write)
        cairosvg.svg2png(url='{0}.svg'.format(key), write_to='{0}.png'.format(key), output_width=3000, dpi=300)


if __name__ == "__main__":
    main()
