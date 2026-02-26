import sys
import io
import os
import importlib


buf = io.StringIO()
orig_stdout = sys.stdout
orig_system = os.system
sys.stdout = buf
os.system = lambda cmd: 0  

try:
    # (Pārliecināmies, ka mods tiek (re)ielādēts, lai tests būtu reproducējams)
    if "task" in sys.modules:
        task = importlib.reload(sys.modules["task"])
    else:
        task = importlib.import_module("task")
finally:
    # Atjauno oriģinālos rīkus
    sys.stdout = orig_stdout
    os.system = orig_system

# Saņemam importēto moduļa izvadi
output = buf.getvalue()

# Pārbaudes: mainīgo vērtības
assert abs(getattr(task, "kakis") - 2.0) < 1e-9, f"kakis expected 2.0, got {getattr(task, 'kakis')}"
assert abs(getattr(task, "suns") - 4.0) < 1e-9, f"suns expected 4.0, got {getattr(task, 'suns')}"
# 'kopā' contains a non-ASCII character in the variable name; use getattr for safety
assert abs(getattr(task, "kopā") - 6.0) < 1e-9, f"kopā expected 6.0, got {getattr(task, 'kopā')}"

# Pārbaude uz izdrukām (vienkārši pārbaudām, vai satur gaidītās virsrakstus)
assert "Kaķis" in output, "Output missing 'Kaķis' line"
assert "Suns" in output, "Output missing 'Suns' line"
assert "Kopā" in output, "Output missing 'Kopā' line"

# Ja visas assert nav neizmetušas izņēmumu, tests pāriet
print("All asserts passed for task.py")