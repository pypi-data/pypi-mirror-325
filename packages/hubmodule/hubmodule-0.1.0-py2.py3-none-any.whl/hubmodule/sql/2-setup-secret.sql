-- Create secure schema and secret table
CREATE SCHEMA IF NOT EXISTS security;
REVOKE ALL ON SCHEMA security FROM PUBLIC;

CREATE TABLE IF NOT EXISTS security.secrets (
    key text PRIMARY KEY,
    value text NOT NULL
);

REVOKE ALL ON security.secrets FROM PUBLIC;

-- Function to access secrets (superuser only)
CREATE OR REPLACE FUNCTION security.get_secret(secret_key text)
RETURNS text
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = security, pg_temp
AS $$
BEGIN
    IF NOT (
        (SELECT usesuper FROM pg_user WHERE usename = CURRENT_USER)
        OR
        CURRENT_USER = 'postgres'
    ) THEN
        RAISE EXCEPTION 'Only superusers or postgres user can access secrets';
    END IF;

    RETURN (SELECT value FROM security.secrets WHERE key = secret_key);
END;
$$;

-- Function to set secrets (superuser only)
CREATE OR REPLACE FUNCTION security.set_secret(secret_key text, secret_value text)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = security, pg_temp
AS $$
BEGIN
    IF NOT (
        (SELECT usesuper FROM pg_user WHERE usename = CURRENT_USER)
        OR
        CURRENT_USER = 'postgres'
    ) THEN
        RAISE EXCEPTION 'Only superusers or postgres user can set secrets';
    END IF;

    INSERT INTO security.secrets (key, value)
    VALUES (secret_key, secret_value)
    ON CONFLICT (key) DO UPDATE SET value = EXCLUDED.value;
END;
$$;

-- Create and set jwt_secret (superuser only)
SELECT security.set_secret(
    'jwt_secret',
    encode(gen_random_bytes(64), 'base64')
);
