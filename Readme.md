# asciitree

Given a CoNLL-U formatted dependency parse the objective is to output an ASCII
representation like so:

         root
          |
          | +-------dobj---------+
          | |                    |
    nsubj | |   +------det-----+ | +-----nmod------+
    +--+  | |   |              | | |               |
    |  |  | |   |      +-nmod-+| | |      +-case-+ |
    +  |  + |   +      +      || + |      +      | |
    I  prefer  the  morning   flight  through  Denver

Will support other inputs in the future.

## Setup

Create a virtual environment in python3, then activate it and install
dependencies

    python3.8 -m venv --prompt asciitree __venv__
    source __venv__/bin/activate
    make install
