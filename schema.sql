drop table if exists user;
    create table user (
    id integer primary key autoincrement,
    email text not null,
    password text not null
);



drop table if exists preferences;
create table preferences (
  id integer primary key autoincrement,
  user_email text not null,
  sex INT(2),
  age INT,
  city_id INT,
  city_name TEXT,
  budget INT(3),
  active INT(2),
  Asian TINYINT(1), American TINYINT(1), Breakfast TINYINT(1), Bubble_Tea TINYINT(1), Cafe TINYINT(1),
  Fast_Food TINYINT(1), Indian TINYINT(1), Italian TINYINT(1), Mediterranean TINYINT(1), Mexican TINYINT(1), Pizza TINYINT(1));
--
-- --
-- -- --   -- Afghan TINYINT(1), African TINYINT(1), American TINYINT(1), Argentine TINYINT(1), Armenian TINYINT(1), Asian TINYINT(1), BBQ TINYINT(1), Bagels TINYINT(1), Bakery TINYINT(1), Bar_Food TINYINT(1), Belgian TINYINT(1), Beverages TINYINT(1), Brazilian TINYINT(1), Breakfast TINYINT(1), British TINYINT(1), Bubble_Tea TINYINT(1), Burger TINYINT(1),
-- -- --   --  Burmese TINYINT(1), Cafe TINYINT(1), Cajun TINYINT(1), California TINYINT(1), Caribbean TINYINT(1), Chilean TINYINT(1), Chinese TINYINT(1), Coffee_and_Tea TINYINT(1), Creole TINYINT(1), Crepes TINYINT(1), Cuban TINYINT(1), Deli TINYINT(1), Desserts TINYINT(1), Dim_Sum TINYINT(1), Diner TINYINT(1), Donuts TINYINT(1), Drinks_Only TINYINT(1),
-- -- --   --  Eastern European TINYINT(1), Ethiopian TINYINT(1), European TINYINT(1), Fast Food TINYINT(1), Filipino TINYINT(1), Fish_and_Chips TINYINT(1), Fondue TINYINT(1), French TINYINT(1), Frozen Yogurt TINYINT(1), Fusion TINYINT(1), German TINYINT(1), Greek TINYINT(1), Grill TINYINT(1), Hawaiian TINYINT(1), Healthy Food TINYINT(1), Ice Cream TINYINT(1), Indian TINYINT(1),
-- -- --   --  Indonesian TINYINT(1), International TINYINT(1), Iranian TINYINT(1), Irish TINYINT(1), Italian TINYINT(1), Jamaican TINYINT(1), Japanese TINYINT(1), Juices TINYINT(1), Kebab TINYINT(1), Korean TINYINT(1), Laotian TINYINT(1), Latin American TINYINT(1), Lebanese TINYINT(1), Malaysian TINYINT(1), Mediterranean TINYINT(1), Mexican TINYINT(1), Middle Eastern TINYINT(1),
-- -- --   --  Mongolian TINYINT(1), Moroccan TINYINT(1), Nepalese TINYINT(1), New American TINYINT(1), Nicaraguan TINYINT(1), Pacific TINYINT(1), Pakistani TINYINT(1), Patisserie TINYINT(1), Peruvian TINYINT(1), Pizza TINYINT(1), Polish TINYINT(1), Portuguese TINYINT(1), Pub Food TINYINT(1), Puerto Rican TINYINT(1), Ramen TINYINT(1), Russian TINYINT(1), Salad TINYINT(1),
-- -- --   --  Salvadorean TINYINT(1), Sandwich TINYINT(1), Seafood TINYINT(1), Sichuan TINYINT(1), Singaporean TINYINT(1), Soul Food TINYINT(1), South African TINYINT(1), South American TINYINT(1), Southern TINYINT(1), Southwestern TINYINT(1), Spanish TINYINT(1), Steak TINYINT(1), Sushi TINYINT(1), Taco TINYINT(1), Taiwanese TINYINT(1), Tapas TINYINT(1), Tea TINYINT(1),
-- -- --   --  Teriyaki TINYINT(1), Tex-Mex TINYINT(1), Thai TINYINT(1), Tunisian TINYINT(1), Turkish TINYINT(1), Vegetarian TINYINT(1), Venezuelan TINYINT(1), Vietnamese TINYINT(1) );
