SELECT token
FROM access_tokens
    JOIN account_users ON account_users.user_id = access_tokens.owner_id
WHERE account_id = $1
    AND role = 1
    AND owner_type = 'User';