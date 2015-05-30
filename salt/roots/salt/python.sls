include:
  - postgresql
  - miscDevLibs

python3:
  pkg:
    - installed

python3-dev:
  pkg:
    - installed
    - require: 
      - pkg: python3

python3-psycopg2:
  pkg:
    - installed
    - require: 
      - pkg: python3-dev

Run VENV Workaround:
  cmd.run:
    - name: /vagrant/scripts/pyVenvForTrusty.sh
    - cwd: /home/vagrant/
    - user: vagrant
    - require:
      - pkg: python3-dev
      - sls: postgresql

Install PIP packages:
  cmd.run:
    - name: /vagrant/scripts/pipInstallReqs.sh
    - cwd: /home/vagrant/
    - user: vagrant
    - watch:
      - cmd: Run VENV Workaround
      - sls: miscDevLibs
