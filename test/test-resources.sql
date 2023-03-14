CREATE OR REPLACE TABLE test_udtf(
    `group` VARCHAR,
    quantity NUMBER,
    price NUMBER
);

INSERT INTO test_udtf (group, quantity, price) 
VALUES ("A", 1, 5),
       ("A", 2, 2),
       ("B", 1, 0),
       ("B", 5, 1),
       ("C", 1, 1);