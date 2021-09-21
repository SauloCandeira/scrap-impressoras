create table impressoras(
--	id INT IDENTITY(1,1) PRIMARY KEY,
	tonner  VARCHAR(20),
	nome  VARCHAR(20),
	ipv4  VARCHAR(20),
	andar VARCHAR(20),
	sala  VARCHAR(20),
	setor  VARCHAR(20),
	total_impressao  VARCHAR(20),
	total_scan  VARCHAR(20),
	total_cilindro  VARCHAR(20),
	dt  VARCHAR(20),
--  dt_carga DATETIME
);

select * from impressoras


delete from dbo.impressoras 

DROP TABLE dbo.impressoras

create table impressoras_graficos(
--	id INT IDENTITY(1,1) PRIMARY KEY,
	tonner  VARCHAR(20),
	nome  VARCHAR(20),
	ipv4  VARCHAR(20),
	andar VARCHAR(20),
	sala  VARCHAR(20),
	setor  VARCHAR(20),
	total_impressao  VARCHAR(20),
	total_scan  VARCHAR(20),
	total_cilindro  VARCHAR(20),
	dt  VARCHAR(20),
--  dt_carga DATETIME
);