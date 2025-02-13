#let
#  pkgs = import <nixpkgs> {
#    # config = {
#    #   enableCuda = true;
#    # };
#  };
#  python312_3 = pkgs.python3.overrideAttrs (old: {
#    version = "3.12.3";
#    src = builtins.fetchTarball {
#      url = "https://github.com/NixOS/nixpkgs/archive/0c19708cf035f50d28eb4b2b8e7a79d4dc52f6bb.tar.gz";
#      sha256 = "sha256:0ngw2shvl24swam5pzhcs9hvbwrgzsbcdlhpvzqc7nfk8lc28sp3"; # Replace with the correct SHA256 hash for the tarball
#    };
#  });
#in

let
    pkgs = import (builtins.fetchTarball {
        url = "https://github.com/NixOS/nixpkgs/archive/0c19708cf035f50d28eb4b2b8e7a79d4dc52f6bb.tar.gz";
    }) {};

    python312_3 = pkgs.python312;
in
pkgs.mkShell {
  name = "venv-shell";
  shellHook = ''
    if [ ! -d "venv" ]; then
      python3 -m venv venv
      source venv/bin/activate
      pip install -U pip
      pip install -e .
    else
      source venv/bin/activate
    fi

    export LD_LIBRARY_PATH=${
      pkgs.lib.makeLibraryPath (with pkgs; [
        pkgs.stdenv.cc.cc
        pkgs.zlib
        libGL
        glib
      ])
    }
  '';

  buildInputs = with pkgs; [
    python312_3
    python312Packages.numpy
    python312Packages.ipython
    python312Packages.magic
  ];
}
