create table Employee
(
    id varchar2(10) not null primary key,
    name varchar2(100),
    address varchar2(200),
    base_salary number,
    age number,
    gender varchar2(20),
    exp_year number
);

create table Developer
(
    id varchar2(10),
    primary_language varchar2(20)
);

create table Tester
(
    id varchar2(10),
    type varchar2(20)
);

create table Account
(
    username varchar2(100) not null primary key,
    password varchar2(100),
    role varchar2(100)
);

alter table Developer
add constraint fk_developer_id foreign key (id) references Employee(id);

alter table Tester
add constraint fk_tester_id foreign key (id) references Employee(id);

create sequence next_developer_id
start with 1
increment by 1
maxvalue 999
nocache;

create sequence next_tester_id
start with 1
increment by 1
maxvalue 999
nocache;

create or replace function format_id(position number)
return varchar2
is
    v_current_id number;
begin
    if position = 1 then
        select next_developer_id.nextval into v_current_id from dual;
        
        if v_current_id < 10 then
            return 'D00' || v_current_id;
        elsif v_current_id < 100 then
            return 'D0' || v_current_id;
        else
            return 'D' || v_current_id;
        end if;
    else
        select next_tester_id.nextval into v_current_id from dual;
        
        if v_current_id < 10 then
            return 'T00' || v_current_id;
        elsif v_current_id < 100 then
            return 'T0' || v_current_id;
        else
            return 'T' || v_current_id;
        end if;
    end if;
end;

--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(1), 'Nguyen Van A', 'Ho Chi Minh city', 7000000, 20, 'Male', 1);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(2), 'Nguyen Van B', 'Ha Noi', 5000000, 15, 'Male', 2);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(1), 'Nguyen Van C', 'Lao Cai', 2000000, 16, 'Male', 5);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(2), 'Nguyen Van D', 'Yen Bai', 3000000, 18, 'Male', 2);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(1), 'Nguyen Van E', 'Kien Giang', 5000000, 21, 'Male', 3);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(2), 'Nguyen Van F', 'Tien Giang', 3000000, 22, 'Male', 2);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(1), 'Nguyen Van G', 'An Giang', 2000000, 25, 'Male', 9);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(2), 'Nguyen Van H', 'Ben Tre', 1000000, 23, 'Male', 8);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(1), 'Nguyen Van I', 'Ca Mau', 5000000, 19, 'Male', 5);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(2), 'Nguyen Van J', 'Can Tho', 6000000, 19, 'Male', 4);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(1), 'Nguyen Thi K', 'Hau Giang', 9000000, 22, 'Female', 2);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(2), 'Nguyen Thi L', 'Dien Bien', 8000000, 20, 'Female', 1);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(1), 'Nguyen Thi M', 'Soc Trang', 7000000, 16, 'Female', 0);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(2), 'Nguyen Thi N', 'Gia Lai', 1000000, 23, 'Female', 9);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(1), 'Nguyen Thi O', 'Lam Dong', 2000000, 24, 'Female', 3);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(2), 'Nguyen Thi P', 'Da Lat', 8000000, 29, 'Female', 1);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(1), 'Nguyen Thi Q', 'Vinh Long', 3000000, 28, 'Female', 2);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(2), 'Nguyen Thi R', 'Bac Lieu', 4000000, 22, 'Female', 6);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(1), 'Nguyen Thi S', 'Tra Vinh', 5000000, 21, 'Female', 4);
--insert into Employee (id, name, address, base_salary, age, gender, exp_year) values (format_id(2), 'Nguyen Thi T', 'Long An', 2000000, 20, 'Female', 2);
--
--insert into Developer (id, primary_language) values ('D001', 'Java');
--insert into Developer (id, primary_language) values ('D002', 'C#');
--insert into Developer (id, primary_language) values ('D003', 'PHP');
--insert into Developer (id, primary_language) values ('D004', 'C');
--insert into Developer (id, primary_language) values ('D005', 'C++');
--insert into Developer (id, primary_language) values ('D006', 'Javascript');
--insert into Developer (id, primary_language) values ('D007', 'Python');
--insert into Developer (id, primary_language) values ('D008', 'Go');
--insert into Developer (id, primary_language) values ('D009', 'Ruby');
--insert into Developer (id, primary_language) values ('D010', 'Rust');
--
--insert into Tester (id, type) values ('T001', 'Manual');
--insert into Tester (id, type) values ('T002', 'Automation');
--insert into Tester (id, type) values ('T003', 'Manual');
--insert into Tester (id, type) values ('T004', 'Automation');
--insert into Tester (id, type) values ('T005', 'Manual');
--insert into Tester (id, type) values ('T006', 'Automation');
--insert into Tester (id, type) values ('T007', 'Manual');
--insert into Tester (id, type) values ('T008', 'Automation');
--insert into Tester (id, type) values ('T009', 'Manual');
--insert into Tester (id, type) values ('T010', 'Automation');
--
--insert into Account values ('admin', '$2a$10$2ASymiRJ6uuf6z1l1eLTkOjO/j9tbPgArsQnPJOkK8701uBeQNmea', 'admin');
--insert into Account values ('user1', '$2a$10$4NDFt5OdnWXTJDz3.oYzDunADs0mqOKGybOY9wb/np5X8b2AqFVRa', 'user');
--insert into Account values ('user2', '$2a$10$ewY1RJ9WIshkuar/ujNXEOb6VEE.HycgEsW4YOu4fw.5rbXSOx82S', 'user');
--
--select * from employee;
--select * from developer;
--select * from tester;
--select * from account;
--
--commit;