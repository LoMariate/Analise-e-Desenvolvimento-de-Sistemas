    DROP SCHEMA IF EXISTS aula04;
    CREATE SCHEMA  IF NOT EXISTS aula04;
    USE aula04;

    DROP TABLE IF EXISTS Produtos;

    CREATE TABLE Produtos (
        codigo CHAR(3) PRIMARY KEY,
        descricao VARCHAR(50) NOT NULL,
        qtdEstoque INT NOT NULL,
        CHECK (qtdEstoque > 0) 
        );

    DROP TABLE IF EXISTS itensVenda;

    CREATE TABLE itensVenda (
        id INT PRIMARY KEY,
        venda INT NOT NULL,
        qtdVendida INT(11) NOT NULL,
        codigoProduto CHAR(3) NOT NULL,
        CONSTRAINT fk_itensVenda_produto
            FOREIGN KEY (codigoProduto) REFERENCES Produtos(codigo)
    );

    CREATE TABLE Log (
        id INT PRIMARY KEY AUTO_INCREMENT,
        produtoCod CHAR(3) NOT NULL,
        nomeAnterior VARCHAR(50) NOT NULL,
        nomeNovo VARCHAR(50) NOT NULL,
        dataHora DATETIME NOT NULL,
        CONSTRAINT fk_log_produto
            FOREIGN KEY (produtoCod) REFERENCES Produtos(codigo)
    );

    INSERT INTO Produtos (codigo, descricao, qtdEstoque) VALUES (1, 'Feijao', 10);
    INSERT INTO Produtos (codigo, descricao, qtdEstoque) VALUES (2, 'Arroz', 5);
    INSERT INTO Produtos (codigo, descricao, qtdEstoque) VALUES (3, 'Farinha', 15);
    SELECT * FROM Produtos;

    DELIMITER //

    CREATE TRIGGER trg_itensvenda_AI AFTER INSERT
    ON Itensvenda
    FOR EACH ROW
    BEGIN
        UPDATE Produtos
        SET qtdEstoque = qtdEstoque - NEW.qtdVendida
        WHERE codigo = NEW.codigoProduto;
    END //

    DELIMITER ;

    DELIMITER //

    CREATE TRIGGER trg_itensvenda_AD AFTER DELETE
    ON Itensvenda
    FOR EACH ROW
    BEGIN
        UPDATE Produtos
        SET qtdEstoque = qtdEstoque + OLD.qtdVendida
        WHERE codigo = OLD.codigoProduto;
    END //

    DELIMITER ;

    DELIMITER //

    CREATE TRIGGER trg_itensvenda_AU AFTER UPDATE
    ON Itensvenda
    FOR EACH ROW
    BEGIN
        UPDATE Produtos
        SET qtdEstoque = qtdEstoque + OLD.qtdVendida - NEW.qtdVendida
        WHERE codigo = NEW.codigoProduto;
    END //

    DELIMITER ;

    SELECT * FROM Produtos;
    INSERT INTO itensVenda VALUES (1, 1, '003',2);
    INSERT INTO itensVenda VALUES (2, 1, '001',3);
    INSERT INTO itensVenda VALUES (3, 1, '002',1);
    INSERT INTO itensVenda VALUES (4, 2, '002',1);
    INSERT INTO itensVenda VALUES (5, 2, '003',4);
    INSERT INTO itensVenda VALUES (6, 2, '001',3);
    INSERT INTO itensVenda VALUES (7, 3, '001',1);
    INSERT INTO itensVenda VALUES (8, 3, '002',2);
    SELECT * FROM Produtos;

    DELETE FROM itensVenda WHERE id = 1;
    SELECT * FROM Produtos;