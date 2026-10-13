import os, shutil

REQUIRED = [
    "static/css/style.css",
    "static/css/auth.css",
    "static/js/app.js",
    "static/js/fx.js",
    "static/img/logo.svg",
    "static/img/favicon.svg",
    "templates/base.html",
    "templates/login.html",
    "templates/signup.html",
    "templates/_gold_scene.html",
]

SKIP = {".git", "venv", ".venv", "__pycache__", "node_modules"}


def find_elsewhere(name, target):
    """Look for a file with this name anywhere in the project."""
    target = os.path.normpath(target)
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SKIP]
        if name in files:
            path = os.path.normpath(os.path.join(root, name))
            if path != target:
                return path
    return None


print("Checking project files...\n")

for path in REQUIRED:
    name = os.path.basename(path)
    if os.path.exists(path):
        print("OK       ", path, "(%d bytes)" % os.path.getsize(path))
        continue

    other = find_elsewhere(name, path)
    if other:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        shutil.move(other, path)
        print("MOVED    ", other, "->", path)
    else:
        print("MISSING  ", path, "  <-- you need to create this file")

# remove empty leftover folders inside static/
for root, dirs, files in os.walk("static", topdown=False):
    if root != "static" and not os.listdir(root):
        os.rmdir(root)
        print("REMOVED EMPTY FOLDER", root)

# sanity checks on content
print()
def read(p):
    try:
        with open(p, encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""

css = read("static/css/style.css")
if "f5f7fb" in css:
    print("WARNING: static/css/style.css is still the OLD light version. Paste the gold style.css.")
elif css:
    
    print("style.css looks like the gold version.")

auth = read("static/css/auth.css")
if auth and len(auth) < 5000:
    print("WARNING: static/css/auth.css looks too short. Paste the full file.")

if "gold effects" not in read("templates/base.html"):
    print("WARNING: templates/base.html does not have the gold block yet.")

print("\nDone. Now restart the app (Ctrl+C, then python app.py) and press Ctrl+Shift+R in the browser.")