{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.pillow  # For image rendering
    pkgs.python3Packages.tkinter # For tkinter GUI
  ];

  # Optionally, set the Python environment
  PYTHONPATH = "${pkgs.python3Packages.pillow}:${pkgs.python3Packages.tkinter}";

  # Enable GUI support
  shellHook = ''
    export DISPLAY=:0
  '';
}
