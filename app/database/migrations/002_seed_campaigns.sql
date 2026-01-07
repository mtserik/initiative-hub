-- =========================================
-- Seed inicial de usuários, campanhas e membros
-- =========================================

-- EXTENSION necessária para gen_random_uuid (se ainda não existir)
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- -----------------------------------------
-- 1. Usuários fake
-- -----------------------------------------

INSERT INTO "users" (id, email, username)
VALUES
    ('11111111-1111-1111-1111-111111111111', 'gm1@example.com', 'gm_one'),
    ('22222222-2222-2222-2222-222222222222', 'player1@example.com', 'player_one'),
    ('33333333-3333-3333-3333-333333333333', 'player2@example.com', 'player_two')
ON CONFLICT (email) DO NOTHING;

-- -----------------------------------------
-- 2. Campanhas fake
-- -----------------------------------------

INSERT INTO "campaigns" (id, name, description, system_key)
VALUES
    (
        'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
        'A Sombra do Norte',
        'Uma campanha sombria em terras congeladas.',
        'dnd5e'
    ),
    (
        'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
        'Neon Blood',
        'Conspirações corporativas em uma megacidade.',
        'cyberpunk'
    )
ON CONFLICT (id) DO NOTHING;

-- -----------------------------------------
-- 3. Membros das campanhas
-- -----------------------------------------

INSERT INTO "campaign_members" (
    id,
    campaign_id,
    user_id,
    role
)
VALUES
    -- GM da campanha A Sombra do Norte
    (
        gen_random_uuid(),
        'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
        '11111111-1111-1111-1111-111111111111',
        'gm'
    ),

    -- Players da campanha A Sombra do Norte
    (
        gen_random_uuid(),
        'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
        '22222222-2222-2222-2222-222222222222',
        'player'
    ),
    (
        gen_random_uuid(),
        'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
        '33333333-3333-3333-3333-333333333333',
        'player'
    ),

    -- GM da campanha Neon Blood
    (
        gen_random_uuid(),
        'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
        '11111111-1111-1111-1111-111111111111',
        'gm'
    )
ON CONFLICT DO NOTHING;
