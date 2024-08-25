from flask_app.config.mysqlconnection import connect
from flask import flash, session   # type: ignore
from datetime import datetime
current_time = datetime.now()
from flask_app.models import user


class Report:
    DB = 'cdr_schema'
    def __init__(self, data):
        self.id = data['id']
        self.project_name = data['project_name']
        self.job_no = data['job_no']
        self.date = data['date']  
        self.report = data['report']        
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM reports JOIN
        users ON reports.user_id = users.id
    
        """
        results = connect(cls.DB).query_db(query)
        print(results)
        output = []
        for join_dict in results:
            this_report = cls(join_dict)
            user_data = {
                'id' : join_dict['users.id'],
                'first_name' : join_dict['first_name'],
                'last_name' : join_dict['last_name'],
                'email' : join_dict['email'],
                'password' : join_dict['password'],          
                'created_at' : join_dict['users.created_at'],
                'updated_at' : join_dict['users.updated_at']
            }
       
            this_report.creator = user.User(user_data)
            output.append(this_report)
        return output
    
    @classmethod
    def get_by_id(cls, user_id):
        query = """
        SELECT * FROM reports JOIN
        users ON reports.user_id = users.id
        WHERE reports.id = %(id)s;
    
        """
        data = {"id": user_id}
       
        results = connect(cls.DB).query_db(query, data)
        print(results)
        this_report = cls(results[0])   
        for each_dict in results:        
            user_data = {
                        'id' : each_dict['users.id'],
                        'first_name' : each_dict['first_name'],
                        'last_name' : each_dict['last_name'],
                        'email' : each_dict['email'],
                        'password' : each_dict['password'],          
                        'created_at' : each_dict['users.created_at'],
                        'updated_at' : each_dict['users.updated_at']
                    }
            this_report.creator = user.User(user_data)
        return this_report
          
    @classmethod
    def create(cls, data):
        print(f"model: {data}")
        query = """
        INSERT INTO reports
        (project_name, job_no, date, report, user_id)
        VALUES (%(project_name)s, %(job_no)s, %(date)s, %(report)s, %(user_id)s)
        """
        data = data.to_dict()
        data['user_id'] = session['user_id']
        user_id = connect(cls.DB).query_db(query, data)
        print(user_id)
        
    @classmethod
    def delete_one(cls, data):
        query = """
        DELETE
        FROM reports
        WHERE id = %(id)s;
        """
        results = connect(cls.DB).query_db(query, data)

    @classmethod
    def update_by_id(cls, data, tree_id):
        query = """
        UPDATE reports
        SET
        project_name = %(project_name)s,
        job_no = %(job_no)s,
        date = %(date)s,
        report = %(report)s
        WHERE id = %(id)s;
        """
    
        
        all_data = data.to_dict()
        all_data['id'] = tree_id
        results = connect(cls.DB).query_db(query, all_data)

    @classmethod
    def save(cls, form_data):
         query = """
         INSERT INTO reports
         (project_name, job_no, date, report, user_id)
         VALUES (%(project_name)s, %(job_no)s, %(date)s, %(report)s, %(user_id)s)
         """
         data = form_data.to_dict()
         data['user_id'] = session['user_id']
         user_id = connect(cls.DB).query_db(query, data)
         print(user_id)

    @classmethod
    def view_one(cls, form_data):
         query = """
         INSERT INTO reports
         (project_name, job_no, date, report, user_id)
         VALUES (%(project_name)s, %(job_no)s, %(date)s, %(report)s, %(user_id)s)
         """
         data = form_data.to_dict()
         data['user_id'] = session['user_id']
         user_id = connect(cls.DB).query_db(query, data)
         print(user_id)

    @classmethod
    def view(cls, form_data):
         query = """
         INSERT INTO reports
         (project_name, job_no, date, report, user_id)
         VALUES (%(project_name)s, %(job_no)s, %(date)s, %(report)s, %(user_id)s)
         """
         data = form_data.to_dict()
         data['user_id'] = session['user_id']
         user_id = connect(cls.DB).query_db(query, data)
         print(user_id)
    
    

    @staticmethod
    def valid(form_data):
        is_valid = True
        if not form_data['project_name'].strip():
            is_valid = False
            flash('Project name Required', 'report')
        
        elif len(form_data['project_name']) < 2:
            is_valid = False
            flash('2 Char Min', 'report')

        if not form_data['job_no'].strip():
            is_valid = False
            flash('Job no Required', 'report')
        
        elif len(form_data['job_no']) < 5:
            is_valid = False
            flash('5 Char Min', 'report')

        if not form_data['date'].strip():
            is_valid = False
            flash('Date Required', 'report')

        elif form_data['date'] > str(datetime.now()):
            is_valid = False
            
            flash('Cannot Time Travel', 'report')

        if not form_data['report'].strip():
            is_valid = False
            flash('Report Required', 'report')
        
        elif len(form_data['report']) > 200:
            is_valid = False
            flash('200 Char Max', 'report')

        return is_valid

    @staticmethod
    def edit_valid(form_data):
        is_valid = True

        if not form_data['project_name'].strip():
            is_valid = False
            flash('Project name Required', 'report')
        
        elif len(form_data['project_name']) < 2:
            is_valid = False
            flash('2 Char Min', 'report')

        if not form_data['job_no'].strip():
            is_valid = False
            flash('Job no Required', 'report')
        
        elif len(form_data['job_no']) < 5:
            is_valid = False
            flash('5 Char Min', 'report')

        if not form_data['date'].strip():
            is_valid = False
            flash('Date Required', 'report')

        elif form_data['date'] > str(datetime.now()):
            is_valid = False
            
            flash('Cannot Time Travel', 'report')

        if not form_data['report'].strip():
            is_valid = False
            flash('Report Required', 'report')
        
        elif len(form_data['report']) > 200:
            is_valid = False
            flash('200 Char Max', 'report')

        return is_valid


        
