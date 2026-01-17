def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate BMI from height and weight lists."""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both height and weight must be lists.")
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length")
    if len(height) == 0:
        raise ValueError("Lists cannot be empty")
    for h in height:
        if not isinstance(h, (int, float)) or h <= 0:
            raise ValueError("Height values must be int or float and positive")
    for w in weight:
        if not isinstance(w, (float, int)) or w < 0:
            raise ValueError("Weight values must be int or float and positive")
    bmi = [w / (h ** 2) for h, w in zip(height, weight)]
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check if BMI values are above a given limit."""
    if not isinstance(bmi, list):
        raise TypeError("BMI must be a list")
    if not isinstance(limit, int):
        raise ValueError("Limit must be a number(int)")
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("All BMI values must be numbers")
    return [b > limit for b in bmi]
