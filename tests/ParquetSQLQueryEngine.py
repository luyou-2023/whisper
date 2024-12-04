import pandas as pd
import fastparquet
import duckdb
from typing import List, Dict, Any, Union

#pip install pandas fastparquet duckdb

class ParquetSQLQueryEngine:
    def __init__(self, parquet_file: str):
        self.parquet_file = parquet_file

    def _read_table(self, columns: List[str] = None) -> pd.DataFrame:
        """读取 Parquet 文件为 Pandas DataFrame"""
        if columns:
            return pd.read_parquet(self.parquet_file, engine='fastparquet', columns=columns)
        else:
            return pd.read_parquet(self.parquet_file, engine='fastparquet')

    def query(self, sql_query: str) -> pd.DataFrame:
        """执行 SQL 查询并返回结果"""
        # 使用 DuckDB 执行 SQL 查询
        result_df = duckdb.query(f"SELECT * FROM read_parquet('{self.parquet_file}')").to_df()
        return duckdb.query(sql_query).to_df()

    def write(self, df: pd.DataFrame, mode: str = 'overwrite'):
        """将 DataFrame 写入 Parquet 文件"""
        if mode == 'overwrite':
            df.to_parquet(self.parquet_file, engine='fastparquet')
        elif mode == 'append':
            existing_df = self._read_table()
            combined_df = pd.concat([existing_df, df], ignore_index=True)
            combined_df.to_parquet(self.parquet_file, engine='fastparquet')
        else:
            raise ValueError("mode must be either 'overwrite' or 'append'")



if __name__ == "__main__":
    engine = ParquetSQLQueryEngine("data/example.parquet")

    # 写入数据到 Parquet 文件
    initial_data = pd.DataFrame({
        "column1": [1, 2, 3],
        "column2": ["A", "B", "C"],
        "column3": [True, False, True]
    })
    engine.write(initial_data, mode='overwrite')

    # 使用 SQL 查询读取数据
    result = engine.query("SELECT column1, column2 FROM read_parquet('data/example.parquet') WHERE column3 = TRUE")
    print(result)

    # 追加新数据
    new_data = pd.DataFrame({
        "column1": [4, 5],
        "column2": ["D", "E"],
        "column3": [False, True]
    })
    engine.write(new_data, mode='append')

    # 再次查询以验证追加的数据
    result_after_append = engine.query("SELECT * FROM read_parquet('data/example.parquet')")
    print(result_after_append)
