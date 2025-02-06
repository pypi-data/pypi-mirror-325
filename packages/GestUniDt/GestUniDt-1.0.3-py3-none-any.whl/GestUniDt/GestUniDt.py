import os
import time
import csv
import json
import datetime
from pandas import read_csv, notnull

class Gud:
    def __init__(self):
        self.filename = None
        self.columns = []
        self.col_map = {}
        self.Nrows = 0
        self.lastT = None
        self.last_id = 0
        self.time_format='%Y-%m-%d %H:%M:%S.%f'
        self.file_initialized = False
        printBanner('GestUniDt', 'v1.0.3', 'by eaannist', '█')

    def new(self, filename):
        self.filename = filename
        self.columns = []
        self.col_map = {}
        self.Nrows = 0
        self.lastT = None
        self.last_id = 0
        self.file_initialized = False
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return self
    
    def _ensure_header(self):
        if not self.file_initialized:
            self._init_file()
        else:
            if self.Nrows == 0:
                self._update_header()
                
    def idCol(self):
        if any(col for col in self.columns if col['type'] == 'id'):
            return self
        self.columns.insert(0, {'base': 'id', 'full': 'id', 'type': 'id', 'auto': True})
        self._ensure_header()
        return self

    def timeCol(self):
        if any(col for col in self.columns if col['type'] == 'time'):
            return self
        pos = 1 if (self.columns and self.columns[0]['type'] == 'id') else 0
        self.columns.insert(pos, {'base': 'time', 'full': 'time', 'type': 'time', 'auto': True})
        self._ensure_header()
        return self

    def textCol(self, col_name):
        full_name = f"{col_name}_T"
        self.columns.append({'base': col_name, 'full': full_name, 'type': 'text', 'auto': False})
        self.col_map[col_name] = full_name
        self._ensure_header()
        return self

    def dataCol(self, col_name):
        full_name = f"{col_name}_D"
        self.columns.append({'base': col_name, 'full': full_name, 'type': 'data', 'auto': False})
        self.col_map[col_name] = full_name
        self._ensure_header()
        return self
    
    def _init_file(self):
        with self._acquire_lock():
            with open(self.filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                header = [col['full'] for col in self.columns]
                writer.writerow(header)
        self.file_initialized = True
        
    def _update_header(self):
        with self._acquire_lock():
            with open(self.filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                header = [col['full'] for col in self.columns]
                writer.writerow(header)

    def load(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            raise FileNotFoundError("The file does not exist.")
        with self._acquire_lock():
            with open(self.filename, 'r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader)
        self.columns = []
        self.col_map = {}
        for col in header:
            if col == 'id':
                self.columns.append({'base': 'id', 'full': 'id', 'type': 'id', 'auto': True})
            elif col == 'time':
                self.columns.append({'base': 'time', 'full': 'time', 'type': 'time', 'auto': True})
            elif col.endswith('_T'):
                base = col[:-2]
                self.columns.append({'base': base, 'full': col, 'type': 'text', 'auto': False})
                self.col_map[base] = col
            elif col.endswith('_D'):
                base = col[:-2]
                self.columns.append({'base': base, 'full': col, 'type': 'data', 'auto': False})
                self.col_map[base] = col
            else:
                self.columns.append({'base': col, 'full': col, 'type': 'unknown', 'auto': False})
        df = read_csv(self.filename)
        self.Nrows = len(df)
        if any(col for col in self.columns if col['type'] == 'id'):
            if not df.empty:
                self.last_id = int(df['id'].max())
            else:
                self.last_id = 0
        if any(col for col in self.columns if col['type'] == 'time') and self.Nrows > 0:
            self.lastT = df['time'].iloc[-1]
        self.file_initialized = True
        return self
        
    def _acquire_lock(self, timeout=10):
        return FileLock(self.filename + ".lock", timeout=timeout)
    
    def add(self, *rows):
        if not self.file_initialized:
            if not any(col for col in self.columns if col['type'] == 'text'):
                raise Exception("At least one textCol is required to create a new file.")
            self._init_file()
        new_rows = []
        for row in rows:
            if isinstance(row, list):
                manual_cols = [col for col in self.columns if not col['auto']]
                if len(row) != len(manual_cols):
                    raise Exception(f"Expected {len(manual_cols)} values, got {len(row)}.")
                list_index = 0
                row_data = {}
                for col in self.columns:
                    if col['type'] == 'id':
                        # Use self.last_id to generate a unique id.
                        new_id = self.last_id + 1
                        row_data[col['full']] = new_id
                        self.last_id = new_id
                    elif col['type'] == 'time':
                        current_time = datetime.datetime.now().strftime(self.time_format)
                        row_data[col['full']] = current_time
                    elif col['type'] == 'text':
                        row_data[col['full']] = str(row[list_index])
                        list_index += 1
                    elif col['type'] == 'data':
                        row_data[col['full']] = json.dumps(row[list_index])
                        list_index += 1
                    else:
                        row_data[col['full']] = row[list_index]
                        list_index += 1
                new_rows.append(row_data)
            elif isinstance(row, dict):
                row_data = {}
                for col in self.columns:
                    if col['type'] == 'id':
                        new_id = self.last_id + 1
                        row_data[col['full']] = new_id
                        self.last_id = new_id
                    elif col['type'] == 'time':
                        current_time = datetime.datetime.now().isoformat()
                        row_data[col['full']] = current_time
                    else:
                        if col['base'] not in row:
                            raise Exception(f"Missing value for column '{col['base']}'.")
                        if col['type'] == 'text':
                            row_data[col['full']] = str(row[col['base']])
                        elif col['type'] == 'data':
                            row_data[col['full']] = json.dumps(row[col['base']])
                        else:
                            row_data[col['full']] = row[col['base']]
                new_rows.append(row_data)
            else:
                raise Exception("Each argument must be a list or a dict.")
        with self._acquire_lock():
            with open(self.filename, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=[col['full'] for col in self.columns])
                for row_data in new_rows:
                    writer.writerow(row_data)
                    self.Nrows += 1
                    if any(col for col in self.columns if col['type'] == 'time'):
                        self.lastT = row_data['time']
        return self

    
    def get(self):
        if not self.file_initialized:
            self._init_file()
        with self._acquire_lock():
            df = read_csv(self.filename)
            
        for col in self.columns:
            if col['type'] == 'data':
                full = col['full']
                df[full] = df[full].apply(lambda x: json.loads(x) if notnull(x) and x != "" else None)
        return Query(df, self)
    
    def count(self):
        if not self.file_initialized:
            self._init_file()
        return self.Nrows
    
    def timeFormat(self, tf):
        self.time_format=tf
        return self
    
    def clear(self):
        with self._acquire_lock():
            with open(self.filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                header = [col['full'] for col in self.columns]
                writer.writerow(header)
        self.Nrows = 0
        self.lastT = None
        return self

    def deleteCsvFile(self):
        with self._acquire_lock():
            if os.path.exists(self.filename):
                os.remove(self.filename)
        self.file_initialized = False
        self.Nrows = 0
        self.lastT = None

    def del_(self):
        if not self.file_initialized:
            self._init_file()
        with self._acquire_lock():
            df = read_csv(self.filename)
            
        for col in self.columns:
            if col['type'] == 'data':
                full = col['full']
                df[full] = df[full].apply(lambda x: json.loads(x) if notnull(x) and x != "" else None)
        return DeletionQuery(df, self)
    
class FileLock:
    def __init__(self, lockfile, timeout=10):
        self.lockfile = lockfile
        self.timeout = timeout

    def __enter__(self):
        start_time = time.time()
        while True:
            try:
                self.fd = os.open(self.lockfile, os.O_CREAT | os.O_EXCL | os.O_RDWR)
                break
            except FileExistsError:
                if time.time() - start_time > self.timeout:
                    raise Exception("The file has been locked for too long.")
                time.sleep(0.1)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.close(self.fd)
        os.remove(self.lockfile)
        
class Query:
    def __init__(self, df, gud_instance):
        self.df = df
        self.gud = gud_instance
        self.conditions = []
        self.selected_columns = None

    def where(self, col, cond):
        if col in ['id', 'time']:
            full = col
        elif col in self.gud.col_map:
            full = self.gud.col_map[col]
        else:
            raise Exception(f"Colonna {col} non trovata.")
        parts = cond.strip().split(' ', 1)
        if len(parts) != 2:
            raise Exception("The condition needs to be formatted like: '<operator> <value>'.")
        operator, value_str = parts
        try:
            value = float(value_str)
            if value.is_integer():
                value = int(value)
        except:
            value = value_str
        self.conditions.append((full, operator, value))
        return self

    def cols(self, cols_list):
        full_cols = []
        for col in cols_list:
            if col in ['id', 'time']:
                full_cols.append(col)
            elif col in self.gud.col_map:
                full_cols.append(self.gud.col_map[col])
            else:
                raise Exception(f"Column {col} not found.")
        self.selected_columns = full_cols
        return self

    def first(self, n):
        self.df = self.df.head(n)
        return self

    def last(self, n):
        self.df = self.df.tail(n)
        return self

    def _apply_conditions(self):
        df_filtered = self.df
        eq_conditions = {}
        other_conditions = []
        for col, op, value in self.conditions:
            if op == '=':
                eq_conditions.setdefault(col, []).append(value)
            else:
                other_conditions.append((col, op, value))
        for col, values in eq_conditions.items():
            df_filtered = df_filtered[df_filtered[col].isin(values)]
        for col, op, value in other_conditions:
            if op == '!=':
                df_filtered = df_filtered[df_filtered[col] != value]
            elif op == '<':
                df_filtered = df_filtered[df_filtered[col] < value]
            elif op == '>':
                df_filtered = df_filtered[df_filtered[col] > value]
            elif op == '<=':
                df_filtered = df_filtered[df_filtered[col] <= value]
            elif op == '>=':
                df_filtered = df_filtered[df_filtered[col] >= value]
            else:
                raise Exception(f"Operator {op} not supported.")
        return df_filtered

    def values(self):
        df_result = self._apply_conditions()
        
        if self.selected_columns is None:
            all_cols = [col['full'] for col in self.gud.columns]
            df_result = df_result[all_cols]
        else:
            df_result = df_result[self.selected_columns]

        if df_result.shape[1] == 1:
            return df_result.iloc[:, 0].tolist()
        else:
            return df_result.values.tolist()
        
    def toDf(self):
        df_result = self._apply_conditions()

        if self.selected_columns is None:
            all_cols = [col['full'] for col in self.gud.columns]
            df_result = df_result[all_cols]
        else:
            df_result = df_result[self.selected_columns]

        return df_result
    
class DeletionQuery:
    def __init__(self, df, gud_instance):
        self.df = df
        self.gud = gud_instance
        self.conditions = []
        self.limit_first = None
        self.limit_last = None

    def where(self, col, cond):
        if col in ['id', 'time']:
            full = col
        elif col in self.gud.col_map:
            full = self.gud.col_map[col]
        else:
            raise Exception(f"Colonna {col} non trovata.")
        parts = cond.strip().split(' ', 1)
        if len(parts) != 2:
            raise Exception("The condition needs to be formatted like: '<operator> <value>'.")
        operator, value_str = parts
        try:
            value = float(value_str)
            if value.is_integer():
                value = int(value)
        except:
            value = value_str
        self.conditions.append((full, operator, value))
        return self

    def first(self, n):
        self.limit_first = n
        return self

    def last(self, n):
        self.limit_last = n
        return self

    def _apply_conditions(self):
        df_filtered = self.df
        eq_conditions = {}
        other_conditions = []
        for col, op, value in self.conditions:
            if op == '=':
                eq_conditions.setdefault(col, []).append(value)
            else:
                other_conditions.append((col, op, value))
        for col, values in eq_conditions.items():
            df_filtered = df_filtered[df_filtered[col].isin(values)]
        for col, op, value in other_conditions:
            if op == '!=':
                df_filtered = df_filtered[df_filtered[col] != value]
            elif op == '<':
                df_filtered = df_filtered[df_filtered[col] < value]
            elif op == '>':
                df_filtered = df_filtered[df_filtered[col] > value]
            elif op == '<=':
                df_filtered = df_filtered[df_filtered[col] <= value]
            elif op == '>=':
                df_filtered = df_filtered[df_filtered[col] >= value]
            else:
                raise Exception(f"Operator {op} not supported.")
        return df_filtered

    def execute(self):
        df_filtered = self._apply_conditions()
        if self.limit_first is not None:
            df_filtered = df_filtered.head(self.limit_first)
        if self.limit_last is not None:
            df_filtered = df_filtered.tail(self.limit_last)
        indices_to_delete = df_filtered.index
        with self.gud._acquire_lock():
            df_full = read_csv(self.gud.filename)
            df_remaining = df_full.drop(indices_to_delete)
            df_remaining.to_csv(self.gud.filename, index=False)
        self.gud.Nrows = len(df_remaining)
        if any(col for col in self.gud.columns if col['type'] == 'time'):
            self.gud.lastT = df_remaining['time'].iloc[-1] if self.gud.Nrows > 0 else None
        return len(indices_to_delete)

def printBanner(nome, versione, autore, filler):
    versione_width = len(versione)
    inner_width = max(len(nome) + versione_width, len(f">> {autore}")) + 4
    border = '    ' + filler * (inner_width + 4)
    line2 = f"    {filler}{filler} {nome.ljust(inner_width - versione_width -2)}{versione.rjust(versione_width-2)} {filler}{filler}"
    line3 = f"    {filler}{filler} {f'>> {autore}'.rjust(inner_width-2)} {filler}{filler}"
    banner = f"\n{border}\n{line2}\n{line3}\n{border}\n"
    print(banner)
