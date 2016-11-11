from model.model import Role, Estimate

ROLES = [
    Role("dev", "Developer", True),
    Role("qa", "Quality Assurance", True),
    Role("ba", "Business Analyst", True),
    Role("po", "Product Owner", False),
    Role("spec", "Spectator", False)
]

ESTIMATES = [
    Estimate(0.0, "0"),
    Estimate(0.5, "0.5"),
    Estimate(1.0, "1"),
    Estimate(2.0, "2"),
    Estimate(3.0, "3"),
    Estimate(5.0, "5"),
    Estimate(8.0, "8"),
    Estimate(13.0, "13"),
    Estimate(20.0, "20"),
    Estimate(40.0, "40"),
    Estimate(100.0, "100"),
    Estimate(0.0, "?"),
    Estimate(0.0, "Coffee")
]


def get_role_by_short_name(sn):
    result = [r for r in ROLES if r.short_name == sn]
    if len(result) == 1:
        return result[0]
    else:
        return None
