

--create table quizzes(
--	id VARCHAR(255) primary key,
--	title VARCHAR
--)

--select * from quizzes
--ALTER TABLE quizzes MODIFY id varchar(255)
--
--create table questions (
--	id VARCHAR(255) primary key,
--	quiz_id VARCHAR(255),
--	text TEXT,
--	answers VARCHAR[],
--	correct_answer INTEGER,
--	foreign key (quiz_id) references quizzes(id)
--)
--drop table questions
--select * from questions
--alter table questions modify id varchar(255)


--create table exams (
--	id VARCHAR(255) primary key,
--	user_id VARCHAR(50),
--	quiz_id VARCHAR(255),
--	finish_date Timestamp, 
--	submit Boolean,
--	foreign key (user_id) references users(user_id),
--	foreign key (quiz_id) references quizzes(id)
--)

--select * from exams

--create table exam_questions (
--	id VARCHAR(255) primary key,
--	exam_id VARCHAR(255),
--	question_id VARCHAR(255),
--	page Integer,
--	orders Integer,
--	answers Integer[],
--	correct_answer Integer,
--	check_answer Integer,
--	foreign key (exam_id) references exams(id),
--	foreign key (question_id) references questions(id)
--	
--)


--select * from exam_questions


--create table users(
--	id VARCHAR(255) primary key,
--	user_id VARCHAR(50) unique,
--	hashed_password VARCHAR(100),
--	admin_status Boolean
--)

--select * from users
--drop table users