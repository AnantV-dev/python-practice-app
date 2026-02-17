import toml

file = "pyproject.toml"
data = toml.load(file)

version = data["project"]["version"]
major, minor, patch = map(int, version.split("."))
patch += 1
new_version = f"{major}.{minor}.{patch}"

data["project"]["version"] = new_version
with open(file, "w") as f:
    toml.dump(data, f)

print(f"Bumped version to {new_version}")
