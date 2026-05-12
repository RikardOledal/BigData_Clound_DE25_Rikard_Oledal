CREATE OR REFRESH STREAMING TABLE suppy_chain.bronze.raw_access_logs
  COMMENT "Raw access logs - bronze layer" AS
SELECT
  *
FROM
  STREAM read_files(
    "/Volumes/suppy_chain/default/raw/logs/",
    format => "csv",
    header => "true",
    inferSchema => "true"
  )