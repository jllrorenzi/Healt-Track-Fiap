-- Gerado por Oracle SQL Developer Data Modeler 21.1.0.092.1221
--   em:        2021-05-22 20:35:50 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE t_ht_alimento (
    cd_alimento  NUMBER NOT NULL,
    nm_alimento  VARCHAR2(30 CHAR),
    nr_calorias  NUMBER
);

ALTER TABLE t_ht_alimento ADD CONSTRAINT t_ht_alimento_pk PRIMARY KEY ( cd_alimento );

CREATE TABLE t_ht_atividade (
    t_ht_usuario_nm_usuario_email  VARCHAR2(30 CHAR) NOT NULL,
    t_ht_exercicio_cd_exercicio    NUMBER NOT NULL,
    dt_data_realização             DATE,
    nr_caloria_gasta               NUMBER
);

ALTER TABLE t_ht_atividade ADD CONSTRAINT t_ht_atividade_pk PRIMARY KEY ( t_ht_usuario_nm_usuario_email );

CREATE TABLE t_ht_exercicio (
    cd_exercicio          NUMBER NOT NULL,
    nm_exercico_aerobico  VARCHAR2(30 CHAR),
    nm_exercico_força     VARCHAR2(30 CHAR)
);

ALTER TABLE t_ht_exercicio ADD CONSTRAINT t_ht_exercicio_pk PRIMARY KEY ( cd_exercicio );

CREATE TABLE t_ht_peso (
    t_ht_usuario_nm_usuario_email  VARCHAR2(30 CHAR) NOT NULL,
    nr_peso                        FLOAT(3) NOT NULL,
    dt_data_pesagem                DATE NOT NULL
);

ALTER TABLE t_ht_peso ADD CONSTRAINT t_ht_peso_pk PRIMARY KEY ( t_ht_usuario_nm_usuario_email );

CREATE TABLE t_ht_refeição (
    t_ht_usuario_nm_usuario_email  VARCHAR2(30 CHAR) NOT NULL,
    t_ht_alimento_cd_alimento      NUMBER NOT NULL,
    ds_tipo_refeição               VARCHAR2(15) NOT NULL,
    dt_refeição                    DATE NOT NULL
);

ALTER TABLE t_ht_refeição ADD CONSTRAINT t_ht_refeição_pkv1 PRIMARY KEY ( t_ht_usuario_nm_usuario_email );

CREATE TABLE t_ht_usuario (
    nm_usuario_email   VARCHAR2(30 CHAR) NOT NULL,
    nm_senha           VARCHAR2(10) NOT NULL,
    nm_nome            VARCHAR2(30 CHAR) NOT NULL,
    nm_genero          CHAR(1) NOT NULL,
    dt_data_nasciment  DATE NOT NULL,
    nr_altura          FLOAT(3),
    nr_peso            FLOAT(2)
);

ALTER TABLE t_ht_usuario ADD CONSTRAINT t_ht_usuario_pk PRIMARY KEY ( nm_usuario_email );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE t_ht_atividade
    ADD CONSTRAINT t_ht_atividade_t_ht_exercicio_fk FOREIGN KEY ( t_ht_exercicio_cd_exercicio )
        REFERENCES t_ht_exercicio ( cd_exercicio );

ALTER TABLE t_ht_atividade
    ADD CONSTRAINT t_ht_atividade_t_ht_usuario_fk FOREIGN KEY ( t_ht_usuario_nm_usuario_email )
        REFERENCES t_ht_usuario ( nm_usuario_email );

ALTER TABLE t_ht_peso
    ADD CONSTRAINT t_ht_peso_t_ht_usuario_fk FOREIGN KEY ( t_ht_usuario_nm_usuario_email )
        REFERENCES t_ht_usuario ( nm_usuario_email );

ALTER TABLE t_ht_refeição
    ADD CONSTRAINT t_ht_refeição_t_ht_alimento_fk FOREIGN KEY ( t_ht_alimento_cd_alimento )
        REFERENCES t_ht_alimento ( cd_alimento );

ALTER TABLE t_ht_refeição
    ADD CONSTRAINT t_ht_refeição_t_ht_usuario_fk FOREIGN KEY ( t_ht_usuario_nm_usuario_email )
        REFERENCES t_ht_usuario ( nm_usuario_email );



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             6
-- CREATE INDEX                             0
-- ALTER TABLE                             11
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   1
-- WARNINGS                                 0
