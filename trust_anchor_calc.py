# Illustrative function for the Trust Anchor Metric (Layer 4)

def calculate_trust_anchor(governance_score, compliance_debt_factor):
    """
    Returns a score indicating the auditable integrity of a deployed model artifact.
    Governance score is based on adherence to the Integrity Stack Framework (0-100).
    Compliance Debt Factor increases risk based on known vulnerabilities (0-1).
    """
    
    # Simple, illustrative, non-proprietary calculation:
    raw_score = governance_score / 100 
    
    # The Trust Anchor is penalized by the existence of debt
    trust_anchor = raw_score * (1 - compliance_debt_factor)
    
    return round(max(0, trust_anchor), 4)

# Example Usage:
# print(calculate_trust_anchor(governance_score=95, compliance_debt_factor=0.1)) 
# Output: 0.855
