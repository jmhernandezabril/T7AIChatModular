# replit.nix
{ pkgs }: {
  deps = [
    # El intérprete de Python
    pkgs.python310

    # Frameworks y librerías
    pkgs.python310Packages.flask
    pkgs.python310Packages.streamlit
    pkgs.python310Packages.pandas
    pkgs.python310Packages.plotly
    pkgs.python310Packages.sqlparse
  ];
}