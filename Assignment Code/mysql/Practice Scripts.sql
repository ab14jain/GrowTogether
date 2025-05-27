create database college;

use college;

create table students(
	id int primary key,
    name varchar(50),
    age int not null
);


insert into students value(1, "Abhishek", 25);
insert into students value(2, "Aman", 35);
insert into students value(3, "Nitin", 32);
insert into students value(4, "Sumit", 28);

select * from students;

create database if not exists college;

show databases;
show tables;