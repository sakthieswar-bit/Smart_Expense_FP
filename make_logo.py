import os

LOGO = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200" role="img" aria-label="Smart Expense logo">
  <defs>
    <linearGradient id="gGold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f3d98b"/>
      <stop offset="0.45" stop-color="#c9a24a"/>
      <stop offset="1" stop-color="#6e5524"/>
    </linearGradient>
    <linearGradient id="gGoldDark" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#a78434"/>
      <stop offset="1" stop-color="#4a3a17"/>
    </linearGradient>
    <linearGradient id="gGoldLight" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff0bd"/>
      <stop offset="1" stop-color="#d4af5a"/>
    </linearGradient>
    <linearGradient id="gFlare" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="#f3d98b" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#f3d98b" stop-opacity="0.9"/>
      <stop offset="1" stop-color="#f3d98b" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="gGlow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#c9a24a" stop-opacity="0.35"/>
      <stop offset="1" stop-color="#c9a24a" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="200" height="200" rx="44" fill="#050507"/>
  <rect x="1" y="1" width="198" height="198" rx="43" fill="none" stroke="#2a2210" stroke-width="2"/>
  <circle cx="100" cy="104" r="86" fill="url(#gGlow)"/>

  <g filter="url(#soft)">
    <polygon points="54,124 92,124 154,172 116,172" fill="url(#gGoldDark)"/>
    <polygon points="54,124 72,124 134,172 116,172" fill="url(#gGold)" opacity="0.95"/>

    <polygon points="128,56 154,56 154,126 128,126" fill="url(#gGold)"/>
    <polygon points="128,56 138,56 138,126 128,126" fill="url(#gGoldLight)" opacity="0.5"/>
    <polygon points="48,106 154,106 154,128 70,128" fill="url(#gGoldDark)"/>
    <polygon points="48,106 154,106 154,114 54,114" fill="url(#gGoldLight)" opacity="0.5"/>

    <polygon points="40,34 150,34 168,56 40,56" fill="url(#gGold)"/>
    <polygon points="40,34 150,34 156,41 40,41" fill="url(#gGoldLight)" opacity="0.7"/>

    <polygon points="40,68 168,68 168,90 40,90" fill="url(#gGold)"/>
    <polygon points="40,68 168,68 168,75 40,75" fill="url(#gGoldLight)" opacity="0.7"/>

    <polygon points="128,90 154,90 154,106 128,106" fill="#000" opacity="0.25"/>
    <polygon points="128,56 154,56 154,68 128,68" fill="#000" opacity="0.2"/>
  </g>

  <g fill="none" stroke="#fff0bd" stroke-opacity="0.35" stroke-width="0.8">
    <path d="M40 34 H150 L168 56 H40 Z"/>
    <path d="M40 68 H168 V90 H40 Z"/>
  </g>

  <line x1="14" y1="40" x2="70" y2="8" stroke="url(#gFlare)" stroke-width="2.5" stroke-linecap="round"/>
</svg>
"""

FAV = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f3d98b"/><stop offset="1" stop-color="#8a6a2a"/>
    </linearGradient>
  </defs>
  <rect width="64" height="64" rx="14" fill="#050507"/>
  <g fill="url(#g)">
    <polygon points="13,12 48,12 54,19 13,19"/>
    <polygon points="13,23 54,23 54,30 13,30"/>
    <polygon points="40,19 49,19 49,40 40,40"/>
    <polygon points="16,34 49,34 49,41 22,41"/>
    <polygon points="18,41 28,41 47,56 37,56"/>
  </g>
</svg>
"""

os.makedirs("static/img", exist_ok=True)

for name, text in (("logo.svg", LOGO), ("favicon.svg", FAV)):
    path = os.path.join("static", "img", name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("written", path, os.path.getsize(path), "bytes")

print("Done. Restart the app and press Ctrl+Shift+R.")