--db/bigquery/01-create/create.sql/
CREATE TABLE IF NOT EXISTS `bqtesting-494319.core_dev.products` (
  id INT64,
  name STRING
);


--db/bigquery/02-insert/insert.sql/
INSERT INTO `bqtesting-494319.core_dev.products` (id, name)
VALUES (1, 'Beer'), (2, 'Wine');


