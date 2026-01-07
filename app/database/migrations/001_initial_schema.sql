CREATE TABLE "users" (
  "id" uuid PRIMARY KEY NOT NULL,
  "email" text UNIQUE NOT NULL,
  "username" text NOT NULL,
  "created_at" timestamp NOT NULL DEFAULT (now())
);

CREATE TABLE "campaigns" (
  "id" uuid PRIMARY KEY NOT NULL,
  "name" text NOT NULL,
  "description" text,
  "system_key" text NOT NULL,
  "created_at" timestamp NOT NULL DEFAULT (now())
);

CREATE TABLE "campaign_members" (
  "id" uuid PRIMARY KEY NOT NULL,
  "campaign_id" uuid NOT NULL,
  "user_id" uuid NOT NULL,
  "role" text NOT NULL,
  "created_at" timestamp NOT NULL DEFAULT (now())
);

CREATE TABLE "characters" (
  "id" uuid PRIMARY KEY NOT NULL,
  "name" text NOT NULL,
  "campaign_id" uuid NOT NULL,
  "owner_user_id" uuid,
  "sheet" jsonb NOT NULL,
  "created_at" timestamp NOT NULL DEFAULT (now())
);

CREATE TABLE "sessions" (
  "id" uuid PRIMARY KEY NOT NULL,
  "campaign_id" uuid NOT NULL,
  "title" text NOT NULL,
  "session_date" date,
  "summary" text,
  "created_at" timestamp NOT NULL DEFAULT (now())
);

CREATE UNIQUE INDEX ON "campaign_members" ("campaign_id", "user_id");

ALTER TABLE "campaign_members" ADD FOREIGN KEY ("campaign_id") REFERENCES "campaigns" ("id");

ALTER TABLE "campaign_members" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "characters" ADD FOREIGN KEY ("campaign_id") REFERENCES "campaigns" ("id");

ALTER TABLE "characters" ADD FOREIGN KEY ("owner_user_id") REFERENCES "users" ("id");

ALTER TABLE "sessions" ADD FOREIGN KEY ("campaign_id") REFERENCES "campaigns" ("id");
