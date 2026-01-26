CREATE SCHEMA IF NOT EXISTS store_tx;
SET search_path TO store_tx;

CREATE OR REPLACE PROCEDURE make_purchase(
    p_user_id INT,
    p_product_id INT,
    p_quantity INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_user_id      INT;
    v_price_cents  INT;
    v_stock        INT;
    v_invoice_id   INT;
    v_line_cents   INT;
BEGIN
    IF p_quantity IS NULL OR p_quantity <= 0 THEN
        RAISE EXCEPTION 'Quantity must be > 0';
    END IF;

    START TRANSACTION;


    SELECT id INTO v_user_id
    FROM users
    WHERE id = p_user_id;

    IF v_user_id IS NULL THEN
        RAISE EXCEPTION 'User % does not exist', p_user_id;
    END IF;


    SELECT price_cents, stock
    INTO v_price_cents, v_stock
    FROM products
    WHERE id = p_product_id
        AND is_active = TRUE
    FOR UPDATE;

    IF v_price_cents IS NULL THEN
        RAISE EXCEPTION 'Product % does not exist or is inactive', p_product_id;
    END IF;

    IF v_stock < p_quantity THEN
        RAISE EXCEPTION 'Not enough stock for product %. Stock: %, requested: %',
            p_product_id, v_stock, p_quantity;
    END IF;

    INSERT INTO invoices (user_id)
    VALUES (p_user_id)
    RETURNING id INTO v_invoice_id;


    v_line_cents := v_price_cents * p_quantity;

    INSERT INTO invoice_items (invoice_id, product_id, quantity, unit_cents, line_cents)
    VALUES (v_invoice_id, p_product_id, p_quantity, v_price_cents, v_line_cents);

    UPDATE products
    SET stock = stock - p_quantity
    WHERE id = p_product_id;

    -- Actualizar total factura
    UPDATE invoices
    SET total_cents = v_line_cents
    WHERE id = v_invoice_id;

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
$$;
