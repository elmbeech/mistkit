########
# title: mistkit library
#
# language: python 3
# library: qiskit 1.1.1
# license: apache version 2.0
# date: 2024-06
# author original state_drawer: ibm and its contributors
# author modification and state_to_mist: elmar bucher
#
# run:
#     import qiskit
#     import mistkit
#     miskit.mistify()
#
# description:
#     dhasflaks
########


# library
#from colorama import Fore
import numpy as np
import qiskit

# to overwrite state_drawer
from qiskit import visualization
from qiskit import user_config
from qiskit.utils import optionals as _optionals
from qiskit.visualization.state_visualization import TextMatrix, state_to_latex, plot_state_qsphere, plot_state_hinton, plot_bloch_multivector, plot_state_city, plot_state_paulivec

# constant: number of decimal places to round the coefficient to.
i_round = 9  # number of decimal places to round the coefficient to.

# constant: misty bit unicode characters
lls_word = [
    ['\u25CB', '\u25CF'],  # q0 Black White Circle
    #['\u2B21', '\u2B22'],  # Black White Hexagon (too big)
    #['\u2B1F', '\u2B20'],  # Black White Pentagon (too big)
    #['\u2605', '\u2606'],  # Black White Star (too big)
    ['\u25A1', '\u25A0'],  # q1 Black White Square
    ['\u25AD', '\u25AC'],  # q2 Black White Rectangle
    ['\u25AF','\u25AE'],  # q3 Black White Vertical Rectangle
    ['\u25C7', '\u25C6'],  # q4 Black White Diamond
    ['\u2727', '\u2726'],  # q5 Black White Four Pointed Star
    ['\u25B5', '\u25B4'],  # q6 Black White Up-Pointing Triangle
    ['\u25BF', '\u25BE'],  # q7 Black White Down-Pointing Small Triangle
]


# functions
def state_to_mist(state):
    """
    input: state

    output: string

    run:

    description:
        here the magic happens.
    """
    # prepare output string
    s_mist = '{'

    # check state vector dimensions
    if not all(np.array(state.dims()) == 2):
        sys.exit(f'Error: the misty state implementation can only handle state vectors in the computational base 2. {state.dims()}')

    # print non zero state vector states
    i_states = 2**state.num_qubits
    for i_state in range(i_states):

        # get state value
        c_value = np.round(state.data[i_state], i_round)

        # if non zero state
        if (c_value != 0+0j):

            # get space
            if len(s_mist) > 1 :
                s_mist += ', '

            # get coefficient
            s_value = str(c_value).replace('(','').replace(')','')

            # get signe
            if (s_value[0] != '-'):
                s_value = '+' + s_value

            # get state
            s_state = ''
            s_binary = format(i_state, f'0{state.num_qubits}b')
            for i_bit, s_digit in enumerate(s_binary):
                # get character shape for this bit
                i_index = state.num_qubits - 1 - i_bit
                ls_bit = lls_word[i_index % len(lls_word)]
                # get character white or black
                s_state += ls_bit[int(s_digit)]

            # update output
            s_mist += s_value + ' ' + s_state

    # output
    s_mist += '}'
    return s_mist


# function state_drawer copyed from qiskit version 1.1.1
# source code: https://github.com/Qiskit/qiskit/blob/main/qiskit/visualization/state_visualization.py
# manipulation: add output 'mist' to the state_drawer function.
# license: apache2.0
def state_drawer(state, output=None, **drawer_args):
    """Returns a visualization of the state.

    **repr**: ASCII TextMatrix of the state's ``_repr_``.

    **text**: ASCII TextMatrix that can be printed in the console.

    **mist**: ASCII text string that can be printed in the console.

    **latex**: An IPython Latex object for displaying in Jupyter Notebooks.

    **latex_source**: Raw, uncompiled ASCII source to generate array using LaTeX.

    **qsphere**: Matplotlib figure, rendering of statevector using `plot_state_qsphere()`.

    **hinton**: Matplotlib figure, rendering of statevector using `plot_state_hinton()`.

    **bloch**: Matplotlib figure, rendering of statevector using `plot_bloch_multivector()`.

    **city**: Matplotlib figure, rendering of statevector using `plot_state_city()`.

    **paulivec**: Matplotlib figure, rendering of statevector using `plot_state_paulivec()`.

    Args:
        output (str): Select the output method to use for drawing the
            circuit. Valid choices are ``text``, ``mist``, ``latex``, ``latex_source``,
            ``qsphere``, ``hinton``, ``bloch``, ``city`` or ``paulivec``.
            Default is `'text`'.
        drawer_args: Arguments to be passed to the relevant drawer. For
            'latex' and 'latex_source' see ``array_to_latex``

    Returns:
        :class:`matplotlib.figure` or :class:`str` or
        :class:`TextMatrix` or :class:`IPython.display.Latex`:
        Drawing of the state.

    Raises:
        MissingOptionalLibraryError: when `output` is `latex` and IPython is not installed.
        ValueError: when `output` is not a valid selection.
    """
    config = user_config.get_config()
    # Get default 'output' from config file else use 'repr'
    default_output = "repr"
    if output is None:
        if config:
            default_output = config.get("state_drawer", "repr")
        output = default_output
    output = output.lower()

    # Choose drawing backend:
    drawers = {
        "text": TextMatrix,
        "latex_source": state_to_latex,
        "qsphere": plot_state_qsphere,
        "hinton": plot_state_hinton,
        "bloch": plot_bloch_multivector,
        "city": plot_state_city,
        "paulivec": plot_state_paulivec,
    }
    if output == "latex":
        _optionals.HAS_IPYTHON.require_now("state_drawer")
        from IPython.display import Latex

        draw_func = drawers["latex_source"]
        return Latex(f"$${draw_func(state, **drawer_args)}$$")

    # bue 2024-07: output option added
    if output == "mist":
        return state_to_mist(state)

    if output == "repr":
        return state.__repr__()

    try:
        draw_func = drawers[output]
        return draw_func(state, **drawer_args)
    except KeyError as err:
        raise ValueError(
            f"""'{output}' is not a valid option for drawing {type(state).__name__}
             objects. Please choose from:
            'text', 'mist', 'latex', 'latex_source', 'qsphere', 'hinton',
            'bloch', 'city', or 'paulivec'."""
        ) from err


def mistify():
    """
    input: nop
    output:  overwritten function
    run:
    description:
        add output 'mist' to the state_drawer function.
        overwrite qiskit.visualization.state_visualization.state_drawer function.

    """
    print(f'mistify loaded qiskit verion {qiskit.__version__} ...')
    visualization.state_visualization.state_drawer = state_drawer
    print(f'ok!')

