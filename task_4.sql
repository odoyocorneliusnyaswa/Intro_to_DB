USE alx_book_store;

SELECT 
    COLUMN_NAME AS 'Column Name', 
    DATA_TYPE AS 'Data Type', 
    IS_NULLABLE AS 'Is Nullable', 
    COLUMN_DEFAULT AS 'Default Value', 
    CHARACTER_MAXIMUM_LENGTH AS 'Max Length'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_NAME = 'books' 
    AND TABLE_SCHEMA = 'alx_book_store';
