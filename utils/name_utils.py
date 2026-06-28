import re


PREFIXES = [
    "H.",
    "Hj.",
    "Dr.",
    "dr.",
    "drg.",
    "Prof.",
    "Ir."
]

SUFFIXES = [
    "S.H.",
    "S.E.",
    "S.Kom.",
    "S.T.",
    "S.Ak.",
    "M.H.",
    "M.M.",
    "M.Kom.",
    "M.Pd.",
    "M.Si.",
    "Sp.A",
    "Sp.PD"
]


def clean_name(name: str) -> str:
    # Hapus prefix
    for prefix in PREFIXES:
        if name.startswith(prefix + " "):
            name = name[len(prefix):].strip()

    # Hapus suffix
    parts = [p.strip() for p in name.split(",")]

    # Ambil nama pertama saja
    name = parts[0]

    return re.sub(r"\s+", " ", name).strip()