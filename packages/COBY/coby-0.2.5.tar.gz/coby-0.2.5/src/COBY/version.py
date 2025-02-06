__version__="0.2.5"

major_changes = [
    "Added support for reading and writing pdbx/mmCIF (.cif) files.",
    [
        "Added 'out_cif'/'o_cif' argument to determine output file name for .cif files.",
        "The 'out_all'/'o_all' and 'out_sys'/'o_sys' arguments now also determine the output file name for .cif files.",
        "The .cif file reader requires the following dictionary keys (pdb file equivalent).",
        [
            "'_atom_site.id'           (Atom number)",
            "'_atom_site.auth_atom_id' (Atom name)",
            "'_atom_site.auth_comp_id' (Residue name)",
            "'_atom_site.auth_seq_id'  (Residue number)",
            "'_atom_site.Cartn_x'      (X-value)",
            "'_atom_site.Cartn_y'      (Y-value)",
            "'_atom_site.Cartn_z'      (Z-value)",
        ],
        "The .cif file writer writes the following dictionary keys (pdb file equivalent). The last four values are written because ChimeraX requires them to be present in order for it to read a .cif file.",
        [
            "'_atom_site.id'            (Atom number)",
            "'_atom_site.auth_atom_id'  (Atom name)",
            "'_atom_site.auth_comp_id'  (Residue name)",
            "'_atom_site.auth_seq_id'   (Residue number)",
            "'_atom_site.Cartn_x'       (X-value)",
            "'_atom_site.Cartn_y'       (Y-value)",
            "'_atom_site.Cartn_z'       (Z-value)",
            "'_atom_site.label_asym_id' (Chain identifier. Always writes 'A')",
            "'_atom_site.label_atom_id' (Atom name)",
            "'_atom_site.label_comp_id' (Residue name)",
            "'_atom_site.label_seq_id'  (Residue number)",
            "'_atom_site.type_symbol'   (Atomic symbol. Not that relevant for coarse-grain so it just writes the first letter of the atom name)",
        ],
    ],
]

minor_changes = [
    "COBY.Library:",
    [
        "Removed 'bak.Library_class.py' which was accidentally left in, when uploading version 0.2.4.",
        "Slightly changed the initial argument warning when running COBY.Library using non-valid arguments.",
        "Made COBY.Library available from the terminal. The functionality can be accessed as shown below.",
        [
            "python -m COBY -program Library",
        ],
    ],
    "Made a separate method for structure file (pdb/gro/cif) importing to ensure it always functions the same way.",
]

bug_fixes = [
]

documentation_changes = [
    "Updated documentation for COBY.Library to also include an example of how to access COBY.Library from the terminal.",
]

tutorial_changes = [
]

def version_change_writer(iterable, recursion_depth = 0):
    list_of_strings = []
    for i in iterable:
        if type(i) == str:
            ### Headers
            if recursion_depth == 0:
                list_of_strings.append(i)
            ### Changes. -1 to have no spaces for first recursion. Two spaces "  " to fit with GitHub list formatting.
            else:
                list_of_strings.append("  " * (recursion_depth - 1) + "-" + " " + i)

        elif type(i) in [list, tuple]:
            list_of_strings.extend(version_change_writer(i, recursion_depth + 1))
    return list_of_strings

### Extra empty "" is to add a blank line between sections
all_changes = []
if len(major_changes) > 0:
    all_changes += ["Major changes:", major_changes, ""]

if len(minor_changes) > 0:
    all_changes += ["Minor changes:", minor_changes, ""]

if len(bug_fixes) > 0:
    all_changes += ["Bug fixing:", bug_fixes, ""]

if len(documentation_changes) > 0:
    all_changes += ["Documentation changes:", documentation_changes, ""]

if len(tutorial_changes) > 0:
    all_changes += ["Tutorial changes:", tutorial_changes, ""]

if len(all_changes) > 0:
    all_changes = all_changes[:-1] # Removes the last ""

version_changes_list = version_change_writer(all_changes)
version_changes_str = "\n".join(version_changes_list)

def version_changes():
    print(version_changes_str)

### Abbreviations
changes   = version_changes
changelog = version_changes

