def build_ssh_hamiltonian(n_qubits, t1, t2, boundary_disorder=0.0):
    """
    Construct Su-Schrieffer-Heeger model Hamiltonian.
    
    Parameters:
    -----------
    n_qubits : int
        Chain length (should be even)
    t1, t2 : float
        Alternating bond strengths
    boundary_disorder : float
        Random on-site disorder strength (W parameter)
    
    Returns:
    --------
    Hamiltonian : dict
        Paulilist format: {pauli_string: coefficient}
    """
    pass

def build_mbl_hamiltonian(n_qubits, disorder_strength, interaction_strength=1.0):
    """
    Construct Many-Body Localization test Hamiltonian.
    
    H = sum_i h_i Z_i + sum_i J X_i X_{i+1}
    
    where h_i ~ Uniform[-W, W] is random disorder
    """
    pass

def build_variational_ansatz(n_qubits, module_width, depth, params, mcm_positions=None):
    """
    Build parameterized variational circuit.
    
    Parameters:
    -----------
    n_qubits : int
    module_width : int (k)
    depth : int
    params : array of shape (n_params,)
        Rotation angles
    mcm_positions : list of int
        Layer indices where MCMs are inserted
    
    Returns:
    --------
    circuit : Qiskit QuantumCircuit
    """
    pass
