/*
  PROFESSOR, NOTA IMPORTANTE:
  Este script de teste foi feito para ser executado no VS Code,
  onde cada comando CALL é tratado como uma transação separada.
  
  O script '1_criar_procedure.sql' contém a explicação
  completa sobre a remoção do COMMIT/ROLLBACK interno.
*/

CALL pedido_com_pagamento(1, 250.75, 'pix', NULL, NULL);

CALL pedido_com_pagamento(1, -100.00, 'boleto', NULL, NULL);

SELECT * FROM pedido;

SELECT * FROM pagamento;