-- upgrade --
CREATE TABLE IF NOT EXISTS "testmodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "test" TEXT NOT NULL
);
-- downgrade --
DROP TABLE IF EXISTS "testmodel";
