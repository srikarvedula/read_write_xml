drop database exam;
create database exam;
use exam;

create table exam_table(
	key_id	int
,gender					varchar(10)
,race					varchar(30)
,education				varchar(30)
,lunch					varchar(30)
,test_prep				varchar(50)
,math_score				int
,reading_score			int
,writing_score			int
);

alter table exam_table add constraint exam_table_pk primary key(key_id);

select * from exam_table;