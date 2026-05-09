def ssh_edge_parity_observable(n_qubits, edge_position=0):
    """
    Define edge parity operator |<Z_i Z_{i+1}>|.
    
    Parameters:
    -----------
    n_qubits : int
    edge_position : int
        Which edge to measure (0 = left, n_qubits-2 = right)
    
    Returns:
    --------
    observable : Qiskit SparsePauliOp
    """
    pass

def mbl_imbalance_observable(n_qubits):
    """
    Define many-body localization imbalance.
    
    I(t) = |<Z_odd> - <Z_even>|
    
    where odd/even refers to qubit parity
    """
    pass

def qec_syndrome_observable(n_qubits, syndrome_type='boundary'):
    """
    Define QEC syndrome measurement observable.
    
    For SSH model, syndromes are Z0*Z1 and Z8*Z9 (boundary operators).
    """
    pass
