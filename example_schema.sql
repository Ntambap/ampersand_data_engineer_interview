drop table if exists peoples;


create table peoples
(  
    given_name   varchar,
    family_name  varchar,
    date_of_birth varchar,
	place_of_birth varchar
);


drop table if exists places;

create table places
(
    city   varchar,
    county  varchar,
    country varchar 
);

		
