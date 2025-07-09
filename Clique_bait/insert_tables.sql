INSERT INTO event_identifier
VALUES
  ('1', 'Page View'),
  ('2', 'Add to Cart'),
  ('3', 'Purchase'),
  ('4', 'Ad Impression'),
  ('5', 'Ad Click');

INSERT INTO campaign_identifier
VALUES
  ('1', '1-3', 'BOGOF - Fishing For Compliments', '2020-01-01', '2020-01-14'),
  ('2', '4-5', '25% Off - Living The Lux Life', '2020-01-15', '2020-01-28'),
  ('3', '6-8', 'Half Off - Treat Your Shellf(ish)', '2020-02-01', '2020-03-31');

INSERT INTO page_hierarchy
VALUES
  ('1', 'Home Page', null, null),
  ('2', 'All Products', null, null),
  ('3', 'Salmon', 'Fish', '1'),
  ('4', 'Kingfish', 'Fish', '2'),
  ('5', 'Tuna', 'Fish', '3'),
  ('6', 'Russian Caviar', 'Luxury', '4'),
  ('7', 'Black Truffle', 'Luxury', '5'),
  ('8', 'Abalone', 'Shellfish', '6'),
  ('9', 'Lobster', 'Shellfish', '7'),
  ('10', 'Crab', 'Shellfish', '8'),
  ('11', 'Oyster', 'Shellfish', '9'),
  ('12', 'Checkout', null, null),
  ('13', 'Confirmation', null, null);
  
INSERT INTO users
VALUES 
    (397, '3759ff', '2020-03-30 00:00:00'),
    (215, '863329', '2020-01-26 00:00:00'),
    (191, 'eefcag', '2020-03-15 00:00:00'),
    (89, '764796', '2020-01-07 00:00:00'),
    (127, '17ccc5', '2020-01-22 00:00:00'),
    (81, 'b0b666', '2020-03-01 00:00:00'),
    (260, 'a4f236', '2020-01-08 00:00:00'),
    (203, 'd1182f', '2020-04-18 00:00:00'),
    (23, '12dbc8', '2020-01-18 00:00:00'),
    (375, 'f61d69', '2020-01-03 00:00:00');
    
INSERT INTO events
VALUES 
    ('719fd3', '3d83d3', 5, 1, 4, '2020-03-02 00:29:09.975'),
    ('fb1eb1', 'c5ff25', 5, 2, 8, '2020-01-22 07:59:16.761'),
    ('23fe81', '1e8c2d', 10, 1, 9, '2020-03-21 13:14:11.745'),
    ('ad91aa', '648115', 6, 1, 3, '2020-04-27 16:28:09.824'),
    ('5576d7', 'ac418c', 6, 1, 4, '2020-01-18 04:55:10.149'),
    ('48308b', 'c686c1', 8, 1, 5, '2020-01-29 06:10:38.702'),
    ('46b17d', '78f9b3', 7, 1, 12, '2020-02-16 09:45:31.926'),
    ('9fd196', 'ccf057', 4, 1, 5, '2020-02-14 08:29:12.922'),
    ('edf853', 'f85454', 1, 1, 1, '2020-02-22 12:59:07.652'),
    ('3c6716', '02e74f', 3, 2, 5, '2020-01-31 17:56:20.777');