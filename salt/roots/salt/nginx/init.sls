nginx:
  pkg:
    - installed
  service.running:
    - enable: True
    - watch:
      - file: /etc/nginx/nginx.conf
      - file: /etc/nginx/sites-available/dotmanca

/etc/nginx/nginx.conf:
  file:
    - managed
    - source: salt://nginx/nginx.conf
    - user: root
    - group: root
    - mode: 644

/etc/nginx/sites-available/dotmanca:
  file:
    - managed
    - source: salt://nginx/dotmanca.conf
    - user: root
    - group: root
    - mode: 644

/etc/nginx/sites-enabled/dotmanca:
  file.symlink:
    - target: /etc/nginx/sites-available/dotmanca
    - user: root
    - group: root
    - mode: 644

/etc/nginx/sites-available/default:
  file:
    - absent

/etc/nginx/sites-enable/default:
  file:
    - absent
