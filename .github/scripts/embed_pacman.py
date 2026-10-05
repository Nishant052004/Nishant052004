import re
import os
import xml.etree.ElementTree as ET

pacman_path = os.path.join('dist', 'pacman-contribution-graph-dark.svg')
if not os.path.exists(pacman_path):
    pacman_path = os.path.join('.github', 'assets', 'pacman.svg')

if not os.path.exists(pacman_path):
    print("Pac-Man SVG not found.")
    exit(0)

with open(pacman_path, 'r', encoding='utf-8') as f:
    pacman_svg = f.read()

# Make background transparent
pacman_svg = pacman_svg.replace('<rect width="100%" height="100%" fill="#0d1117"/>', '<rect width="100%" height="100%" fill="transparent"/>')

# Convert outer <svg> of pacman to nested <svg> with position
nested_pacman = re.sub(
    r'^<svg\s+width="1166"\s+height="184"[^>]*>',
    '<svg viewBox="0 0 1166 184" x="30" y="646" width="740" height="117">',
    pacman_svg.strip()
)

profile_path = os.path.join('.github', 'assets', 'profile.svg')
if not os.path.exists(profile_path):
    print("profile.svg not found.")
    exit(0)

with open(profile_path, 'r', encoding='utf-8') as f:
    current_svg = f.read()

# Pattern for ACTIVITY PULSE section
pulse_pattern = re.compile(
    r'(<!-- ═══════════ ACTIVITY PULSE.*?Pac-Man Mode 🟡 ᗧ •••</text>\s*\n\s*)(<svg.*?</svg>)(\s*\n</g>)',
    re.DOTALL
)

if pulse_pattern.search(current_svg):
    updated_svg = pulse_pattern.sub(r'\1' + nested_pacman + r'\3', current_svg)
    try:
        ET.fromstring(updated_svg)
        with open(profile_path, 'w', encoding='utf-8') as f:
            f.write(updated_svg)
        print("Successfully synchronized profile.svg with latest Pac-Man animation!")
    except Exception as e:
        print(f"XML Validation Error: {e}")
else:
    print("ACTIVITY PULSE Pac-Man pattern not matched.")
