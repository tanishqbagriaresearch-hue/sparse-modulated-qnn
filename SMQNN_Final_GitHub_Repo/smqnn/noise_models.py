class NoiseModel:
    """
    Simulate hardware depolarization and MCM noise filtering.
    
    Parameters:
    -----------
    depolarization_rate : float
        Per-gate error rate (p in E_p)
    measurement_error_rate : float
        Readout error rate
    reset_fidelity : float
        Fidelity of MCM reset operation (default 1.0 for ideal)
    """
    
    def apply_depolarizing_channel(self, circuit, depth):
        """
        Apply depolarizing noise to circuit.
        
        Returns:
        --------
        state_fidelity : float
            Trace distance to target state after noise
        """
        pass
    
    def compute_noise_scaling(self, depths_array, mcm_fractions):
        """
        Compute signal fidelity vs circuit depth for different MCM fractions.
        
        Returns:
        --------
        fidelity_vs_depth : dict
            {mcm_fraction: [fidelity values for each depth]}
        """
        pass
    
    def get_effective_correlation_length(self, module_width, mcm_fraction):
        """Return k_eff = k * (1 - f_mcm / 2)"""
        pass
