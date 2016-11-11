from model.model import Role

ROLES = [
    Role("dev", "Developer", True),
    Role("qa", "Quality Assurance", True),
    Role("ba", "Business Analyst", True),
    Role("po", "Product Owner", False),
    Role("spec", "Spectator", False)
]


def get_role_by_short_name(sn):
    result = [r for r in ROLES if r.short_name == sn]
    if len(result) == 1:
        return result[0]
    else:
        return None
