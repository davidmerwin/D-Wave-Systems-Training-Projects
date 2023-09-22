-- CREATE TABLE to store the problem parameters
CREATE TABLE problem_parameters (
  ID UUID,
  SOLVED_ON TIMESTAMP,
  LABEL VARCHAR(50),
  STATUS VARCHAR(50),
  COMPLETED VARCHAR(50),
  SUBMITTED_BY VARCHAR(50),
  TYPE VARCHAR(50),
  NUM_READS INT,
  SUBMITTED_ON TIMESTAMP
);

-- INSERT statement to insert the problem parameters
INSERT INTO problem_parameters VALUES (
  '6dbabf04-9a93-4534-9239-51d9edc7cbe2',
  '2023-05-18T722:14:41702012Z',
  'Copy Value',
  'Training - Embedding',
  'COMPLETED',
  'SOLVER',
  'Advantage_system4.1',
  'qubo',
  10,
  '2023-05-18T722:14:41.533053Z'
);

-- SELECT statement to retrieve the problem parameters
SELECT 
  ID,
  SOLVED_ON,
  LABEL,
  STATUS,
  COMPLETED,
  SUBMITTED_BY,
  TYPE,
  NUM_READS,
  SUBMITTED_ON
FROM problem_parameters;
