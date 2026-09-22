def should_surface(relevance: float, expired: bool, urgent: bool) -> bool:
    if expired:
        return False
    
    return relevance >= 0.8 or urgent


