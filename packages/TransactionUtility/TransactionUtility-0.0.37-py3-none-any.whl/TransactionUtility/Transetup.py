import cx_Oracle
from datetime import datetime
import loggerutility as logger

class Transetup:
    
    sql_models = []

    def check_and_update_transetup(self, sql_model, connection):

        required_keys = ['tran_window']

        missing_keys = [key for key in required_keys if key not in sql_model]

        if missing_keys:
            raise KeyError(f"Missing required keys for transetup table: {', '.join(missing_keys)}")
        else:
            tran_window = sql_model.get('tran_window', '')
            save_flag = sql_model.get('save_flag', '')
            val_flag = sql_model.get('val_flag', '')
            key_flag = sql_model.get('key_flag', '') or 'M'
            key_string = sql_model.get('key_string', '')
            udf_1 = sql_model.get('udf_1', '')
            udf_2 = sql_model.get('udf_2', '')
            udf_3 = sql_model.get('udf_3', '')
            udf_4 = sql_model.get('udf_4', '')
            udf_5 = sql_model.get('udf_5', '')
            repeate_add = sql_model.get('repeate_add', '')
            chg_date = datetime.now().strftime('%d-%m-%y')
            chg_user = sql_model.get('chg_user', '').strip() or 'System'
            chg_term = sql_model.get('chg_term', '').strip() or 'System'
            edi_option = sql_model.get('edi_option', '')
            site_acc_col = sql_model.get('site_acc_col', '')
            confirm_col = sql_model.get('confirm_col', '')
            confirm_val = sql_model.get('confirm_val', '')
            repeat_add_det = sql_model.get('repeat_add_det', '')
            repeatadddet = sql_model.get('repeatadddet', '')
            load_mode = sql_model.get('load_mode', '')
            auto_confirm = sql_model.get('auto_confirm', '')
            ledg_post_conf = sql_model.get('ledg_post_conf', '')
            chg_date_on_conf = sql_model.get('chg_date_on_conf', '')
            tran_id_col = sql_model.get('tran_id_col', '')
            mail_option = sql_model.get('mail_option', '')
            confirm_mode = sql_model.get('confirm_mode', '')
            garbage_opt = sql_model.get('garbage_opt', '')
            val_flag_edi = sql_model.get('val_flag_edi', '')
            verify_password = sql_model.get('verify_password', '')
            cust_acc_col = sql_model.get('cust_acc_col', '')
            sales_pers_acc_col = sql_model.get('sales_pers_acc_col', '')
            supp_acc_col = sql_model.get('supp_acc_col', '')
            item_ser_acc_code = sql_model.get('item_ser_acc_code', '')
            emp_acc_col = sql_model.get('emp_acc_col', '')
            item_ser_acc_col = sql_model.get('item_ser_acc_col', '')
            workflow_opt = sql_model.get('workflow_opt', '')
            table_name = sql_model.get('table_name', '')
            application = sql_model.get('application', '')
            table_desc = sql_model.get('table_desc', '')
            tran_date_col = sql_model.get('tran_date_col', '')
            tran_id__from = sql_model.get('tran_id__from', '')
            tran_id__to = sql_model.get('tran_id__to', '')
            table_name_det1 = sql_model.get('table_name_det1', '')
            table_name_det2 = sql_model.get('table_name_det2', '')
            table_name_det3 = sql_model.get('table_name_det3', '')
            multitire_opt = sql_model.get('multitire_opt', '')
            ref_ser = sql_model.get('ref_ser', '')
            view_mode = sql_model.get('view_mode', '')
            tax_forms = sql_model.get('tax_forms', '')
            sign_status = sql_model.get('sign_status', '')
            user_tran_window = sql_model.get('user_tran_window', '')
            obj_name__parent = sql_model.get('obj_name__parent', '')
            ignoreerrlist_onload = sql_model.get('ignoreerrlist_onload', '')
            childdata_argopt = sql_model.get('childdata_argopt', '')
            edit_tmplt = sql_model.get('edit_tmplt', '')
            wrkflw_init = sql_model.get('wrkflw_init', '')
            edittax = sql_model.get('edittax', '')
            formal_args = sql_model.get('formal_args', '')
            audit_trail_opt = sql_model.get('audit_trail_opt', '')
            edit_opt = sql_model.get('edit_opt', '')
            cache_opt = sql_model.get('cache_opt', '')
            optimize_mode = sql_model.get('optimize_mode', '')
            edit_expr = sql_model.get('edit_expr', '')
            rate_col = sql_model.get('rate_col', '')
            qty_col = sql_model.get('qty_col', '')
            edit_expr_inp = sql_model.get('edit_expr_inp', '')
            rcp_cache_status = sql_model.get('rcp_cache_status', '')
            print_control = sql_model.get('print_control', '')
            transfer_mode = sql_model.get('transfer_mode', '')
            profile_id__res = sql_model.get('profile_id__res', '')
            tran_compl_msg = sql_model.get('tran_compl_msg', '')
            period_option = sql_model.get('period_option', '')
            wrkflw_priority = sql_model.get('wrkflw_priority', '')
            exec_type = sql_model.get('exec_type', '')
            disp_meta_data = sql_model.get('disp_meta_data', '')
            allow_attach = sql_model.get('allow_attach', '')
            start_form = sql_model.get('start_form', '')
            isattachment = sql_model.get('isattachment', '')
            header_form_no = sql_model.get('header_form_no', '')
            confirm_date_col = sql_model.get('confirm_date_col', '')
            confirm_by_col = sql_model.get('confirm_by_col', '')
            msg_onsave = sql_model.get('msg_onsave', '')
            wf_status = sql_model.get('wf_status', '')
            restart_form = sql_model.get('restart_form', '')
            cms_path = sql_model.get('cms_path', '')
            brow_data_def = sql_model.get('brow_data_def', '')
            def_view = sql_model.get('def_view', '')
            view_opts = sql_model.get('view_opts', '')
            isgwtinitiated = sql_model.get('isgwtinitiated', '')
            default_data_row = sql_model.get('default_data_row', '')
            in_wf_val = sql_model.get('in_wf_val', '')
            in_wf_col = sql_model.get('in_wf_col', '')
            cancel_val = sql_model.get('cancel_val', '')
            cancel_col = sql_model.get('cancel_col', '')
            thumb_alt_col = sql_model.get('thumb_alt_col', '')
            thumb_image_col = sql_model.get('thumb_image_col', '')
            thumb_obj = sql_model.get('thumb_obj', '')
            attach_count_min = sql_model.get('attach_count_min', '')
            function_type = sql_model.get('function_type', '')
            compl_action = sql_model.get('compl_action', '')
            default_editor = sql_model.get('default_editor', '')
            msg_no = sql_model.get('msg_no', '')
            obj_type = sql_model.get('obj_type', '')
            status_col = sql_model.get('status_col', '')
            enable_editor = sql_model.get('enable_editor', '')
            offline_opt = sql_model.get('offline_opt', '')
            close_col = sql_model.get('close_col', '')
            close_val = sql_model.get('close_val', '')
            thread_key_col = sql_model.get('thread_key_col', '')
            load_order = sql_model.get('load_order', '')
            sync_from_app = sql_model.get('sync_from_app', '')

            cursor = connection.cursor()
            cursor.execute(f"""
                SELECT COUNT(*) FROM transetup 
                WHERE TRAN_WINDOW = '{tran_window}'
            """)
            count = cursor.fetchone()[0]
            cursor.close()
            logger.log(f"Transetup count ::: {count}")
            if count > 0:
                cursor = connection.cursor()
                update_query = f"""
                    UPDATE transetup SET
                        SAVE_FLAG = '{save_flag}', VAL_FLAG = '{val_flag}', KEY_FLAG = '{key_flag}',
                        KEY_STRING = '{key_string}', UDF_1 = '{udf_1}', UDF_2 = '{udf_2}', UDF_3 = '{udf_3}',
                        UDF_4 = '{udf_4}', UDF_5 = '{udf_5}', REPEATE_ADD = '{repeate_add}', CHG_DATE = TO_DATE('{chg_date}', 'DD-MM-YYYY'),
                        CHG_USER = '{chg_user}', CHG_TERM = '{chg_term}', EDI_OPTION = '{edi_option}',
                        SITE_ACC_COL = '{site_acc_col}', CONFIRM_COL = '{confirm_col}', CONFIRM_VAL = '{confirm_val}',
                        REPEAT_ADD_DET = '{repeat_add_det}', REPEATADDDET = '{repeatadddet}', LOAD_MODE = '{load_mode}',
                        AUTO_CONFIRM = '{auto_confirm}', LEDG_POST_CONF = '{ledg_post_conf}',
                        CHG_DATE_ON_CONF = '{chg_date_on_conf}', TRAN_ID_COL = '{tran_id_col}',
                        MAIL_OPTION = '{mail_option}', CONFIRM_MODE = '{confirm_mode}', GARBAGE_OPT = '{garbage_opt}',
                        VAL_FLAG_EDI = '{val_flag_edi}', VERIFY_PASSWORD = '{verify_password}',
                        CUST_ACC_COL = '{cust_acc_col}', SALES_PERS_ACC_COL = '{sales_pers_acc_col}',
                        SUPP_ACC_COL = '{supp_acc_col}', ITEM_SER_ACC_CODE = '{item_ser_acc_code}',
                        EMP_ACC_COL = '{emp_acc_col}', ITEM_SER_ACC_COL = '{item_ser_acc_col}',
                        WORKFLOW_OPT = '{workflow_opt}', TABLE_NAME = '{table_name}', APPLICATION = '{application}',
                        TABLE_DESC = '{table_desc}', TRAN_DATE_COL = '{tran_date_col}', TRAN_ID__FROM = '{tran_id__from}',
                        TRAN_ID__TO = '{tran_id__to}', TABLE_NAME_DET1 = '{table_name_det1}',
                        TABLE_NAME_DET2 = '{table_name_det2}', TABLE_NAME_DET3 = '{table_name_det3}',
                        MULTITIRE_OPT = '{multitire_opt}', REF_SER = '{ref_ser}', VIEW_MODE = '{view_mode}',
                        TAX_FORMS = '{tax_forms}', SIGN_STATUS = '{sign_status}', USER_TRAN_WINDOW = NULL,
                        OBJ_NAME__PARENT = '{obj_name__parent}', IGNOREERRLIST_ONLOAD = '{ignoreerrlist_onload}',
                        CHILDDATA_ARGOPT = '{childdata_argopt}', EDIT_TMPLT = NULL,
                        WRKFLW_INIT = '{wrkflw_init}', EDITTAX = '{edittax}', FORMAL_ARGS = NULL,
                        AUDIT_TRAIL_OPT = '{audit_trail_opt}', EDIT_OPT = '{edit_opt}', CACHE_OPT = NULL,
                        OPTIMIZE_MODE = '{optimize_mode}', EDIT_EXPR = '{edit_expr}', RATE_COL = '{rate_col}',
                        QTY_COL = '{qty_col}', EDIT_EXPR_INP = '{edit_expr_inp}', RCP_CACHE_STATUS = '{rcp_cache_status}',
                        PRINT_CONTROL = '{print_control}', TRANSFER_MODE = '{transfer_mode}',
                        PROFILE_ID__RES = '{profile_id__res}', TRAN_COMPL_MSG = '{tran_compl_msg}',
                        PERIOD_OPTION = '{period_option}', WRKFLW_PRIORITY = '{wrkflw_priority}',
                        EXEC_TYPE = '{exec_type}', DISP_META_DATA = '{disp_meta_data}', ALLOW_ATTACH = '{allow_attach}',
                        START_FORM = '{start_form}', ISATTACHMENT = '{isattachment}', HEADER_FORM_NO = '{header_form_no}',
                        CONFIRM_DATE_COL = '{confirm_date_col}', CONFIRM_BY_COL = '{confirm_by_col}',
                        MSG_ONSAVE = '{msg_onsave}', WF_STATUS = '{wf_status}', RESTART_FORM = '{restart_form}',
                        CMS_PATH = '{cms_path}', BROW_DATA_DEF = '{brow_data_def}', DEF_VIEW = '{def_view}',
                        VIEW_OPTS = '{view_opts}', ISGWTINITIATED = '{isgwtinitiated}',
                        DEFAULT_DATA_ROW = NULL, IN_WF_VAL = '{in_wf_val}', IN_WF_COL = '{in_wf_col}',
                        CANCEL_VAL = '{cancel_val}', CANCEL_COL = '{cancel_col}', THUMB_ALT_COL = '{thumb_alt_col}',
                        THUMB_IMAGE_COL = '{thumb_image_col}', THUMB_OBJ = '{thumb_obj}',
                        ATTACH_COUNT_MIN = NULL, FUNCTION_TYPE = '{function_type}',
                        COMPL_ACTION = '{compl_action}', DEFAULT_EDITOR = '{default_editor}', MSG_NO = '{msg_no}',
                        OBJ_TYPE = '{obj_type}', STATUS_COL = '{status_col}', ENABLE_EDITOR = '{enable_editor}',
                        OFFLINE_OPT = '{offline_opt}', CLOSE_COL = '{close_col}', CLOSE_VAL = '{close_val}',
                        THREAD_KEY_COL = '{thread_key_col}', LOAD_ORDER = NULL, SYNC_FROM_APP = '{sync_from_app}'
                    WHERE TRAN_WINDOW = '{tran_window}'
                    """

                logger.log(f"\n--- Class Transetup ---\n")
                logger.log(f"{update_query}")
                cursor.execute(update_query)
                cursor.close()
                logger.log(f"Updated: {tran_window}")
            else:
                cursor = connection.cursor()
                insert_query = f"""
                    INSERT INTO transetup (
                    TRAN_WINDOW, SAVE_FLAG, VAL_FLAG, KEY_FLAG, KEY_STRING, UDF_1, UDF_2, UDF_3, UDF_4,
                    UDF_5, REPEATE_ADD, CHG_DATE, CHG_USER, CHG_TERM, EDI_OPTION, SITE_ACC_COL,
                    CONFIRM_COL, CONFIRM_VAL, REPEAT_ADD_DET, REPEATADDDET, LOAD_MODE, AUTO_CONFIRM,
                    LEDG_POST_CONF, CHG_DATE_ON_CONF, TRAN_ID_COL, MAIL_OPTION, CONFIRM_MODE,
                    GARBAGE_OPT, VAL_FLAG_EDI, VERIFY_PASSWORD, CUST_ACC_COL, SALES_PERS_ACC_COL,
                    SUPP_ACC_COL, ITEM_SER_ACC_CODE, EMP_ACC_COL, ITEM_SER_ACC_COL, WORKFLOW_OPT,
                    TABLE_NAME, APPLICATION, TABLE_DESC, TRAN_DATE_COL, TRAN_ID__FROM, TRAN_ID__TO,
                    TABLE_NAME_DET1, TABLE_NAME_DET2, TABLE_NAME_DET3, MULTITIRE_OPT, REF_SER,
                    VIEW_MODE, TAX_FORMS, SIGN_STATUS, USER_TRAN_WINDOW, OBJ_NAME__PARENT,
                    IGNOREERRLIST_ONLOAD, CHILDDATA_ARGOPT, EDIT_TMPLT, WRKFLW_INIT, EDITTAX,
                    FORMAL_ARGS, AUDIT_TRAIL_OPT, EDIT_OPT, CACHE_OPT, OPTIMIZE_MODE, EDIT_EXPR,
                    RATE_COL, QTY_COL, EDIT_EXPR_INP, RCP_CACHE_STATUS, PRINT_CONTROL, TRANSFER_MODE,
                    PROFILE_ID__RES, TRAN_COMPL_MSG, PERIOD_OPTION, WRKFLW_PRIORITY, EXEC_TYPE,
                    DISP_META_DATA, ALLOW_ATTACH, START_FORM, ISATTACHMENT, HEADER_FORM_NO,
                    CONFIRM_DATE_COL, CONFIRM_BY_COL, MSG_ONSAVE, WF_STATUS, RESTART_FORM, CMS_PATH,
                    BROW_DATA_DEF, DEF_VIEW, VIEW_OPTS, ISGWTINITIATED, DEFAULT_DATA_ROW, IN_WF_VAL,
                    IN_WF_COL, CANCEL_VAL, CANCEL_COL, THUMB_ALT_COL, THUMB_IMAGE_COL, THUMB_OBJ,
                    ATTACH_COUNT_MIN, FUNCTION_TYPE, COMPL_ACTION, DEFAULT_EDITOR, MSG_NO, OBJ_TYPE,
                    STATUS_COL, ENABLE_EDITOR, OFFLINE_OPT, CLOSE_COL, CLOSE_VAL, THREAD_KEY_COL,
                    LOAD_ORDER, SYNC_FROM_APP
                    ) VALUES (
                    '{tran_window}', '{save_flag}', '{val_flag}', '{key_flag}', '{key_string}', '{udf_1}', '{udf_2}', '{udf_3}',
                    '{udf_4}', '{udf_5}', '{repeate_add}', TO_DATE('{chg_date}', 'DD-MM-YYYY'), '{chg_user}', '{chg_term}', '{edi_option}',
                    '{site_acc_col}', '{confirm_col}', '{confirm_val}', '{repeat_add_det}', '{repeatadddet}',
                    '{load_mode}', '{auto_confirm}', '{ledg_post_conf}', '{chg_date_on_conf}', '{tran_id_col}',
                    '{mail_option}', '{confirm_mode}', '{garbage_opt}', '{val_flag_edi}', '{verify_password}',
                    '{cust_acc_col}', '{sales_pers_acc_col}', '{supp_acc_col}', '{item_ser_acc_code}',
                    '{emp_acc_col}', '{item_ser_acc_col}', '{workflow_opt}', '{table_name}', '{application}',
                    '{table_desc}', '{tran_date_col}', '{tran_id__from}', '{tran_id__to}', '{table_name_det1}',
                    '{table_name_det2}', '{table_name_det3}', '{multitire_opt}', '{ref_ser}', '{view_mode}',
                    '{tax_forms}', '{sign_status}', NULL, '{obj_name__parent}',
                    '{ignoreerrlist_onload}', '{childdata_argopt}', NULL, '{wrkflw_init}', '{edittax}',
                    NULL, '{audit_trail_opt}', '{edit_opt}', NULL, '{optimize_mode}', '{edit_expr}',
                    '{rate_col}', '{qty_col}', '{edit_expr_inp}', '{rcp_cache_status}', '{print_control}',
                    '{transfer_mode}', '{profile_id__res}', '{tran_compl_msg}', '{period_option}',
                    '{wrkflw_priority}', '{exec_type}', '{disp_meta_data}', '{allow_attach}', '{start_form}',
                    '{isattachment}', '{header_form_no}', '{confirm_date_col}', '{confirm_by_col}', '{msg_onsave}',
                    '{wf_status}', '{restart_form}', '{cms_path}', '{brow_data_def}', '{def_view}', '{view_opts}',
                    '{isgwtinitiated}', NULL, '{in_wf_val}', '{in_wf_col}', '{cancel_val}',
                    '{cancel_col}', '{thumb_alt_col}', '{thumb_image_col}', '{thumb_obj}', NULL,
                    '{function_type}', '{compl_action}', '{default_editor}', '{msg_no}', '{obj_type}', '{status_col}',
                    '{enable_editor}', '{offline_opt}', '{close_col}', '{close_val}', '{thread_key_col}',
                    NULL, '{sync_from_app}'
                    )
                """
                logger.log(f"\n--- Class Transetup ---\n")
                logger.log(f"{insert_query}")
                cursor.execute(insert_query)
                cursor.close()
                logger.log(f"Inserted: {tran_window}")

    def get_table_name(self, join_list):
        result = ''
        for single_json in join_list:
            if single_json['main_table'] == True:
                return single_json['table']
        return result

    def process_data(self, conn, sql_models_data, obj_name):
        logger.log(f"Start of Transetup Class")
        main_table_name = ''
        self.sql_models = sql_models_data
        for sql_model in self.sql_models:
            if "sql_model" in sql_model and "joins" in sql_model['sql_model'] and "join_predicates" in sql_model['sql_model']['joins'] and "joins" in sql_model['sql_model']['joins']['join_predicates']:
                joins_lst = sql_model['sql_model']['joins']['join_predicates']['joins']
                table_name = self.get_table_name(joins_lst)
                main_table_name = table_name.upper()
                logger.log(f"main_table_name ::: {main_table_name}")

            if "form_no" in sql_model['sql_model']:
                # logger.log(f"Transetup sql_model ::: {sql_model}")
                if sql_model['sql_model']['form_no'] == '1' or sql_model['sql_model']['form_no'] == 1:
                    trans_id_col_list = []
                    key_string = ""
                    key_flag = ""
                    ref_ser = ""
                    site_acc_col = ""
                    for column in sql_model['sql_model']['columns']:
                        if column['column']['default_value'].lower() == "login_site":
                            site_acc_col = column['column']['db_name'].upper()
                            column['column']['default_value'] = ""
                        if (column['column']['key'] == True or column['column']['key'] == "true" or column['column']['key'] == "True") and column['column']['table_name'].upper() == main_table_name:
                            trans_id_col_list.append(column['column']['db_name'].upper())
                            if column['column']['default_value'] == "auto_generate()" or column['column']['default_value'] == "auto-generate()":
                                key_string = "seq10"
                                key_flag = "A"

                                obj_name_splits = obj_name.split("_")   
                                split_len = len(obj_name_splits)
                                
                                if split_len >= 4:
                                    ref_ser = "".join([part[:2].upper() for part in obj_name_splits[-3:]])
                                elif split_len == 3:
                                    ref_ser = "".join([part[:3].upper() for part in obj_name_splits[-2:]])
                                elif split_len == 2:
                                    ref_ser = obj_name_splits[-1][:6].upper()
                                elif split_len == 1:
                                    ref_ser = obj_name_splits[0][:6].upper()
                                else:
                                    ref_ser = ""

                                logger.log(f"obj_name_splits value ::: {obj_name_splits}")
                                logger.log(f"ref_ser value ::: {ref_ser}")
                                column['column']['default_value'] = ""
                                column['column']['mandatory'] = "false"

                    logger.log(f"obj_name ::: w_{obj_name}")

                    fixed_model_data = {
                        "tran_window": f"w_{obj_name}", "save_flag": "", "val_flag": "", "key_flag": f"{key_flag}", "key_string": f"{key_string}", "udf_1": "", "udf_2": "", "udf_3": "", "udf_4": "", "udf_5": "", "repeate_add": "",
                        "chg_date": "", "chg_user": "", "chg_term": "", "edi_option": "", "site_acc_col": f"{site_acc_col}", "confirm_col": "", "confirm_val": "", "repeat_add_det": "", "repeatadddet": "", "load_mode": "",
                        "auto_confirm": "", "ledg_post_conf": "", "chg_date_on_conf": "", "tran_id_col": f"{','.join(trans_id_col_list)}", "mail_option": 0, "confirm_mode": 0, "garbage_opt": "", "val_flag_edi": "", 
                        "verify_password": "", "cust_acc_col": "", "sales_pers_acc_col": "", "supp_acc_col": "", "item_ser_acc_code": "", "emp_acc_col": "",  "item_ser_acc_col": "", "workflow_opt": 0, 
                        "table_name": f"{main_table_name.upper()}", "application": "", "table_desc": "", "tran_date_col": "", "tran_id__from": "", "tran_id__to": "", 
                        "table_name_det1": "", "table_name_det2": "", "table_name_det3": "", "multitire_opt": "", "ref_ser": f"{ref_ser}", "view_mode": "F", "tax_forms": "", "sign_status": "", "user_tran_window": "",
                        "obj_name__parent": "", "ignoreerrlist_onload": "", "childdata_argopt": "", "edit_tmplt": "", "wrkflw_init": "", "edittax": "", "formal_args": "", "audit_trail_opt": 2, "edit_opt": "", "cache_opt": "",
                        "optimize_mode": "", "edit_expr": "", "rate_col": "", "qty_col": "", "edit_expr_inp": "", "rcp_cache_status": "", "print_control": "N", "transfer_mode": "", "profile_id__res": "", "tran_compl_msg": "", "period_option": "M",
                        "wrkflw_priority": "", "exec_type": "", "disp_meta_data": "", "allow_attach": "", "start_form": "", "isattachment": "", "header_form_no": "", "confirm_date_col": "", "confirm_by_col": "", "msg_onsave": "",
                        "wf_status": "", "restart_form": "", "cms_path": "", "brow_data_def": "Y", "def_view": "", "view_opts": "", "isgwtinitiated": "", "default_data_row": "", "in_wf_val": "", "in_wf_col": "", "cancel_val": "",
                        "cancel_col": "", "thumb_alt_col": "", "thumb_image_col": "", "thumb_obj": "", "attach_count_min": "", "function_type": "", "compl_action": "", "default_editor": "compact", "msg_no": "", "obj_type": "",
                        "status_col": "", "enable_editor": "", "offline_opt": "", "close_col": "", "close_val": "", "thread_key_col": "", "load_order": "", "sync_from_app": ""
                        }
                    self.check_and_update_transetup(fixed_model_data, conn)
        logger.log(f"End of Transetup Class")
