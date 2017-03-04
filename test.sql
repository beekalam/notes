#+name: my-query
#+header: :engine postgresql
#+header: :dbhost 127.0.0.1
#+header: :dbuser postgres
#+header: :dbpassword jjj
#+header: :database test2
#+begin_src sql
SELECT s,md5 FROM huge_data_table limit 10;
#+end_src
