{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    nodePackages.npm
    (python37.withPackages (ps: with ps; [ virtualenv ]))
    libmysqlclient
    openldap
    cyrus_sasl
  ];

  shellHook = ''
    unset SOURCE_DATE_EPOCH
    [ -d venv ] || virtualenv -p python3 venv
    source venv/bin/activate
  '';
}