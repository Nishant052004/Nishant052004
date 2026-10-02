import re
import urllib.request
import xml.etree.ElementTree as ET
import os

# Fetch live snake SVG
url = 'https://raw.githubusercontent.com/Nishant052004/Nishant052004/output/github-contribution-grid-snake-dark.svg'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    resp = urllib.request.urlopen(req)
    snake_svg = resp.read().decode('utf-8')
except Exception as e:
    print(f"Error fetching snake SVG: {e}")
    exit(0)

# Convert outer <svg> of snake to nested <svg> with position
nested_snake = re.sub(
    r'^<svg\s+[^>]*>',
    '<svg viewBox="-16 -32 880 192" x="30" y="646" width="740" height="162">',
    snake_svg.strip()
)

profile_path = os.path.join('.github', 'assets', 'profile.svg')
if not os.path.exists(profile_path):
    print("profile.svg not found")
    exit(0)

with open(profile_path, 'r', encoding='utf-8') as f:
    current_svg = f.read()

# Replace existing nested snake in ACTIVITY PULSE
pulse_pattern = re.compile(
    r'(<!-- ═══════════ ACTIVITY PULSE.*?Live Contribution Grid 🐍</text>\s*\n\s*)(<svg.*?</svg>)(\s*\n</g>)',
    re.DOTALL
)

if pulse_pattern.search(current_svg):
    updated_svg = pulse_pattern.sub(r'\1' + nested_snake + r'\3', current_svg)
    try:
        ET.fromstring(updated_svg)
        with open(profile_path, 'w', encoding='utf-8') as f:
            f.write(updated_svg)
        print("Successfully synchronized profile.svg with latest snake animation!")
    except Exception as e:
        print(f"XML Validation Error: {e}")
else:
    print("ACTIVITY PULSE pattern not matched")
