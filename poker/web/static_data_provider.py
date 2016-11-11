from model.model import Role

ROLES = [
    Role("dev", "Developer", True),
    Role("qa", "Quality Assurance", True),
    Role("ba", "Business Analyst", True),
    Role("po", "Product Owner", False),
    Role("spec", "Spectator", False)
]
