nginx:
  pkg:
    - installed

nginx_run:
  service.running:
    - name: nginx
    - enable: True
    - watch:
      - file: /etc/nginx/nginx.conf
      - file: /etc/nginx/sites-available/dotmanca
    - require:
      - file: /etc/nginx/sites-enabled/dotmanca
      - file: /etc/nginx/nginx.conf
      - pkg: nginx
  
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
    - require:
      - pkg: nginx

/etc/nginx/sites-enabled/dotmanca:
  file.symlink:
    - target: /etc/nginx/sites-available/dotmanca
    - user: root
    - group: root
    - mode: 644
    - require:
      - file: /etc/nginx/sites-available/dotmanca

/etc/nginx/sites-enabled/default:
  file.absent:
    - name: /etc/nginx/sites-enabled/default
    - require:
      - pkg: nginx
