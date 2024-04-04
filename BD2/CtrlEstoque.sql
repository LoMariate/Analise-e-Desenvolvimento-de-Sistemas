DROP SCHEMA IF EXISTS A05;
CREATE SCHEMA IF NOT EXISTS A05;
USE A05;

DROP TABLE IF EXISTS produto;

CREATE TABLE produto (
    id INT(11) PRIMARY KEY AUTO_INCREMENT,
    status CHAR(1) NOT NULL DEFAULT 'A',
    descricao VARCHAR(50),
    estoqueMinimo INT(11),
    estoqueMaximo INT(11), 
)

INSERT INTO produto (descricao, estoqueMinimo, estoqueMaximo)
VALUES
(“PENDRIVE”, 10, 100),
(“MOUSE”, 10, 100),
(“IOGURTE”, 5, 50),
(“TEQUILA”, 5, 40),
(“PRESUNTO”, 5, 20);

DROP TABLE IF EXISTS produtoentrada;

CREATE TABLE produtoentrada (
    id INT(11) PRIMARY KEY,
    idProduto INT(11),
    qtd INT(11),
    vlrUnitario DECIMAL(9,2) NULL DEFAULT 0.00,
    dataEntrada DATE,
    CONSTRAINT fk_produtoentrada_produto
        FOREIGN KEY (idProduto) REFERENCES produto(id)
)

DROP TABLE IF EXISTS produtosaida;

CREATE TABLE produtosaida (
    id INT(11) PRIMARY KEY,
    idProduto INT(11),
    qtd INT(11),
    vlrUnitario DECIMAL(9,2) NULL DEFAULT 0.00,
    dataSaida DATE,
    CONSTRAINT fk_produtosaida_produto
        FOREIGN KEY (idProduto) REFERENCES produto(id)
)

DROP TABLE IF EXISTS estoque;

CREATE TABLE estoque (
    id INT(11) PRIMARY KEY,
    idProduto INT(11),
    qtd INT(11),
    vlrUnitario DECIMAL(9,2) NULL DEFAULT 0.00,
    CONSTRAINT fk_estoque_produto
        FOREIGN KEY (idProduto) REFERENCES produto(id)
)

DELIMITER $$
CREATE PROCEDURE SP_AtualizaEstoque (var_idProduto INT, var_qtd INT, var_vlrUnitario DECIMAL(9,2))

BEGIN
    DECLARE var_contador INT(11);

    SELECT COUNT(*) INTO var_contador FROM estoque e WHERE e.idProduto = var_idProduto;

    IF var_contador > 0 THEN
        UPDATE estoque e
        SET e.qtd = e.qtd + var_qtd,
            e.vlrUnitario = var_vlrUnitario
        WHERE e.idProduto = var_idProduto;
    ELSE
        INSERT INTO estoque (idProduto, qtd, vlrUnitario)
        VALUES (var_idProduto, var_qtd, var_vlrUnitario);
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER trg_produtoentrada_AI AFTER INSERT
ON produtoentrada
FOR EACH ROW
BEGIN
    CALL SP_AtualizaEstoque(NEW.idProduto, NEW.qtd, NEW.vlrUnitario);
END $$
DELIMITER ;