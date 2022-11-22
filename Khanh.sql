create database Nhansu;
use Nhansu;
drop table KeToan;
create table KeToan (
	STT int auto_increment,
    Ho varchar(255),
    Ten varchar(255),
    Address varchar(255),
    SDT varbinary(255),
    CMT varbinary(255) not NULL unique,
    constraint PK_ketoan primary key (STT, CMT)
);
set @pw = "!#%&(@$^*)";
Insert into Ketoan (Ho, Ten, Address, SDT, CMT) values ("Ngô","Khánh","Tân Bình", 
			AES_ENCRYPT("0707316296",@pw), AES_ENCRYPT("0100101", @pw));
Insert into Ketoan (Ho, Ten, Address, SDT, CMT) values ("Quang","Khánh","Tân Bình", 
			AES_ENCRYPT("07466556",@pw), AES_ENCRYPT("0450501",@pw));

select Ho, Ten, Address, aes_decrypt(SDT,@pw) as SDT , aes_decrypt(CMT,@pw) as CMT from KeToan;

select * from KeToan;