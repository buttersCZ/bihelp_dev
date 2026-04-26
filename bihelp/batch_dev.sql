--db/bigquery/01-create/create.sql/
CREATE TABLE IF NOT EXISTS `prod_project.core.products` (
  id INT64,
  name STRING
);


--db/bigquery/02-insert/insert.sql/
INSERT INTO `prod_project.core.products` (id, name)
VALUES (1, 'Beer'), (2, 'Wine');


