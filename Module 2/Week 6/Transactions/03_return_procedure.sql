CREATE SCHEMA IF NOT EXISTS store_tx;
SET search_path TO store_tx;

CREATE OR REPLACE PROCEDURE return_invoice(p_invoice_id INT)
LANGUAGE plpgsql
AS $$
DECLARE
    v_invoice_id INT;
    v_is_returned BOOLEAN;
    r RECORD;
BEGIN
    START TRANSACTION;


    SELECT id, is_returned
    INTO v_invoice_id, v_is_returned
    FROM invoices
    WHERE id = p_invoice_id
    FOR UPDATE;

    IF v_invoice_id IS NULL THEN
        RAISE EXCEPTION 'Invoice % does not exist', p_invoice_id;
    END IF;

    IF v_is_returned = TRUE THEN
        RAISE EXCEPTION 'Invoice % is already returned', p_invoice_id;
    END IF;


    FOR r IN
        SELECT product_id, quantity
        FROM invoice_items
        WHERE invoice_id = p_invoice_id
        FOR UPDATE
    LOOP
        UPDATE products
        SET stock = stock + r.quantity
        WHERE id = r.product_id;
    END LOOP;


    UPDATE invoices
    SET is_returned = TRUE,
        returned_at = CURRENT_TIMESTAMP
    WHERE id = p_invoice_id;

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
$$;
