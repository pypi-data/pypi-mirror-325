def setup_simple_firewall(rules: dict) -> None:
    print("Applying firewall rules...")
    for rule, action in rules.items():
        print(f"Rule: {rule}, Action: {action}")
