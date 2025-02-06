import cx_Oracle
import json
from DatabaseConnectionUtility import Oracle 
import loggerutility as logger

class UserRights:

    menu_model = {}

    def check_user_rights(self, application, connection):
        if not connection:
            return False
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT COUNT(*) FROM USER_RIGHTS WHERE APPLICATION = '{application}'")
            count = cursor.fetchone()[0]
            cursor.close()
            return count
        except cx_Oracle.Error as error:
            logger.log(f"Error: {error}")
            return False
        
    def process_data(self, conn, app_model):
        logger.log(f"Start of UserRights Class")
        self.menu_model = app_model
        application_name = self.menu_model['application']['id']
        logger.log(f"application_name ::: {application_name}")
        exsist = self.check_user_rights(application_name, conn)
        logger.log(f"exsist ::: {exsist}")
        if exsist:
            cursor = conn.cursor()
            model_obj_name_list = [i['obj_name'].lower() for i in self.menu_model['navigation']]
            logger.log(f"model_obj_name_list:: {model_obj_name_list}")

            cursor.execute(f"""SELECT obj_name FROM USER_RIGHTS WHERE TRIM(APPLICATION) = TRIM('{application_name}')""")
            data_obj_name_list = cursor.fetchall()
            logger.log(f"data_obj_name_list:: {data_obj_name_list}")
            for obj_name_list in data_obj_name_list:
                obj_name = obj_name_list[0]
                if obj_name not in model_obj_name_list:
                    raise KeyError(f"Data for APPLICATION: {application_name} having no user rights.")          
            cursor.close()
            for navigation in self.menu_model['navigation']:
                logger.log(f"navigation::; {navigation}")
                logger.log(f"application_name ::: {application_name}")
                logger.log(f"obj_name ::: {navigation['obj_name'].lower()}")
                cursor = conn.cursor()
                update_query = f"""
                    UPDATE USER_RIGHTS SET
                        MENU_ROW = '{navigation['menu_row']}',
                        MENU_COL = '{navigation['menu_col']}',
                        MENU_SUBCOL = '{navigation['menu_subcol']}',
                        LEVEL_4 = '{navigation['level_4']}',
                        LEVEL_5 = '{navigation['level_5']}'
                    WHERE TRIM(APPLICATION) = TRIM('{application_name}') 
                    AND TRIM(OBJ_NAME) = TRIM('{navigation['obj_name'].lower()}')
                """

                logger.log(f"\n--- Class UserRights ---\n")
                logger.log(f"{update_query}")
                cursor.execute(update_query)
                logger.log(f"executed cursor count {cursor.rowcount}")
                cursor.close()

        logger.log(f"End of UserRights Class")