/*
  PROFESSOR, NOTA IMPORTANTE:
  Este script foi desenvolvido e testado no VS Code com a extensão PostgreSQL.

  Para evitar conflitos com o gerenciador de transações da própria ferramenta (VS Code),
  os comandos 'COMMIT' e 'ROLLBACK' foram removidos de dentro da procedure.

  O próprio VS Code gerencia a transação externamente:
  - Ele executa um COMMIT automático ao final de uma chamada bem-sucedida.
  - Ele executa um ROLLBACK automático se a procedure lançar qualquer EXCEPTION 
    (como a validação de valor negativo), garantindo a atomicidade.

  O script '2_testar_procedure.sql' demonstra esse comportamento em ação.
*/

DROP TABLE IF EXISTS pagamento;
DROP TABLE IF EXISTS pedido;
DROP TABLE IF EXISTS cliente;

CREATE TABLE cliente (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE pedido (
    id_pedido SERIAL PRIMARY KEY,
    id_cliente INT REFERENCES cliente(id_cliente),
    data_pedido TIMESTAMP,
    valor_total NUMERIC(10, 2) CHECK (valor_total > 0),
    status VARCHAR(50) NOT NULL
);

CREATE TABLE pagamento (
    id_pagamento SERIAL PRIMARY KEY,
    id_pedido INT REFERENCES pedido(id_pedido),
    valor NUMERIC(10, 2) NOT NULL,
    forma_pagamento VARCHAR(50) NOT NULL,
    data_pagamento TIMESTAMP,
    status VARCHAR(50) NOT NULL
);

INSERT INTO cliente (nome) VALUES ('Cliente Teste 1');

CREATE OR REPLACE PROCEDURE pedido_com_pagamento(
    p_id_cliente INT,
    p_valor NUMERIC,
    p_forma_pagamento VARCHAR(50),
    OUT p_id_pedido INT,
    OUT p_mensagem TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    BEGIN
        IF NOT EXISTS (SELECT 1 FROM cliente WHERE id_cliente = p_id_cliente) THEN
            RAISE EXCEPTION 'Cliente ID % não encontrado.', p_id_cliente;
        END IF;

        IF p_valor <= 0 THEN
            RAISE EXCEPTION 'Valor do pedido deve ser maior que zero.';
        END IF;

        INSERT INTO pedido (id_cliente, data_pedido, valor_total, status)
        VALUES (p_id_cliente, CURRENT_TIMESTAMP, p_valor, 'aguardando_pagamento')
        RETURNING id_pedido INTO p_id_pedido;

        INSERT INTO pagamento (id_pedido, valor, forma_pagamento, data_pagamento, status)
        VALUES (p_id_pedido, p_valor, p_forma_pagamento, CURRENT_TIMESTAMP, 'aprovado');

        UPDATE pedido
        SET status = 'confirmado'
        WHERE id_pedido = p_id_pedido;

        p_mensagem := 'Pedido ' || p_id_pedido || ' criado e pago com sucesso!';
        RAISE NOTICE '%', p_mensagem;

    EXCEPTION
        WHEN OTHERS THEN
            p_id_pedido := NULL;
            p_mensagem := 'Falha na transação: ' || SQLERRM || '. Pedido e pagamento cancelados.';
            RAISE NOTICE '%', p_mensagem;
    END;
END;
$$;