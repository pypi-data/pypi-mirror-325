CREATE OR REPLACE FUNCTION set_token(token text, is_local boolean DEFAULT false)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    payload record;
BEGIN
    -- Verify and process the token directly
    SELECT * INTO payload FROM verify(
        token,
        security.get_secret('jwt_secret')
    );

    IF NOT payload.valid THEN
        RAISE EXCEPTION 'JWT verification failed';
    END IF;

    -- Set only the payload
    PERFORM set_config('app.jwt_payload', payload.payload::text, is_local);
END;
$$;
