import cx_Oracle
from datetime import datetime
import loggerutility as logger

class ApplMst:
    sql_models = []

    def insert_or_update_applmst(self, application, connection):
        if not connection:
            return

        required_keys = ['id']
        missing_keys = [key for key in required_keys if key not in application]

        if missing_keys:
            raise KeyError(f"Missing required keys for APPL_MST table: {', '.join(missing_keys)}")
        else:
            app_name = application.get('id', '').strip()
            logger.log(f"application name :: {app_name}")
            logger.log(f"application length :: {len(app_name)}")
            app_name = app_name.upper()
            logger.log(f"app_name ::: {app_name}")
            descr = application.get('description', '')
            chg_date = datetime.now().strftime('%d-%m-%y')
            chg_user = application.get('chg_user', '').strip() or 'System'
            chg_term = application.get('chg_term', '').strip() or 'System'
            appl_group = application.get('group', '')
            appl_color = application.get('theme_color', '')
            appl_order = application.get('appl_order', '')
            conn_option = application.get('conn_option', '')
            appl_type = application.get('appl_type', '')
            search_domain = application.get('search_domain', '')
            appl_grp_descr = application.get('appl_grp_descr', '')
            appl_group_color = application.get('appl_group_color', '')
            title = application.get('title', '')
            logger.log(f"app_name :: {app_name}")

            cursor = connection.cursor()
            queryy = f"""
                SELECT COUNT(*) FROM APPL_MST 
                WHERE APP_NAME = '{app_name}'
            """
            logger.log(f"\n--- Class ApplMst ---\n")
            logger.log(f"{queryy}")
            cursor.execute(queryy)
            row_exists = cursor.fetchone()[0]
            logger.log(f"row_exists :: {row_exists}")
            cursor.close()

            if row_exists:
                cursor = connection.cursor()
                update_query = f"""
                    UPDATE APPL_MST SET
                        DESCR = '{descr}',
                        CHG_DATE = TO_DATE('{chg_date}', 'DD-MM-YY'),
                        CHG_USER = '{chg_user}',
                        CHG_TERM = '{chg_term}',
                        APPL_GROUP = '{appl_group}',
                        APPL_COLOR = '{appl_color}',
                        APPL_ORDER = '{appl_order}',
                        CONN_OPTION = '{conn_option}',
                        APPL_TYPE = '{appl_type}',
                        SEARCH_DOMAIN = '{search_domain}',
                        APPL_GRP_DESCR = '{appl_grp_descr}',
                        APPL_GROUP_COLOR = '{appl_group_color}',
                        TITLE = '{title}'
                    WHERE TRIM(APP_NAME) = TRIM('{app_name}')
                """
                logger.log(f"\n--- Class ApplMst ---\n")
                logger.log(f"{update_query}")
                cursor.execute(update_query)
                logger.log(f"Successfully updated row.")
                cursor.close()

            else:
                cursor = connection.cursor()
                insert_query = f"""
                    INSERT INTO APPL_MST (
                        APP_NAME, DESCR, CHG_DATE, CHG_USER, CHG_TERM,
                        APPL_GROUP, APPL_COLOR, APPL_ORDER, CONN_OPTION,
                        APPL_TYPE, SEARCH_DOMAIN, APPL_GRP_DESCR, APPL_GROUP_COLOR, TITLE
                    ) VALUES (
                        '{app_name}', '{descr}', TO_DATE('{chg_date}', 'DD-MM-YY'), '{chg_user}', '{chg_term}',
                        '{appl_group}', '{appl_color}', '{appl_order}', '{conn_option}',
                        '{appl_type}', '{search_domain}', '{appl_grp_descr}', '{appl_group_color}', '{title}'
                    )
                """
                logger.log(f"\n--- Class ApplMst ---\n")
                logger.log(f"{insert_query}")
                cursor.execute(insert_query)
                logger.log(f"Successfully inserted row.")
                cursor.close()
        

    def process_data(self, conn, menu_model):
        logger.log(f"Start of ApplMst Class")
        if "application" in menu_model:
            application = menu_model["application"]
            self.insert_or_update_applmst(application, conn)
        logger.log(f"End of ApplMst Class")
            
        
