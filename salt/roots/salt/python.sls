python3:
  pkg:
    - installed

python-virtualenv:
  pkg:
    - installed

prepare-virtual-env:
  cmd.run:
    - user: vagrant
    - name: "virtualenv -p /usr/bin/python3 django-env"
    - require:
      - pkg: python3
      - pkg: python-virtualenv
