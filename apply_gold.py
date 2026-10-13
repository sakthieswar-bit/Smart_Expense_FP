import re, shutil, os

M = [
 ("#8b5cf6","#f5c451"),("#d946ef","#e8a92a"),("#c4b5fd","#f7d27a"),("#a78bfa","#f7d27a"),
 ("rgba(139, 92, 246,","rgba(245, 196, 81,"),("rgba(217, 70, 239,","rgba(232, 169, 42,"),
 ("rgba(47, 91, 255,","rgba(245, 196, 81,"),
 ("#1f1b33","#2b2415"),("#0a0a12","#0d0b07"),("#11111c","#15110a"),
 ("#8b8aa3","#a39878"),("#f5f5fa","#f4ecd8"),("#a5a3c0","#c7bb9a"),("#d6d5e6","#e6dcc3"),
 ("#55546e","#6f664d"),("#1a1830","#231c0e"),("#2a2548","#3a2f17"),
]

def remap(s):
    for a, b in M:
        s = s.replace(a, b)
    return s

def load(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def save(path, text):
    shutil.copyfile(path, path + ".bak")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("updated", path)

def swap(text, old, new, label):
    if old not in text:
        print("  WARNING: could not find", label)
        return text
    return text.replace(old, new, 1)

# ---------------- style.css ----------------
p = "static/css/style.css"
css = remap(load(p))
css = swap(css, '@import url("https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap");',
    '@import url("https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap");', "font import")
css = swap(css, "--bg: #000000;", "--bg: #060504;", "--bg")
css = swap(css, "--blue: #2f5bff;", "--blue: linear-gradient(135deg, #ffe08a, #e8a92a);", "--blue")
css = swap(css, "--gradient: linear-gradient(90deg, #f5c451, #e8a92a);",
    "--gradient: linear-gradient(90deg, #fff1b8, #f5c451 45%, #e8a92a);", "--gradient")
css = css.replace("#4a70ff", "#fff0b3")
css = re.sub(r"(\.btn \{[^}]*?)color: white;", r"\1color: #1a1203;", css, count=1, flags=re.S)
css = re.sub(r"(\.auth-btn \{[^}]*?)color: white;", r"\1color: #1a1203;", css, count=1, flags=re.S)
css = swap(css, ".logo {\n    font-size: 22px;", '.logo {\n    font-family: "Cinzel", Georgia, serif;\n    font-size: 22px;', ".logo")
save(p, css)

# ---------------- base.html ----------------
EXTRA = '''
    /* ---------- gold effects ---------- */
    .content h1, .content h2, .topbar h1, .logo {
        font-family: "Cinzel", Georgia, serif;
        letter-spacing: 0.02em;
    }
    .content h1, .content h2 { font-weight: 700; }

    .stat-card-value {
        font-family: "Cinzel", Georgia, serif;
        background: linear-gradient(180deg, #fff1b8, #e8a92a);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        color: transparent !important;
    }

    .stat-card, .chart-card, .dashboard-card, .budget-card, .report-card,
    .transactions-card, .form-card, .edit-form-card, .budget-form-card,
    .category-form-card, .categories-card, .notification-card {
        background-image: linear-gradient(180deg, rgba(245, 196, 81, 0.06), transparent 45%) !important;
        box-shadow: inset 0 1px 0 rgba(255, 225, 138, 0.14) !important;
        transition: border-color 0.25s ease, box-shadow 0.25s ease, transform 0.25s ease;
    }
    .stat-card:hover, .budget-card:hover {
        border-color: rgba(245, 196, 81, 0.5) !important;
        box-shadow: 0 0 34px rgba(245, 196, 81, 0.14), inset 0 1px 0 rgba(255, 225, 138, 0.2) !important;
        transform: translateY(-2px);
    }

    #goldDust { position: fixed; inset: 0; width: 100%; height: 100%; pointer-events: none; z-index: -1; }

    @media (prefers-reduced-motion: reduce) {
        .stat-card:hover, .budget-card:hover { transform: none; }
    }
</style>

<!-- CHART.JS -->'''

p = "templates/base.html"
b = load(p)
if "gold effects" in b:
    print("base.html already converted, skipping")
else:
    b = remap(b)
    b = swap(b, '<link rel="icon"',
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n    <link rel="icon"', "icon link")
    b = swap(b, "        background: #2f5bff !important;\n        color: #fff !important;",
        "        background: linear-gradient(135deg, #ffe08a, #e8a92a) !important;\n        color: #1a1203 !important;", "button colors")
    b = swap(b, "        background: #4a70ff !important;\n        box-shadow: 0 0 22px rgba(245, 196, 81, 0.45) !important;",
        "        background: linear-gradient(135deg, #fff0b3, #f5c451) !important;\n        box-shadow: 0 0 24px rgba(245, 196, 81, 0.5) !important;", "button hover")
    b = swap(b, "</style>\n\n<!-- CHART.JS -->", EXTRA, "override block end")
    b = swap(b, "<script src=\"{{ url_for('static', filename='js/app.js') }}\"></script>",
        "<script src=\"{{ url_for('static', filename='js/app.js') }}\"></script>\n<script src=\"{{ url_for('static', filename='js/fx.js') }}\"></script>", "app.js tag")
    save(p, b)

# ---------------- app.js (chart colors) ----------------
p = "static/js/app.js"
js = load(p)
js = swap(js, '''const categoryColors = [
        "#8b5cf6", "#d946ef", "#2f5bff", "#22d3ee",
        "#a78bfa", "#f472b6", "#6366f1", "#c084fc"
    ];''', '''const categoryColors = [
        "#f5c451", "#e8a92a", "#fff0b3", "#b8791a",
        "#d9b15a", "#8a5a0c", "#f7d98c", "#c98b1e"
    ];''', "category colors")
js = swap(js, 'const textColor = "#a5a3c0";', 'const textColor = "#c7bb9a";', "text color")
js = swap(js, 'const mutedColor = "#8b8aa3";', 'const mutedColor = "#a39878";', "muted color")
js = swap(js, 'const gridColor = "#1f1b33";', 'const gridColor = "#2b2415";', "grid color")
js = js.replace('borderColor: "#000000"', 'borderColor: "#060504"')
js = swap(js, 'backgroundColor: ["#8b5cf6", "#d946ef"]', 'backgroundColor: ["#f5c451", "#b8791a"]', "bar colors")
save(p, js)

print("done")