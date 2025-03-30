--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

-- Started on 2025-03-30 22:13:39 KST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 222 (class 1259 OID 16445)
-- Name: exam_questions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.exam_questions (
    id character varying(255) NOT NULL,
    exam_id character varying(255),
    question_id character varying(255),
    page integer,
    orders integer,
    answers character varying[],
    correct_answer integer,
    check_answer integer
);


ALTER TABLE public.exam_questions OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16428)
-- Name: exams; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.exams (
    id character varying(255) NOT NULL,
    user_id character varying(255),
    quiz_id character varying(255),
    finish_date timestamp without time zone,
    submit boolean
);


ALTER TABLE public.exams OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16402)
-- Name: questions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.questions (
    id character varying(255) NOT NULL,
    quiz_id character varying(255),
    text text,
    answers character varying[],
    correct_answer integer
);


ALTER TABLE public.questions OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16395)
-- Name: quizzes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.quizzes (
    id character varying(255) NOT NULL,
    title character varying
);


ALTER TABLE public.quizzes OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16388)
-- Name: setting; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.setting (
    id character varying(255) NOT NULL,
    category character varying,
    value integer,
    set_date timestamp without time zone
);


ALTER TABLE public.setting OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16421)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id character varying(255) NOT NULL,
    user_id character varying(50),
    hashed_password character varying(100),
    admin_status boolean
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 3638 (class 0 OID 16445)
-- Dependencies: 222
-- Data for Name: exam_questions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.exam_questions (id, exam_id, question_id, page, orders, answers, correct_answer, check_answer) FROM stdin;
90ceb73a-8b86-4bee-b638-99bafae61c81	71b93a04-b40b-4917-94bf-7ffc614e9bda	74d379a0-1c8c-4549-8aae-39271b9772cb	0	0	{14,15,22,29}	0	0
f3a61070-6efb-4993-be8b-e34c1afa8eaf	71b93a04-b40b-4917-94bf-7ffc614e9bda	11c9aec2-5793-4991-ac62-b3081d206e80	0	1	{12,18,21,24}	1	1
e3f4c933-e26f-454b-b2a8-c8503f7f956a	71b93a04-b40b-4917-94bf-7ffc614e9bda	def5c30e-2227-4df5-a2f9-31c45515f55a	0	2	{"길이 + 너비","길이 × 너비","(길이 + 너비) ÷ 2","길이 - 너비"}	1	2
\.


--
-- TOC entry 3637 (class 0 OID 16428)
-- Dependencies: 221
-- Data for Name: exams; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.exams (id, user_id, quiz_id, finish_date, submit) FROM stdin;
71b93a04-b40b-4917-94bf-7ffc614e9bda	ac1322d1-44e8-4ec1-b6bf-f3679fc5316b	20cca824-69a6-4d58-965c-967b7beda2b5	2025-03-30 22:08:06.401506	t
\.


--
-- TOC entry 3635 (class 0 OID 16402)
-- Dependencies: 219
-- Data for Name: questions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.questions (id, quiz_id, text, answers, correct_answer) FROM stdin;
74d379a0-1c8c-4549-8aae-39271b9772cb	20cca824-69a6-4d58-965c-967b7beda2b5	다음 중 7의 배수는 무엇인가요?	{14,15,22,29}	0
11c9aec2-5793-4991-ac62-b3081d206e80	20cca824-69a6-4d58-965c-967b7beda2b5	다음 수식의 결과로 올바른 것은 무엇인가요? 3*(4+2)	{12,18,21,24}	1
def5c30e-2227-4df5-a2f9-31c45515f55a	20cca824-69a6-4d58-965c-967b7beda2b5	직사각형의 넓이를 구하는 공식은 무엇인가요?	{"길이 + 너비","길이 × 너비","(길이 + 너비) ÷ 2","길이 - 너비"}	1
\.


--
-- TOC entry 3634 (class 0 OID 16395)
-- Dependencies: 218
-- Data for Name: quizzes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.quizzes (id, title) FROM stdin;
20cca824-69a6-4d58-965c-967b7beda2b5	test
\.


--
-- TOC entry 3633 (class 0 OID 16388)
-- Dependencies: 217
-- Data for Name: setting; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.setting (id, category, value, set_date) FROM stdin;
12ac1695-cea2-4994-83d4-d20530e70ae4	page	10	2025-03-29 15:56:39.555632
\.


--
-- TOC entry 3636 (class 0 OID 16421)
-- Dependencies: 220
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, user_id, hashed_password, admin_status) FROM stdin;
ac1322d1-44e8-4ec1-b6bf-f3679fc5316b	test	$2b$12$d0NrRXG7C3zE8b6KL5Ygyu4lE0fCrfrSS7FnJRMREmMMEHl1rdwne	f
8df3a841-d38c-45bf-90b4-f2b454a62ba4	admin	$2b$12$xVtBqPOWGSJyBbYe5WCbMuTJaJUk9QOoq6MqOzP2n0Jh4nvWis.ga	t
\.


--
-- TOC entry 3482 (class 2606 OID 16451)
-- Name: exam_questions exam_questions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exam_questions
    ADD CONSTRAINT exam_questions_pkey PRIMARY KEY (id);


--
-- TOC entry 3480 (class 2606 OID 16434)
-- Name: exams exams_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exams
    ADD CONSTRAINT exams_pkey PRIMARY KEY (id);


--
-- TOC entry 3474 (class 2606 OID 16408)
-- Name: questions questions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_pkey PRIMARY KEY (id);


--
-- TOC entry 3472 (class 2606 OID 16401)
-- Name: quizzes quizzes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.quizzes
    ADD CONSTRAINT quizzes_pkey PRIMARY KEY (id);


--
-- TOC entry 3470 (class 2606 OID 16394)
-- Name: setting setting_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.setting
    ADD CONSTRAINT setting_pkey PRIMARY KEY (id);


--
-- TOC entry 3476 (class 2606 OID 16425)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 3478 (class 2606 OID 16427)
-- Name: users users_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_user_id_key UNIQUE (user_id);


--
-- TOC entry 3486 (class 2606 OID 16452)
-- Name: exam_questions exam_questions_exam_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exam_questions
    ADD CONSTRAINT exam_questions_exam_id_fkey FOREIGN KEY (exam_id) REFERENCES public.exams(id);


--
-- TOC entry 3487 (class 2606 OID 16457)
-- Name: exam_questions exam_questions_question_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exam_questions
    ADD CONSTRAINT exam_questions_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.questions(id);


--
-- TOC entry 3484 (class 2606 OID 16440)
-- Name: exams exams_quiz_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exams
    ADD CONSTRAINT exams_quiz_id_fkey FOREIGN KEY (quiz_id) REFERENCES public.quizzes(id);


--
-- TOC entry 3485 (class 2606 OID 16435)
-- Name: exams exams_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exams
    ADD CONSTRAINT exams_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- TOC entry 3483 (class 2606 OID 16409)
-- Name: questions questions_quiz_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_quiz_id_fkey FOREIGN KEY (quiz_id) REFERENCES public.quizzes(id);


-- Completed on 2025-03-30 22:13:39 KST

--
-- PostgreSQL database dump complete
--

