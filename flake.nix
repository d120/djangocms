{
  description = "An instance of django CMS used to build d120.de.";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-22.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = nixpkgs.legacyPackages.${system}; in {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
            nodePackages.npm
            (python39.withPackages (ps: with ps; [ virtualenv ]))
            libmysqlclient
            openldap
            cyrus_sasl
            gettext
          ];
        };
      }
    );

}
