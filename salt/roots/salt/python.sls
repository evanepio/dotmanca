python3:
  pkg:
    - installed

python3-dev:
  pkg:
    - installed
  require: 
    - pkg: python3

python3-psycopg2:
  pkg:
    - installed
  require: 
    - pkg: python3
