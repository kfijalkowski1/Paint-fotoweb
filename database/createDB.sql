CREATE TABLE slots (
    visit_id SERIAL PRIMARY KEY,
    visit_name VARCHAR(255),
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    is_reserved BOOLEAN NOT NULL
);

CREATE TABLE Albums (
    album_id SERIAL PRIMARY KEY,
    album_name VARCHAR(255) NOT NULL,
    album_desc TEXT,
    album_path TEXT
);

CREATE TABLE Messages (
    message_id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    message TEXT NOT NULL,
    sender_name VARCHAR(100) NOT NULL,
    sender_surname VARCHAR(100) NOT NULL
);

-- Create a function to check for overlapping slots
CREATE OR REPLACE FUNCTION check_overlapping_slots()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM slots
        WHERE
            (NEW.start_time, NEW.end_time) OVERLAPS (start_time, end_time)
    ) THEN
        RAISE EXCEPTION 'Slot times overlap with an existing slot';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create the trigger
CREATE TRIGGER trg_check_overlapping_slots
BEFORE INSERT OR UPDATE ON slots
FOR EACH ROW
EXECUTE FUNCTION check_overlapping_slots();
