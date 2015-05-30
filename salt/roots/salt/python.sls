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

python-create-venv-using-workaround:
  cmd.run:
    - name: /vagrant/scripts/pyVenvForTrusty.sh
    - cwd: /home/vagrant/
    - user: vagrant
    - require:
      - pkg: python3-dev
      - sls: postgresql

python-pip-install-requirements:
  cmd.run:
    - name: /vagrant/scripts/pipInstallReqs.sh
    - cwd: /home/vagrant/
    - user: vagrant
    - watch:
      - cmd: python-create-venv-using-workaround
      - sls: miscDevLibs
