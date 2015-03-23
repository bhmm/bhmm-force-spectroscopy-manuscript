__author__ = 'noe'


def generate_initial_model(observations, nstates, output_model_type, verbose=False):
    """Use a heuristic scheme to generate an initial model.

    Parameters
    ----------
    observations : list of ndarray((T_i))
        list of arrays of length T_i with observation data
    nstates : int
        The number of states.
    output_model_type : str, optional, default='gaussian'
        Output model type.  ['gaussian', 'discrete']
    verbose : bool, optional, default=False
        If True, will be verbose in output.

    Examples
    --------

    Generate initial model for a gaussian output model.

    >>> from bhmm import testsystems
    >>> [model, observations, states] = testsystems.generate_synthetic_observations(output_model_type='gaussian')
    >>> initial_model = generate_initial_model(observations, model.nstates, 'gaussian')

    Generate initial model for a discrete output model.

    >>> from bhmm import testsystems
    >>> [model, observations, states] = testsystems.generate_synthetic_observations(output_model_type='discrete')
    >>> initial_model = generate_initial_model(observations, model.nstates, 'discrete')

    """
    if output_model_type == 'discrete':
        from bhmm.init import discrete
        return discrete.initial_model_discrete(observations, nstates, lag=1, reversible=True, verbose=verbose)
    elif output_model_type == 'gaussian':
        from bhmm.init import gaussian
        return gaussian.initial_model_gaussian1d(observations, nstates, reversible=True, verbose=verbose)
    else:
        raise NotImplementedError('output model type '+str(output_model_type)+' not yet implemented.')
