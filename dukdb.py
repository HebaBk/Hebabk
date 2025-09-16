import duckdb

# تنفيذ استعلام SQL وإرجاع النتيجة
result = duckdb.sql("SELECT 42 AS answer").fetchdf()  # fetchdf أفضل من fetchall()
print(result)

# الوصول للقيمة مباشرة
print("Answer =", result["answer"][0])
