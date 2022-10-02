import pandas as pd
import psycopg2 as pg

class data_import():
    def con(self):
        con = pg.connect(host='localhost', database='foodservice',
        user='postgres', password='postgres')
        return con

    def user(self):
        table = pd.read_excel("exports/user.xlsx")
        i = 0
        try:
            len_id = len(table['id'])
        except:
            len_id = 0
        while i < len_id:
            try:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                insert into auth_user (
                    id,
                    password,
                    last_login,
                    is_superuser,
                    username,
                    first_name,
                    last_name,
                    email,
                    is_staff,
                    is_active,
                    date_joined
                )
                values (
                    {table['id'][i]},
                    '{table['password'][i]}',
                    '{table['last_login'][i]}',
                    {table['is_superuser'][i]},
                    {table['username'][i]},
                    '{table['first_name'][i]}',
                    '{table['last_name'][i]}'
                    '{table['email'][i]}'
                    {table['is_staff'][i]}
                    {table['is_active'][i]}
                    '{table['date_joined'][i]}'
                ) 
                ''')
                conn.commit()
                conn.close()
            except:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                update default_company set
                    id = {table['id'][i]},
                    password = '{table['password'][i]}',
                    last_login = '{table['last_login'][i]}',
                    is_superuser = {table['is_superuser'][i]},
                    username = {table['username'][i]},
                    first_name = '{table['first_name'][i]}',
                    last_name = '{table['last_name'][i]}'
                    email = '{table['email'][i]}'
                    is_staff = {table['is_staff'][i]}
                    is_active = {table['is_active'][i]}
                    date_joined = '{table['date_joined'][i]}'
                where
                    id = {table['id'][i]}
                ''')
                conn.commit()
                conn.close()
            i+=1

    def company(self):
        table = pd.read_excel("exports/company.xlsx")
        i = 0
        try:
            len_id = len(table['id'])
        except:
            len_id = 0
        while i < len_id:
            try:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                insert into default_company (
                    id, 
                    slug, 
                    company, 
                    cnpj, 
                    owner_id, 
                    created, 
                    updated
                )
                values (
                    {table['id'][i]},
                    '{table['slug'][i]}',
                    '{table['company'][i]}',
                    '{table['cnpj'][i]}',
                    {table['owner_id'][i]},
                    '{table['created'][i]}',
                    '{table['updated'][i]}'
                ) 
                ''')
                conn.commit()
                conn.close()
            except:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                update default_company set
                    slug = '{table['slug'][i]}',
                    company = '{table['company'][i]}',
                    cnpj = '{table['cnpj'][i]}',
                    owner_id = {table['owner_id'][i]},
                    created = '{table['created'][i]}',
                    updated = '{table['updated'][i]}'
                where
                    id = {table['id'][i]}
                ''')
                conn.commit()
                conn.close()
            i+=1

    def companyposition(self):
        table = pd.read_excel("exports/companyposition.xlsx")
        i = 0
        try:
            len_id = len(table['id'])
        except:
            len_id = 0
        while i < len_id:
            try:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                insert into default_companyposition (
                    id, 
                    position,
                    company_id, 
                    created, 
                    updated
                )
                values (
                    {table['id'][i]},
                    '{table['position'][i]}',
                    {table['company_id'][i]},
                    '{table['created'][i]}',
                    '{table['updated'][i]}'
                )
                ''')
                conn.commit()
                conn.close()
            except:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                update default_companyposition set
                    position = '{table['position'][i]}',
                    company_id = {table['company_id'][i]},
                    created = '{table['created'][i]}',
                    updated = '{table['updated'][i]}'
                where
                    id = {table['id'][i]}
                ''')
                conn.commit()
                conn.close()
            i+=1

    def companyworker(self):
        table = pd.read_excel("exports/companyworker.xlsx")
        i = 0
        try:
            len_id = len(table['id'])
        except:
            len_id = 0
        while i < len_id:
            try:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                insert into default_companyworker (
                    id,
                    cpf,
                    rg,
                    phone_number,
                    company_id,
                    person_id,
                    position_id,
                    created,
                    updated
                )
                values (
                    {table['id'][i]},
                    '{table['cpf'][i]}',
                    '{table['rg'][i]}',
                    '{table['phone_number'][i]}',
                    {table['company_id'][i]},
                    {table['person_id'][i]},
                    {table['position_id'][i]},
                    '{table['created'][i]}',
                    '{table['updated'][i]}'
                )
                ''')
                conn.commit()
                conn.close()
            except:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                update default_companyworker set
                    cpf = '{table['cpf'][i]}',
                    rg = '{table['rg'][i]}',
                    phone_number = '{table['phone_number'][i]}',
                    company_id = {table['company_id'][i]},
                    person_id = {table['person_id'][i]},
                    position_id = {table['position_id'][i]},
                    created = '{table['created'][i]}',
                    updated = '{table['updated'][i]}'
                where
                    id = {table['id'][i]}
                ''')
                conn.commit()
                conn.close()
            i+=1

    def bugreport(self):
        table = pd.read_excel("exports/bugreport.xlsx")
        i = 0
        try:
            len_id = len(table['id'])
        except:
            len_id = 0
        while i < len_id:
            conn = self.con()
            cur = conn.cursor()
            cur.execute(f'''
            insert into default_bugreport (
                id,
                bug,
                company_id,
                company_worker_id,
                created,
                updated
            )
            values (
                {table['id'][i]},
                {table['bug'][i]},
                {table['company_id'][i]},
                {table['company_worker_id'][i]},
                '{table['created'][i]}',
                '{table['updated'][i]}'
            )
            ''')
            conn.commit()
            conn.close()
            i+=1

    def newregister(self):
        table = pd.read_excel("exports/newregister.xlsx")
        i = 0
        try:
            len_id = len(table['id'])
        except:
            len_id = 0
        while i < len_id:
            try: 
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                insert into default_newregister (
                    id,
                    email,
                    first_name,
                    last_name,
                    phone_number,
                    created,
                    updated
                )
                values (
                    {table['id'][i]},
                    '{table['email'][i]}',
                    "{table['first_name'][i]}",
                    "{table['last_name'][i]}",
                    '{table['phone_number'][i]}',
                    '{table['created'][i]}',
                    '{table['updated'][i]}'
                )
                ''')
                conn.commit()
                conn.close()
            except: 
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                update default_newregister set
                    email = '{table['email'][i]}',
                    first_name = '{table['first_name'][i].replace("'", '"')}',
                    last_name = '{table['last_name'][i].replace("'", '"')}',
                    phone_number = '{table['phone_number'][i]}',
                    created = '{table['created'][i]}',
                    updated = '{table['updated'][i]}'
                where
                    id = {table['id'][i]}
                ''')
                conn.commit()
                conn.close()
            i+=1

    def productbrand(self):
        table = pd.read_excel("exports/productbrand.xlsx")
        i = 0
        try:
            len_id = len(table['id'])
        except:
            len_id = 0
        while i < len_id:
            try:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                insert into register_productbrand (
                    id,
                    brand,
                    company_id,
                    company_worker_id,
                    created,
                    updated
                )
                values (
                    {table['id'][i]},
                    {table['brand'][i].replace("'", '"')},
                    {table['company_id'][i]},
                    {table['company_worker_id'][i]},
                    '{table['created'][i]}',
                    '{table['updated'][i]}'
                )
                ''')
                conn.commit()
                conn.close()
            except:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                update register_productbrand set
                    brand = '{table['brand'][i].replace("'", '"')}',
                    company_id = {table['company_id'][i]},
                    company_worker_id = {table['company_worker_id'][i]},
                    created = '{table['created'][i]}',
                    updated = '{table['updated'][i]}'
                where 
                    id = {table['id'][i]}
                ''')
                conn.commit()
                conn.close()
            i+=1

    def productmeasure(self):
        table = pd.read_excel("exports/productmeasure.xlsx")
        i = 0
        try:
            len_id = len(table['id'])
        except:
            len_id = 0
        while i < len_id:
            try:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                insert into register_productmeasure (
                    id,
                    measure,
                    company_id,
                    company_worker_id,
                    created,
                    updated
                )
                values (
                    {table['id'][i]},
                    {table['measure'][i]},
                    {table['company_id'][i]},
                    {table['company_worker_id'][i]},
                    '{table['created'][i]}',
                    '{table['updated'][i]}'
                )
                ''')
                conn.commit()
                conn.close()
            except:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                update register_productmeasure set
                    measure = '{table['measure'][i]}',
                    company_id = {table['company_id'][i]},
                    company_worker_id = {table['company_worker_id'][i]},
                    created = '{table['created'][i]}',
                    updated = '{table['updated'][i]}'
                where
                    id = {table['id'][i]}
                ''')
                conn.commit()
                conn.close()
            i+=1

    def product(self):
        table = pd.read_excel("exports/product.xlsx")
        i = 0
        try:
            len_id = len(table['id'])
        except:
            len_id = 0
        while i < len_id:
            try:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                insert into register_product (
                    id,
                    name,
                    stock,
                    cost,
                    brand_id,
                    measure_id,
                    price,
                    type,
                    company_id,
                    company_worker_id,
                    created,
                    updated
                )
                values (
                    {table['id'][i]},
                    '{table['name'][i]}',
                    {table['stock'][i]},
                    {table['cost'][i]},
                    {table['brand_id'][i]},
                    {table['measure_id'][i]},
                    {table['price'][i]},
                    {table['type'][i]},
                    {table['company_id'][i]},
                    {table['company_worker_id'][i]},
                    '{table['created'][i]}',
                    '{table['updated'][i]}'
                )
                ''')
                conn.commit()
                conn.close()
            except:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                update register_product set
                    {table['id'][i]},
                    '{table['name'][i]}',
                    {table['stock'][i]},
                    {table['cost'][i]},
                    {table['brand_id'][i]},
                    {table['measure_id'][i]},
                    {table['price'][i]},
                    {table['type'][i]},
                    {table['company_id'][i]},
                    {table['company_worker_id'][i]},
                    '{table['created'][i]}',
                    '{table['updated'][i]}'
                )
                ''')
                conn.commit()
                conn.close()
            i+=1

    def productitems(self):
        table = pd.read_excel("exports/productitems.xlsx")
        i = 0
        try:
            len_id = len(table['id'])
        except:
            len_id = 0
        while i < len_id:
            try:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                insert into register_productitems (
                    id,
                    product_id,
                    productitem_id,
                    quantity,
                    company_id,
                    company_worker_id,
                    created,
                    updated
                )
                values (
                    {table['id'][i]},
                    {table['product_id'][i]},
                    {table['productitem_id'][i]},
                    {table['quantity'][i]},
                    {table['company_id'][i]},
                    {table['company_worker_id'][i]},
                    '{table['created'][i]}',
                    '{table['updated'][i]}'
                )
                ''')
                conn.commit()
                conn.close()
            except:
                conn = self.con()
                cur = conn.cursor()
                cur.execute(f'''
                update register_productitems set
                    product_id = {table['product_id'][i]},
                    productitem_id = {table['productitem_id'][i]},
                    quantity = {table['quantity'][i]},
                    company_id = {table['company_id'][i]},
                    company_worker_id = {table['company_worker_id'][i]},
                    created = '{table['created'][i]}',
                    updated = '{table['updated'][i]}'
                where
                    id = {table['id'][i]}
                ''')
                conn.commit()
                conn.close()

    def sale(self):
        table = pd.read_excel("exports/sale.xlsx")
        i = 0
        while i < len(table['id']):
            conn = self.con()
            cur = conn.cursor()
            cur.execute(f'''
            insert into register_saleitems (
                id,
                delivery,
                value,
                total,
                company_id,
                company_worker_id,
                created,
                updated
            )
            values (
                {table['id'][i]},
                {table['delivery'][i]},
                {table['value'][i]},
                {table['total'][i]},
                {table['company_id'][i]},
                {table['company_worker_id'][i]},
                '{table['created'][i]}',
                '{table['updated'][i]}'
            )
            ''')
            conn.commit()
            conn.close()
            i+=1

    def saleitems(self):
        table = pd.read_excel("exports/saleitems.xlsx")
        i = 0
        while i < len(table['id']):
            conn = self.con()
            cur = conn.cursor()
            cur.execute(f'''
            insert into register_saleitems (
                id,
                sale_id,
                product_id,
                quantity,
                price,
                company_id,
                company_worker_id,
                created,
                updated
            )
            values (
                {table['id'][i]},
                {table['sale_id'][i]},
                {table['product_id'][i]},
                {table['quantity'][i]},
                {table['price'][i]},
                {table['company_id'][i]},
                {table['company_worker_id'][i]},
                '{table['created'][i]}',
                '{table['updated'][i]}'
            )
            ''')
            conn.commit()
            conn.close()
            i+=1




if __name__ == '__main__':
    data_import().user()
    data_import().company()
    data_import().companyposition()
    data_import().companyworker()
    data_import().bugreport()
    data_import().newregister()
    data_import().productbrand()
    data_import().productmeasure()
    data_import().sale() 
    data_import().saleitems() 